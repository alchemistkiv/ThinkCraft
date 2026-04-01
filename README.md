# thinkcraft

`thinkcraft` is the authoring-source package for structured thinking skills and related command projections.

This is not the runtime artifact and it is not an implementation layer. This directory holds canonical source markdown, package metadata, projection templates, schemas, and docs that later project into runtime-specific targets elsewhere.

## Purpose of this package

- Keep the six thinking skills in one authoring package: `brainstorm`, `clarify`, `analyze`, `design`, `decide`, `reflect`
- Preserve the shared section skeleton across all skills: `Goal`, `When to use`, `Inputs`, `Process`, `Output shape`, `Guardrails`, `Handoff`
- Keep package and skill metadata normalized in `manifest.yaml`
- Document a clear `source -> projection -> target runtime` model
- Treat `.claude/commands/*.md` as a Claude Code compatible projection rather than canonical source
- Maintain a consistent voice: direct, plainspoken, teammate-like, and light on ceremony
- Add clearer prioritization support so outputs are easier to compare, rank, and hand off
- Keep field names in a form that maps deterministically to a bundled skill model without making this package itself runtime-specific

## Package contents

- `manifest.yaml`: source-of-truth package and skill metadata
- `skills/*.md`: authoring markdown sources for the bundled thinking skills
- `templates/commands/*.md`: canonical templates for the disk-command projection
- `catalog/skills.index.json`: machine-readable skill catalog aligned with the manifest model
- `catalog/exports.yaml`: declared projection surfaces and their targets
- `schemas/*.json`: validation contracts for manifest data and disk-command frontmatter
- `adapters/*/mapping.yaml`: field mappings from source into projection targets
- `docs/bundled-mapping.md`: mapping between authoring fields and bundled representation
- `docs/integration-surfaces.md`: source, projection, and runtime integration model
- `docs/disk-command-format.md`: Claude Code compatible disk-command format
- `docs/portability.md`: portability goals and boundaries
- `docs/mvp.md`: MVP boundary, non-goals, and acceptance criteria
- `SKILLS.md`: short catalog of the skill family in this package
- `LICENSE`: MIT license for open-source release
- `CHANGELOG.md`: release history for this package
- `CONTRIBUTING.md`: contribution guidelines for documentation and skill authoring
- `release-checklist.md`: package-level release readiness checklist

## Package stance

- The skill family should sound like a sharp teammate, not a consultant.
- The writing should lead with the point and keep structure light unless heavier formatting earns its keep.
- The package should avoid obvious restatement, ceremonial framing, and management-speak.
- Decision-oriented skills should make prioritization visible instead of leaving everything at the same weight.

## Source, projection, target runtime

This package uses a three-layer model:

- `source`: canonical authoring files in the repository root
- `projection`: deterministic exported shapes such as `bundled` and `disk-commands`
- `target runtime`: the environment that consumes those projected artifacts

The important boundary is that projection files are compatible delivery artifacts, not canonical source.

For example, `.claude/commands/*.md` is defined here as a Claude Code compatible projection. It is useful for end-user consumption, but it does not replace `manifest.yaml`, `skills/*.md`, or `templates/commands/*.md` as the authoring source of record.

## Out of scope

This package does not define or implement:

- runtime behavior
- package manager behavior
- skill selection algorithms
- registry integration
- tool policy enforcement
- runtime wiring
- command discovery implementation
- command execution implementation

Because of that boundary, this directory should be treated as bundled skill authoring source rather than a runnable runtime package.
