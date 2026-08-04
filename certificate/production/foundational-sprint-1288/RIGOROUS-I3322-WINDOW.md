# A rigorous unconditional I3322 value window

Status: **exact finite lower strategy plus exact commuting upper certificate**

## Theorem

In the normalization used throughout this repository,

```text
0.25087519579012
  < omega_tensor
  <= omega_commuting
  <= 0.250876384514.
```

The exact certified lower endpoint before conservative decimal truncation is

```text
12543759789506110612298899972337267226579686749153092291074262435566245661191728498315730882404009
----------------------------------------------------------------------------------------------------
49999999999999997269998467282792711398000000000000000000000000000000000000000000000000000000000000
```

and the exact upper endpoint is

```text
125438192257 / 500000000000.
```

Their exact difference is approximately

```text
1.1887238777740562e-6.
```

## Lower-bound owner

`finite-strategy-candidate.json` specifies 128 rational profile coordinates
with endpoints `+1,-1` and 127 positive rational state coordinates.  For each
internal profile coordinate `c_j`, the exact verifier constructs a 60-place
rational lower floor for `sqrt(1-c_j^2)` and proves its square does not exceed
the radicand.

The exact local Pal--Vertesi block identity then realizes the normalized
Jacobi quotient as a legitimate 127-dimensional tensor-product I3322
strategy. Because every neighboring state product is positive, replacing the
square root by its certified lower floor lowers the Bell value.  The resulting
quotient is evaluated entirely with `Fraction` arithmetic by
`exact_finite_strategy_lower_bound.py`.

The floating optimizer is not a theorem owner. It only found the committed
rational witness.

## Upper-bound owner

Sprint 1287 proves the exact rational commuting-operator upper bound from a
positive piecewise-linear Bellman subsolution and the representation-free
operator remainder decomposition. See
`../foundational-sprint-1287/EXACT-NEAR-OPTIMAL-UPPER-BOUND.md`.

## Independence from the failed weld

The lower certificate is a direct finite strategy. The upper certificate is a
direct global inequality. Neither uses:

- the excluded shooting-chart amplitude compatibility equation;
- a globally glued infinite wall;
- Bellman fixed-point equality at the historical candidate;
- finite-dimensional nonattainment; or
- tensor/commuting equality.

## Claim boundary

This interval does not resolve the exact I3322 value. It permits distinct
tensor-product and commuting-operator suprema anywhere inside the window. It
does not prove that any supremum is unattained, that `C_q != C_qs`, or that
`C_q` is nonclosed. The frozen DOI releases remain historical claims under
correction.
