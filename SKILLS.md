# Skill Catalog

This file gives a quick authoring-side view of the skill family in this repository. It does not describe runtime behavior. It shows what each canonical source skill is for, how the set fits together, and how the package projects into runtime-facing formats.

## Package principles

- This directory is the authoring-source layer for bundled skill content.
- This directory also defines projection templates for disk-based command delivery.
- Each skill covers one thinking mode or a clean transition between modes.
- All skill files keep the same section skeleton: `Goal`, `When to use`, `Inputs`, `Process`, `Output shape`, `Guardrails`, `Handoff`.
- Skill text is written to be direct, plainspoken, and teammate-like rather than ceremonial or report-heavy.
- Where prioritization matters, outputs should show ranking, weighting, or comparison basis instead of flattening everything into one list.
- Metadata is normalized in `manifest.yaml` and kept in a form that maps cleanly to the Rust `BundledSkill` model.
- `.claude/commands/*.md` is treated as a Claude Code compatible projection, not the canonical source of the package.

## Source and projection model

- `source`: `manifest.yaml`, `skills/*.md`, and `templates/commands/*.md`
- `projection`: `bundled` or `disk-commands`
- `target runtime`: the host that consumes a projected artifact

The skill markdown files under `skills/` remain the canonical instruction source for the bundled skill surface. The command markdown files under `.claude/commands/` are only a compatible projection for disk-based usage.

## Skill family

### `brainstorm`
Opens the solution space, groups candidate directions, and carries forward a short scored shortlist instead of a loose pile of ideas.

### `clarify`
Reduces ambiguity in a request, makes assumptions explicit, and stabilizes the problem frame with natural transitions and minimal ceremony.

### `analyze`
Examines constraints, risks, dependencies, and cause-and-effect relationships, then ranks the real risks instead of treating every concern equally.

### `design`
Turns a chosen direction into an actionable structure, flow, component boundary, or interface shape while keeping open decisions and comparison basis visible.

### `decide`
Compares options with shared weighted criteria, gating constraints, and confidence notes so the final choice is easier to defend.

### `reflect`
Reviews a plan, decision, or design after the fact and audits whether the scorecard, assumptions, and confidence levels were actually sound.

## Suggested reading order

- Use `clarify` when the problem statement is still blurry.
- Use `brainstorm` when the solution space is still early and needs expansion.
- Use `analyze` when impacts, risks, or dependencies need to be understood.
- Use `design` when structure and flow need to be shaped.
- Use `decide` when one direction must be selected among alternatives.
- Use `reflect` when the quality of the current outcome needs to be tested.

## Runtime-facing projection files

If an end user wants Claude Code compatible command files, the supported path in this package is:

- start from `templates/commands/*.md`
- project or copy them into `.claude/commands/*.md`
- invoke them in the target runtime

That gives a usable runtime-facing format while preserving the repository root as the authoring source of truth.
