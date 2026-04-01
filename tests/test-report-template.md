# Validation Test Report Template

## Run Metadata

- Date:
- Operator:
- Package path:
- Validator command:
- Python version:

## Expected Result

- [ ] Exit code `0` for the package
- [ ] Readable report generated
- [ ] Warnings separated from errors

## Package Validation

- Status:
- Exit code:
- Error count:
- Warning count:
- Notes:

## Fixture Checks

### invalid-manifest-missing-source.yaml

- Status:
- Expected: parse succeeds, validation fails when `source_file` is missing or invalid in a manifest-derived scenario
- Notes:

### invalid-skill-missing-section.md

- Status:
- Expected: validation fails because at least one required markdown section is missing
- Notes:

### valid-minimal-skill.md

- Status:
- Expected: markdown section validation succeeds
- Notes:

## Follow-up Actions

- None
