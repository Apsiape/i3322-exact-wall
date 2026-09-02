# Exact I3322 quantum wall

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21782008.svg)](https://doi.org/10.5281/zenodo.21782008)

## Start here

**Want to check the claims yourself? [VERIFY.md](VERIFY.md)** — every
claim mapped to a runnable check with its expected output, what each
layer does and does not verify, and suggested 15-minute / 2-hour /
full-audit reading paths.

**The paper: [paper/resolution.pdf](paper/resolution.pdf)** — *"The
I3322 quantum value is attained spatially but not in finite dimension"*.
One document, all three results: both attainment theorems, the
dimension-complexity theorem (its Section 5), proof architecture, claim
boundaries, correction history, and full citations. (The rate result
previously lived in a standalone companion note; it was folded into the
paper on 2026-08-25, and the standalone note is preserved in the frozen
v3.3.0 release, DOI
[`10.5281/zenodo.21843326`](https://doi.org/10.5281/zenodo.21843326).
`paper/rate-companion.tex` is now a supersession notice.)

**What is proved.** Let `S` denote the common I3322 quantum value,
certified unconditionally in the window
`0.2508753845015185 < S <= 0.250875388108398` (width `3.607e-9`).

1. **Theorem (N)** — no finite-dimensional quantum strategy (any local
   dimensions, mixed states, POVMs) attains `S`. This proves the
   conjecture of Pal–Vertesi (2010). Their separate *assertion* of
   infinite-dimensional attainment is Theorem (S), established on an
   independent route.
2. **Theorem (S)** — `S` **is** attained by a spatial strategy
   on `ell^2(Z) (x) ell^2(Z)`.
3. **Corollaries** — the quantum correlation set `C_q(3,3;2,2)` is
   **not closed**, and `C_qs \ C_q` is nonempty, at the smallest venue
   by input count, among two-outcome bipartite scenarios, in which
   nonclosure is known. No minimality is claimed over scenarios with
   larger output alphabets.
4. **Theorem (Rate)** (paper, Section 5) —
   `D(epsilon) = Theta(log(1/epsilon))`: reaching `S` to accuracy
   `epsilon` requires and suffices local dimension of order
   `log(1/epsilon)`, with explicit derived constant `23.9010650` on the
   upper half.

**Where the evidence lives:**

- [Theorem (N) certificate directory](certificate/production/theorem-N-four-receipts-at-S/)
  — signed statement, proof documents, three rounds of adversarial
  review, exact-arithmetic guards.
- [Theorem (S) certificate directory](certificate/production/theorem-S-spatial-attainment-at-S/)
  — proof documents and review record.
- [Rate certificate directory](certificate/production/rate-theta-log/)
  — the sealed lower-bound chain and the upper-bound bundle, each with
  its complete audit record.
- [Machine-checked cores (Lean 4 + Mathlib)](lean/I3322Kernel/) — the
  paper's displayed formulas, no `sorry`, standard axioms only.
- [Replayable window certificates](certificate/release/) — run
  `python certificate/release/verify_release.py` (details below).
- [Claim-to-certificate map](paper/CERTIFICATE-MAP.md) and
  [independent review records](review/).

**What is not claimed.** Two things remain open: the exact value of
`S` beyond its certified window, and whether the Pal–Vertesi family in
particular converges to `S`. The window itself is a certified *input*
to this work, not a contribution of it — Mghirbi's July 2026 release
gave a tighter enclosure, and it is cited as prior art. Earlier
releases of this repository claimed an exact identification; that
claim was refuted by this project's own audit, publicly decertified,
and the present theorems were rebuilt on independent routes. The full
correction history is preserved below and in the frozen DOI releases —
it is part of the record, not an embarrassment to be hidden.

> ⚠ **Everything below this line is a historical provenance narrative,
> written in chronological sprint-numbered layers as the campaign ran.
> It is NOT the current claim set, and individual paragraphs in it
> assert things that were later refuted by this project's own audits —
> including the bi-infinite "wall" construction and the exact constant
> `q*`. The current claims are the four items above and the paper.
> The layers are retained so every claim's history is auditable.**

---

> **Finite-dimensional nonattainment and nonclosure restored (v3.0.0,
> 2026-08-05).** The Sprint-1285 audit that decertified the historical
> headline stands. A new, independent proof route now re-establishes the two
> corollaries at the current common value: **no finite-dimensional quantum
> strategy attains the I3322 supremum `S`, and `C_q(3,3;2,2)` is not
> closed.** The proof survived three rounds of independent refutation-first
> adversarial review; the final round signed the statement and its exact
> dependency list. See
> [`certificate/production/theorem-N-four-receipts-at-S/`](certificate/production/theorem-N-four-receipts-at-S/)
> (signed statement, complete proof documents, review record, and
> algebraic/exact-arithmetic guards). A second
> reviewed theorem establishes **spatial attainment of
> `S`** on `ell^2(Z) tensor ell^2(Z)`, hence
> **`C_qs(3,3;2,2) \ C_q(3,3;2,2)` is nonempty**; see
> [`certificate/production/theorem-S-spatial-attainment-at-S/`](certificate/production/theorem-S-spatial-attainment-at-S/).
> The decertified historical amplitude route is not repaired but dissolved:
> amplitudes are read off an existing conditional spectral measure, so the
> failed compatibility equation is never posed. The exact optimum
> (identification of `S` beyond its certified `3.61e-9` window) remains
> **open** and is not claimed; the dimension-necessity lower bound, open when
> this note was written, is now proved (paper, Section 5). Frozen DOI releases
> are preserved as historical records; the correction history is part of the
> record. The resolution paper —
> [paper/resolution.pdf](paper/resolution.pdf) — states both theorems with
> proof architecture, correction history, review methodology, and full
> citations.

**Rigorous partial repair at repository HEAD.** Sprints 1287--1294
prove, from committed rational Bellman subsolutions and an exact abstract
operator weld,

```text
omega_tensor <= omega_commuting <= 0.250875388108398
```

with the upper endpoint interpreted as an exact decimal. Sprint 1294 commits a
symmetric endpoint-clustered 25,601-knot witness and exactly optimizes it on a
`10^-15` grid. A separately written standard-library engine reconstructs its
nonuniform hull, all 46,458 common intervals, and both endpoint receipts
without importing the production verifier. The bound is unconditional. The
registered target of a window below `3e-9` failed and remains recorded; the
exact theorem is stronger than Sprint 1293 but did not by itself restore
equality, nonattainment, spatial separation, or nonclosure. See
[`ENDPOINT-CLUSTERED-COLLIDER-RESULT.md`](certificate/production/foundational-sprint-1294/ENDPOINT-CLUSTERED-COLLIDER-RESULT.md).

Sprint 1292 installs an explicit 255-dimensional strategy, certifies it with
rational square-root floors, and independently reconstructs it at 160-digit
interval precision. Together the certificates give the unconditional window

```text
0.2508753845015185 < omega_tensor
                   <= omega_commuting <= 0.250875388108398,
```

of width below `3.607e-9`. See
[`RIGOROUS-DIMENSION-255-LOWER.md`](certificate/production/foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md).

**Model-value equality repaired.** Sprint 1295 proves a universal
Bellman--path variational theorem and applies it to the exact Pal--Vertesi
carrier. An independently written exact-rational audit reconstructs the
source/target orientation, Schur-pivot floor, continuity argument, old
operator-weld contract, and 24 carrier embeddings across both parity branches.
Consequently the numerical window now brackets one common value:

```text
omega_tensor(I3322) = omega_commuting(I3322)
                    = the common Bellman/path variational value.
```

This does not identify that value with the historical shooting decimal.
Finite-dimensional nonattainment and nonclosure at the common value are now
restored by the independent route in
[`certificate/production/theorem-N-four-receipts-at-S/`](certificate/production/theorem-N-four-receipts-at-S/);
spatial attainment at the current value is established in v3.1.0
(see the theorem-S certificate directory).
See
[`BELLMAN-PATH-EQUIVALENCE-THEOREM.md`](certificate/production/foundational-sprint-1295/BELLMAN-PATH-EQUIVALENCE-THEOREM.md).

The historical release claimed a computer-assisted proof that the tensor-product and
commuting-operator suprema of the canonical three-setting, two-outcome
`I3322` Bell functional equal the rigorously characterized constant

```text
q* = 0.250875384513976536...
q* in [0.250875384513976535514, 0.250875384513976536486].
```

It further asserted that the bi-infinite wall defines an explicit
vector-state maximizer on `ell^2(Z) tensor ell^2(Z)` through the alternating
Pal--Vertesi projectors. **That construction is decertified**: its
amplitude-compatibility equation fails by an exactly certified margin in
`[1.40e-4, 1.79e-4]`, excluding zero, reproduced by two independent interval
engines. The current Theorem (S) does not repair it — it reaches `S` on a
route that never poses that equation.

The historical release also derived, from those wall truncations, a geometric
sufficiency rate against `q*`:

```text
0 < q* - Q_d <= exp[-d log(R) + O(1)],
R = 1.07809205080209208....
```

Both the constant `q*` and this derivation are part of the decertified layer;
the current rate result is the paper's Section 5,
`D(epsilon) = Theta(log(1/epsilon))`, with the carrier-uniform derived bound
`1/kappa_eff <= 23.9010650` and no sharpness claimed. A prospective
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
conditional constant ledger below is retained as a historical record
of that campaign.

> **Superseded 2026-08-07.** The rate question is now settled:
> `D(epsilon) = Theta(log(1/epsilon))` at local-dimension scope
> (existential constants; the upper half with the derived safe bound
> `1/kappa_eff <= 23.9010650`, no sharpness claimed). The result is
> stated and proved in the companion rate note (`paper/`; folded into
> `paper/resolution.tex` Section 5 as of 2026-08-25), with
> complete certificates, guard scripts, and the full audit record —
> including every denial round of its promotion gate — in
> `certificate/production/rate-theta-log/`. The paragraph above
> records the state of the campaign before that proof and is not the
> current claim.

Consequently,

```text
C_q(3,3;2,2) != C_qs(3,3;2,2),
```

and `C_q(3,3;2,2)` is not closed. A separate Jordan-decomposition argument
proves that any two-outcome bipartite scenario in which either party has only
two inputs has closed (indeed compact) `C_q`, so among **two-outcome**
scenarios three inputs per party is the smallest possible venue by input
count. No minimality is claimed over scenarios with larger output alphabets.

Archival identifiers: concept DOI
[`10.5281/zenodo.21782008`](https://doi.org/10.5281/zenodo.21782008); frozen
`v4.0.0` (release of record, merged paper) DOI
[`10.5281/zenodo.22099128`](https://doi.org/10.5281/zenodo.22099128); frozen
`v3.3.0` (rate mint, standalone companion note) DOI
[`10.5281/zenodo.21843326`](https://doi.org/10.5281/zenodo.21843326) —
note: this record's Zenodo metadata carries the stale version string
"3.2.3" from the `.zenodo.json` shipped at tag time, but its archive file
is `i3322-exact-wall-v3.3.0.zip` and it is the v3.3.0 release of record;
frozen `v3.2.3` DOI
[`10.5281/zenodo.21826916`](https://doi.org/10.5281/zenodo.21826916); frozen
`v2.0.0` correction-release DOI
[`10.5281/zenodo.21799071`](https://doi.org/10.5281/zenodo.21799071); frozen
`v1.2.0` DOI
[`10.5281/zenodo.21782750`](https://doi.org/10.5281/zenodo.21782750); frozen
`v1.1.0` DOI
[`10.5281/zenodo.21782527`](https://doi.org/10.5281/zenodo.21782527); frozen
`v1.0.0` DOI
[`10.5281/zenodo.21782009`](https://doi.org/10.5281/zenodo.21782009).

The promoted results establish finite-dimensional nonattainment of the
common value S and spatial attainment of S (the spatial strategy uses
the alternating block FORM of Pal--Vertesi with labels and amplitudes derived
independently; whether their family converges to S is not settled, and the
exact value beyond the certified window remains open). This is not a claim of
priority for the block construction or for general finite/infinite-dimensional
separation, which are known from earlier work.

Mghirbi's July 2026 release
[`10.5281/zenodo.21477901`](https://doi.org/10.5281/zenodo.21477901)
gave a proof-carrying exact enclosure of width below `10^-9` — **tighter than
the window used here**. That enclosure is a certified *input* to this work,
not a contribution of it. What the present results add is equality of the two
models, nonattainment, and spatial attainment, none of which those
certificates address. The exact value of `S` remains open, and this is not
the first exact certified bound for I3322.

## Paper

- **[Resolution paper — the current paper](paper/resolution.pdf)**
  (v4.0.0, the merged paper of record; readable source in the paper/
  directory)
- [Claim-to-certificate map](paper/CERTIFICATE-MAP.md)
- [Priority audit](paper/PRIORITY-AUDIT.md)
- [Independent frontier-model review and adjudication](review/README.md)
- Historical (superseded by the resolution paper; preserved for
  provenance): [legacy manuscript](paper/manuscript.pdf),
  [technical supplement](paper/technical-supplement.pdf),
  [readable legacy source](paper/MANUSCRIPT.md), release notes
  [v1.1.0](paper/RELEASE-NOTES-v1.1.0.md) /
  [v1.2.0](paper/RELEASE-NOTES-v1.2.0.md) /
  [v1.3.0](paper/RELEASE-NOTES-v1.3.0.md)

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

## Machine-checked algebraic cores (Lean 4)

`lean/I3322Kernel/` contains a Lean 4 + Mathlib formalization of the
paper's displayed algebraic formulas: the quarter-ceiling
amplitude-elimination chain, the exact endpoint margins (as exact
rational identities, with antitonicity in the level), and the
finite-closure lemma (two strictly antitone bijections of a finite
linear order coincide). All theorems build with no `sorry` and report
only the standard axioms under `#print axioms`. The claim boundary is
stated in [lean/I3322Kernel/README.md](lean/I3322Kernel/README.md):
these are the algebraic cores, not the full theorems — the
measure-theoretic and operator-algebraic chains are not formalized.

```powershell
cd lean/I3322Kernel
lake exe cache get
lake build
lake env lean AxiomCheck.lean
```

## Repository structure

- `paper/`: manuscript, supplement, normalization, scope, and priority record;
- `certificate/production/`: Arb/SymPy/NumPy proof dependencies and explicitly
  marked conditional lower-bound research;
- `certificate/independent/`: separate interval reconstruction;
- `certificate/release/`: manifest, replay entry point, and release audits;
- `lean/I3322Kernel/`: machine-checked algebraic cores (Lean 4 + Mathlib).

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
