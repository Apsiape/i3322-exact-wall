# Finite-difference full receipts before localizing the carrier

Status: **proved abstract localization theorem; final I3322 parameter ledger
remains open**

## 1. Four addresses and three tails

Fix an ordered grid with cells `1,...,n` and a finite cut window `J` of length
`W`.  Every event carries four cell addresses

```text
s_A, s_B, o_A, o_B,                                 (1)
```

for the Alice/Bob source and response-output coordinates, together with an
original tail indicator `I_0(ell)` and two shifted indicators
`I_A(ell),I_B(ell)`.

For the cumulative prefix `Q_j={1,...,j}`, define the **full** response
residuals

```text
D_A,j(ell)=integral [1_{o_A in Q_j} I_A
                     -1_{s_A in Q_j} I_0] dmu,

D_B,j(ell)=integral [1_{o_B in Q_j} I_B
                     -1_{s_B in Q_j} I_0] dmu.       (2)
```

These are exactly the quantities to which Sprint 1249 applies.  No event has
yet been removed.

Call an event address-good when

```text
s_A=s_B  and  o_A=o_B.                              (3)
```

Let `M_bad` be the mass of the complement.  On the good set define the
localized output-cell discrepancy

```text
r_i^G(ell)=integral_G 1_{o_A=i}
                     [I_A(ell)-I_B(ell)] dmu.        (4)
```

## 2. Exact cellwise telescoping

Finite-difference (2):

```text
d_A,i=D_A,i-D_A,i-1,
d_B,i=D_B,i-D_B,i-1.                                (5)
```

Let

```text
m_i=integral [1_{s_A=i}-1_{s_B=i}] I_0 dmu.         (6)
```

Before restricting to the good set, direct cancellation gives

```text
r_i^full=d_A,i-d_B,i+m_i.                           (7)
```

This is the four-term response triangle at cell level.  It is important that
(7) is formed before any complement is estimated.

## 3. The localization inequality

Finite differencing costs

```text
sum_i integral_J |d_sigma,i|
 <=2 sum_j integral_J |D_sigma,j|.                  (8)
```

For one source-bad event, (6) occupies at most two cells, so

```text
sum_i integral_J |m_i|<=2W M_source-bad.            (9)
```

For one address-bad event, the endpoint term removed from `r_i^full`
occupies at most two output cells, so its total `L1(J)` cost is at most
`2W` times its mass.  Applying the triangle inequality only after (7)--(9)
proves

```text
boxed:
sum_i integral_J |r_i^G|
 <=2 sum_j integral_J [|D_A,j|+|D_B,j|]
   +4W M_bad.                                       (10)
```

The constant multiplying bad mass is independent of `n`.  A prefix-by-prefix
complement estimate would instead charge the same event up to `n` times and
is therefore the wrong proof order.

## 4. I3322 specialization

For the shared grid of Sprint 1265, (3) means simultaneously

```text
y,u share a cell,
a(y),-u share a cell.                               (11)
```

The two terms in (2) are full order--resolution response rectangles and are
owned by Sprint 1249.  The grid-shift theorem bounds `M_bad` by

```text
w^-1 integral [|y-u|+|a(y)+u|] dPi.                (12)
```

Combining (10) with Sprint 1266 therefore preserves both cancellations that
the old packet localization lost:

1. cut flux is paid before prefix inversion; and
2. address failure is paid after finite differencing.

What remains is now an explicit parameter question rather than an untyped
operator arrow.  The window length in `4W M_bad` still multiplies the
horizontal address cost in (12).  One must either absorb that term in a
complete deficit ledger or replace the uniform grid by a bounded-complexity
sign partition.  No universal dimension lower bound is promoted here.

