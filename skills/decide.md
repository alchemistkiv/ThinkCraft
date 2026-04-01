# decide

## Goal

Choose a defensible direction among multiple reasonable options by using explicit criteria and trade-off rationale.

## When to use

- More than one viable alternative exists.
- The basis for the decision needs to be written explicitly.
- Stakeholder preferences or priority conflicts are present.
- Direction selection needs to be finalized before implementation.

## Inputs

- Options to compare
- Decision criteria
- Constraints and acceptable risk level
- Analysis or design output, if available

## Process

1. Lead with the point: fix the decision context, the boundary of the decision, and the valid option list.
2. Separate gating constraints from scored criteria; if an option fails a hard constraint, mark it before scoring.
3. State the decision criteria clearly and add weights when relative importance matters.
4. Compare all options against the same criteria set; do not invent option-specific criteria.
5. Build a simple scorecard that shows weighted criteria, raw scores, weighted totals, and any gating failures.
6. Write each option's major advantage, cost, hard-to-reverse risk, and confidence note separately.
7. Mark uncertainties and unknowns that could change the decision outcome.
8. Select one direction; explain why it wins, why the others do not, which risks are being accepted consciously, and what confidence level the decision deserves.

## Output shape

- Decision summary
- Weighted criteria template
- Option-by-option scorecard
- Gating constraints
- Selected direction and rationale
- Consciously accepted risks
- Confidence notes

## Guardrails

- Write like a sharp teammate, not a consultant.
- Lead with the recommendation, then make the basis visible.
- Keep structure light unless a scorecard or constraint table materially improves the choice.
- Avoid obvious restatement, management-speak, and fake ceremony.
- Do not announce a conclusion without a rationale.
- Do not evaluate each option with different measures while implying a fair comparison.
- Do not hide uncertainty and present the decision as more certain than it is.
- Do not leave multiple winners and effectively postpone the decision.
- Do not use false precision; if weights or scores are rough, say they are rough.
- Do not list criteria without tying them back to the chosen outcome; the winning criteria must be visible.
- Do not drift back into analysis or design writing; if no selection will be made, say so and hand off explicitly.

## Handoff

After the decision, use `design` to shape the solution, `reflect` to test weak points in the choice, or `analyze` if deeper examination is still required.
