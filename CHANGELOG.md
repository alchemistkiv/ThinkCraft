# Changelog

All notable changes to `thinkcraft` are documented in this file.

The format follows Keep a Changelog. This repository is versioned as a standalone authoring-source package.

## [Unreleased]

- No unreleased changes recorded.

## [0.1.0] - 2026-04-01

First public preview of the standalone `thinkcraft` repository.

### Added

- Added the standalone release metadata document in `docs/github-metadata.md`.
- Added the preview release note in `docs/releases/v0.1.0-preview.md`.
- Added MIT licensing and baseline release files for public distribution.
- Added a lightweight package validator in `tests/validate_package.py` with supporting validation docs and fixtures.
- Added projection examples under `examples/project/` for Claude Code compatible command usage.

### Changed

- Established `thinkcraft` as the repository identity for the bundled-skill authoring-source package.
- Rewrote release-facing documentation in English and aligned it around an authoring-model-first, usage-second position.
- Clarified the `source -> projection -> runtime` architecture across package docs.
- Framed `.claude/commands/*.md` consistently as a Claude Code compatible projection rather than canonical source.
- Kept the package runtime-independent and avoided installer, registry, or execution-engine claims.

### Included

- Canonical metadata in `manifest.yaml`
- Six source skills under `skills/`
- Command-template source files under `templates/commands/`
- Projection mapping docs under `adapters/`, `catalog/`, and `docs/`
