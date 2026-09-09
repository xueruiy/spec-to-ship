"""真实运行项目链接命令，验证可读文件、幂等性及冲突保护。"""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/link-project-skills.py"


class ProjectInstallTests(unittest.TestCase):
    def run_link(self, project: Path, *options: str) -> subprocess.CompletedProcess:
        """project 为临时项目；options 为实际传给 CLI 的只读检查等参数。"""
        return subprocess.run([sys.executable, str(SCRIPT), str(project), *options], capture_output=True, text=True)

    def test_install_readable_and_idempotent(self) -> None:
        """检查模式不写入；真实安装后所有文件可经链接读取，重复执行不改链接。"""
        with tempfile.TemporaryDirectory(prefix="sts-install-") as temporary:
            project = Path(temporary)
            result = self.run_link(project, "--check")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((project / ".agents").exists())
            result = self.run_link(project)
            self.assertEqual(result.returncode, 0, result.stderr)
            source_skills = sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file())
            native_names = {entry["name"] for entry in json.loads((ROOT / "upstream-manifest.json").read_text())["skills"]}
            self.assertEqual({p.name for p in source_skills}, native_names | {"sts-workflow", "sts-acceptance", "sts-closeout"})
            before = {}
            for source in source_skills:
                linked = project / ".agents/skills" / source.name
                self.assertTrue(linked.is_symlink())
                self.assertEqual(linked.resolve(), source)
                before[linked] = linked.lstat().st_mtime_ns
                # 读取全目录，确保 references、assets 和脚本也能从业务项目入口使用。
                for original in source.rglob("*"):
                    if original.is_file():
                        self.assertEqual((linked / original.relative_to(source)).read_bytes(), original.read_bytes())
            result = self.run_link(project)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(before, {p: p.lstat().st_mtime_ns for p in before})

    def test_add_workflow_to_existing_installation(self) -> None:
        """已有原生与验收收尾入口时，只增加新导航入口，保留所有旧链接。"""
        with tempfile.TemporaryDirectory(prefix="sts-upgrade-") as temporary:
            project = Path(temporary)
            destination = project / ".agents/skills"
            destination.mkdir(parents=True)
            existing = {}
            for skill in (ROOT / "skills").iterdir():
                if (skill / "SKILL.md").is_file() and skill.name != "sts-workflow":
                    target = destination / skill.name
                    target.symlink_to(skill, target_is_directory=True)
                    existing[target] = target.lstat().st_mtime_ns
            self.assertEqual(len(existing), 14)
            result = self.run_link(project, "--check")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((destination / "sts-workflow").exists())
            result = self.run_link(project)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((destination / "sts-workflow").resolve(), ROOT / "skills/sts-workflow")
            self.assertEqual(existing, {p: p.lstat().st_mtime_ns for p in existing})

    def test_conflict_preserves_user_files_without_partial_links(self) -> None:
        """后排序 Skill 冲突也必须在创建任何链接前失败。"""
        with tempfile.TemporaryDirectory(prefix="sts-conflict-") as temporary:
            project = Path(temporary)
            conflict = project / ".agents/skills/to-tickets"
            conflict.mkdir(parents=True)
            user_file = conflict / "SKILL.md"
            user_file.write_text("用户已有内容")
            for options in [(), ("--check",)]:
                result = self.run_link(project, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(user_file.read_text(), "用户已有内容")
                self.assertEqual(list(conflict.parent.iterdir()), [conflict])

    def test_redirected_directory_rejected(self) -> None:
        """项目入口重定向到外部目录时拒绝写入，不污染外部环境。"""
        with tempfile.TemporaryDirectory(prefix="sts-boundary-") as temporary:
            base = Path(temporary)
            project, external = base / "project", base / "external"
            project.mkdir()
            external.mkdir()
            (project / ".agents").symlink_to(external, target_is_directory=True)
            result = self.run_link(project)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(list(external.iterdir()), [])

    def test_dangling_skill_conflict_preserved(self) -> None:
        """失效的同名用户链接也不能被静默覆盖。"""
        with tempfile.TemporaryDirectory(prefix="sts-dangling-") as temporary:
            project = Path(temporary)
            destination = project / ".agents/skills"
            destination.mkdir(parents=True)
            conflict = destination / "grilling"
            conflict.symlink_to(project / "missing")
            result = self.run_link(project)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(conflict.is_symlink())
            self.assertEqual(list(destination.iterdir()), [conflict])


if __name__ == "__main__":
    unittest.main()
