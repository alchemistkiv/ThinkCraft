# analyze

## Goal

Examine constraints, dependencies, risks, cause-and-effect relationships, and technical impacts in a systematic way.

## When to use

- You need to understand why an approach is suitable or unsuitable.
- A root-cause, impact-area, or trade-off review is needed.
- You need structured reasoning before making a decision.
- Risk and cost visibility are still low.

## Inputs

- Situation, plan, or alternative to examine
- Current evidence, observations, or data points
- Known constraints
- Evaluation criteria

## Process

1. Lead with the point: define the analysis target, the main question, and the evaluation boundary.
2. Separate evidence, observations, and assumptions; do not combine data and interpretation in one point.
3. Break down constraints, dependencies, and affected areas under clear headings.
4. For each major finding, explain the cause-effect chain or impact mechanism; do not leave the why unstated.
5. Build a ranked risk table using `likelihood`, `impact`, `reversibility`, and `confidence`; sort the table so the highest-priority risks are obvious.
6. Call out low-confidence conclusions separately so weak evidence does not look settled.
7. Reduce the analysis into explicit insights that can feed the next decision or design step; keep unresolved unknowns separate.

## Output shape

- Analysis frame
- Key findings
- Ranked risk table
- Uncertainties and confidence level
- Clear takeaways for the design or decision stage

## Guardrails

- Write like a sharp teammate, not a consultant.
- Lead with the answer or risk signal, then show the supporting chain.
- Keep structure light unless a table or grouped list genuinely improves readability.
- Avoid obvious restatement, management-speak, and padded theory.
- Do not blur the boundary between evidence, assumption, and interpretation.
- Do not present all findings with equal weight; the analysis is not complete without prioritization.
- Do not use certainty language without evidence; if confidence is low, say so.
- Do not mistake list-making for analysis; explain cause-effect or impact mechanics.
- Do not weaken decision support with unnecessary theory, history, or abstraction.
- Do not slide into making the decision while analysis is still incomplete; if a choice is needed, hand off to `decide`.

## Handoff

Move to `design` if the structure of a solution must be defined, to `decide` if one option must be chosen, or back to `clarify` if the problem statement is still blurry.
