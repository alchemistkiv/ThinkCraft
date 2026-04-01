# Integration Surfaces

`thinkcraft` remains an authoring-source package. It does not implement a package manager, runtime loader, registry, or execution engine. Its job is to define canonical source material that other targets can project into runtime-specific shapes.

## Core model

The package is organized around a three-step model:

1. `source`
2. `projection`
3. `target runtime`

In this model:

- `source` is the canonical authoring layer in the repository root
- `projection` is a deterministic transformation of that source for one delivery format
- `target runtime` is the environment that consumes the projected artifact

## Canonical source

The canonical source stays in human-edited files:

- `manifest.yaml` for package and skill metadata
- `skills/*.md` for canonical skill instruction bodies
- `catalog/skills.index.json` for a normalized machine-readable index derived from the same package metadata model
- `templates/commands/*.md` for canonical disk-command templates that can be copied into a project

Canonical source is where authoring decisions are made. Projections must not silently redefine semantics that belong in source.

## Projection surfaces

The package currently documents two projection surfaces.

### `bundled`

The `bundled` projection is for environments that ingest source metadata and markdown into an embedded or packaged skill catalog.

- Source inputs: `manifest.yaml`, `skills/*.md`
- Projection mapping: `adapters/bundled/mapping.yaml`
- Target runtime example: an internal bundled-skill registry or generated constant set

This projection keeps `skills/*.md` as the canonical instruction source.

### `disk-commands`

The `disk-commands` projection is for environments that discover commands from files placed on disk.

- Source inputs: `manifest.yaml`, `templates/commands/*.md`
- Projection mapping: `adapters/disk-commands/mapping.yaml`
- Target runtime example: a project-local `.claude/commands/*.md` folder

The `.claude/commands/*.md` form is a Claude Code compatible projection. It is not the canonical source of truth for the thinking package.

## Integration contracts

Each integration surface should preserve these contracts:

- Stable skill ids: `brainstorm`, `clarify`, `analyze`, `design`, `decide`, `reflect`
- Stable package identity: `thinkcraft`
- English-language source text
- Explicit separation between canonical source and runtime-specific projection
- Reversible provenance where practical, so projected artifacts can be traced back to source files

## Why this separation matters

Keeping source and projection separate improves portability.

- The same authoring package can target more than one runtime without copying intent into multiple canonical locations.
- Runtime-specific file formats can evolve without forcing a rewrite of the authoring layer.
- Consumers can validate projections against schemas and mapping documents instead of guessing field meaning.
- Example projects can demonstrate delivery formats without redefining the package architecture.

## Non-goals

This document does not define:

- a release pipeline
- a package manager contract
- runtime tool enforcement
- command discovery implementation details
- execution semantics inside Claude Code or any other host
