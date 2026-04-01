---
name: analyze
description: Examine constraints, risks, dependencies, and trade-offs.
argument_hint: Provide the topic, evidence, constraints, dependencies, and the questions that need answers.
source_package: thinkcraft
source_template: templates/commands/analyze.md
projection: disk-commands
runtime_compatibility: claude-code
---

# analyze

Use this command when the core direction exists but consequences and risk need to be understood.

## What to do

- Define the question being analyzed.
- Separate hard constraints from soft preferences.
- Map dependencies, failure modes, and second-order effects.
- Rank the meaningful risks instead of flattening them.
- Note evidence strength and uncertainty.

## Output

- Analysis frame
- Constraints and dependencies
- Ranked risk list
- Trade-off notes
- Recommended follow-up direction
