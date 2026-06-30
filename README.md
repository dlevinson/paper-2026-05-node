# Replication Materials For Network Origin-Demand Estimation Using Percolation (NODE)

## Contribution

This paper introduces NODE, a deterministic, cost-ordered method for constructing origin–destination matrices while respecting destination opportunity constraints. Using shortest-path network costs and a reproducible allocation order, it provides a computationally transparent alternative to fitted gravity and utility models and clarifies when its expected flows resemble conventional trip-distribution forms.

This package is registered as uploaded to the public GitHub repository: https://github.com/dlevinson/paper-2026-05-node. Upload scope is governed by `PACKAGE_MANIFEST.csv`, with paper PDFs retained as local reference-only assets.

## Citation

Levinson. (2026). Network Origin-Demand Estimation Using Percolation (NODE). Findings (2026). https://doi.org/10.32866/001c.147387

## Package Scope

This draft package contains the minimal Python NODE implementation extracted from the supplementary information TeX source. The paper is methodological and uses a toy network demonstration rather than a proprietary empirical dataset, so the appropriate public release boundary is code and explanatory provenance, not raw data.

## License

The published Findings page identifies the paper license as CC BY-SA 4.0. The operative root license is `LICENSE.md`, which applies the same Creative Commons Attribution-ShareAlike 4.0 International license to the repository's author-created code, scripts, documentation, and derived materials. The full text is also in `data/LICENSE`.

The published paper PDF in `paper/` and any third-party source materials retain their original terms and are not relicensed here.

## Contents

- `code/node_minimal_from_si.py`: minimal NODE allocation function extracted from the SI code listing.
- `code/legacy/examples/toy_network_demo.py`: runnable deterministic toy-network example using the SI function.
- `code/legacy/source/si.tex`: source TeX copied from the local SI folder for provenance review.
- `metadata/CITATION.cff`: draft citation metadata.
- `metadata/PACKAGE_STATUS.md`: audit notes and remaining decisions.

## Reproduction Scope

The SI TeX source contains the core `node()` allocation function. This package adds a small deterministic toy-network runner that exercises that function and reproduces the deterministic allocation pattern reported in the paper. I did not find an end-to-end script in the inspected SI TeX that also regenerates every paper artifact, such as the figure graphic and the stochastic draw, with plotting commands and random seed handling.

## Suggested Use

Run:

```bash
python code/legacy/examples/toy_network_demo.py
```

Or import the function from `code/node_minimal_from_si.py` and provide origin supplies, destination capacities, and an OD cost dictionary. The function returns the allocation matrix and residual origin/destination capacities.

## Exclusions

Publisher PDFs and article proofs are not included. No third-party data or human-subject data are included.



<!-- published-paper-reference:start -->
## Published Paper Reference

- Local published/final PDF reference: `paper/00_published_reference_node_percolation.pdf`
- Official published source: https://findingspress.org/article/147387
- Official PDF/source link: https://findingspress.org/article/147387.pdf
- Paper-reference note: Findings published PDF.
<!-- published-paper-reference:end -->

<!-- package-hardening-status:start -->
## Package Hardening Status

Generated: 2026-05-20 12:05:29 AEST

- Pipeline: `UPLOADED`
- Sidecars added/updated: `PACKAGE_STATUS.md`, `PACKAGE_MANIFEST.csv`, `LICENSE_STATUS.md`.
- Paper reference copies are for local audit convenience and are not public-upload assets without rights review.
- Existing private GitHub repository: https://github.com/dlevinson/paper-2026-05-node.
<!-- package-hardening-status:end -->
