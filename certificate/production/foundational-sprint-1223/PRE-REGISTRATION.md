# Sprint 1223 pre-registration -- moving dihedral partitions

Date: 2026-08-03

## Target

Avoid the impossible demand for one finite partition invariant under both
contact reflections. Transport the partition itself and quantify only its
distortion.

## Registered theorem

Let `Q_s` be the shifted width-`h` partition of the predecessor coordinate.
For a word `g` in the involutions

```text
a(u)=P^-1(-P(u)),
b(u)=-u,                                             (1)
```

use the moved partition `g Q_s`. A following reflection `r in {a,b}` should
map its cells exactly to `(r g)Q_s`, with no rounding.

Sprint 1217's `1/10<P'<2` should imply

```text
Lip(a),Lip(a^-1)<=20,
Lip(b)=1.                                           (2)
```

If `g` contains `m` copies of `a`, shifted rounding in `gQ_s` should satisfy

```text
rho_g<=[40 sqrt(10)/h] 20^m sqrt(epsilon_0).        (3)
```

## Failure conditions

- partition transport is not exact;
- the derivative ratio for `a` is oriented incorrectly;
- inverse distortion exceeds `20^m`;
- or moving partitions secretly require a common refinement.

## Claim boundary

This theorem controls each time slice. It does not yet prove that repeated
top-`d` rank compression across multiple moved partitions consumes only `d`
total chain sites.
