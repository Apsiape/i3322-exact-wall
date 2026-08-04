# Grid-free Bellman contact controls the full ordered flag

Status: **proved representation-free averaged flag theorem**

## Theorem

Let `psi` be a pure finite-dimensional strategy, let `D` be its coefficient
operator, and let

```text
epsilon_0=<psi,r_0(X,U)psi>.
```

Use Sprint 1232's saturated predecessor coordinate `Y`. For every
`s in [-1,1]`, define cumulative spectral projections

```text
E_s=1_{Y(X)<=s},       F_s=1_{U<=s}.                 (1)
```

Then

```text
integral_[-1,1] ||E_sD-D F_s^T||_HS^2 ds
 <= sqrt(40 epsilon_0).                              (2)
```

For the regularized Schmidt supports `W_A,t,W_B,t` of Sprint 1242 and
`r=rank(D)`, one also has

```text
integral_[-1,1]
 |Tr(E_s W_A,t)-Tr(F_s W_B,t)|^2 ds
 <= r sqrt(40 epsilon_0)/(4t).                       (3)
```

## Proof

Because `Y(X)` and `U` act on opposite parties, they have a joint spectral
measure `mu_psi`. The coefficient-matrix norm is the corresponding indicator
mismatch:

```text
||E_sD-D F_s^T||_HS^2
 = integral |1_{Y(x)<=s}-1_{u<=s}|^2 dmu_psi(x,u).  (4)
```

For any two numbers `y,u in [-1,1]`, their two cumulative indicators disagree
on exactly the interval between them. Hence

```text
integral_[-1,1]
 |1_{y<=s}-1_{u<=s}|^2 ds=|y-u|.                    (5)
```

Tonelli's theorem, followed by Cauchy--Schwarz, gives

```text
integral ||E_sD-D F_s^T||_HS^2 ds
 = integral |Y(x)-u| dmu_psi
 <= sqrt(integral (Y(x)-u)^2 dmu_psi).               (6)
```

Sprint 1232 proves globally

```text
r_0(x,u)>=(u-Y(x))^2/40.                             (7)
```

Equations (6)--(7) prove (2). Finally Sprint 1242 gives pointwise

```text
|Tr(E_s W_A,t)-Tr(F_s W_B,t)|^2
 <= r ||E_sD-D F_s^T||_HS^2/(4t).                   (8)
```

Integrating (8) and applying (2) proves (3).

## Why this is different from packet rounding

The earlier route discretized the contact graph and then tried to promote
cellwise mass estimates into common response targets. That promotion failed
because complement/drift mass could enter a target cell from another branch.

Equations (2)--(3) do not make that move. The family `(E_s,F_s)` is the full
nested order flag, all thresholds are retained, and no complement is thrown
away. The estimate is therefore insensitive to spectral density, cell
boundaries, and occurrence multiplicity.

The remaining problem is not contact localization. It is a robust finite
order theorem for the two response-transported soft flags.
