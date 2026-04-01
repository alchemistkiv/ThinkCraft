#!/usr/bin/env python3
"""Portable source validator for thinkcraft.

This script intentionally uses only the Python standard library.
It validates the current source manifest and referenced skill markdown files.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, cast


REQUIRED_PACKAGE_FIELDS = [
    "name",
    "version",
    "kind",
    "language",
    "runtime_independent",
    "description",
]

REQUIRED_SKILL_FIELDS = [
    "name",
    "description",
    "aliases",
    "when_to_use",
    "argument_hint",
    "allowed_tools",
    "user_invocable",
    "source_file",
]

REQUIRED_MARKDOWN_SECTIONS = [
    "Goal",
    "When to use",
    "Inputs",
    "Process",
    "Output shape",
    "Guardrails",
    "Handoff",
]

ALLOWED_TOOLS_WHITELIST = {
    "bash",
    "read",
    "glob",
    "grep",
    "webfetch",
}

OPTIONAL_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
]


class YamlSubsetError(Exception):
    pass


def parse_scalar(value: str) -> Any:
    if value == "true":
        return True
    if value == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def strip_comment(line: str) -> str:
    in_single = False
    in_double = False
    out = []
    for char in line:
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            break
        out.append(char)
    return "".join(out).rstrip()


def parse_manifest_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    lines = text.splitlines()
    for line_number, raw_line in enumerate(lines, start=1):
        line = strip_comment(raw_line)
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        if indent % 2 != 0:
            raise YamlSubsetError(f"Line {line_number}: indentation must use multiples of two spaces")

        content = line.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise YamlSubsetError(f"Line {line_number}: invalid indentation structure")

        parent = stack[-1][1]

        if content.startswith("- "):
            if not isinstance(parent, list):
                raise YamlSubsetError(f"Line {line_number}: list item found under non-list parent")
            item_body = content[2:].strip()
            if not item_body:
                item: Any = {}
                parent.append(item)
                stack.append((indent, item))
                continue
            if ":" in item_body:
                key, value = item_body.split(":", 1)
                key = key.strip()
                value = value.strip()
                item = {key: parse_scalar(value)} if value else {key: {}}
                parent.append(item)
                stack.append((indent, item))
                if not value:
                    stack.append((indent + 2, item[key]))
            else:
                parent.append(parse_scalar(item_body))
            continue

        if ":" not in content:
            raise YamlSubsetError(f"Line {line_number}: expected key/value mapping")

        key, value = content.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not isinstance(parent, dict):
            raise YamlSubsetError(f"Line {line_number}: mapping found under non-dict parent")

        if value:
            parent[key] = parse_scalar(value)
            continue

        next_non_empty = None
        for look_ahead in lines[line_number:]:
            candidate = strip_comment(look_ahead)
            if candidate.strip():
                next_non_empty = candidate
                break

        if next_non_empty is not None:
            next_indent = len(next_non_empty) - len(next_non_empty.lstrip(" "))
            next_content = next_non_empty.strip()
            if next_indent <= indent:
                parent[key] = ""
                continue
            parent[key] = [] if next_content.startswith("- ") else {}
        else:
            parent[key] = {}

        stack.append((indent, parent[key]))

    return root


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def ok(self) -> bool:
        return not self.errors


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def validate_markdown_sections(path: Path, report: ValidationReport) -> None:
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        report.error(f"Unable to read skill markdown '{path.as_posix()}': {exc}")
        return

    for section in REQUIRED_MARKDOWN_SECTIONS:
        pattern = rf"^##\s+{re.escape(section)}\s*$"
        if not re.search(pattern, content, flags=re.MULTILINE):
            report.error(
                f"Skill markdown '{path.as_posix()}' is missing required section: '## {section}'"
            )


def validate_package(package_root: Path) -> ValidationReport:
    report = ValidationReport()
    manifest_path = package_root / "manifest.yaml"

    if not manifest_path.exists():
        report.error(f"Missing manifest file: {manifest_path.as_posix()}")
        return report

    try:
        manifest_text = manifest_path.read_text(encoding="utf-8")
    except OSError as exc:
        report.error(f"Unable to read manifest: {exc}")
        return report

    try:
        manifest = parse_manifest_yaml(manifest_text)
    except YamlSubsetError as exc:
        report.error(f"Manifest parse failed: {exc}")
        return report

    package = manifest.get("package")
    if not isinstance(package, dict):
        report.error("Manifest must contain a top-level 'package' mapping")
        return report

    for field_name in REQUIRED_PACKAGE_FIELDS:
        value = package.get(field_name)
        if isinstance(value, bool):
            continue
        if not is_non_empty_string(value):
            report.error(f"Missing or empty required source metadata field: package.{field_name}")

    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        report.error("Manifest 'skills' must be a non-empty list")
        return report

    seen_names: set[str] = set()
    seen_aliases: set[str] = set()

    for index, skill in enumerate(skills, start=1):
        prefix = f"skills[{index}]"
        if not isinstance(skill, dict):
            report.error(f"{prefix} must be a mapping")
            continue

        for field_name in REQUIRED_SKILL_FIELDS:
            if field_name not in skill:
                report.error(f"Missing required skill field: {prefix}.{field_name}")

        name = skill.get("name")
        if not is_non_empty_string(name):
            report.error(f"Missing or empty required skill name: {prefix}.name")
        else:
            skill_name = cast(str, name)
            if skill_name in seen_names:
                report.error(f"Duplicate skill name: '{skill_name}'")
            if skill_name in seen_aliases:
                report.error(f"Skill name collides with an alias: '{skill_name}'")
            seen_names.add(skill_name)

        aliases = skill.get("aliases")
        if not isinstance(aliases, list):
            report.error(f"{prefix}.aliases must be a list")
            aliases = []

        local_aliases: set[str] = set()
        for alias in aliases:
            if not is_non_empty_string(alias):
                report.error(f"{prefix}.aliases contains an empty or invalid value")
                continue
            if alias in local_aliases:
                report.error(f"Duplicate alias within {prefix}: '{alias}'")
            if alias in seen_aliases:
                report.error(f"Alias reused across skills: '{alias}'")
            if alias in seen_names:
                report.error(f"Alias collides with a skill name: '{alias}'")
            local_aliases.add(alias)
            seen_aliases.add(alias)

        allowed_tools = skill.get("allowed_tools")
        if not isinstance(allowed_tools, list):
            report.error(f"{prefix}.allowed_tools must be a list")
        else:
            for tool_name in allowed_tools:
                if not is_non_empty_string(tool_name):
                    report.error(f"{prefix}.allowed_tools contains an empty or invalid value")
                    continue
                if tool_name not in ALLOWED_TOOLS_WHITELIST:
                    report.error(
                        f"{prefix}.allowed_tools contains unsupported tool '{tool_name}'"
                    )

        source_file = skill.get("source_file")
        if not is_non_empty_string(source_file):
            report.error(f"Missing or empty required skill field: {prefix}.source_file")
        else:
            source_file_path = cast(str, source_file)
            source_path = package_root / source_file_path
            if not source_path.exists():
                report.error(f"Referenced source_file does not exist: {source_file_path}")
            else:
                validate_markdown_sections(source_path, report)

    for relative_name in OPTIONAL_FILES:
        if not (package_root / relative_name).exists():
            report.warn(f"Missing optional file: {relative_name}")

    return report


def print_report(package_root: Path, report: ValidationReport) -> None:
    print(f"Validation target: {package_root}")
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")
    print()

    for message in report.errors:
        print(f"ERROR {message}")
    for message in report.warnings:
        print(f"WARN  {message}")

    if report.errors or report.warnings:
        print()

    print(f"RESULT: {'PASS' if report.ok else 'FAIL'}")


def resolve_package_root(argv: list[str]) -> Path:
    if len(argv) > 2:
        raise SystemExit("Usage: validate_package.py [PACKAGE_ROOT]")
    if len(argv) == 2:
        return Path(argv[1]).resolve()
    return Path(__file__).resolve().parents[1]


def main(argv: list[str]) -> int:
    package_root = resolve_package_root(argv)
    report = validate_package(package_root)
    print_report(package_root, report)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
