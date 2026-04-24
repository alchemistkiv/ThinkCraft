# Product Decision Workflow

This workflow shows how the six `thinkcraft` skills can support a product decision without turning the package into a runtime or planner.

Use it when a product idea, feature request, or roadmap item is still too loose to implement safely.

## Flow

```text
clarify -> brainstorm -> analyze -> decide -> design -> reflect
```

## 1. Clarify the request

Use `clarify` when the request could mean several different things.

Example input:

```text
We want ThinkCraft to support more advanced Claude Code workflows. What should we add first?
```

Expected output:

- clarified problem statement
- explicit assumptions
- in-scope and out-of-scope boundaries
- critical open questions

Carry forward only the stabilized problem frame. Do not start designing yet.

## 2. Open the option space

Use `brainstorm` to generate genuinely different directions.

Possible axes:

- projection automation
- validation depth
- usage documentation
- runtime integration guidance
- skill-set expansion

Expected output:

- grouped ideas
- one-line rationale per idea
- shortlist with quick scores
- two to four candidates worth analyzing

Do not pick a winner yet. The goal is to avoid choosing the first attractive idea too early.

## 3. Analyze shortlisted candidates

Use `analyze` to inspect constraints, dependencies, risks, and impact.

Questions to answer:

- Which candidate improves package reliability fastest?
- Which candidate could accidentally turn the repo into a runtime package?
- Which candidate is easiest to validate in CI?
- Which candidate is most useful to a new reader?

Expected output:

- analysis frame
- constraints and dependencies
- ranked risk table
- confidence notes
- recommendation-ready takeaways

## 4. Decide the next direction

Use `decide` when several reasonable candidates remain.

Example criteria:

| Criterion | Weight |
| --- | ---: |
| Protects source/projection boundary | 5 |
| Improves user trust | 4 |
| Easy to validate | 4 |
| Low maintenance cost | 3 |
| Helps real usage | 3 |

Expected output:

- gating constraints
- weighted criteria
- option scorecard
- selected direction
- accepted risks
- confidence level

## 5. Design the implementation shape

Use `design` after the direction is selected.

For example, if the selected direction is projection reliability, design the structure:

```text
scripts/project_disk_commands.py
        ↓
examples/project/.claude/commands/*.md
        ↓
tests/check_projection_drift.py
        ↓
.github/workflows/validate.yml
```

Expected output:

- design summary
- components and responsibilities
- flow description
- open decisions
- implementation starting point

## 6. Reflect before implementation or release

Use `reflect` on the resulting plan or PR.

Review questions:

- Did the decision stay within the authoring-source boundary?
- Does the change imply runtime behavior that the package does not own?
- Are projected files traceable back to source?
- Is the scoring too precise for the evidence?
- What would make this plan fail in real use?

Expected output:

- quality assessment
- weak assumptions
- parts that still hold
- corrections or follow-up actions

## When to stop

Stop after `reflect` when the next implementation step is clear enough for a small PR.

If major uncertainty remains, loop back only to the skill that addresses the gap:

- unclear request: `clarify`
- weak candidate set: `brainstorm`
- unknown risks: `analyze`
- unresolved choice: `decide`
- unclear implementation shape: `design`
