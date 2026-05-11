# Replication Materials For Network Origin-Demand Estimation Using Percolation (NODE)

This is a draft package staged from the Stage 3 ready-to-package queue. It is not yet an uploaded release.

## Citation

Levinson. (2026). Network Origin-Demand Estimation Using Percolation (NODE). Findings (2026). https://doi.org/10.32866/001c.147387

## Package Scope

This draft package contains the minimal Python NODE implementation extracted from the supplementary information TeX source. The paper is methodological and uses a toy network demonstration rather than a proprietary empirical dataset, so the appropriate public release boundary is code and explanatory provenance, not raw data.

## Contents

- `code/node_minimal_from_si.py`: minimal NODE allocation function extracted from the SI code listing.
- `source/si.tex`: source TeX copied from the local SI folder for provenance review.
- `metadata/CITATION.cff`: draft citation metadata.
- `metadata/LICENSE_REVIEW_NEEDED.txt`: license/status note before public upload.
- `metadata/PACKAGE_STATUS.md`: audit notes and remaining decisions.

## Important Gap

The SI states that minimal code is included to reproduce the figure, deterministic table, and a stochastic draw. The TeX file inspected here contains the minimal `node()` allocation function, but I did not find a standalone figure/table/stochastic reproduction script or toy-network runner in the SI TeX source. Before upload, decide whether this package should be described narrowly as the extracted minimal implementation, or whether a fuller reproduction script should be added.

## Suggested Use

Import the function from `code/node_minimal_from_si.py` and provide origin supplies, destination capacities, and an OD cost dictionary. The function returns the allocation matrix and residual origin/destination capacities.

## Exclusions

Publisher PDFs and article proofs are not included. No third-party data or human-subject data are included.
