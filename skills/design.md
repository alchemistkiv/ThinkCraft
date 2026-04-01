# design

## Goal

Create an actionable solution structure, flow, component boundary, or interaction model for the selected direction.

## When to use

- The problem is clear enough and the solution now needs shape.
- Components, data flow, or responsibility boundaries must be defined.
- Structural clarity is needed before implementation starts.
- One of the alternatives needs to be made concrete at the design level.

## Inputs

- Clear problem statement
- Requirements and constraints
- Analysis findings
- Preferred direction or chosen strategy, if any

## Process

1. Lead with the point: fix the design goal, scope boundary, and success criteria.
2. Break the solution into major components, responsibility areas, or decision surfaces.
3. Map data, control, or user flows from start to finish.
4. Define what each component does, what it does not do, and which interface it exposes.
5. Collect critical trade-offs, open decision points, and dependent assumptions under separate headings.
6. For each open decision, state the comparison basis explicitly, such as `latency`, `complexity`, `operability`, `cost`, or `migration risk`.
7. Summarize the design with enough clarity to start implementation, but do not drop prematurely into code-level detail.

## Output shape

- Design summary
- Major components or sections
- Flow or interaction description
- Open decisions and assumptions
- Comparison basis for unresolved choices
- Starting point for implementation

## Guardrails

- Write like a sharp teammate, not a consultant.
- Lead with the design shape, then support it with structure and trade-offs.
- Keep structure light unless a matrix, flow, or grouped breakdown clearly helps.
- Avoid obvious restatement, management-speak, and bloated framing.
- Do not produce an abstract design that looks elegant but conflicts with real constraints.
- Do not leave component boundaries or responsibilities ambiguous.
- Do not treat a component list as a complete design when no flow has been described.
- Do not drop risks or dependencies discovered during analysis.
- Do not damage readability with unnecessary detail; keep design decisions separate from implementation notes.
- Do not present unresolved areas as settled; label open decisions explicitly.

## Handoff

Use `decide` if design alternatives still need a selection, `reflect` if the design needs a robustness check, or `analyze` if risk review is still incomplete.
