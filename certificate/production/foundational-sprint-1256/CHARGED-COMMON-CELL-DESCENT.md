# Contact debt buys a common coarse source without deleting a complement

Status: **proved positive-measure descent; response-output descent remains
open**

## 1. Restrict the canonical coupling, not a Hilbert vector

Let `Pi` be the joint Alice-order x Bob-order x log-resolution measure from
Sprint 1254.  For `H>0`, let

```text
Gamma_H=Pi restricted to {-H<=zeta<=0},
M_H=Gamma_H(all).                                    (1)
```

Its two order marginals are the Alice and Bob event cores.  Sprint 1255
gives the dimension-free state-mass lower bound

```text
M_H >=[1-exp(-H)]/[2(1+exp(-H))],                   (2)
```

while total event mass gives `M_H<=d`.

At `zeta=-L`, Sprint 1254 proves

```text
integral |y-u|^2 d pi_(exp(-L))
 <=360 epsilon_0 exp(3L).                            (3)
```

Integrating from `L=0` to `H` yields

```text
C_H:=integral |y-u|^2 d Gamma_H
 <=120 epsilon_0[exp(3H)-1].                         (4)
```

## 2. Shifted order cells

For width `h>0` and shift `s in [0,h)`, let `Q_s` be the half-open interval
grid with boundaries `s+kh`.  Put

```text
Bad_s={(y,u,zeta): y and u lie in different Q_s cells}. (5)
```

For fixed `y,u`, averaging over `s` gives

```text
Pr_s[Bad_s]<=min(1,|y-u|/h)<=|y-u|/h.               (6)
```

Tonelli and Cauchy--Schwarz therefore give

```text
average_s Gamma_H(Bad_s)
 <=h^-1 integral |y-u| d Gamma_H
 <=sqrt(M_H C_H)/h
 <=sqrt(120 d epsilon_0[exp(3H)-1])/h.               (7)
```

Hence at least one deterministic shift satisfies the same upper bound.

## 3. The retained common source

For such a shift, restrict `Gamma_H` to the positive set

```text
Good_s=Bad_s^c.                                      (8)
```

Each event in `Good_s` has one common coarse order address.  Its retained
mass obeys

```text
Gamma_H(Good_s)
 >=[1-exp(-H)]/[2(1+exp(-H))]
   -sqrt(120 d epsilon_0[exp(3H)-1])/h.              (9)
```

This is a classical restriction of a positive measure after the complete
operator information has been lifted.  It is not a localization of the
response vector.  The omitted complement is exactly `Gamma_H(Bad_s)` and is
fully billed by (7), so the Sprints 1227--1239 countermodels do not apply.

## 4. Scope

Equation (9) closes the **source commonization** part of the continuous-to-
coarse descent.  The next theorem must show that the order-or-resolution wall
survives the cell diameter and then transport these common-cell measures
through the two response outputs.  No universal dimension lower bound is
claimed here.

