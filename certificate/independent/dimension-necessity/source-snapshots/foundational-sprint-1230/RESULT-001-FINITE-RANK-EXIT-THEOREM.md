# One spectral slice must pay recurrence or exit

Status: **exact abstract theorem and simplified drift architecture; final
I3322 discard collection remains open**

## 1. Reverse endpoint theorem

Let chains be indexed by `i`. For chain `i`, suppose

```text
z_(k+1,i)=c_(k,i)z_(k,i)+s_(k,i),
0<c_(k,i),
max(c_(k,i),1/c_(k,i))<=M,
0<=k<n_i,
n_i<=d.                                             (1)
```

Iterating backward gives `z_(0,i)` as the terminal amplitude plus `n_i`
residual terms, each with coefficient at most `M^d`. Cauchy--Schwarz yields

```text
z_(0,i)^2
 <=(n_i+1)M^(2d)
   [z_(n_i,i)^2+sum_(k<n_i)s_(k,i)^2]
 <=(d+1)M^(2d)[...].                                (2)
```

Summing over arbitrary many chains proves

```text
sum_i [z_(n_i,i)^2+sum_(k<n_i)s_(k,i)^2]
 >=W_initial/[(d+1)M^(2d)],                         (3)

W_initial=sum_i z_(0,i)^2.
```

There is no total-chain-count hypothesis.

## 2. Why one slice is enough

Choose one shifted predecessor partition `Q={I_i}`. A local operator on a
`d`-dimensional space has at most `d` nonzero projections `1_(I_i)(U)` in
this initial slice. Follow only those nonzero cells through the exact moving
frames.

On a positive or negative quantitative drift component, Sprint 1224 makes

```text
I_i, tau(I_i), ..., tau^k(I_i)                      (4)
```

pairwise disjoint as long as the chain remains in the retained drift region.
Their nonzero spectral projections are orthogonal. Therefore every initial
cell has at most `d` retained good sites. By step `d` it must do one of three
things:

1. reach a zero local spectral projection;
2. leave the contact/active capture and pay discard; or
3. enter the near-fixed sector and pay Sprint 1229.

These are exactly the terminal amplitudes in (3). No global orbit
disintegration, simultaneous top-`d` selection, or scalar gain flow is
required.

For each fixed time, the transported descendants of distinct initial cells
remain disjoint because the moving frame is a bijection. Sprint 1225's direct
sum estimate therefore controls the sum of packet errors at that time with no
chain-count factor. Summing over at most `d` times costs only a factor `d` in
certificate energy.

## 3. I3322 constants

Sprint 1218 gives

```text
max(c,1/c)<=78/5.                                   (5)
```

Thus initial retained drift mass `W_D` pays

```text
exit energy+recurrence energy
 >=W_D/[(d+1)(78/5)^(2d)].                          (6)
```

This is stronger and cleaner than applying Sprint 1215 to a globally chosen
history family. The cost of converting the left side of (6) to Bell deficit
is still allowed to contain:

- a factor `d` from the number of response times;
- the moving-grid contact loss, of order `20^(2d)sqrt(epsilon)`; and
- fixed active/inactive and near-fixed constants.

All are compatible with an exponential lower bound on `q_*-Q_d`.

## 4. Remaining assembly statement

The final proof now needs one inequality, not a new object:

```text
terminal exit energy + recurrence energy
 <= C_1 d epsilon + C_2 20^(2d)sqrt(epsilon),        (7)
```

after the inactive and near-fixed sectors are charged. Combining (6)--(7)
immediately gives a computable exponential lower bound. Sprint 1231 must
write (7) with every discard counted once and no silent probability-density
assumption.

