# Marginal volume does not determine correspondence gluing

Status: **exact finite counterexample; Sprint 1240 survives only as a
component of an order-sensitive invariant**

## Counterexample

Let

```text
D=diag(1,2,5,11).
```

Let `P` reverse the four coordinates and let `Q` swap `1<->2` and `3<->4`.
Both are self-adjoint permutation involutions. Define positive diagonal
multipliers

```text
(C_P)_ii = D_(P i,P i)/D_(i,i),
(C_Q)_ii = D_(Q i,Q i)/D_(i,i).                      (1)
```

Then

```text
P D P^T = C_P D,
Q D Q^T = C_Q D.                                     (2)
```

Each multiplier is a reciprocal cocycle:

```text
(C_P)_ii (C_P)_(P i,P i)=1,
(C_Q)_ii (C_Q)_(Q i,Q i)=1,                          (3)
```

and both have determinant one. Moreover, both right sides in (2) are merely
permutations of the diagonal of `D`. Therefore

```text
s(C_P D)=s(C_Q D)=s(D),                              (4)
```

so every exterior-power norm, characteristic polynomial, regularized volume
`Phi_t`, and soft-rank total agrees exactly.

Nevertheless

```text
C_P D != C_Q D.                                      (5)
```

The two correspondences have different target flags. Equation (5) is the
operator form of the target-alignment defect that invalidated the scalar
packet proof.

## Interpretation

Sprint 1240 did not fail: the Schmidt operator and its regularized volumes are
valid branch-resolved invariants. What fails is using either response's
*marginal* singular data as though it encoded their relative gluing.

The exact I3322 proof has one additional ingredient not present in this
doppelganger: both transports are decreasing maps of the same ordered contact
support. A finite ordered set has one decreasing bijection, whereas the
permutation `Q` above is not globally decreasing. The quantitative invariant
must therefore retain the cumulative spectral flag.

The sharpened gate is

```text
contact-supported Schmidt operator
 + two approximately transported ordered flags
 + finite soft rank
 -> common reversal or a charged boundary.            (6)
```

No theorem in this sprint asserts (6).
