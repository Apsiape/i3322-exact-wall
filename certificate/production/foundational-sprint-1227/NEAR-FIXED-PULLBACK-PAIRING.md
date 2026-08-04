# Pullback cells align common packet norms, not spectral fibres

Status: **exact set-theoretic pullback and shifted separation theorem; the
former fibrewise-promotion claim remains retracted**

## 1. Common source and target projections

Let

```text
a(u)=P^-1(-P(u)),
b(u)=-u,
tau=a b.
```

For a shifted target partition `Q_s={I_j}`, define

```text
H_j=a(I_j) intersect b(I_j).                       (1)
```

If `u in H_j`, then `a(u),b(u) in I_j`.  With commuting opposite-party
operators `X,U`, define the concrete joint projections

```text
G_j =1_(P(H_j))(X) 1_(H_j)(U),
G'_j=1_(P(I_j))(X) 1_(I_j)(U).                     (2)
```

They are internally orthogonal in `j`.  Since `H_j` lies in both response
pullback cells, `G_j` lies below both response source coarse blocks; `G'_j`
lies below both response target coarse blocks. Thus the two-frame packet
theorem can be *formed* for both responses using the same source and target
packet norms. This is weaker than, and does not require, an identification of
the pointwise target fibres. It also does not bound the two-frame complement
terms: the sums of these common packets need not capture the full vectors to
which the global response estimates apply.

The source family `{G_j}` and target family `{G'_j}` are not asserted mutually
orthogonal.  In particular, a global contact remainder may be counted once by
each family. Sprint 1229 retains the resulting factor two.

## 2. Near-fixed overlap loss

From `tau=a b` and involutivity of `a`,

```text
a tau=b.
```

On the near-fixed region `|tau(u)-u|<=Delta`, the certified Lipschitz bound
`Lip(a)<=20` gives

```text
|a(u)-b(u)|<=20 Delta.                             (3)
```

A point is omitted from the common pullback precisely when `a(u)` and `b(u)`
fall into different cells.  The exact shifted-grid separation identity gives

```text
Pr_s[unpaired at u]<=|a(u)-b(u)|/h<=20 Delta/h.    (4)
```

After integration against any subprobability measure, one deterministic shift
therefore leaves unpaired mass at most `20 Delta/h`. The same averaging may be
performed over the finite sum of all source/target occurrences; no cell-count
factor appears.

## 3. Retraction retained

Common coarse addresses do not construct a partial isometry between
pointwise reflected spectral fibres.  A direct-integral lift of Sprint 1226
with zero coefficient oscillation is therefore not claimed.  Sprint 1228 uses
only the common norms from (2), and Sprint 1229 explicitly pays cellwise
coefficient oscillation. A further localization lemma is still required to
control

```text
||(I-sum_j G_j)L_sigma psi||,
||(I-sum_j G'_j)L_sigma psi||.
```

The shifted unpaired-mass estimate controls these terms only after an
appropriate near-fixed restriction; it does not justify deleting the mass
outside that restriction.
