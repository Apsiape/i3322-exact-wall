# Drift makes moving cells consume local rank only once

Status: **exact conditional temporal-rank theorem; near-fixed charging and
coordinate-error assembly remain open**

## 1. Ordered moving-cell theorem

Let `tau:I->I` be increasing. On a positive drift component suppose

```text
tau(u)-u>=Delta>0.                                  (1)
```

Let `K_0,...,K_(n-1)` be interval cells, possibly drawn from different
partitions, each of diameter at most `H`. Choose `c_k in K_k` and suppose

```text
|c_(k+1)-tau(c_k)|<=eta.                            (2)
```

Then

```text
c_(k+1)-c_k>=Delta-eta.                             (3)
```

If `Delta>eta+2H`, every point of `K_(k+1)` lies strictly to the right of
every point of `K_k`: even the conservative endpoint estimate loses at most
`2H`. By iteration all cells are pairwise disjoint and strictly ordered.

For negative drift, apply the same argument to the reversed order. Thus the
constant is orientation independent.

## 2. Local dimension bound

Let `U` be a self-adjoint operator on a local `d`-dimensional Hilbert space.
Disjoint Borel intervals have mutually orthogonal spectral projections:

```text
1_(K_j)(U) 1_(K_k)(U)=0,       j!=k.                (4)
```

Every nonzero projection has rank at least one. Consequently an ordered
moving-cell chain with nonzero packet mass has

```text
n<=sum_k rank 1_(K_k)(U)<=d.                        (5)
```

This counts local spectral subspaces, not partition labels. The partitions
may change at every step; disjointness in the common spectrum of `U` is what
owns the rank.

## 3. Moving-frame constant

A base shifted cell has diameter `h`. Sprint 1223 shows that a frame with at
most `n` nonlinear `a` reflections has cell diameter at most

```text
H<=20^n h.                                          (6)
```

If `eta<Delta`, the choice

```text
h<=(Delta-eta)/(4*20^n)                             (7)
```

gives `2H<Delta-eta` with slack, so (5) applies. The inverse mesh cost in
Sprint 1222 is then at most

```text
1/h<=4*20^n/(Delta-eta).                            (8)
```

Combining (8) with the moving-frame rounding factor `20^n` produces at worst
`20^(2n)` distortion. This is crude but exponential, not superexponential.

## 4. Consequence for the proof architecture

The former temporal overcount

```text
d blocks per frame x n frames
```

is invalid on a drift component. Low-error ancestry moves monotonically
through disjoint spectral intervals, and the complete history consumes at
most `d` local ranks. Sprint 1215's endpoint theorem can therefore use `n<=d`
once the hypotheses `Delta` and `eta` are supplied.

## 5. Remaining two-region assembly

Fix a threshold `Delta>0` and split the active chart into

```text
drift region:      |tau(u)-u|>=Delta,
near-fixed region: |tau(u)-u|<Delta.                (9)
```

The drift region is governed by this theorem. The near-fixed region must be
charged by combining its small base displacement with Sprint 1211's universal
neutral-cycle margin: either its Bellman holonomy is nonneutral, or the two
closure residuals pay at least `q_*-1/4`.

The last structural assembly obligations are therefore explicit:

1. derive a coordinate-step error `eta` from the Hilbert packet debts;
2. turn the Sprint 1211 scalar closure margin into a mass bound on the
   near-fixed region; and
3. optimize `Delta` and `h` before comparing endpoint energy with the
   certificate.

No final dimension inequality is claimed before those estimates land.
