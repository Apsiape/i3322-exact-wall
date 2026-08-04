# A common output cell carries one vertical orientation

Status: **proved I3322 geometric theorem; final operator-error integration
remains open**

## 1. The Alice reversal is bi-Lipschitz

Recall

```text
a(u)=P^-1(-P(u)).                                    (1)
```

On the certified active chart, Sprint 1217 gives

```text
1/10<=P'(u)<=2.                                     (2)
```

Differentiation of (1) yields

```text
|a'(u)|=P'(u)/P'(a(u))>=1/20.                       (3)
```

Hence the inverse of the decreasing map `a` is Lipschitz with constant `20`.

## 2. Output cells control source diameter

Take two retained events whose actual Alice outputs `a(y)` lie in one
width-`delta` cell and whose actual Bob outputs `-u` lie in that same cell.
Then

```text
|y_1-y_2|<=20 delta,
|u_1-u_2|<=delta.                                   (4)
```

With `p=2 log(alpha)` and `q=2 log(beta)`, the derivative ledger gives

```text
Lip(p)<=28,       Lip(q)<=14.                       (5)
```

Therefore

```text
|(p-q)(e_1)-(p-q)(e_2)|
 <=28(20 delta)+14 delta
 =574 delta.                                        (6)
```

## 3. One orientation per common output cell

On the horizontally small sector of Sprint 1261,

```text
|p-q|>=g=25m_0/169.                                (7)
```

Choose

```text
delta<=g/574=25m_0/97006.                           (8)
```

Then the oscillation (6) is at most `g`.  Two values of opposite sign and
magnitude at least `g` differ by at least `2g`; consequently every
horizontally small retained event in one common output cell has the same sign
of `p-q`.

This removes the final within-prefix cancellation left by source-only
coarsening.  Aggregating over all source cells inside one output cell now
preserves the vertical translation area exactly.  Because each marginal has
at most `d` order atoms, the union occupies at most `2d` output cells; Sprint
1259 therefore recovers their total vertical bill with at most a `4d` prefix
factor.

## 4. Remaining assembly

The remaining inequality has no unnamed geometric datum.  For each common
output prefix, compare:

1. the Alice shifted source tail to its Alice response-output tail;
2. the Bob shifted source tail to its Bob response-output tail; and
3. the two response-output tails on the doubly addressed canonical coupling.

The first two are owned by Sprint 1249.  The third is zero on the retained
joint measure and costs only the explicitly recorded source/output/band
complements on the full measure.  Integrating those receipts over the finite
cut window is the final analytic ledger.  It is not carried out here, so no
universal dimension lower bound is claimed.

