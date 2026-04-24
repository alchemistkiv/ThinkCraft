#!/usr/bin/env python3
"""Check that generated projection examples match canonical templates."""

from __future__ import annotations

import sys
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_ROOT = PACKAGE_ROOT / "scripts"

sys.path.insert(0, SCRIPTS_ROOT.as_posix())

from project_disk_commands import project_commands  # noqa: E402


def main() -> int:
    try:
        changes = project_commands(check=True)
    except Exception as exc:  # pragma: no cover - command-line safety net
        print(f"ERROR {exc}", file=sys.stderr)
        return 1

    if changes:
        print("Projection drift detected between templates and example commands:")
        for path in changes:
            print(f"- {path}")
        print()
        print("Refresh projected commands with:")
        print("python scripts/project_disk_commands.py")
        return 1

    print("Projection drift check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
