# Disk Command Format

This document describes the disk-command projection used for Claude Code compatible command files under `.claude/commands/*.md`.

## Position in the model

Disk commands are a projection, not a canonical source.

- Canonical source: `manifest.yaml`, `skills/*.md`, `templates/commands/*.md`
- Projection: frontmatter + markdown body copied into `.claude/commands/*.md`
- Target runtime: any runtime that reads command files from disk, including Claude Code compatible layouts

## File shape

Each disk command is a markdown file with YAML frontmatter followed by a markdown body.

```md
---
name: brainstorm
description: Expand candidate directions before committing to one.
argument_hint: Topic, goal, context, and constraints.
source_package: thinkcraft
source_template: templates/commands/brainstorm.md
projection: disk-commands
runtime_compatibility: claude-code
---

# brainstorm

Use this command to open the solution space before narrowing it.
```

## Required frontmatter fields

- `name`: Stable command id
- `description`: Short reader-facing summary
- `argument_hint`: What the caller should provide
- `source_package`: Canonical package id, currently `thinkcraft`
- `source_template`: Path to the canonical template in this package
- `projection`: Projection id, currently `disk-commands`
- `runtime_compatibility`: Runtime compatibility label, currently `claude-code`

The body should remain readable markdown and should match the operational intent of the source template.

## Compatibility statement

Files placed in `.claude/commands/*.md` are a Claude Code compatible projection. They are intended for runtime consumption after copy or export. They are not the package's canonical source.

## Authoring constraints

- Keep the file self-contained after copy
- Preserve the command id from canonical source
- Preserve English-language instructions
- Avoid runtime-specific logic beyond what the on-disk format requires
- Keep provenance fields so users can trace the file back to `thinkcraft`

## Validation

The frontmatter contract is described in `schemas/disk-command-frontmatter.schema.json`.

Consumers may validate:

- required frontmatter fields
- allowed projection id
- allowed runtime compatibility label
- presence of a non-empty markdown body

## Projection workflow

1. Start with a canonical template under `templates/commands/*.md`.
2. Copy the file into a project-local `.claude/commands/` directory.
3. Keep the frontmatter intact so provenance and compatibility remain visible.
4. Invoke the command by name in the target runtime.

This workflow allows the package to stay runtime-independent while still offering a documented disk-based delivery path.
