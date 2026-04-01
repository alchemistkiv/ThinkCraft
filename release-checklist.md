# Release Checklist

Use this checklist before publishing or tagging a standalone release of `thinkcraft`.

## Positioning and messaging

- Confirm `README.md` leads with the authoring-source identity before any usage guidance.
- Confirm release-facing docs describe the repository as runtime-independent source, not as an installer or runtime package.
- Confirm `.claude/commands/*.md` is described as a Claude Code compatible projection and never as canonical source.
- Confirm release notes can stand alone for someone landing on the repo or release page with no prior context.
- Confirm repository and release copy uses `source -> projection -> runtime` consistently.

## Content and language

- Confirm release-facing content is fully in English.
- Confirm `manifest.yaml` keeps `language: en`.
- Confirm all six skill source files remain in English with the required shared headings.
- Confirm `README.md`, `SKILLS.md`, `CHANGELOG.md`, and release docs use the same authoring-source terminology.
- Confirm example and projection docs stay aligned with the landing-page positioning.

## Standalone release notes

- Confirm `CHANGELOG.md` includes the release version and date.
- Confirm `docs/releases/<version>.md` exists for the release being published.
- Confirm the release note opens with a short preview or status statement.
- Confirm the release note includes: what the repo is, what is included, what is intentionally out of scope, validation status, and preview caveats.
- Confirm `docs/github-metadata.md` matches the current repository positioning and can be reused for GitHub description, About text, topics, and release-page copy.
- Confirm release-note wording does not imply packaged installation, automatic runtime wiring, or production stability beyond the stated preview level.

## Manifest and source integrity

- Confirm `manifest.yaml` preserves the existing structural shape.
- Confirm every skill entry has `name`, `description`, `aliases`, `when_to_use`, `argument_hint`, `allowed_tools`, `user_invocable`, and `source_file`.
- Confirm every `source_file` points to an existing file under `skills/`.
- Confirm `catalog/skills.index.json` still aligns with manifest values.
- Confirm canonical source remains traceable from metadata to markdown files.

## Projection integrity

- Confirm `catalog/exports.yaml` defines the documented projections.
- Confirm adapter mappings under `adapters/` still describe intended field movement clearly.
- Confirm command templates preserve their frontmatter and markdown body structure.
- Confirm example project files remain clearly labeled as projections.
- Confirm release copy explains usage only after authoring-source context is established.

## Required files

- Confirm `README.md` exists.
- Confirm `SKILLS.md` exists.
- Confirm `LICENSE` exists and contains MIT text.
- Confirm `CHANGELOG.md` exists.
- Confirm `CONTRIBUTING.md` exists.
- Confirm `release-checklist.md` exists.
- Confirm `docs/github-metadata.md` exists.
- Confirm `docs/releases/` contains the current release note.
- Confirm `docs/bundled-mapping.md`, `docs/integration-surfaces.md`, `docs/disk-command-format.md`, `docs/portability.md`, and `docs/mvp.md` exist.
- Confirm `schemas/manifest.schema.json` and `schemas/disk-command-frontmatter.schema.json` exist.

## Validation and release execution

- Run `python tests/validate_package.py` from the repository root.
- Confirm the validator returns exit code `0`.
- Confirm warnings, if any, are understood and acceptable for the release.
- Stage the final release docs together so the preview note, changelog, and README stay in sync.
- Tag and publish using a version string that matches the standalone repository release note.
