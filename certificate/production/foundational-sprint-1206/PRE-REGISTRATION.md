# Sprint 1206 pre-registration -- spatial attainment of the I3322 wall

Date: 2026-08-03

## Question

Does the certified I3322 value `q_*` have a normal infinite-dimensional
tensor-product realization, i.e. is there a correlation

```text
p in C_qs(3,3;2,2) with I3322(p)=q_*?
```

## Candidate already present in the archive

Sprint 1195 proves more than convergence of finite values. It states that the
certified bi-infinite cosine profile `c=(c_j)_(j in Z)` has a positive
geometrically decaying eigenvector `lambda in ell^2(Z)` satisfying

```text
H(c) lambda = q_* lambda.
```

The finite Pal--Vertesi strategies are alternating two-dimensional projector
blocks whose Bell expectation is the Jacobi quadratic form. The registered
candidate is to put those same blocks on `ell^2(Z)`, use the normalized Schmidt
vector

```text
|psi> = sum_j lambda_j |j,j>,
```

and extend the finite reduction by norm convergence.

## Registered predictions

1. The infinite alternating block operators are orthogonal projections and
   hence bounded.
2. The geometric tail estimate makes `psi` a normal vector state in
   `ell^2(Z) tensor ell^2(Z)`.
3. The direct I3322 expectation equals `<lambda,H(c)lambda>` exactly.
4. Therefore the state attains `q_*` spatially.
5. Combining this with finite-dimensional nonattainment proves
   `C_q(3,3;2,2) != C_qs(3,3;2,2)`.
6. The result is minimal only in the previously proved coordinatewise ordering
   of bipartite binary input counts; no stronger output/party/network
   minimality is claimed.

## Kill conditions

- The certified orbit supplies only unrelated finite profiles, not one
  bi-infinite profile.
- The reconstructed eigenvector is not in `ell^2`.
- One of the six infinite measurement operators fails to be a projection or
  fails boundedness.
- The finite Jacobi reduction relies on endpoint terms that do not vanish in
  the bi-infinite limit.
- The direct Bell expectation differs from the Jacobi quadratic form.
- The archived `C_qs` convention excludes normal vector states on separable
  infinite Hilbert spaces.

## Negative branch

If any construction gate fails, attempt to prove that every normal spatial
attainer would violate the equality-kernel transport equations. Do not use the
finite decreasing-bijection argument on an infinite ordered support: that is
exactly the step that ceases to apply.

## Publication gate

No public upgrade until the block realization is written explicitly, the
finite-to-infinite passage is proved without exchanging conditionally
convergent series, the model notation is literature-audited, and the direct
identity has an independent computational guard.
