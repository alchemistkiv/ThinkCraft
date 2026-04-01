---
name: brainstorm
description: Expand candidate directions before narrowing to one.
argument_hint: Provide the topic, goal, context, constraints, and any rejected ideas.
source_package: thinkcraft
source_template: templates/commands/brainstorm.md
projection: disk-commands
runtime_compatibility: claude-code
---

# brainstorm

Use this command when the solution space is still too narrow.

## What to do

- Restate the problem frame in one sentence.
- Separate fixed constraints from changeable assumptions.
- Generate at least three genuinely different idea axes.
- Produce concrete candidates under each axis.
- Remove duplicates and weak variants.
- Carry forward a shortlist with quick `novelty`, `feasibility`, and `expected upside` scores.

## Output

- Short problem frame
- Grouped idea list
- One-line rationale per idea
- Shortlist with light scoring
- Best candidates to analyze next
