# Sprint 1244 pre-registration -- mixed flag distance

Date: 2026-08-04

## Target

Construct a mixed invariant that compares the relative gluing of two response
correspondences. It must detect the Sprint 1241 doppelganger and extend from
permutations to branch-mixing stochastic kernels.

## Registered prediction

For permutations `p,q` of an `n`-point ordered set, cumulative input flags
`E_k`, target flags `pE_kp^T,qE_kq^T`, and positive diagonal weights `w_j`,

```text
sum_(k=1)^(n-1) Tr[W |pE_kp^T-qE_kq^T|]
 = sum_j w_j |p^(-1)(j)-q^(-1)(j)|.                 (1)
```

For row-stochastic transition kernels, the same cumulative-flag expression
is the weighted sum of rowwise one-dimensional Wasserstein-1 distances.

## Failure conditions

- the inverse-permutation orientation in (1) is wrong;
- the formula needs a cross term unavailable for stochastic kernels;
- distinct permutations can have zero distance with positive weights;
- or the branch-mixing extension is not a genuine metric row by row.

## Claim boundary

This sprint defines and proves the correct relative-gluing observable. It does
not yet derive its smallness from the I3322 remainder or its largeness from
finite rank.
