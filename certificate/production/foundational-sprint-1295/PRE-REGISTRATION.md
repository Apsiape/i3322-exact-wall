# Pre-registration: universal Bellman--path equivalence

## Wager

The possible branching advantage in the Bellman--Hellinger flow dual is not a
real value gap.  The Bellman primal is exactly the supremum of finite Jacobi
path spectra.  The mechanism is scalar Schur-complement viability, not a
claim that every dual flow itself is a path.

## Abstract theorem target

Let `X` be compact, `d:XxX->R` continuous, and `b:X->[0,infinity)`
continuous.  For every word `x_0,...,x_n`, let `J_x` be the `n x n`
tridiagonal matrix with

```text
diag(J_x)_k = d(x_k,x_(k+1)),
offdiag(J_x)_(k-1,k) = b(x_k).
```

Define

```text
S = sup_(n,x) lambda_max(J_x)

P = inf_(g in C(X), g>0)
      sup_(i,j in X) [d(i,j) + b(i)^2/g(i) + g(j)].
```

Registered theorem: `P=S`.

## Required proof gates

1. **Upper direction:** weighted Young inequality must give `S<=P` with the
   source/target indices exactly matching the I3322 Bellman convention.
2. **Uniform pivot floor:** for `q>S`, every leading Schur pivot of every word
   must be at least `q-S`; a merely positive but nonuniform pivot is
   insufficient.
3. **Terminal-pivot construction:** the infimum of pivots over histories ending
   at `j` must satisfy the Bellman inequality with the correct inequality
   orientation.
4. **Continuity:** the constructed storage function must belong to `C(X)`, not
   merely be measurable or semicontinuous.  The proof must use the uniform
   endpoint modulus inherited from `d`.
5. **Endpoint safety:** zeros of `b`, including the I3322 endpoints, may not be
   removed by division.
6. **Finite hostile guards:** exact rational fixtures must check the pivot
   recursion, Young accounting, and a branching contact graph.
7. **I3322 typing:** the existing operator weld must quantify over arbitrary
   positive continuous Bellman storage functions, and finite aligned Jacobi
   paths must be genuine tensor-product strategies with identical value.

## Registered consequences if all gates close

```text
omega_tensor(I3322) = omega_commuting(I3322) = P = S.
```

This identifies the exact value variationally and proves that branching flow
cannot create a tensor/commuting value gap for this functional.

## Non-consequences

Do not infer that:

- the historical decimal is the exact value;
- the optimum is unattained in finite dimension;
- `C_q` is nonclosed or differs from `C_qs`;
- every optimizing Hellinger flow can literally be represented by one path;
- the infimum defining `P` is attained.

Failure of any proof gate leaves Sprint 1295 as a killed theorem candidate and
does not weaken the exact finite upper/lower window.
