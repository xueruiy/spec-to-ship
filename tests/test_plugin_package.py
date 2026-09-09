"""验证整包可移植性、原生完整性与已知的宿主/helper兼容差异。"""
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/spec-to-ship"
NATIVE = json.loads((ROOT / "upstream-manifest.json").read_text())
EXPLICIT = {"grill-with-docs", "handoff", "implement", "setup-matt-pocock-skills", "to-spec", "to-tickets"}
spec = importlib.util.spec_from_file_location("verify_upstream", ROOT / "scripts/verify-upstream.py")
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


class PluginPackageTests(unittest.TestCase):
    def copy_package(self, destination: Path) -> Path:
        """destination 为隔离临时仓库；复制分发包及来源清单，不依赖旧根目录。"""
        bundle = destination / "plugins/spec-to-ship"
        shutil.copytree(PLUGIN, bundle)
        shutil.copyfile(ROOT / "upstream-manifest.json", destination / "upstream-manifest.json")
        return bundle

    def test_relocated_bundle_keeps_all_resources(self) -> None:
        """整包复制到新位置后，原生和自定义的资源、模板、相邻技能仍可读取。"""
        with tempfile.TemporaryDirectory(prefix="sts-plugin-") as temporary:
            root = Path(temporary)
            bundle = self.copy_package(root)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(verifier.verify(root), 0)
            names = {p.name for p in (bundle / "skills").iterdir() if (p / "SKILL.md").is_file()}
            expected = {entry["name"] for entry in NATIVE["skills"]} | {"sts-workflow", "sts-acceptance", "sts-closeout"}
            self.assertEqual(names, expected)
            for file in bundle.rglob("*.md"):
                body = re.sub(r"```.*?```", "", file.read_text(), flags=re.S)
                for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
                    if re.match(r"[a-zA-Z]+://", target) or target.startswith("#"):
                        continue
                    # 资源引用必须留在插件归档内，不能靠开发仓库或旧软链接补齐。
                    resource = (file.parent / target.split("#")[0]).resolve()
                    self.assertTrue(resource.is_relative_to(bundle.resolve()), (file, target))
                    self.assertTrue(resource.exists(), (file, target))
            self.assertTrue((bundle / "licenses/mattpocock-skills.LICENSE").is_file())
            for name, filename in [("sts-acceptance", "acceptance.md"), ("sts-closeout", "closeout.md")]:
                self.assertTrue((bundle / f"skills/{name}/assets/{filename}").is_file())

    def test_native_modification_is_rejected(self) -> None:
        """一个原生文件改变时也必须失败，不能仅以入口总数判断完整。"""
        with tempfile.TemporaryDirectory(prefix="sts-native-change-") as temporary:
            root = Path(temporary)
            bundle = self.copy_package(root)
            original = bundle / "skills/implement/SKILL.md"
            original.write_text(original.read_text() + "\nlocal patch\n")
            with self.assertRaisesRegex(ValueError, "hash 不一致"):
                verifier.verify(root)

    def test_missing_native_resource_is_rejected(self) -> None:
        """丢失深层参考脚本时整包校验失败，不只检查SKILL.md。"""
        with tempfile.TemporaryDirectory(prefix="sts-native-missing-") as temporary:
            root = Path(temporary)
            bundle = self.copy_package(root)
            (bundle / "skills/diagnosing-bugs/scripts/hitl-loop.template.sh").unlink()
            with self.assertRaisesRegex(ValueError, "原生文件集合变化"):
                verifier.verify(root)

    def test_marketplace_resolves_single_self_contained_package(self) -> None:
        """repo marketplace解析到唯一分发包，包内无本机链接或业务产物。"""
        marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        entry, = marketplace["plugins"]
        self.assertEqual((ROOT / entry["source"]["path"]).resolve(), PLUGIN)
        self.assertEqual(entry["source"]["source"], "local")
        self.assertEqual(entry["policy"], {"installation": "AVAILABLE", "authentication": "ON_INSTALL"})
        manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertFalse((ROOT / "skills").exists())
        self.assertFalse(any(p.is_symlink() for p in PLUGIN.rglob("*")))
        self.assertEqual({p.name for p in PLUGIN.iterdir()}, {".codex-plugin", "skills", "licenses"})

    @unittest.skipUnless(os.environ.get("PLUGIN_VALIDATOR"), "设置PLUGIN_VALIDATOR才运行系统helper兼容检查")
    def test_helper_has_only_known_explicit_invocation_rejections(self) -> None:
        """PLUGIN_VALIDATOR指定系统helper；只允许已核实的6项原生标记拒绝，其他问题失败。"""
        result = subprocess.run([sys.executable, os.environ["PLUGIN_VALIDATOR"], str(PLUGIN)], text=True, capture_output=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        # Codex已发现这些显式入口；此处记录helper仍拒绝的真实差异，不改文件或假报完整通过。
        expected = {f"- skill `{name}` frontmatter field `disable-model-invocation` must be false" for name in EXPLICIT}
        lines = result.stdout.splitlines()
        self.assertEqual(lines[0], "Plugin validation failed:", result.stdout + result.stderr)
        self.assertEqual(set(lines[1:]), expected)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
