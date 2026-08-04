# Near-matched cells cannot cancel their vertical debt

Status: **proved abstract cancellation barrier; common output-prefix receipt
remains open**

## 1. Split the stable quarter wall

On every retained event, Sprint 1257 gives

```text
m_0/2 <=K|A-B|+G|p-q|,
K=182/5,       G=169/100.                            (1)
```

Set

```text
theta=m_0/(4K)=5m_0/728,
g=m_0/(4G)=25m_0/169.                               (2)
```

Call an event horizontally large if `|A-B|>=theta`.  Every other event obeys

```text
|p-q|>=g.                                           (3)
```

## 2. The small cells force one orientation

The certified derivative box gives

```text
Lip(p)<=28,       Lip(q)<=14.                        (4)
```

For two events whose source coordinates lie in one width-`h` common cell,

```text
|(p-q)(e_1)-(p-q)(e_2)|<=42h.                       (5)
```

The Sprint-1257 width condition is much stronger than needed:

```text
h<=25m_0/41769
=>42h<=1050m_0/41769 <25m_0/169=g.                  (6)
```

Two values of opposite sign and magnitude at least `g` differ by at least
`2g`.  Hence all horizontally small events in one common cell have the same
sign of `p-q`.

## 3. Large events are billed, not deleted

Let `M_S,M_L` be the core masses of the horizontally small and large events,
and let

```text
D_H=integral_core |A-B| dmu.                         (7)
```

Then

```text
M_L<=D_H/theta.                                     (8)
```

For cell `i`, restrict the measure to the core `zeta in [-H,0]`, and let
`r_i(L)` be the difference of its two vertically shifted tail indicators,
including both small and large core events.  Suppose `|p|,|q|<=B`.  The
same-sign property and the translation-area identity give

```text
integral |r_i^S(L)| dL >=g M_(S,i),
integral |r_i^L(L)| dL <=2B M_(L,i).                (9)
```

The reverse triangle inequality therefore yields

```text
sum_i integral |r_i(L)| dL
 >=g M_S-2B M_L.                                   (10)
```

If `E_sync` is the synchronized-prefix area of Sprint 1259 and `n<=d`,

```text
sum_i integral |r_i|<=2d E_sync.                   (11)
```

Combining (8)--(11) proves the cancellation-safe core estimate

```text
boxed:
M_core
 <=(2d/g) E_sync
   +[(1+2B/g)/theta] D_H.                           (12)
```

Every term has an owner.  Horizontally large events pay through `D_H`; their
maximum possible vertical cancellation pays the factor `2B`.  On the rest,
cellwise sign coherence turns the vertical shift into observable tail area.

## 4. What remains

Sprint 1252 controls the uncoarsened horizontal cost, and Sprints 1256 and
1260 control the source-cell complement over every relevant tail.  Equation
(12) shows that the last mathematical comparison is now narrower than a
general fibre-transport theorem: construct common **output** prefixes for the
horizontally small retained events and bound their `E_sync` by the two
operator response receipts plus the explicitly billed source/output
interfaces.

That output-prefix theorem is not proved here.  No universal dimension lower
bound is claimed. In particular, applying an operator response receipt to the
core-restricted `r_i` must charge every event crossing either vertical
boundary; the theorem does not infer that restriction for free.
