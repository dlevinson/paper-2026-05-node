# Package Status

Generated: 2026-05-11 20:17:00

## Stage 3 Status

- Row ID: `paper-2026-05`
- Preflight state: `ready_for_draft_package`
- Upload action: `code_only_candidate`
- Rights status: `likely_clear_with_provenance`

## What Was Staged

The draft package stages the SI TeX source, an extracted Python file containing the minimal `node()` function from the SI listing, and a small deterministic toy-network runner.

## License

The published Findings page identifies the paper license as CC BY-SA 4.0. This package applies the same CC BY-SA 4.0 license to the staged materials.

## Reproduction Scope

The added example runs the deterministic toy-network allocation from the paper text. The inspected SI TeX did not contain a full end-to-end script with plotting commands and stochastic-seed handling for every displayed paper artifact. That means the package should be described as a minimal implementation plus deterministic example, not as a full computational-reproduction archive.

## Remaining Decisions

1. Confirm whether this minimal implementation plus deterministic runner is the intended public deposit scope.
2. If exact reproduction of all displayed artifacts is desired, add a fuller runner for the figure and stochastic draw.
3. Keep publisher PDFs out of the upload package unless separate rights clearance exists.
