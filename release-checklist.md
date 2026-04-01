# Release Checklist

Use this checklist before publishing or tagging an open-source release of `thinkcraft`.

## Content and language

- Confirm the canonical source language is English and `manifest.yaml` uses `language: en`.
- Confirm release-facing source documentation is fully in English.
- Confirm all skill files use English prose while preserving the required section names.
- Confirm all command templates and example projection files use English prose.
- Confirm terminology is consistent across `README.md`, `SKILLS.md`, docs, manifest, and skill files.
- Confirm the package consistently describes `source -> projection -> target runtime`.

## Manifest validation

- Confirm `manifest.yaml` keeps the existing structural shape.
- Confirm every skill entry has `name`, `description`, `aliases`, `when_to_use`, `argument_hint`, `allowed_tools`, `user_invocable`, and `source_file`.
- Confirm every `source_file` points to an existing file under `skills/`.
- Confirm manifest values are release-appropriate, reader-facing, and sufficient as source metadata in English.
- Confirm `catalog/skills.index.json` remains aligned with the manifest field set and values.

## Projection validation

- Confirm `catalog/exports.yaml` defines at least the `bundled` and `disk-commands` projections.
- Confirm `adapters/bundled/mapping.yaml` and `adapters/disk-commands/mapping.yaml` describe the intended field movement clearly.
- Confirm `.claude/commands/*.md` is described as a Claude Code compatible projection rather than canonical source.
- Confirm command templates preserve frontmatter plus markdown body.
- Confirm `schemas/disk-command-frontmatter.schema.json` matches the documented frontmatter fields.

## Required files

- Confirm `README.md` exists.
- Confirm `SKILLS.md` exists.
- Confirm `LICENSE` exists and contains the MIT license text.
- Confirm `CHANGELOG.md` exists.
- Confirm `CONTRIBUTING.md` exists.
- Confirm `release-checklist.md` exists.
- Confirm `docs/bundled-mapping.md` and `docs/mvp.md` exist.
- Confirm `docs/integration-surfaces.md`, `docs/disk-command-format.md`, and `docs/portability.md` exist.
- Confirm `schemas/manifest.schema.json` and `schemas/disk-command-frontmatter.schema.json` exist.
- Confirm `templates/commands/` and `examples/project/` exist.

## Structure validation

- Confirm the source tree still acts as authoring source rather than runtime code.
- Confirm no runtime or Rust code was introduced in this package.
- Confirm no package manager or runtime implementation was introduced for projections.
- Confirm no Node package metadata file was added.
- Confirm all six skill files preserve the same section sequence.
- Confirm the source-level structure remains readable for bundling and future validation.
- Confirm projection artifacts are traceable back to canonical source files.

## Release tagging notes

- Update `CHANGELOG.md` with the release version and date before tagging.
- Tag releases in a way that matches this repository's documented release conventions.
- If the package is versioned independently later, keep the tag naming scheme explicit and documented.
- Include a short release note stating that `thinkcraft` is an authoring-source package with documented bundled and disk-command projections.
