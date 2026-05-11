# Replication Materials For Network Origin-Demand Estimation Using Percolation (NODE)

This is a draft package staged from the Stage 3 ready-to-package queue. It is private until the release scope is checked, but the license is aligned with the published paper.

## Citation

Levinson. (2026). Network Origin-Demand Estimation Using Percolation (NODE). Findings (2026). https://doi.org/10.32866/001c.147387

## Package Scope

This draft package contains the minimal Python NODE implementation extracted from the supplementary information TeX source. The paper is methodological and uses a toy network demonstration rather than a proprietary empirical dataset, so the appropriate public release boundary is code and explanatory provenance, not raw data.

## License

The published Findings page identifies the paper license as CC BY-SA 4.0. This package therefore uses the same Creative Commons Attribution-ShareAlike 4.0 International license. See `LICENSE`.

## Contents

- `code/node_minimal_from_si.py`: minimal NODE allocation function extracted from the SI code listing.
- `examples/toy_network_demo.py`: runnable deterministic toy-network example using the SI function.
- `source/si.tex`: source TeX copied from the local SI folder for provenance review.
- `metadata/CITATION.cff`: draft citation metadata.
- `metadata/PACKAGE_STATUS.md`: audit notes and remaining decisions.

## Reproduction Scope

The SI TeX source contains the core `node()` allocation function. This package adds a small deterministic toy-network runner that exercises that function and reproduces the deterministic allocation pattern reported in the paper. I did not find an end-to-end script in the inspected SI TeX that also regenerates every paper artifact, such as the figure graphic and the stochastic draw, with plotting commands and random seed handling.

## Suggested Use

Run:

```bash
python examples/toy_network_demo.py
```

Or import the function from `code/node_minimal_from_si.py` and provide origin supplies, destination capacities, and an OD cost dictionary. The function returns the allocation matrix and residual origin/destination capacities.

## Exclusions

Publisher PDFs and article proofs are not included. No third-party data or human-subject data are included.
