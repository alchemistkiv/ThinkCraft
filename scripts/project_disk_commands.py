#!/usr/bin/env python3
"""Project canonical disk-command templates into example Claude Code commands.

This script keeps the repository's disk-command projection deterministic.
It copies markdown command templates from ``templates/commands`` into the
example project under ``examples/project/.claude/commands`` without changing
frontmatter or body content.

The package remains runtime-independent. This script only refreshes the
example projection shape stored in the repository.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PACKAGE_ROOT / "templates" / "commands"
TARGET_DIR = PACKAGE_ROOT / "examples" / "project" / ".claude" / "commands"


def list_markdown_files(path: Path) -> list[Path]:
    if not path.exists():
        raise FileNotFoundError(f"Missing directory: {path.as_posix()}")
    return sorted(item for item in path.iterdir() if item.is_file() and item.suffix == ".md")


def project_commands(check: bool = False) -> list[str]:
    source_files = list_markdown_files(SOURCE_DIR)
    if not source_files:
        raise RuntimeError(f"No command templates found in {SOURCE_DIR.as_posix()}")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    changes: list[str] = []

    expected_names = {source.name for source in source_files}

    for source in source_files:
        target = TARGET_DIR / source.name
        source_text = source.read_text(encoding="utf-8")

        if target.exists() and target.read_text(encoding="utf-8") == source_text:
            continue

        changes.append(target.relative_to(PACKAGE_ROOT).as_posix())
        if not check:
            target.write_text(source_text, encoding="utf-8")

    for target in list_markdown_files(TARGET_DIR):
        if target.name in expected_names:
            continue
        changes.append(target.relative_to(PACKAGE_ROOT).as_posix())
        if not check:
            target.unlink()

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Project disk-command templates into the example project.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the projected example commands are out of date.",
    )
    args = parser.parse_args()

    try:
        changes = project_commands(check=args.check)
    except Exception as exc:  # pragma: no cover - command-line safety net
        print(f"ERROR {exc}", file=sys.stderr)
        return 1

    if args.check and changes:
        print("Projection drift detected:")
        for path in changes:
            print(f"- {path}")
        print()
        print("Run: python scripts/project_disk_commands.py")
        return 1

    if changes:
        print("Projected disk commands:")
        for path in changes:
            print(f"- {path}")
    else:
        print("Disk-command projection is up to date.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
