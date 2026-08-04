# The near-fixed sector has an explicit packet-mass gap

Status: **exact inequality for already captured common packets; promotion to
the full near-fixed sector remains conditional on a localization lemma**

## 1. Certified derivative bounds

Write

```text
r(t)=sqrt(F(-t)/F(t)),
A(t)=b(t)r(t),
b(t)=sqrt(1-t^2)/2.                                 (1)
```

The Bob weight has the reflected ratio and obeys the same estimates. From
`1/5<F<13/10`, `|F'|<=3/2`, and `|t|<=9/10`,

```text
r<3,
|r'|<23,
|b'|<3/2,
|A'|,|B'|<16.                                      (2)
```

Since `A,B>1/12`,

```text
Lip(sqrt(A)),Lip(sqrt(B))<28.                       (3)
```

Also `sqrt(A),sqrt(B)>1/4` and `<6/5`. Sprint 1228's ratio
constant is therefore bounded by

```text
1/m+M/m^2 < 4+(6/5)16 <24.                         (4)
```

For a width-`h` pullback cell, `H_j` has diameter at most `h` because
`H_j subset b(I_j)` and `b` is an isometry. Since `Lip(P)<=2`, Alice's
source and target `X` cells have diameter at most `2h`; Bob's `U` cells have
diameter at most `h`. Hence the point-representative response errors obey

```text
|e_A| <=4 E_A+1344 h z,
|e_B| <=4 E_B+ 672 h z,                             (5)
```

where `E_A,E_B` are the raw scalar transport errors obtained by reverse
triangle and `z` is the source packet norm.

## 2. Contact coefficient oscillation

On the active square,

```text
r_0=q_*-d-A-B,
d=xu+(x-u)/2-1.
```

Each coordinate derivative of `r_0` has magnitude below `18`. The source and
target joint cells have `X` diameter at most `2h` and `U` diameter at most
`h`, so

```text
osc_cell(r_0)<=54h.                                 (6)
```

If `v` is a packet in the cell and `r_*` is the representative value, reverse
triangle gives

```text
r_* ||v|| <= ||r_0 v||+54h||v||.                   (7)
```

Moreover `0<=r_0<4`, so

```text
||r_0 v||^2<=4 <v,r_0v>.                            (8)
```

## 3. Explicit absorbed closure inequality

Apply Sprint 1226 at the representative pair and use (5)--(8). For the
captured source/target mass `W=z^2+z'^2`, contact energy `epsilon_0`, and raw
transport-error energy `E_A^2+E_B^2`,

```text
mu^2 W
 <=48 epsilon_0
   +(4656/25)(E_A^2+E_B^2)
   +C_h h^2 W,                                      (9)

mu=7/8000,
C_h=6(54)^2+(291/25)[(1344)^2+(672)^2]
   =131498424/5.                                    (10)
```

Indeed, the source and target packet families are each internally
orthogonal, but need not be mutually orthogonal.  Their combined contact
energy is therefore at most `2 epsilon_0`.  The contact terms consequently
contribute at most `6*4*(2 epsilon_0)+6(54h)^2W`. The two response terms
contribute at most

```text
(291/50)*32(E_A^2+E_B^2)
 +(291/25)[1344^2+672^2]h^2W,
```

which is (9).

Choose once and for all

```text
h_0=10^-7.                                          (11)
```

Exact rational arithmetic gives

```text
C_h h_0^2 < mu^2/2.                                 (12)
```

Therefore

```text
(mu^2/2)W
 <=48 epsilon_0+(4656/25)(E_A^2+E_B^2).             (13)
```

An already captured common packet family is charged by certificate-owned
energy with a fully explicit, dimension-independent constant. No fibre
isometry, amplitude-ratio division at zero, or packet-count factor occurs in
this conditional inequality.

## 4. Geometric capture

Sprint 1227's shifted pullback theorem leaves at most

```text
theta=20 Delta/h_0                                   (14)
```

of the near-fixed mass unpaired. This loss would re-enter the right side of
(13) through the two-frame target/source discard, multiplied by the response
constant, **provided** a localized-response theorem first controls the
restriction and its interface. The shifted overlap estimate alone does not
supply that theorem. Conditional on such a result, the final assembly would
choose a fixed
`theta<<mu^2` and set

```text
Delta_0=theta h_0/20.                               (15)
```

There is no scale obstruction: `Delta_0` is dimension-independent and may be
arbitrarily small. But `Delta_0=h_0/320`, which gives only `theta=1/16`, is
**not** promoted as sufficient for absorption.

## Scope

This theorem closes coefficient oscillation only after a valid common packet
capture has been supplied. It does not yet:

- localize the global response defect to the near-fixed restriction or charge
  the resulting commutator/interface terms;
- construct the global layered path decomposition on the drift sector;
- charge all source/target discards in one displayed inequality;
- remove the inactive predecessor strip; or
- state the final bound on `q_*-Q_d`.
