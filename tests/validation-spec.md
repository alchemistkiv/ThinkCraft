# Validation Specification

## Scope

The validator is intentionally narrow and low risk. It validates source metadata and authoring content shape for this standalone `thinkcraft` repository only.

It does not execute runtime code, generate artifacts, or depend on third-party Python packages.

## Validation Rules

### 1. Manifest parse

The validator must parse `manifest.yaml` using a small built-in parser that supports the current source metadata YAML subset:

- nested mappings
- lists of mappings
- inline scalar lists such as `[read, glob, grep]`
- booleans and basic scalar strings

If parsing fails, validation fails.

### 2. Required source metadata fields

The top-level `package` object must exist and include these fields:

- `name`
- `version`
- `kind`
- `language`
- `runtime_independent`
- `description`

Missing or empty values fail validation.

### 3. Skills list

The top-level `skills` field must:

- exist
- be a list
- contain at least one item

Otherwise validation fails.

### 4. Unique names and aliases

Each skill must define a non-empty `name`.

The validator must fail when:

- two skills share the same `name`
- a skill alias is repeated within the same skill
- an alias is reused by another skill
- an alias matches any skill name

### 5. Source files

Each skill must declare `source_file`.

The validator must fail when the referenced file does not exist relative to the package root.

### 6. Required markdown sections

Each referenced skill markdown file must contain these headings:

- `## Goal`
- `## When to use`
- `## Inputs`
- `## Process`
- `## Output shape`
- `## Guardrails`
- `## Handoff`

Missing headings fail validation.

### 7. Allowed tools whitelist

Each skill may define `allowed_tools` as a list.

Every tool name must be present in the validator's local whitelist.

Initial whitelist:

- `bash`
- `read`
- `glob`
- `grep`
- `webfetch`

Unknown values fail validation.

### 8. Optional files

The validator should check for these source-level release files:

- `README.md`
- `LICENSE`
- `CHANGELOG.md`
- `CONTRIBUTING.md`

Missing optional files are warnings, not errors.

## Reporting

The validator prints:

- target path
- error count
- warning count
- a readable line for each issue
- final `PASS` or `FAIL` result

It returns exit code `0` for pass and `1` for fail.
