---
name: decide
description: Choose among viable options with explicit criteria.
argument_hint: Provide the options, criteria, relative weights, constraints, and risk tolerance.
source_package: thinkcraft
source_template: templates/commands/decide.md
projection: disk-commands
runtime_compatibility: claude-code
---

# decide

Use this command when multiple options remain viable and one direction must be selected.

## What to do

- List the real options.
- Define weighted criteria and gating constraints.
- Score each option consistently.
- Call out accepted risks and low-confidence judgments.
- Select one option and explain why it wins.

## Output

- Decision frame
- Weighted criteria
- Option scorecard
- Accepted risks and confidence notes
- Final recommendation
