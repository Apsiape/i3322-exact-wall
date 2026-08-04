# The quarter wall is a pointwise order-or-resolution dichotomy

Status: **proved scalar theorem; global event-measure integration remains
separate**

## 1. Two response ratios on one exact contact

Fix `u` on the certified active contact graph and put

```text
x=P(u),
a(u)=P^(-1)(-P(u)),

alpha(u)=sqrt(F(-P(u))/F(P(u))),
beta(u) =sqrt(F(u)/F(-u)).                           (1)
```

The active box gives

```text
5/13 < alpha,beta < 13/5.                            (2)
```

Let `b_x=b(x)`, `b_u=b(u)`, and choose the weighted mean

```text
rho=(b_x alpha+b_u beta)/(b_x+b_u).                  (3)
```

The active contact is interior, so the denominator is positive.  In the
notation of Sprint 1226, `r_0(x,u)=0`, and (3) makes `R_+=0`.  The exact
closure coercivity therefore gives

```text
m_0 <= |R_-|,
m_0=q_*-1/4.                                         (4)
```

The certificate-owned decomposition of `R_-` is

```text
R_-=rho r_0(-x,-u)+A(-x)(rho-alpha)+B(-u)(rho-beta). (5)
```

Because the deviations from a weighted mean have opposite signs,

```text
|rho-alpha|+|rho-beta|=|alpha-beta|.                 (6)
```

Using `rho<=13/5` and `A,B<=13/10`,

```text
m_0 <= (13/5)|r_0(-x,-u)|+(13/10)|alpha-beta|.       (7)
```

## 2. Order mismatch owns the reflected contact debt

By definition, `P(a(u))=-x`.  The exact contact-covariance theorem says that
the active predecessor graph is the double-contact zero set; hence the
response-reflected pair `(-x,a(u))` is again on that zero set, and

```text
r_0(-x,a(u))=0.                                      (8)
```

On `[-9/10,9/10]`, the certified identities

```text
F'=1/2-P,       1/5<F<13/10,       1/10<P'<2
```

give `|B'|<12`.  Since

```text
partial_v r_0(-x,v)=x+1/2-B'(v),
```

the safe rational bound is

```text
|r_0(-x,-u)| <=14 |a(u)+u|.                          (9)
```

## 3. Resolution mismatch owns the ratio debt

For positive numbers in the interval (2),

```text
|alpha-beta| <=(13/5)|log alpha-log beta|.           (10)
```

The exact Alice involution gives

```text
alpha(a(u))=1/alpha(u).                              (11)
```

Moreover the same certified derivative box gives

```text
|(log alpha)'|<14.                                   (12)
```

The composed event translation of Sprint 1250 is

```text
h(u)=2 log beta(u)+2 log alpha(-u).                  (13)
```

Combining (11)--(13),

```text
|log alpha-log beta|
 <=|h(u)|/2+14|a(u)+u|.                              (14)
```

Substitution of (9), (10), and (14) into (7) gives the
slightly sharper coefficients `2093/25` and `169/100`.  Rounding upward to
simple rationals yields

```text
boxed:  m_0 <=84 |a(u)+u|+(17/10)|h(u)|.             (15)
```

## 4. Meaning

Equation (15) is the missing scalar bridge between the exact quarter wall
and the canonical event measure.  It says that no active contact event can
simultaneously make the two response reversals almost equal and make the
composed resolution translation almost neutral.

Unlike the older amplitude-packet closure, (15) does not identify the two
response target fibres.  The two observable debts are exactly the horizontal
and vertical motions of one positive measure.

This theorem alone is not a dimension lower bound.  The remaining task is a
finite-rank event theorem converting approximate invariance into an upper
bound for the integrated `|h|` term while charging the logarithmic boundary.
