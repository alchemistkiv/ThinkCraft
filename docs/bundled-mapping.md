# Authoring Format -> `BundledSkill` Mapping

This package is a runtime-independent authoring-source layer. Its purpose is to carry human-editable markdown and manifest data into `BundledSkill` records that can be used from `bundled_skills.rs` on the Rust side, with either lossless or intentionally controlled transformation.

## Design principle

- `manifest.yaml` is the canonical metadata source before bundling.
- `skills/*.md` files are the canonical instruction-body source.
- Metadata and body content are combined during a build or generation step.
- Runtime-specific fields are not stored in the authoring layer; if needed, they should be derived later.

## Recommended field mapping

The mapping below is intended to carry authoring fields into a typical Rust `BundledSkill` structure:

| Authoring source | Field | Rust target | Notes |
| --- | --- | --- | --- |
| `skills[].name` | short id | `BundledSkill.name` | Stable, machine-friendly identifier |
| `skills[].description` | short description | `BundledSkill.description` | Can be used for UI and selection logic |
| `skills[].aliases` | synonymous triggers | `BundledSkill.aliases` | Improves search and matching |
| `skills[].when_to_use` | selection semantics | `BundledSkill.when_to_use` | Discovery and routing signal |
| `skills[].argument_hint` | argument help | `BundledSkill.argument_hint` or similar field | Can be surfaced as CLI or TUI guidance |
| `skills[].allowed_tools` | policy hint | `BundledSkill.allowed_tools` | Runtime enforcement may live elsewhere |
| `skills[].user_invocable` | direct invocability | `BundledSkill.user_invocable` | Useful for UI surfacing |
| `skills[].source_file` | instruction source | build-time input | Does not need to be carried into runtime as-is |
| `skills/*.md` | markdown body | `BundledSkill.instructions` or `content` | Embedded as one string |

## Carrying over the markdown skill skeleton

Each markdown skill file uses the same heading skeleton:

- `Goal`
- `When to use`
- `Inputs`
- `Process`
- `Output shape`
- `Guardrails`
- `Handoff`

That skeleton can be handled during bundling in two different ways:

1. `Raw body embedding`
   - The markdown body is embedded as-is into `BundledSkill` as a single string.
   - This has the lowest transformation cost.

2. `Structured extraction`
   - The headings are parsed into an intermediate AST or section map.
   - Those sections are then rendered again into the runtime format.
   - This is a better fit for future linting, quality checks, and partial rendering.

At MVP scope, `raw body embedding` is sufficient. The shared skeleton keeps a later move to `structured extraction` straightforward.

## Recommended build flow

1. Parse `manifest.yaml`.
2. Read `source_file` for each skill.
3. Validate file existence and required section headings.
4. Merge metadata with body content.
5. Produce a Rust `BundledSkill` instance or generated constant data.

## Validation rules

- `name` must be unique.
- `aliases` must not collide with other skill names.
- `source_file` must exist.
- Markdown bodies must not be empty.
- All required section headings must be present.
- `allowed_tools` values must stay within a normalized whitelist.

## Intentionally excluded from the authoring layer

- runtime execution state
- tool permission enforcement implementation
- versioned binary embedding strategy
- registry, install, or remote fetch behavior

That separation allows `thinkcraft` to stay both human-readable as an authoring source tree and clean as input to the Rust bundling pipeline.
