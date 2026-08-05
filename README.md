# Exact I3322 quantum wall

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21782008.svg)](https://doi.org/10.5281/zenodo.21782008)

> **Certificate status alert (2026-08-04).** A post-release exact Arb audit
> found a load-bearing global-amplitude mismatch in the Bellman upper-bound
> assembly. The complete unique-root bracket gives a mismatch in
> `[0.00014027592551842303, 0.00017894047518170395]`, excluding zero. The
> numerical candidate is not thereby disproved, but the headline optimum,
> nonattainment, separation, and nonclosure claims are **not presently closed
> by this certificate**. See
> [`paper/CERTIFICATE-STATUS-ALERT.md`](paper/CERTIFICATE-STATUS-ALERT.md) and
> Sprint 1285. A separate `mpmath.iv` engine independently reconstructs the
> exclusion. Frozen DOI releases are preserved as historical records while the
> proof is repaired.

**Rigorous partial repair at repository HEAD.** Sprints 1287 and 1290 prove, from a
committed 6,401-knot rational Bellman subsolution and an exact abstract
operator weld,

```text
omega_tensor <= omega_commuting <= 0.250875494588345
```

with the upper endpoint interpreted as an exact decimal. Sprint 1290 obtains
this sharper value by exactly optimizing the already committed witness on a
`10^-15` grid. It is an unconditional
upper bound, but it does not restore exact equality, nonattainment, spatial
separation, or nonclosure. See
[`SHARPENED-RIGOROUS-I3322-WINDOW.md`](certificate/production/foundational-sprint-1290/SHARPENED-RIGOROUS-I3322-WINDOW.md).

Sprint 1292 installs an explicit 255-dimensional strategy, certifies it with
rational square-root floors, and independently reconstructs it at 160-digit
interval precision. Together the certificates give the unconditional window

```text
0.2508753845015185 < omega_tensor
                   <= omega_commuting <= 0.250875494588345,
```

of width below `1.101e-7`. See
[`RIGOROUS-DIMENSION-255-LOWER.md`](certificate/production/foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md).

The historical release claimed a computer-assisted proof that the tensor-product and
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

Sprints 1240--1270 now provide an operator-valued restart. The response
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
inequality.  A two-resolution Bellman scout now identifies a sharper possible
replacement: the intrinsic diagonal drift appears to have exactly three
simple zeros, producing four sign chambers whose boundary points are uniformly
separated from horizontal coalescence.  This would replace the fine grid by a
constant-complexity partition.  A first shooting-atlas reconstruction failed
because it propagated the local chart beyond its reflection section; that
failure is retained as a negative receipt.  The exact reverser
`R(x,y,u)=(-y,-x,1/v)` now repairs the ancestry: all three symbolic reverser
residuals vanish, and the corrected 18-chart numerical atlas independently
recovers the same three roots on the symmetric active carrier.  The root count
is still not claimed until a full-domain interval certificate lands.  A
hostile normalization audit then killed the tempting shortcut
`F(x)F(-x)=b(x)^2`: the exact characteristic reverser does not transport the
global Bellman normalization for free.  The corrected exact accounting uses
the positive defect `K(x)=F(x)F(-x)/b(x)^2`, so the drift contains an explicit
branch-gluing term rather than being the raw reflection residual.  Exact
algebra identifies `K` as the tariff in both geometric symmetrization and the
reflected Bellman comparison.  A two-resolution hostile scout then separates
that tariff from the cocycle drift: its zeros do not coincide with the two
outer drift walls.  Thus the interval campaign must carry both structures;
neither is a reparameterization of the other.  The resulting proof target is
now log-free: the drift has the exact sign and zeros of
`D(x)=F(x)F(P(x))-F(-x)F(-P(x))`.  Two independent numerical resolutions
recover the same three roots with no sign disagreement, but the full-domain
Arb zero-count certificate remains open.  Two attempted shooting-atlas
shortcuts are now rejected: choosing the least characteristic sheet produces
15 false roots, while first filtering by positive local `P'` loses boundary
coverage.  The remaining proof must enclose the globally selected Bellman
fixed point itself; local value and local Morse type do not encode its boundary
condition.  A max-plus Lyapunov scout suggested a possible global replacement:
although the unweighted Bellman derivative amplifies locally by as much as
`1.264`, a positive weight of dynamic range below `5.5` makes both sampled
response graphs `0.9`-contractive.  The fine discretization splits the plateau
into two adjacent self-loops.  The canonical continuous predecessor-debt lift
then failed its preregistered resolution-stability gate: its two potentials
differ by `0.25235` against a `0.005` allowance because nearby trajectories
spend different numbers of iterates at a locally expanding negative
bottleneck.  The weighted-norm route is therefore unresolved, not viable, and
the next gate is to distinguish a true parabolic contact from a strict transit
gap in a higher-resolution continuous reconstruction.  A memory-safe ordered
lower-envelope engine now matches the dense operator to `8.9e-16` and extends
the ladder to 12,801 nodes.  The negative transit gap falls to `5.46e-5` while
the local multiplier remains `1.162`, meeting a preregistered
parabolic-contact-consistent classification.  This is evidence that the
contraction architecture is structurally obstructed, but neither the limiting
contact nor the obstruction is claimed without interval certification.  No
sampled contraction is promoted to a theorem.  A hostile grid-phase attack
then keeps all nine nearby-resolution gaps below `1.23e-4`, and deeper
25,601/51,201-node runs give `6.95e-5`/`2.18e-5`, with multiplier above
`1.1616`.  After that preregistered run, Bellman equality and envelope
stationarity exposed the conditional algebraic contact equation
`4x^4-(4q+5)x^2+(q+2)=0`; its outer negative root is
`-0.87827294518`.  The conditional normal form now has an exact symbolic and
Arb certificate, with candidate multiplier `1.1622824700`.  Its 51,201-node
value and derivative match to `4.95e-9` and `6.25e-5`, while the sampled
argmin misses its preregistered gate—an expected ill-conditioning at a
parabolic contact.  A cross-certificate audit then identifies the candidate
exactly: it is the reversed image `(-C,-C,1/R)` of the already certified high
plateau `(C,C,R)`.  Its derivative multiplier is exactly `R^2>1`, so no
bounded positive weighted sup norm can make the global Bellman derivative a
contraction.  The sampled contractions were discretization artifacts.  The
remaining three-root campaign must evaluate the certified characteristic
graph directly by interval sign or degree methods.  A selector collision then
shows that the local shooting amplitude and global boundary-iteration profile
differ by `1.15e-3`, shifting the outer drift root by `1.77e-3`.  The local
atlas also misses Bellman contact by `1.62e-4`, versus `2.97e-8` for the global
iteration.  Thus the exact graph must be equipped with explicitly certified
global normalization transitions before it can support the interval root
count; reversible local amplitudes are not enough.  A three-order consistency
audit then finds a persistent `1.624859e-4` reflected source/target amplitude
mismatch despite `3.9e-16` raw Bellman residuals and `1.2e-15` target overlap
agreement.  This exposes an unchecked normalization gate in the aligned-wall
certificate stack.  It is not yet a theorem retraction: an Arb
matched-coordinate exclusion is the immediate adjudication gate. The
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
