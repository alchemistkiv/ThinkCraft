# reflect

## Goal

Review an existing thinking output after the fact to expose gaps, weak assumptions, quality risks, and the next improvement steps.

## When to use

- A plan, decision, or design is complete but still needs a quality check.
- A fast decision needs its rationale reviewed again.
- You need to test for missing risks, skipped assumptions, or weak logic.
- The quality of the thinking needs inspection before the next step.

## Inputs

- Output to review
- Target or success criteria
- Known risks
- Suspicious areas, if any

## Process

1. Lead with the point: fix the target, quality bar, and review boundary for the output.
2. Separate the output's claims, evidence, assumptions, conclusions, and any scorecard logic it relies on.
3. Look for missing evidence, skipped scenarios, weak links, overconfident language, and criteria bias.
4. Audit any scorecard or ranking method: check whether the criteria, weights, and cutoffs match the real decision.
5. Run a false-precision check so rough judgment is not dressed up as exact arithmetic.
6. Test when the output would break or stop being valid by using inverse or stress scenarios.
7. Prioritize findings by impact; do not present cosmetic issues at the same level as structural risk.
8. Close with what still holds, what must be corrected, and which follow-up actions should happen next.

## Output shape

- Short quality assessment
- Identified gaps or weak points
- Parts that remain valid
- Corrections or follow-up actions
- Scorecard audit and false-precision check

## Guardrails

- Write like a sharp teammate, not a consultant.
- Lead with the strongest finding, then explain what it changes.
- Keep structure light unless the audit needs a table or checklist to stay clear.
- Avoid obvious restatement, management-speak, and performative critique.
- Do not stop at criticism without producing actionable follow-up.
- Do not overemphasize small formatting issues while hiding the real risks.
- Do not notice unsupported areas and still wave them through as good enough.
- Do not hide the need for fresh analysis, decision work, or design revision; hand off clearly when needed.
- Do not settle for reflex approval or a shallow quality pass; actually test the assumption-evidence-conclusion chain.
- Do not confuse precise-looking numbers with trustworthy reasoning; challenge unjustified scoring.
- Do not default to invalidating the entire output; call out the parts that remain solid.

## Handoff

Use `clarify` if the gap is in the problem definition, `analyze` if technical review is missing, `decide` if the choice must be reconsidered, or `design` if the solution structure needs revision.
