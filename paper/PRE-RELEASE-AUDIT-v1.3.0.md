# Hostile pre-release audit -- prospective v1.3.0

**Audit date:** 2026-08-04
**Decision:** prospective two-sided packet blocked; constructive half survives,
universal lower bound remains conditional; hold archival release

This audit attempted to break the quantitative dimension theorem at its four
most exposed interfaces: the optimized strategy class, the construction,
the universal lower bound, and the public interpretation.

## Public theorem contract

For the canonical normalized I3322 functional, let `Q_d` optimize over all
bipartite tensor-product strategies with both local dimensions at most `d`,
arbitrary mixed states, and arbitrary binary POVMs. The first prospective
packet claimed

```text
kappa d^-4 Gamma^-d <= q_*-Q_d <= exp[-d log R+O(1)],
Gamma=312^4,
```

and consequently, as `epsilon` tends to zero,

```text
D(epsilon)=Theta(log(1/epsilon)).
```

That contract has failed its lower-bound gate. The surviving public contract is
`0<q_*-Q_d<=exp[-d log R+O(1)]`; it does not claim a universal dimension lower
bound.

## Hostile gates

| Gate | Attack | Result |
|---|---|---|
| Normalization | Compare repository projector coefficients with Collins--Gisin and dichotomic conventions | Pass; exact affine concordance |
| `Q_d` quantifier | Look for an implicit pure-state/PVM restriction or Naimark dimension increase | Pass; compactness plus successive same-space extreme-point replacement |
| Construction | Delete either boundary term from the finite Jacobi compression | Pass; both wrong controls leave nonzero symbolic residuals |
| Constructive exponent | Reconstruct `R` and `log R` without production interval code, then challenge the bounded prefactor | Corrected; the manuscript now states the exponentially summable ratio error that yields `C R^-d` |
| Universal lower bound | Search for aligned-spectrum, density, finite-chain-count, hidden fibre, or omitted-dependency assumptions | **Fail:** common projections do not localize the global response defect; a commutator/flux premise is missing |
| Multiplicity | Recount all principal/intermediate frames and response/exit reuse | Pass; full `2d+1` frame and adjacent-use charges appear before final constants |
| Final algebra | Rebuild `A`, `B`, `Gamma`, and the minimum defining `kappa` | Corrected; source/target contact families cost `2 epsilon_0`, changing `24` to `48` and slightly decreasing `kappa` |
| Asymptotic inversion | Try to infer the lower `D(epsilon)` bound without an upper control on `D` | Pass only when the constructive upper bound is used jointly; manuscript now states the result as `epsilon` tends to zero |
| Reproducibility | Replay from a clean clone with no private-corpus path | Pending final post-repair manifest and full replay |
| Literature boundary | Search for prior I3322 finite-dimension asymptotics and general quantitative dimension witnesses | No matching I3322 theorem found; general dimension-witness priority explicitly credited |

## Corrections earned by this audit

1. The manuscript no longer claims `Theta(log(1/epsilon))`; it retains only
   logarithmic-dimensional sufficiency.
2. Navascues--Feix--Araujo--Vertesi are credited for convergent
   dimension-constrained hierarchies, including I3322 applications.
3. Coladangelo is credited for a substantially stronger quantitative
   dimension blowup in a purpose-built larger game.
4. The novelty sentence is narrowed to the exact finite-section flux identity
   and constructive rate for the canonical three-setting binary functional.
   No "first" language is used.
5. Three independent frontier-model lanes were internally registered. Their
   chronology was not externally time-sealed. They returned release-blocking
   findings: omitted proof owners, an active/saturated packet mismatch, a
   factor-of-two contact charge, and a missing localized-response implication.
   All were reproduced rather than adjudicated by vote.
6. The public reconstruction chronology is now described as separately
   written but not externally time-sealed.

## Residual risks that certificates cannot retire

- The lower bound is not presently proved. The exact missing premise is a
  localized-response/commutator or packet-completion estimate. Multiple model
  contexts share broad model-family priors; their agreement is not proof by
  vote.
- The conditional necessity base `Gamma` does not currently define a theorem;
  the existence and sharp rate of a universal quantitative lower bound are
  open.
- A negative literature search cannot establish priority, especially for
  very recent or poorly indexed work.
- The theorem is mathematically device-independent inside its stated model;
  the explicit constant is not presently an experimentally practical
  dimension witness.

## Release rule

Do not tag or mint the two-sided v1.3. Preserve every model report and the
countermodel. A future v1.3 must either (a) prove and re-audit the missing
localization theorem, or (b) be deliberately narrowed to the constructive
truncation-rate theorem, followed by a clean manifest replay. A correction
from review is a successful audit outcome, not a failed release.
