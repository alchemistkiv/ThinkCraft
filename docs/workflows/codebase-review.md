# Codebase Review Workflow

This workflow shows how `thinkcraft` can guide a structured review of a repository, package, or implementation plan.

It is intentionally source-oriented. It does not assume ThinkCraft can inspect or execute code by itself. The target runtime or user provides repository context, files, diffs, logs, or observations.

## Flow

```text
clarify -> analyze -> decide -> design -> reflect
```

Use `brainstorm` only when the review reveals multiple possible improvement directions and the option space needs to open again.

## 1. Clarify the review target

Use `clarify` to define what is being reviewed.

Example input:

```text
Review this repository and tell me what to improve before publishing it.
```

Clarify:

- whether the review is about product fit, code quality, package structure, docs, release readiness, or runtime behavior
- which files or folders are in scope
- what quality bar matters
- which risks would actually change the next step

Expected output:

- review target
- scope boundary
- assumptions
- critical questions

## 2. Analyze structure and risk

Use `analyze` once the target is clear.

Review dimensions:

| Area | What to inspect |
| --- | --- |
| Source structure | Is the source of truth clear? |
| Projection paths | Can generated or copied artifacts drift? |
| Validation | Are important contracts checked automatically? |
| Docs | Can a new reader understand what the repo is and is not? |
| Release readiness | Are changelog, license, metadata, and examples aligned? |
| Maintenance | Are there manual sync points likely to break? |

Expected output:

- key findings
- ranked risk table
- confidence notes
- concrete improvement candidates

## 3. Decide what to fix first

Use `decide` when the analysis produces several possible improvements.

Example options:

- add projection generator
- add projection drift check
- add CI validation workflow
- add workflow examples
- expand skill set
- add runtime integration docs

Example gating constraints:

- must not turn the repo into a runtime
- must preserve source/projection separation
- must be understandable without private context
- must be small enough for a focused PR

Expected output:

- selected fix bundle
- rejected alternatives
- accepted risks
- confidence notes

## 4. Design the change set

Use `design` to turn the selected fix bundle into a concrete PR shape.

Example structure:

```text
scripts/project_disk_commands.py        # refreshes projected example commands
tests/check_projection_drift.py         # fails if projection is stale
.github/workflows/validate.yml          # runs validation in CI
docs/workflows/*.md                     # shows practical usage flows
```

For each file, define:

- responsibility
- what it should not do
- how it connects to existing source
- how it will be validated

Expected output:

- PR structure
- file responsibilities
- implementation notes
- open decisions

## 5. Reflect on the review result

Use `reflect` before merging or publishing.

Review questions:

- Did the PR fix the highest-priority weakness?
- Did it introduce more machinery than the package needs?
- Does it keep the repo runtime-independent?
- Does it make future drift easier to detect?
- Would a new contributor know how to use the change?

Expected output:

- what improved
- what remains weak
- next follow-up PRs
- merge confidence

## Good output shape for a repository review

```text
Top finding:
- ...

Risks:
- ...

Recommended first PR:
- ...

Files to change:
- ...

What not to do yet:
- ...

Follow-up later:
- ...
```

## Common traps

- Turning every observation into a fix
- Expanding scope from review into full rewrite
- Treating docs, examples, generator, runtime, and registry as one PR
- Adding a runtime before the source package has stable projection contracts
- Reviewing everything at the same severity
