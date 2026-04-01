# Contributing

This package is the authoring-source home for the `thinkcraft` bundled skill family. Contributions should keep that role intact.

## Scope

- Keep changes inside this repository.
- Treat this package as source material for bundling, not as runtime code.
- Preserve the current structural model unless there is a clear package-level reason to change it.

## Content rules

- Canonical language is English (`en`).
- Keep skill section names exactly as written: `Goal`, `When to use`, `Inputs`, `Process`, `Output shape`, `Guardrails`, `Handoff`.
- Preserve the authoring-source vocabulary used across the package: `authoring source`, `bundled skill`, `manifest`, `mapping`.
- Keep prose direct, reviewable, and suitable for open-source readers who do not know the internal history of the package.

## Manifest and skill expectations

- Keep the `manifest.yaml` shape stable.
- Update manifest values in English when release-facing source text changes.
- Make sure each `skills/*.md` file still matches the manifest entry for that skill.
- Do not add runtime-specific implementation details to authoring documents unless the package scope changes intentionally.

## Release-facing files

Open-source releases of this authoring source are expected to keep the following files present:

- `README.md`
- `SKILLS.md`
- `manifest.yaml`
- `LICENSE`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `release-checklist.md`
- `docs/bundled-mapping.md`
- `docs/mvp.md`
- `skills/*.md`

## Review checklist

Before considering a contribution ready:

- confirm language consistency in English
- confirm skill section headings remain unchanged
- confirm the manifest still points to the correct source files
- confirm the source tree still reads as authoring source rather than runtime behavior
- confirm new wording stays compatible with MIT-licensed open-source publication
