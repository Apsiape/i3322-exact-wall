# Regularized Schmidt flags

Status: **proved operator calculus; finite-rank closure gate isolated**

## 1. Soft support

For a coefficient operator `D : conjugate(H_B) -> H_A` and `t>0`, define

```text
W_A,t=D(tI+D^*D)^(-1)D^*,
W_B,t=D^*(tI+DD^*)^(-1)D.                            (1)
```

Both are positive contractions. If `s_1,...,s_r` are the singular values of
`D`, their common nonzero spectrum is

```text
s_j^2/(t+s_j^2).                                     (2)
```

Consequently

```text
Tr W_A,t=Tr W_B,t<=rank(D),                           (3)
W_A,t D=D W_B,t.                                     (4)
```

As `t` decreases, (1) approaches the support projections of `D`; for fixed
`t`, Schmidt directions much smaller than `sqrt(t)` are suppressed. This is
the required interpolation between unstable literal rank and the state-mass
weight that hid multiplicity in the packet proof.

## 2. Contact transports soft flags

Let `E` and `F` be orthogonal projections on the two local spaces. Cyclicity
of trace and (1) give

```text
Tr(E W_A,t)-Tr(F W_B,t)
 = Tr[D^*(E D-D F)(tI+D^*D)^(-1)].                   (5)
```

The singular values of `D(tI+D^*D)^(-1)` are
`s/(t+s^2)<=1/(2 sqrt(t))`. Hence, with
`r=rank(D)`,

```text
|Tr(E W_A,t)-Tr(F W_B,t)|
 <= sqrt(r)/(2 sqrt(t)) ||E D-D F||_HS.              (6)
```

For the I3322 contact graph, take cumulative flags

```text
E_s=1_{X<=P(s)},       F_s=1_{U<=s}.                 (7)
```

Under exact Bellman contact, `E_sD=DF_s^T`, so (6) is zero for every
threshold. Near contact, the right side is precisely the coefficient-matrix
form of the state-dependent spectral mismatch. Unlike a cell partition, the
family `(E_s,F_s)` is nested and retains order.

## 3. Stability under response correspondences

Write

```text
W_t(M)=M(tI+M^*M)^(-1)M^*
      =I-t(tI+MM^*)^(-1).                            (8)
```

The resolvent identity gives

```text
||W_t(M)-W_t(N)||_HS
 <= ||MM^*-NN^*||_HS/t
 <= (||M||+||N||)/t ||M-N||_HS.                     (9)
```

If `N=UMV` for unitaries `U,V`, then

```text
W_t(N)=U W_t(M) U^*.                                (10)
```

Equations (9)--(10), combined with Sprint 1240's two response
correspondences, control transported soft flags without choosing individual
Schmidt vectors or resolving degenerate singular spaces.

## 4. The exact gate

Sprint 1241 showed that marginal singular spectra cannot distinguish two
different involutions. Their cumulative flags do distinguish them. The
remaining I3322 theorem is now:

```text
small Bell deficit
 -> contact identifies the two nested soft flags
 -> both response correspondences approximately reverse that same flag
 -> finite soft rank forces the reversals to glue, or pays a boundary.     (11)
```

The first two arrows now have an operator calculus. The last arrow is a
robust finite-order theorem and remains open. It is narrower than the former
packet problem: no arbitrary grid, no ancestry multiplicity, and no deletion
of the complement is allowed.
