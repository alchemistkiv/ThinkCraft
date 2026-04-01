# Skill Catalog

This file gives the package-level view of the `thinkcraft` skill family from the authoring side. It describes the canonical source skills, how they fit together, and how they project into runtime-facing forms without changing the repository's source-of-record role.

## Package stance

- `thinkcraft` is an authoring-source repository for bundled thinking skills
- Skill markdown under `skills/` is canonical source
- Command templates under `templates/commands/` are canonical source for the disk-command projection path
- `.claude/commands/*.md` is a Claude Code compatible projection shape, not the source of truth
- The repository aims for direct, plainspoken, teammate-like writing rather than ceremonial prompt prose

## Skill family

### `clarify`

Use `clarify` when the request is still unstable. It reduces ambiguity, surfaces assumptions, and gives the next step a cleaner problem frame.

### `brainstorm`

Use `brainstorm` when the option space needs to open up. It generates multiple viable directions and carries forward a shortlist instead of a loose pile of ideas.

### `analyze`

Use `analyze` when constraints, risks, dependencies, or cause-and-effect relationships need a more systematic pass. It ranks the real risks instead of flattening everything into one undifferentiated list.

### `design`

Use `design` when one direction needs a workable structure. It shapes flows, boundaries, interfaces, and open decisions while keeping comparison logic visible.

### `decide`

Use `decide` when multiple reasonable options remain. It compares them with explicit criteria, weighting, accepted risks, and confidence notes.

### `reflect`

Use `reflect` when a plan, decision, or design needs an after-the-fact audit. It checks whether the reasoning, assumptions, and scorecard quality actually hold up.

## Shared source structure

Every source skill keeps the same section skeleton:

- `Goal`
- `When to use`
- `Inputs`
- `Process`
- `Output shape`
- `Guardrails`
- `Handoff`

That shared structure keeps the package easier to validate, compare, and project.

## Source and projection reminder

The repository follows a `source -> projection -> runtime` model.

- `source`: `manifest.yaml`, `skills/*.md`, `templates/commands/*.md`
- `projection`: exported shapes such as `bundled` and `disk-commands`
- `runtime`: any host that consumes those projected artifacts

Usage in Claude Code compatible projects is a downstream projection story. The authoring source remains here.
