#!/usr/bin/env python3
"""校验固定原生文件、依赖与引用；可对照指定的固定版本 Git checkout。"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def verify(root: Path, source: Path | None = None) -> int:
    """root 为本仓库；source 可选，为原生仓库 checkout，使用 git show 读取固定提交。"""
    manifest = json.loads((root / "upstream-manifest.json").read_text())
    names = {skill["name"] for skill in manifest["skills"]}
    count = 0
    for skill in manifest["skills"]:
        if not set(skill["depends_on"]) <= names:
            raise ValueError(f"未收录依赖：{skill['name']}")
        expected = {entry["path"] for entry in skill["files"]}
        actual = {str(p.relative_to(root)) for p in (root / "skills" / skill["name"]).rglob("*") if p.is_file()}
        if actual != expected:
            raise ValueError(f"原生文件集合变化：{skill['name']}，差异 {actual ^ expected}")
        for entry in skill["files"]:
            check_file(root, entry, manifest["commit"], source)
            count += 1
    check_file(root, manifest["license"], manifest["commit"], source)
    # 仅检查 Markdown 的真实资源链接；代码围栏中的业务项目示例不是安装资源。
    link_count = 0
    for name in names:
        for file in (root / "skills" / name).rglob("*.md"):
            text = re.sub(r"```.*?```", "", file.read_text(), flags=re.S)
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if re.match(r"[a-zA-Z]+://", target) or target.startswith("#"):
                    continue
                path = file.parent / target.split("#")[0]
                if not path.exists():
                    raise ValueError(f"资源链接不存在：{file.relative_to(root)} -> {target}")
                link_count += 1
    # 诊断 Skill 以代码格式引用脚本，不能仅检查 Markdown 链接。
    if not (root / "skills/diagnosing-bugs/scripts/hitl-loop.template.sh").is_file():
        raise ValueError("缺少原生 HITL 脚本")
    print(f"通过：{len(names)} 个原生 Skills，{count} 个原生文件及 MIT，{link_count} 个资源链接；依赖齐备。")
    print("已与固定 Git 提交原文比对。" if source else "已与 manifest hash 比对；未连接上游。")
    return 0


def check_file(root: Path, entry: dict, commit: str, source: Path | None) -> None:
    """entry 指定本地路径、来源路径和 hash；source 提供时进一步比较 Git 原始字节。"""
    data = (root / entry["path"]).read_bytes()
    if hashlib.sha256(data).hexdigest() != entry["sha256"]:
        raise ValueError(f"hash 不一致：{entry['path']}")
    if source:
        original = subprocess.check_output(["git", "-C", str(source), "show", f"{commit}:{entry['source']}"])
        if data != original:
            raise ValueError(f"与固定提交不一致：{entry['path']}")


def main() -> int:
    """解析可选上游 checkout 参数，报告验证失败而不修改任何文件。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="可选上游 Git checkout")
    args = parser.parse_args()
    try:
        return verify(Path(__file__).resolve().parents[1], args.source)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"校验失败：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
