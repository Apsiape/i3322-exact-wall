# Contact, response, and flux force the two order reversals together

Status: **proved measure-coupling theorem; amplitude closure remains open**

## 1. One-dimensional identity

Let `nu` be a finite positive measure on an interval and let `a,b` be
decreasing maps.  The random variables `a(U)` and `b(U)`, with `U` distributed
according to `nu`, are comonotone.  Their common-source coupling is therefore
the monotone optimal coupling on the line, and

```text
W_1(a_*nu,b_*nu)=integral |a(u)-b(u)| dnu(u).         (1)
```

Equivalently, either side is the integral of the absolute difference of the
two cumulative distribution functions.  This is the continuum form of
Sprint 1244's weighted-footrule identity.

## 2. The common cut measures

Fix `t>0`.  Let `nu_A` and `nu_B` be the horizontal marginals of the Alice and
Bob event measures above `log(t)`.  Their total masses agree because the left
and right soft supports have the same nonzero spectrum.

Sprint 1243 and the soft-flag trace inequality give

```text
W_1(nu_A,nu_B)
 <=sqrt[d/(2t)] (40 epsilon_0)^(1/4)=:Delta_0.        (2)
```

Indeed, the cumulative difference at threshold `s` is at most
`sqrt(d)/(2sqrt(t))` times the contact intertwiner norm.  Integrating over the
length-two order interval and applying Cauchy--Schwarz together with
Sprint 1243 proves (2).

## 3. Each response is invariant up to debt and vertical flux

Let `nu_A^V` be the horizontal marginal obtained after Alice's vertical
response shift and then applying the same cut.  Sprint 1249 controls its
cumulative difference from `a_*nu_A`.  Integrating over the order interval
gives

```text
D_CDF(nu_A^V,a_*nu_A)<=9 sqrt(d epsilon_A/t).        (3)
```

The vertical-shift coupling changes membership in the retained tail only on
events counted by `Flux_A`.  Hence

```text
D_CDF(nu_A^V,nu_A)<=2 Flux_A.                        (4)
```

Here `D_CDF` is the integral of absolute cumulative differences; it remains
defined when the two finite measures have slightly different masses.  The
same statements hold for Bob:

```text
D_CDF(nu_B^V,b_*nu_B)<=9 sqrt(d epsilon_B/t),
D_CDF(nu_B^V,nu_B)<=2 Flux_B.                        (5)
```

Therefore

```text
W_1(a_*nu_A,nu_A)
 <=9 sqrt(d epsilon_A/t)+2 Flux_A,

W_1(b_*nu_B,nu_B)
 <=9 sqrt(d epsilon_B/t)+2 Flux_B.                  (6)
```

The equal-mass endpoints in (6) turn `D_CDF` back into ordinary `W_1`.

## 4. Coalescence bound

The certified derivative box gives `Lip(a)<=20`.  Pushforward stability and
the triangle inequality imply

```text
W_1(a_*nu_B,b_*nu_B)
 <=(1+Lip(a))W_1(nu_A,nu_B)
   +W_1(a_*nu_A,nu_A)+W_1(b_*nu_B,nu_B).             (7)
```

Using (1)--(6), `b(u)=-u`, and `Lip(a)<=20` gives

```text
integral |a(u)+u| dnu_B(u)
 <=21 sqrt[d/(2t)] (40 epsilon_0)^(1/4)
   +9 sqrt(d/t)(sqrt(epsilon_A)+sqrt(epsilon_B))
   +2(Flux_A+Flux_B).                                (8)
```

This is grid-free and fibre-blind in the correct sense: orthogonal response
targets carrying the same ordered event mass need not be identified as
vectors.  Their scalar amplitudes are compared through the complete measure,
while every vertical-cut discrepancy is paid by flux.

## 5. With the averaged cut

Take the cut supplied by Sprint 1251 with `L<=kappa d`, so `t>=exp(-kappa d)`
and

```text
Flux_A+Flux_B<=4 log(13/2)/kappa.                    (9)
```

Then

```text
integral |a(u)+u| dnu_B(u)
 <=21 sqrt(d/2) exp(kappa d/2)(40 epsilon_0)^(1/4)
   +9 sqrt(d) exp(kappa d/2)
      (sqrt(epsilon_A)+sqrt(epsilon_B))
   +8 log(13/2)/kappa.                               (10)
```

For fixed large `kappa`, exponentially small Bell deficit therefore forces a
positive retained event core onto the region where the two order reversals
nearly coincide.

The remaining amplitude lemma must show that on this near-coincidence region,
the two vertical response translations cannot both preserve the retained
event measure without paying the certified quarter margin.  No universal
dimension lower bound is claimed until that lemma lands.

