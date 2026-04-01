# thinkcraft Validation Tests

This directory contains a lightweight, portable validation layer for the `thinkcraft` authoring source tree.

The goal is to catch common source-shape and content issues without changing runtime code, adding runtime implementation, or adding external dependencies.

## Contents

- `validate_package.py`: Manual validator for the source manifest and skill files
- `validation-spec.md`: Validation rules and expected behavior
- `test-report-template.md`: Template for recording manual validation runs
- `fixtures/`: Small sample files for validator checks and future manual testing

## Validation position in the architecture

The package follows a `source -> projection -> target runtime` model.

- `source`: canonical authoring files in the repository root
- `projection`: exported shapes such as `bundled` and `disk-commands`
- `target runtime`: the environment that consumes a projection

The existing validator is source-oriented. It validates the authoring package shape, not a runtime implementation.

## What the validator checks

- Manifest can be parsed
- Required source metadata fields are present
- `skills` list exists and is non-empty
- Skill `name` values are unique
- Skill aliases are unique across the source tree
- `source_file` paths exist
- Skill markdown files contain required sections
- `allowed_tools` values are limited to a local whitelist
- Optional release docs are reported if missing: `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`

Future validation can also cover:

- schema conformance for `schemas/manifest.schema.json`
- frontmatter conformance for disk-command templates
- projection catalog consistency in `catalog/exports.yaml`
- manifest alignment with `catalog/skills.index.json`

## How to run

Run from the source root:

```bash
python tests/validate_package.py
```

Or run from anywhere by passing the source path:

```bash
python tests/validate_package.py .
```

## Exit codes

- `0`: validation completed with no errors
- `1`: validation found one or more errors

Warnings do not change the exit code.

## Example output

```text
Validation target: C:\repo\claude-code\packages\thinkcraft
Errors: 0
Warnings: 0

RESULT: PASS
```

## Projection note

If `.claude/commands/*.md` files are validated later, they should be treated as Claude Code compatible projection files rather than canonical source files.
