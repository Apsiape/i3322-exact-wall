# Exact I3322 quantum wall

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21782008.svg)](https://doi.org/10.5281/zenodo.21782008)

This repository contains a computer-assisted proof that the tensor-product and
commuting-operator suprema of the canonical three-setting, two-outcome
`I3322` Bell functional equal the rigorously characterized constant

```text
q* = 0.250875384513976536...
q* in [0.250875384513976535514, 0.250875384513976536486].
```

Neither model has a finite-dimensional maximizer. The certified bi-infinite
wall nevertheless defines an explicit normal vector-state maximizer on
`ell^2(Z) tensor ell^2(Z)` through the alternating Pal--Vertesi projectors.

Its centered finite sections obey an exact boundary-flux identity. If `Q_d`
is the unrestricted tensor-product optimum in local dimension at most `d`,
allowing binary POVMs, then the explicit wall truncations prove

```text
0 < q* - Q_d <= exp[-d log(R) + O(1)],
R = 1.07809205080209208....
```

Thus `log(1/epsilon)/log(R)+O(1)` local dimension is sufficient. A prospective
matching universal lower bound was blocked by adversarial review: its
near-fixed packet step lacks a localized-response/commutator estimate. The
subsequent coupled-sector repair forces a fixed amount of drift mass, but an
exact shared-factor countermodel shows that scalar packet norms lose the
multiplicity provenance needed at terminal near-entry.

Sprints 1240--1267 now provide an operator-valued restart. The response
remainders have been lifted to two-sided correspondences of the complete
Schmidt coefficient operator. Regularized Schmidt support gives a nested
ordered-flag filtration; Bellman contact controls its averaged left/right
mismatch without grids; and the amplitude cocycle acts exactly by translating
the logarithmic resolution scale. A hostile doppelganger proves that marginal
singular spectra alone remain insufficient, so a mixed flag/Wasserstein
distance records the relative gluing of the two responses. Differentiating the
filtration produces a canonical positive measure on ordered contact position
and logarithmic Schmidt resolution: its total mass is exactly Schmidt rank,
its first vertical moment is the flag-localized log-determinant potential, and
every regularized flag is one of its rectangles. A hostile control also
improved response stability from `1/t` to a dimension-free `1/sqrt(t)` law.
The two response actions now compose exactly on that measure; logarithmic cut
averaging charges the boundary flux; and the quarter wall has been rewritten
as a pointwise order-or-resolution displacement.  A new canonical positive
joint lift retains the complete Alice/Bob multiplicity provenance, and an
abstract finite monotone-flow theorem proves that rank-limited flows pay a
path endpoint or a fixed-point translation.  A charged shifted-grid theorem
now buys a common coarse source from the canonical joint coupling, and the
quarter wall survives that descent with an explicit diameter tax.  Hostile
transport controls show why neither total variation on rounded atoms nor
ordinary joint Wasserstein distance has the right information type.  The
complete ordered flag instead recovers the vertical translation bill from
synchronized prefix tails with only a linear rank factor.  The remaining gate
is to prove that the I3322 operator receipts control those synchronized
prefixes on the canonical carrier.  The canonical carrier is now covered over
every queried upper tail; trace normalization prices the upper vertical cap;
and one shared shifted grid gives common prefixes simultaneously to the two
original order coordinates and the two response outputs.  Lipschitz geometry
forces one vertical orientation inside every retained output cell, so hidden
multiplicity can no longer cancel the resolution debt.  A one-sided prefix
theorem now shows that the lower response flux is paid before, rather than
after, the linear rank cost of prefix recovery.  The remaining gate is to
localize the full operator response rectangles to the address-good carrier
while preserving their four-term telescoping cancellation.  Finite
differencing before localization now proves exactly that: address-bad mass
has a window-length cost independent of the number of cells.  The remaining
gate is to absorb that explicit window-weighted address bill, together with
the already controlled response and flux terms, into one final deficit
inequality. The
conditional constant ledger is retained as an open proof
campaign, but this repository
does **not** presently claim
`D(epsilon)=Theta(log(1/epsilon))`.

Consequently,

```text
C_q(3,3;2,2) != C_qs(3,3;2,2),
```

and `C_q(3,3;2,2)` is not closed. A separate Jordan-decomposition argument
proves that every binary scenario with at most two inputs on either side has
`C_q=C_qs` and is compact, so the three-input-per-party scenario is minimal by
input counts for both phenomena.

Archival identifiers: concept DOI
[`10.5281/zenodo.21782008`](https://doi.org/10.5281/zenodo.21782008); frozen
`v1.2.0` DOI
[`10.5281/zenodo.21782750`](https://doi.org/10.5281/zenodo.21782750); frozen
`v1.1.0` DOI
[`10.5281/zenodo.21782527`](https://doi.org/10.5281/zenodo.21782527); frozen
`v1.0.0` DOI
[`10.5281/zenodo.21782009`](https://doi.org/10.5281/zenodo.21782009).

The result resolves the conjectural value and finite-dimensional
nonattainment reported by Pal and Vertesi in 2010, and certifies their
infinite alternating construction as a spatial maximizer. It is not a claim
of priority for that construction or for general finite/infinite-dimensional
separation, which are known from earlier work.

Mghirbi's July 2026 release
[`10.5281/zenodo.21477901`](https://doi.org/10.5281/zenodo.21477901)
previously gave a proof-carrying exact enclosure of width below `10^-9`. The
present result closes that remaining interval and proves nonattainment; it is
not the first exact certified bound for I3322.

## Paper

- [Main manuscript](paper/manuscript.pdf)
- [Prospective v1.3.0 release notes](paper/RELEASE-NOTES-v1.3.0.md)
- [v1.2.0 release notes](paper/RELEASE-NOTES-v1.2.0.md)
- [v1.1.0 release notes](paper/RELEASE-NOTES-v1.1.0.md)
- [Technical supplement](paper/technical-supplement.pdf)
- [Readable manuscript source](paper/MANUSCRIPT.md)
- [Claim-to-certificate map](paper/CERTIFICATE-MAP.md)
- [Priority audit](paper/PRIORITY-AUDIT.md)
- [Independent frontier-model review and adjudication](review/README.md)

## Reproduce the certificate

The release was tested with CPython 3.13.12. Install the four pinned numerical
dependencies in a clean environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Quick custody and semantic verification:

```powershell
python certificate/release/verify_release.py
```

Complete production and independently implemented interval replay:

```powershell
python certificate/release/verify_release.py --full
```

The full replay regenerates every load-bearing receipt, including intermediate
cyclic, symmetrization, and operator-remainder guards. On the reference
workstation it takes several minutes. The independent path uses `mpmath.iv`
and a locally implemented rectangular complex-interval layer; it imports no
production Arb/FLINT module.

## Repository structure

- `paper/`: manuscript, supplement, normalization, scope, and priority record;
- `certificate/production/`: Arb/SymPy/NumPy proof dependencies and explicitly
  marked conditional lower-bound research;
- `certificate/independent/`: separate interval reconstruction;
- `certificate/release/`: manifest, replay entry point, and release audits.

The repository is deliberately standalone. It contains no dependency on the
broader private or public foundational-theory corpus from which the problem was
originally investigated.

## Computational disclosure

Frontier language models were used extensively for proof discovery,
implementation, adversarial auditing, and editorial assistance. Seth Douglas
assumes responsibility for this release. Every load-bearing computer-assisted
claim is mapped to replayable source and a frozen receipt.

## Author

**Seth Douglas**

[ORCID 0009-0007-4708-3252](https://orcid.org/0009-0007-4708-3252)

[apsiape@gmail.com](mailto:apsiape@gmail.com)

## License

Paper prose, figures, and PDFs are licensed under
[CC BY 4.0](LICENSES/CC-BY-4.0.txt). Executable source code is licensed under
the [BSD 3-Clause License](LICENSES/BSD-3-Clause.txt). See [LICENSE.md](LICENSE.md)
for the file-level boundary.
