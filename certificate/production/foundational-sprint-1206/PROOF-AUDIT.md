# Sprint 1206 proof audit

Status: the explicit spatial branch survives. The negative branch is retired.

## Claim

The certified I3322 wall is attained by a normal vector state on
`ell^2(Z) tensor ell^2(Z)`. Combined with finite-dimensional nonattainment,
this gives

```text
C_q(3,3;2,2) != C_qs(3,3;2,2).
```

## Dependency ledger

| Obligation | Source | Status |
|---|---|---|
| one bi-infinite wall profile | Sprint 1195, Section 5 | certified input |
| positive geometric two-sided tail | Sprint 1195, Section 5 | certified input |
| `lambda in ell^2(Z)` | Sprint 1195, Section 5 | certified input |
| `H(c)lambda=q_*lambda` | Sprint 1195, Section 5 | certified input |
| unrestricted upper bound `I3322<=q_*` | Sprint 1197 | certified input |
| no finite-dimensional attainer | Sprint 1198 | certified input |
| alternating projectors define bounded operators | direct sums of rank-one blocks | analytic |
| Bell expectation equals Jacobi form | local expansion | analytic; two guards |
| infinite sums are legitimate | finite bandwidth plus Cauchy--Schwarz | analytic |
| model membership | explicit normal vector state on a spatial tensor product | analytic |

## Hostile checks

### 1. Is the wall only a sequence of unrelated finite profiles?

No. Sprint 1195 first constructs the complete characteristic connection and
then explicitly reconstructs one positive two-sided geometric eigenvector of
the associated bi-infinite Jacobi operator. Finite profiles enter afterward,
as truncations proving sharpness.

### 2. Do endpoint terms secretly create the Jacobi identity?

No. `spatial_realization_verify.py` checks both the published open finite
carrier and endpoint-free alternating cycles. All 24 exact-rational fixtures
give Bell minus Jacobi equal to zero. Deleting the receiver on one matching
gives a nonzero residual in all 24 controls.

`spatial_symbolic_verify.py` independently expands the smallest periodic
carrier containing both matching parities. Its polynomial remainder is zero
modulo only `s_j^2+c_j^2=1`, and all six projection identities reduce to zero.

### 3. Is an infinite limit of observables being assumed?

No. Each observable is defined directly as an orthogonal direct sum on one of
the two perfect matchings of `Z`. No operator topology or subsequence is used.

### 4. Is the state singular or commuting-only?

No. The normalized vector

```text
sum_j lambda_j e_j tensor e_j
```

belongs to the ordinary Hilbert tensor product because `lambda in ell^2`.
Its vector functional is normal.

### 5. Are conditionally convergent sums rearranged?

No. Diagonal terms are bounded by a constant times `sum lambda_j^2`. Neighbor
terms obey

```text
sum_j |lambda_(j-1) lambda_j|
 <= ||lambda shifted||_2 ||lambda||_2 < infinity.
```

Every Bell term is a sum over disjoint two-site blocks, so the expansion is
absolutely convergent.

### 6. Does `C_qs` mean this model in the literature?

Yes. The standard hierarchy uses `C_q` for finite-dimensional tensor-product
correlations and `C_qs` for correlations on arbitrary spatial tensor products.
The present vector-state construction is a particularly concrete member of
the latter. It also lies in `C_qa`, consistent with the standard inclusion
`C_q subset C_qs subset C_qa`.

### 7. Is this a new construction being claimed?

No. The alternating block ansatz and its infinite-dimensional interpretation
are due to Pal and Vertesi (2010). Their optimality and finite-dimensional
insufficiency statements were conjectural. The new contribution is the exact
upper theorem and nonattainment theorem that turn that ansatz into a certified
maximizer and hence into an I3322 witness in `C_qs \ C_q`.

## Surviving boundaries

- No uniqueness or self-testing theorem is claimed.
- No separation of `C_qs` from `C_qa`, or of `C_qa` from `C_qc`, is claimed.
- No quantitative dimension-versus-error law is claimed.
- Minimality is coordinatewise only among bipartite binary-output input
  counts.
- The general separation `C_q != C_qs` is not new; the value is its realization
  by the canonical I3322 functional in the minimal binary input scenario.

## Verdict

The earlier statement that spatial attainment remained open was an internal
assembly error. The exact wall theorem already supplied the normalizable
bi-infinite state, while the Bell paper used it only to generate finite
Rayleigh quotients. Installing the same certified wall in the Pal--Vertesi
alternating blocks closes the omitted implication.
