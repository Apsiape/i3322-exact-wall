# Exact aligned I3322 wall theorem

Status: **proved for the aligned open Jacobi family; no unrestricted quantum
claim**

## Statement

Let `c_0=1`, `c_n=-1`, `c_i in [-1,1]`, and let `H(c)` be the finite aligned
open I3322 Jacobi carrier

```text
H_ii       = c_i c_(i+1) + (c_i-c_(i+1))/2 - 1,
H_(i-1),i  = sqrt(1-c_i^2)/2.
```

There is an exact validated connection parameter `q_*` with

```text
q_* = 0.250875384513976536... +/- 4.9e-19
```

such that

```text
sup over every finite aligned open carrier lambda_max(H(c)) = q_*.
```

The supremum is approached by growing domain-wall truncations. This theorem
does **not** prove that arbitrary I3322 strategies align, that a finite carrier
attains the supremum, or that `q_*` is the unrestricted tensor-product quantum
value.

## 1. The Bellman operator

For a positive function `F` on `[-1,1]`, define

```text
(T_q F)(y) = min_x L_x(y),
L_x(y) = q+1-x/2-(x-1/2)y-(1-x^2)/(4F(x)).
```

The exact shooting map of Sprints 1114--1116 is the characteristic map of this
operator. With shooting state `(z,x,u)`, put

```text
F(z)=sqrt(1-z^2)u/2.
```

The Bellman equality gives the next ratio coordinate exactly, and Bellman
stationarity gives the next position coordinate exactly (Sprint 1191).

## 2. The missing envelope identity

After eliminating `F(x)` by the Bellman equality, introduce

```text
beta = dF(x) - (1/2-z) dx.
```

The independent symbolic verifier in this sprint proves

```text
M^* beta = beta/v^2.                         (1)
```

The identity also has a direct four-line derivation. Put
`s=sqrt(1-z^2)`, `r=sqrt(1-x^2)`, and

```text
N=q-[zx+(z-x)/2-1]-s/(2u),   v=2N/r.
```

Then Bellman equality says `F(x)=N`, whence

```text
beta = [-x-1/2+z/(2us)] dz + s/(2u^2) du.
```

At the next state,

```text
beta_next = [-y-1/2+x/(2vr)] dx + r/(2v^2) dv.
```

Differentiating `v=2N/r` gives

```text
dv = (2/r) beta + [2(1/2-z)/r + vx/r^2] dx.
```

Substitution of the shooting formula for `y` cancels the complete `dx`
coefficient and leaves exactly `beta/v^2`. Thus (1) is an algebraic identity,
not an interval inference.

At the high plateau, `1/R^2` is exactly

```text
D/A = (1-C)(2C+1)^2 / ((1+C)(2C-1)^2),
```

the isolated stable multiplier from Sprint 1115. It is not the unique
unstable multiplier `mu>1`.

Let `gamma` be the validated local unstable parameterization,
`M gamma(t)=gamma(mu t)`, and set

```text
h(t)=beta_gamma(t)(gamma'(t)).
```

Differentiating invariance and using (1) gives

```text
mu h(mu t) = h(t)/v(t)^2.
```

The unstable eigenvector lies in `ker(beta)` because its multiplier differs
from `D/A`. Iterating the displayed identity backward to `t/mu^n -> 0`, where
`h` is bounded and `1/(mu v^2)<1` on the certified local chart, forces
`h(t)=0`. Equation (1) propagates this identity through every certified finite
iterate. Hence the complete characteristic orbit obeys

```text
F'(x)=1/2-z.                                  (2)
```

This closes the weld that was only numerical in Sprint 1191.

## 3. Global characteristic graph and concavity

The corrected exact interval certificates give all four required pieces.

- Sprint 1192: the positive branch from the plateau to the reflection section
  is a strictly monotone graph; reflection supplies its central mate.
- Sprint 1193: the negative unstable branch is a strictly monotone positive
  wing ending at target `+1`; reflection supplies the left wing.
- Every certified pivot is positive.
- Together the pieces map the active predecessor interval
  `[-x_*,x_*]` continuously and monotonically onto every target in `[-1,1]`,
  where `x_*=0.898116482394039...`.

Write the resulting increasing predecessor map as `P(y)`. Equation (2) says

```text
F'(y)=1/2-P(y).
```

Therefore `F'` is decreasing and `F` is concave. For every active predecessor
`x=P(y_x)`, the affine function `L_x` has the same value and slope as `F` at
`y_x`. A tangent line to a concave function lies above its graph, so

```text
L_x(y) >= F(y)     for every active x and every y.       (3)
```

Sprint 1194 proves the same inequality for every inactive outer predecessor
`|x|>x_*`: slope ordering reduces the right tail to `L_x(1)>=F(1)`, and the
exact stationarity-target derivative makes this quantity monotone from its
calibrated endpoint; reflection handles the left tail.

Every target has its active equality contact. Combining that equality with
(3) and the inactive-tail guard yields the exact fixed-point identity

```text
T_(q_*) F = F > 0 on [-1,1].                  (4)
```

The choice `x=1` in (4) also gives the boundary cap

```text
F(y) <= q_* + (1-y)/2.                        (5)
```

## 4. Dimension-free upper bound

The pivots of `q_* I-H(c)` satisfy

```text
p_0 = q_*+(1-c_1)/2,
p_i = q_*+1-c_i/2-(c_i-1/2)c_(i+1)
      -(1-c_i^2)/(4p_(i-1)).
```

By (5), `p_0>=F(c_1)`. If `p_(i-1)>=F(c_i)>0`, monotonicity in the positive
pivot and (4) imply `p_i>=F(c_(i+1))>0`. Thus all LDL pivots are positive and

```text
lambda_max(H(c)) < q_*
```

for every finite aligned open carrier.

## 5. Sharpness

The exact connection converges exponentially backward to the positive
plateau with ratio coordinate `R>1`; reflection gives the opposite tail.
Consequently the reconstructed positive Jacobi eigenvector decays
geometrically in both directions and belongs to `ell^2`. It solves the
bi-infinite carrier equation at `q_*`.

Truncate this vector and its cosine profile symmetrically, install the required
open endpoint values `1` and `-1`, and use the truncated vector as a Rayleigh
test vector. Only the two vanishing tails see the endpoint replacement, so
the Rayleigh quotients converge to `q_*`. Hence the finite aligned supremum is
at least `q_*`; the LDL theorem gives the reverse inequality.

## Adjudication

The former `1e-8` rational slack in Sprint 1183 is removed. The failed
ordinary-degree route of Sprint 1189 and the continuation experiments of
Sprint 1190 are no longer load-bearing. Their failure was productive: the
correct object was not a mesh fixed-point degree, but the exact contact
geometry already carried by the validated domain wall.
