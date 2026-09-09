#!/usr/bin/env python3
"""将本仓库 Skills 透明链接到业务项目；不安装依赖或修改全局配置。"""
import argparse
from pathlib import Path
import sys


def link_project(project: Path, check: bool = False) -> list[Path]:
    """project 为已存在的项目目录；check 为 True 时仅检查目标，不写文件。"""
    project = project.expanduser().resolve(strict=True)
    if not project.is_dir() or project == Path.home():
        raise ValueError("请指定项目目录，不能使用用户主目录")
    source = Path(__file__).resolve().parents[1] / "skills"
    skills = sorted(p for p in source.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not skills:
        raise ValueError("仓库 skills 目录为空")
    destination = project / ".agents" / "skills"
    # 拒绝重定向目录，避免项目级链接意外写入全局或其他项目。
    for part in (project / ".agents", destination):
        if part.is_symlink() or (part.exists() and not part.is_dir()):
            raise ValueError(f"目标目录不可用：{part}")
    # 全局同名 Skill 可能仍被发现；只报告，不改写也不假定项目优先级。
    for skill in skills:
        for global_root in (Path.home() / ".codex" / "skills", Path.home() / ".agents" / "skills"):
            other = global_root / skill.name / "SKILL.md"
            if other.is_file() and other.resolve() != (skill / "SKILL.md").resolve():
                print(f"同名全局入口：{other}；请用项目绝对路径明确选择固定版本。", file=sys.stderr)
    planned = []
    # 全量预检后才写入；已有同名文件或其他链接绝不覆盖。
    for skill in skills:
        target = destination / skill.name
        if target.is_symlink() and target.resolve() == skill:
            continue
        if target.exists() or target.is_symlink():
            raise ValueError(f"同名冲突，未写入任何链接：{target}")
        planned.append((skill, target))
    if not check:
        destination.mkdir(parents=True, exist_ok=True)
        created = []
        try:
            for skill, target in planned:
                target.symlink_to(skill, target_is_directory=True)
                created.append(target)
        except OSError:
            # 仅回退本次新建且仍指向预期源的链接，保留用户其他内容。
            for target in created:
                if target.is_symlink() and target.resolve() == source / target.name:
                    target.unlink()
            raise
    return [target for _, target in planned]


def main() -> int:
    """解析项目路径和只读检查开关，输出将新增或已新增的链接。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="业务项目目录")
    parser.add_argument("--check", action="store_true", help="只检查冲突并列出计划，不写文件")
    args = parser.parse_args()
    try:
        planned = link_project(args.project, args.check)
    except (OSError, ValueError) as error:
        print(f"接入失败：{error}", file=sys.stderr)
        return 1
    print("待链接：" if args.check else "已链接：")
    for path in planned:
        print(path)
    if not planned:
        print("全部链接已指向本仓库，无需更改")
    print("源目录必须保留；本脚本未修改 tracker、AGENTS 或全局 Skills。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
