# Portability

`thinkcraft` is designed to be portable because it treats authoring source as distinct from runtime projection.

## Source -> projection -> target runtime

The portability model is:

- `source`: canonical authoring files in the repository root
- `projection`: exported representation for a specific delivery shape
- `target runtime`: the host that consumes that representation

This separation means the package can preserve one canonical meaning while supporting multiple runtime formats.

## What portability improves

### Runtime independence

The package does not depend on one loader, one package manager, or one execution implementation. That keeps the source tree usable even when runtime details change elsewhere.

### Projection-specific compatibility

Each projection can carry its own mapping and validation rules.

- `bundled` focuses on embedded or generated skill catalogs
- `disk-commands` focuses on Claude Code compatible command files on disk

This avoids mixing runtime-specific concerns back into the canonical source files.

### Safer reuse

Teams can reuse the same source package in different environments:

- one runtime can bundle skills into internal artifacts
- another can export command markdown onto disk
- example projects can show the projected layout without redefining the source format

### Traceable provenance

Projection artifacts can retain provenance metadata such as package name, projection id, and source template path. That makes it clear where a runtime-facing file came from.

## Portability boundaries

Portability does not mean every runtime behaves the same. It means the package preserves one source model and documents how that model maps outward.

This package intentionally does not implement:

- package installation flows
- runtime command dispatch
- registry sync
- platform-specific enforcement logic

## Portability checklist

Portable authoring in this package means:

- canonical source stays in the repository root
- projections are named and documented explicitly
- schemas describe machine-readable contracts
- mapping files explain how fields move across surfaces
- example output is labeled as projection, not source

## Result

The package can now be treated as a source package that projects cleanly into more than one target shape, with Claude Code compatible disk commands documented as one projection rather than the definition of the package itself.
