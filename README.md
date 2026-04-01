# thinkcraft

Authoring-source package for portable thinking skills and Claude Code compatible command projections.

`thinkcraft` is a standalone repository that defines a small family of structured thinking skills as canonical source. It is designed for people who want a clean authoring layer first: stable skill text, normalized metadata, documented projections, and validation that keeps the package readable and portable.

## What It Is

- An authoring-source repository for six thinking skills: `brainstorm`, `clarify`, `analyze`, `design`, `decide`, `reflect`
- A canonical metadata model in `manifest.yaml`
- A documented source tree that can project into multiple delivery shapes without moving authorship into runtime files
- A portable package that treats Claude Code compatible command files as a projection, not as the source of truth
- A small validation layer for checking source structure and release readiness

## What It Is Not

- Not a runtime package
- Not an installer
- Not a package manager integration
- Not a registry, loader, or execution engine
- Not a command discovery implementation
- Not a tool-permission enforcement layer

This repository preserves the authoring identity of the package. It describes how source can project into runtime-facing forms, but it does not pretend to be the runtime itself.

## Skill Set

The package ships six thinking-oriented source skills with a shared structure and a consistent voice.

- `clarify` reduces ambiguity and stabilizes the request
- `brainstorm` opens the option space and carries forward a shortlist
- `analyze` examines constraints, dependencies, and ranked risks
- `design` shapes the chosen direction into a practical structure
- `decide` compares alternatives with explicit criteria and rationale
- `reflect` reviews whether the output, assumptions, and scorecard hold up after the fact

Every source skill keeps the same section skeleton: `Goal`, `When to use`, `Inputs`, `Process`, `Output shape`, `Guardrails`, `Handoff`.

## Source -> Projection -> Runtime Model

`thinkcraft` is organized around a three-layer model.

- `source`: the canonical authoring layer in this repository
- `projection`: deterministic output shapes derived from source
- `target runtime`: any host that consumes a projected artifact

In practice, that means:

- `manifest.yaml` and `skills/*.md` define the bundled skill authoring source
- `templates/commands/*.md` defines the canonical command-template source for disk-command projection
- `.claude/commands/*.md` is a Claude Code compatible projection shape, whether shown in `examples/project/` or copied into another repo

The important boundary is simple: projection files are useful delivery artifacts, but they are not the canonical source of the package.

## Quick Start

Read the repository as an authoring package first.

```bash
git clone <repo-url>
cd thinkcraft
python tests/validate_package.py
```

Then inspect the source-of-record files:

1. `README.md` for package position and release context
2. `manifest.yaml` for package and skill metadata
3. `skills/*.md` for canonical skill bodies
4. `templates/commands/*.md` for Claude Code compatible command-template source

## Try It In Claude Code Compatible Projects

If you want to try the projected command form in a Claude Code compatible project:

1. Start from `examples/project/.claude/commands/`
2. Copy one or more command files into your target project's `.claude/commands/` directory
3. Keep frontmatter and provenance fields intact
4. Invoke the command by name inside the target project

That workflow is intentionally projection-oriented. The copied command files are for usage in the target project, while this repository remains the authoring-source package.

## Repository Structure

```text
thinkcraft/
|- manifest.yaml
|- skills/
|- templates/commands/
|- adapters/
|- catalog/
|- schemas/
|- docs/
|- examples/project/
|- tests/
|- README.md
|- SKILLS.md
|- CHANGELOG.md
`- release-checklist.md
```

Key files and directories:

- `manifest.yaml` stores package identity and normalized skill metadata
- `skills/` stores canonical markdown instructions for the skill family
- `templates/commands/` stores canonical source templates for disk-command projection
- `adapters/` documents how source fields map into projection targets
- `catalog/` describes exported surfaces and skill indexing metadata
- `schemas/` defines validation contracts for manifest and command frontmatter shapes
- `docs/` captures architecture notes, projection guidance, release metadata, and portability boundaries
- `examples/project/` demonstrates the Claude Code compatible projection in a project-shaped layout
- `tests/validate_package.py` validates the source package rather than any runtime

## Validation

The repository includes a lightweight validator for the authoring source tree.

```bash
python tests/validate_package.py
```

It checks package metadata, source file references, required markdown sections, allowed tool names, and basic release-file presence. The validator is intentionally source-focused: it verifies the package shape without turning this repository into a runtime or installer.

## Roadmap

- Keep the six core thinking skills stable and internally consistent
- Strengthen projection documentation and provenance between source and exported shapes
- Expand validation coverage for schemas, projection metadata, and catalog alignment
- Add more release-facing documentation for standalone distribution and preview drops
- Explore additional thinking skills only after the current source model stays clean under real use

## Release Status

`thinkcraft` is at `v0.1.0` and should be treated as an early public preview of the authoring-source package.

- The source model is established and validated
- The repository is suitable for review, experimentation, and projection into Claude Code compatible command files
- Surface details can still evolve as the standalone package position hardens

See `docs/releases/v0.1.0-preview.md` for the standalone preview note and `CHANGELOG.md` for release history.

## License

Released under the MIT License. See `LICENSE`.
