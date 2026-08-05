# Literature placement: Bellman--path equivalence

**Search date:** 2026-08-04

**Posture:** the theorem is promoted for its proved content and its I3322
application, not as a priority claim for a new general spectral principle.

## Nearest established mechanisms

The proof combines three classical mechanisms.

1. **Ground-state positivity.**  Allegretto--Piepenbrink theory relates
   positivity of a Schrödinger quadratic form on a graph to positive
   (super)solutions.  Keller, Pinchover, and Pogorzelski develop this relation
   for weighted graphs in
   [arXiv:1708.09664](https://arxiv.org/abs/1708.09664).  The exact-square
   Young remainder in Sprint 1295 is a one-dimensional path analogue of a
   ground-state transform.
2. **Riccati/Schur recursion.**  The terminal-pivot recursion is the scalar
   discrete Riccati equation obtained by successive Schur complementation of
   a Jacobi matrix.  Sprint 1295 uses it uniformly over every finite word and
   then takes an infimum over histories.
3. **Path-uniform storage and Collatz--Wielandt ideas.**  Path-complete
   Lyapunov inequalities certify every word in a switched system; see Ahmadi,
   Jungers, Parrilo, and Roozbehani,
   [arXiv:1111.3427](https://arxiv.org/abs/1111.3427).  Nonlinear
   Perron--Frobenius theory supplies related inf--sup characterizations through
   positive test functions; see Lins,
   [arXiv:2111.01219](https://arxiv.org/abs/2111.01219).  The present transform
   is additive and reciprocal rather than homogeneous, so those results are
   conceptual neighbors, not cited as direct theorem dependencies.

## What the scoped search did and did not find

Searches covered combinations of `Jacobi`, `Riccati`, `finite paths`,
`arbitrary switching`, `path-complete Lyapunov`, `Collatz--Wielandt`,
`ground-state transform`, and `positive superharmonic`.  They found the
neighboring theories above but not the exact compact-space formula

```text
sup_(finite words x) lambda_max(J_x)
= inf_(continuous g>0) sup_(i,j)
    [d(i,j)+b(i)^2/g(i)+g(j)].
```

This is a negative scoped search, not evidence of priority.  The safest
description is:

> a specialized path-uniform ground-state/Riccati variational theorem, with a
> new application that proves equality of the tensor and commuting values of
> I3322.

The I3322 antecedent remains Pál and Vértesi,
[arXiv:1006.3032](https://arxiv.org/abs/1006.3032), whose alternating
finite/infinite-dimensional construction supplies the carrier geometry.  The
current result does not validate their conjectured decimal or their
finite-dimensional nonattainment conjecture.

## Publication boundary

Permitted:

- state and prove the abstract theorem;
- state that its exact placement appears to combine known mechanisms;
- claim the I3322 tensor/commuting **value equality** proved by the theorem;
- say that no exact antecedent was found in this search.

Not permitted:

- call the abstract theorem a new Collatz--Wielandt or
  Allegretto--Piepenbrink theorem without a deeper priority review;
- identify the common I3322 value with the historical decimal;
- restore nonattainment, spatial attainment, or nonclosure;
- infer that every Bellman--Hellinger flow is literally one path.
