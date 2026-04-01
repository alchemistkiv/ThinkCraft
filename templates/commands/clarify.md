---
name: clarify
description: Reduce ambiguity before committing to a problem frame.
argument_hint: Provide the request, ambiguous terms, known definitions, context, and open questions.
source_package: thinkcraft
source_template: templates/commands/clarify.md
projection: disk-commands
runtime_compatibility: claude-code
---

# clarify

Use this command when the request is underspecified or mixes several possible meanings.

## What to do

- Restate the request in plain language.
- Identify ambiguous words, missing constraints, and hidden assumptions.
- Separate facts from inferred intent.
- Propose the most likely interpretations.
- Recommend a tighter problem frame that can be used for the next step.

## Output

- Clear request restatement
- Ambiguity list
- Assumptions and confidence notes
- Recommended clarified framing
- Next suggested command if applicable
