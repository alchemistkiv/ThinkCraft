# MVP Boundary

For `thinkcraft`, the MVP provides the smallest consistent source format needed to author thinking-oriented bundled skill packages.

## MVP goals

- Define six thinking skills under one package.
- Use a shared markdown skeleton for every skill.
- Normalize metadata in `manifest.yaml`.
- Provide a field set that can map to the Rust `BundledSkill` structure.
- Preserve a runtime-independent source package.
- Establish a tree that can later be bundled, linted, and generated from.
- Make the package voice consistent: direct, plainspoken, structured, and teammate-like.
- Add lightweight numeric support where prioritization improves output quality.

## MVP scope

- package file tree
- skill texts
- manifest metadata
- mapping documentation
- concise package README

## Non-goals

- writing a runtime skill-loading mechanism
- changing or generating `bundled_skills.rs`
- implementing a skill selection algorithm
- building a tool permission enforcement layer
- adding localization, multilingual content, or a translation pipeline
- adding automatic linting, schema validation, or CI integration
- defining a prompt-orchestration runtime or planner behavior
- adding telemetry, analytics, or usage tracking

## Success criteria

The MVP is successful if:

- the package is readable on its own and understandable as authoring source
- all skill files follow the same structural skeleton
- the manifest carries the required fields for every skill
- the mapping document explains the conversion logic to Rust clearly
- the skill family sounds more like a sharp teammate than a consultant
- prioritization and scoring support are visible where they materially improve decisions

## Acceptance criteria

- `README.md` states clearly that the package is bundled skill authoring source rather than a runtime artifact.
- `SKILLS.md` explains the skill family in authoring-source terms and clarifies the usage distinction between skills.
- `skills/brainstorm.md`, `skills/clarify.md`, `skills/analyze.md`, `skills/design.md`, `skills/decide.md`, and `skills/reflect.md` all preserve the same section headings.
- The `Process` section in every skill contains staged, directive, traceable steps suitable for output review.
- The `Guardrails` section in every skill explicitly limits failure modes such as scope drift, unsupported inference, premature closure, and incorrect handoff.
- `manifest.yaml` remains semantically stable and keeps the same format structure.
- Documents across the package use `authoring source`, `bundled skill`, `manifest`, and `mapping` in a consistent way.
- Relevant skills explicitly steer tone toward direct, teammate-like writing and away from ceremonial framing, obvious repetition, and management-speak.
- `brainstorm` produces a shortlist with quick scores.
- `analyze` produces a ranked risk table with likelihood, impact, reversibility, and confidence.
- `design` makes open decisions and their comparison basis explicit.
- `decide` includes weighted criteria, a scorecard, gating constraints, accepted risks, and confidence notes.
- `reflect` audits scorecard quality, false precision, and criteria bias rather than only critiquing the final answer.

## Natural expansion areas after MVP

- adding a YAML schema or JSON schema
- writing a build-time validator
- adding a markdown section parser
- generating test fixtures or golden outputs
- adding more thinking skills such as `compare`, `critique`, `reframe`, or `synthesize`
