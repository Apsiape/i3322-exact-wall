# One charged grid commonizes every tail used by the flow

Status: **proved strengthened source descent; output-prefix comparison remains
open**

## 1. The deep-resolution half

Let `Pi` be the canonical joint order--resolution coupling of Sprint 1254.
At `t=exp(zeta)<=1`, that sprint proves

```text
integral |y-u|^2 d pi_t <=360 epsilon_0/t^3.         (1)
```

Therefore

```text
integral_(-K)^0 integral |y-u|^2 d pi_(exp(zeta)) d zeta
 <=120 epsilon_0 [exp(3K)-1].                       (2)
```

## 2. The high-resolution half is integrable

Write, as in Sprint 1254,

```text
Z_t=sqrt(t)D(tI+rho_B)^-1,
C=Y D-D U.                                          (3)
```

For `t>=1`, the same exact commutator identity gives

```text
||Y Z_t-Z_t U||_HS
 <=||C||_HS/sqrt(t)+2||C||_HS/t^(3/2)
 <=3||C||_HS/sqrt(t).                               (4)
```

Since `||C||_HS^2<=40 epsilon_0`,

```text
integral |y-u|^2 d pi_t <=360 epsilon_0/t.          (5)
```

Using `d zeta=d t/t`,

```text
integral_0^infinity integral |y-u|^2 d pi_(exp(zeta)) d zeta
 <=360 epsilon_0.                                   (6)
```

Combining (2) and (6) yields the complete upper-tail bill

```text
boxed:
C_K:=integral_({zeta>=-K}) |y-u|^2 dPi
 <=120 epsilon_0 [exp(3K)+2].                       (7)
```

No lower spectral cutoff occurs.

## 3. One shifted order grid

The upper-tail mass is at most the total event mass, hence at most Schmidt
rank `d`.  Averaging a width-`h` interval grid over its shift exactly as in
Sprint 1256 gives a deterministic shift with

```text
Pi({zeta>=-K, different order cells})
 <=sqrt(120 d epsilon_0 [exp(3K)+2])/h.              (8)
```

Thus one grid commonizes every tail whose lowest queried resolution is at
least `-K`.  In particular, the Sprint-1255 cut range

```text
-R<=L<=H+R,       |p|,|q|<=B                        (9)
```

is fully covered by choosing

```text
K=H+R+B.                                            (10)
```

Every event entering any `f_i(L+p_i)` or `f_i(L+q_i)` then lies in the
commonized upper tail.  The earlier core lower bound remains valid, with the
larger explicit bad-mass bill (8).

## 4. Consequence and boundary

This closes a latent scope issue in the first common-cell theorem: the grid is
now valid simultaneously for the core and every shifted tail used by a finite
flow argument. It still does not compare the two response output prefixes.
That synchronized-prefix receipt remains the sole analytic gate identified in
Sprint 1259, and no universal dimension lower bound is claimed.

