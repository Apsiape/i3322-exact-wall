# The I3322 quantum value: attainment and dimension complexity

Seth Douglas · [ORCID](https://orcid.org/0009-0007-4708-3252)

## Start here

- [Current paper](paper/resolution.pdf) and [LaTeX source](paper/resolution.tex).
- [Verification and precise proof coverage](VERIFY.md).
- [Corrections and historical-document precedence](paper/REVISION-NOTES.md).
- [Certificate dependency map](paper/CERTIFICATE-MAP.md).
- [Release procedure](paper/ARXIV-SUBMISSION.md).

Version 4.1.0 is the revised proof and verification snapshot, archived at
[DOI 10.5281/zenodo.22698978](https://doi.org/10.5281/zenodo.22698978).
The published tag and archive are immutable. The main branch additionally
includes a citation-only DOI update and rebuilt PDF; its bytes differ from
the archived PDF, but its mathematical content is unchanged.
Historical v4.0.0 is
permanently identified by [DOI 10.5281/zenodo.22099128](https://doi.org/10.5281/zenodo.22099128).
The [concept DOI](https://doi.org/10.5281/zenodo.21782008) identifies the version
family, not unarchived working files. [Release decisions](release/RELEASE-DECISIONS.json)
are separate from successful verification.

## Results and scope

For the Collins--Gisin normalization, the paper establishes finite-dimensional
nonattainment of the quantum supremum S, spatial attainment on l2(Z) tensor
l2(Z), and D(epsilon) = Theta(log(1/epsilon)). The constructive upper
coefficient is 23.9010650 for all sufficiently small epsilon, with natural
logarithms; no explicit onset or sharp constant is claimed. Binary POVMs and
mixed states are included without dimension increase in the reduction.

The proofs use a certified common tensor/commuting value and a rational window;
the exact value beyond that window is not identified. Mghirbi's prior
enclosures and related dynamics, and concurrent work by Pauwels and Coladangelo,
are cited. Pauwels' Theorem 1 identifies the supremum of the full finite
Pal--Vertesi family with the finite quantum supremum; that question is not open.
A prescribed numerical parameter sequence is a different object.

Lean checks **37 selected declarations**, using standard axioms only, not the
complete analytic theorem. Convex-envelope regularity, orbit disintegration,
signed-potential existence and the quantum-to-flow reduction remain analytic.
Finite tests and repeated audits do not replace those proofs.

## Repository layout

| Path | Purpose |
|---|---|
| `paper/resolution.tex`, `paper/LOWER-BOUND-REVISION.tex`, `paper/resolution.pdf` | Current manuscript |
| `certificate/production/lower-weighted-flow/` | Current lower-proof controls |
| `certificate/production/`, `certificate/independent/` | Preserved sources and historical evidence; use the dependency map |
| `lean/I3322Kernel/` | Pinned selected formal lemmas |
| `tools/` | Bounded verification and release-integrity tools |
| `release/` | Source manifest and explicit release decisions |

Older manuscripts, companion PDFs, status files and release notes remain for
provenance, **not as alternative current papers**. The correction notes name
superseded arguments. Local audit prompts, orchestration, builds and dependency
caches are ignored. Scientific certificate history has not been deleted.

Paper/documentation: CC BY 4.0. Executable Python/Lean code: BSD 3-Clause.
See [LICENSE.md](LICENSE.md). Contact: [apsiape@gmail.com](mailto:apsiape@gmail.com).
