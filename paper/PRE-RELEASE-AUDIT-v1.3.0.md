# Hostile pre-release audit -- prospective v1.3.0

**Audit date:** 2026-08-04
**Decision:** mathematically coherent internally; hold archival release for
external theorem review

This audit attempted to break the quantitative dimension theorem at its four
most exposed interfaces: the optimized strategy class, the construction,
the universal lower bound, and the public interpretation.

## Public theorem contract

For the canonical normalized I3322 functional, let `Q_d` optimize over all
bipartite tensor-product strategies with both local dimensions at most `d`,
arbitrary mixed states, and arbitrary binary POVMs.  The prospective release
claims

```text
kappa d^-4 Gamma^-d <= q_*-Q_d <= exp[-d log R+O(1)],
Gamma=312^4,
```

and consequently, as `epsilon` tends to zero,

```text
D(epsilon)=Theta(log(1/epsilon)).
```

It does not claim matching exponential rates, a sharp prefactor, experimental
accessibility, or a bound for signaling, postselected, network, or
commuting-operator dimension models.

## Hostile gates

| Gate | Attack | Result |
|---|---|---|
| Normalization | Compare repository projector coefficients with Collins--Gisin and dichotomic conventions | Pass; exact affine concordance |
| `Q_d` quantifier | Look for an implicit pure-state/PVM restriction or Naimark dimension increase | Pass; compactness plus successive same-space extreme-point replacement |
| Construction | Delete either boundary term from the finite Jacobi compression | Pass; both wrong controls leave nonzero symbolic residuals |
| Constructive exponent | Reconstruct `R` and `log R` without production interval code | Pass; independent `mpmath.iv` interval lies strictly above zero |
| Universal lower bound | Search for aligned-spectrum, density, finite-chain-count, or hidden fibre assumptions | Pass in the sealed reconstruction; packets use finite joint spectral masses, moving partitions, and per-chain rank only |
| Multiplicity | Recount all principal/intermediate frames and response/exit reuse | Pass; full `2d+1` frame and adjacent-use charges appear before final constants |
| Final algebra | Rebuild `A`, `B`, `Gamma`, and the minimum defining `kappa` | Pass; independent exact SymPy audit |
| Asymptotic inversion | Try to infer the lower `D(epsilon)` bound without an upper control on `D` | Pass only when the constructive upper bound is used jointly; manuscript now states the result as `epsilon` tends to zero |
| Reproducibility | Replay from a clean clone with no private-corpus path | Pass; 220 frozen files before this audit, byte-clean after full replay |
| Literature boundary | Search for prior I3322 finite-dimension asymptotics and general quantitative dimension witnesses | No matching I3322 theorem found; general dimension-witness priority explicitly credited |

## Corrections earned by this audit

1. The manuscript now scopes `Theta(log(1/epsilon))` explicitly to
   `epsilon -> 0`.
2. Navascues--Feix--Araujo--Vertesi are credited for convergent
   dimension-constrained hierarchies, including I3322 applications.
3. Coladangelo is credited for a substantially stronger quantitative
   dimension blowup in a purpose-built larger game.
4. The novelty sentence is narrowed to a two-sided asymptotic order for the
   canonical three-setting binary functional.  No "first" language is used.

## Residual risks that certificates cannot retire

- The lower bound has a long analytic packet/discard proof.  Independent
  reconstruction substantially reduces correlated implementation error but
  is not a substitute for expert line-by-line review.
- The necessity base `Gamma` is extremely conservative and does not match the
  constructive base `R`; the sharp rate is open.
- A negative literature search cannot establish priority, especially for
  very recent or poorly indexed work.
- The theorem is mathematically device-independent inside its stated model;
  the explicit constant is not presently an experimentally practical
  dimension witness.

## Release rule

Do not tag or mint v1.3 solely because the internal stack passes.  First send
the manuscript, supplement, and this audit to at least one expert in Bell
inequalities/operator algebras with the specific request: attack the
same-dimension reduction, moving-packet multiplicities, and the passage from
the energy ledger to the `Q_d` quantifier.  A correction from that review is a
successful audit outcome, not a failed release.
