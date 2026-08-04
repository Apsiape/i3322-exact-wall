# One grid supplies the common prefix required by both responses

Status: **proved common-carrier theorem; numerical receipt integration remains
open**

## 1. The four-coordinate grid

Let `Gamma` be the positive canonical joint event measure on a finite vertical
band.  Write

```text
A=a(y),       B=-u.                                  (1)
```

For a width-`w` interval grid with shift `s`, call an event bad if either

```text
y and u occupy different cells,
A and B occupy different cells.                     (2)
```

For each fixed event, shift averaging gives

```text
Pr_s[bad]
 <=|y-u|/w+|A-B|/w.                                 (3)
```

Tonelli therefore supplies one deterministic shift satisfying

```text
boxed:
Gamma(Bad_s)
 <=w^-1 integral [|y-u|+|A-B|] dGamma.              (4)
```

This one-grid specialization is stronger than the independent two-stage
address of Sprint 1263 for the purpose of response composition.

## 2. Prefix indicators coincide twice

Let `Q_k` be any cumulative union of grid cells.  On the retained good set,

```text
1_{y in Q_k}=1_{u in Q_k},
1_{a(y) in Q_k}=1_{-u in Q_k}.                      (5)
```

The first identity compares the untransformed Alice and Bob event marginals
on one canonical carrier.  The second compares the two response-transformed
marginals on the same carrier.  Thus, for every common grid prefix, the exact
triangle has the required type:

```text
Alice shifted source prefix
  --Alice response receipt--> Alice original prefix
  --joint good-set identity--> Bob original prefix
  --Bob response receipt--> Bob shifted source prefix. (6)
```

Every replacement in (6) uses the same numerical set `Q_k`.  No fibre label,
spectral atom matching, or post-hoc prefix correspondence is selected.

## 3. Compatibility with the previous constants

Choose the shared width to be the output width of Sprint 1264,

```text
w=25m_0/97006.                                      (7)
```

This is smaller than the source width `25m_0/41769`, so the Sprint-1257
coarse quarter wall and Sprint-1261 source-cell sign bound remain valid.
Sprint 1264 then gives sign coherence across the entire common output cell.

The retained output cells form at most `2d` occupied addresses because each
of the two order marginals has at most `d` atoms.  Complete prefix tails
therefore recover the vertical bill with the `4d` factor already recorded in
Sprint 1264.

## 4. What remains

The missing arrow is no longer geometric or type-theoretic.  Insert the
Sprint-1249 response error at each prefix in (6), integrate over the finite
band's cut window, and add:

1. the one-grid bad mass from (4);
2. the lower boundary flux selected by Sprint 1251; and
3. the dimension-free upper cap from Sprint 1262.

That explicit ledger has not yet been optimized or independently replayed.
No universal dimension lower bound is claimed here.

