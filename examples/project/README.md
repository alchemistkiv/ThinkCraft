# Example Project Projection

This directory shows the `disk-commands` projection of `thinkcraft` in a project-shaped layout.

The files under `examples/project/.claude/commands/` are Claude Code compatible command files. They are runtime-facing projection examples, not canonical package source.

## What this example demonstrates

- How projected command files can appear inside a compatible project
- How provenance and frontmatter can stay visible in copied command files
- How the authoring-source package stays separate from the project that consumes the projection

## Try it in a compatible project

1. Copy one or more files from `examples/project/.claude/commands/` into your target project's `.claude/commands/` directory.
2. Keep the frontmatter intact.
3. Invoke the command by name in the target project.

```text
examples/project/.claude/commands/brainstorm.md
-> target-project/.claude/commands/brainstorm.md
-> invoke brainstorm
```

## Recommended command flow

- Start with `clarify` when the request is ambiguous
- Use `brainstorm` to expand candidate directions
- Use `analyze` to examine risks and constraints
- Use `design` to shape the selected direction
- Use `decide` when one option must win
- Use `reflect` to audit the result afterward

## Source reminder

The canonical source for this package still lives outside this example:

- `skills/*.md` for bundled-skill source
- `templates/commands/*.md` for command-template source
- `manifest.yaml` for normalized metadata

This example exists to demonstrate projection usage without changing the package's authoring-source identity.
