# Example Project

This example shows the `disk-commands` projection of `thinkcraft`.

The files under `examples/project/.claude/commands/` are Claude Code compatible projection files. They are examples of runtime-facing command files, not the canonical source for the package.

## Try the flow

1. Copy one or more files from `examples/project/.claude/commands/` into your own project's `.claude/commands/` directory.
2. Keep the frontmatter intact so provenance and projection metadata stay visible.
3. Invoke the command by name in Claude Code.

Example flow:

```text
copy brainstorm.md -> .claude/commands/brainstorm.md -> invoke brainstorm
```

## Recommended usage order

- Start with `clarify` if the request is ambiguous.
- Use `brainstorm` to expand the option space.
- Use `analyze` to understand risks and constraints.
- Use `design` to structure the chosen direction.
- Use `decide` when one option must win.
- Use `reflect` to review the result after the fact.

## Source and projection reminder

The canonical authoring source remains in this repository.

- `skills/*.md` are canonical source for the bundled skill surface.
- `templates/commands/*.md` are canonical source for the disk-command surface.
- `.claude/commands/*.md` is a Claude Code compatible projection.

This example exists to show how an end user can copy projected command files into a project and try them immediately.
