# Canonical moving packets close the ancestry ledger

Status: **analytic functional-analytic theorem plus 100,000 exact hostile
finite models; not a blind external reconstruction**

## 1. Canonical family

Let `Q={I_i}` be the initial predecessor partition.  At every moved frame
`g_k`, define

```text
G_(k,i)=1_(P(g_k I_i))(X) 1_(g_k I_i)(U).           (1)
```

The factors commute because `X` and `U` act on opposite tensor factors.
They therefore define one canonical joint projection rather than a choice of
fibre coordinates.

For a response reflection `r`, the exact coarse address theorem takes frame
`g_k` to `r g_k`.  The two-frame packet theorem permits arbitrary fine source
and target projections below those coarse blocks.  Choose precisely

```text
source=G_(k,i),       target=G_(k+1,i),
g_(k+1)=r g_k.                                      (2)
```

Its packet error measures the failure of the response unitary to carry the
other party's fine condition.  Nothing requires exact conjugacy of the fine
projections.  Most importantly, the target in (2) is literally the source in
the next application.  Thus the target norm at time `k` and source norm at
time `k+1` are one number by definition, not by a partial isometry.

For a full `tau=ab` step, insert the canonical intermediate frame `b g_k`.
The Bob target is the Alice source, and the Alice target is the next `tau`
source.  Sprint 1214's scalar composition therefore applies to a genuinely
transport-closed amplitude path.

## 2. Horizontal ownership

For fixed `k`, the sets `g_k(I_i)` are pairwise disjoint because `g_k` is a
Borel bijection.  Their `P` images are pairwise disjoint because `P` is
monotone.  Hence

```text
G_(k,i)G_(k,j)=0,       i!=j.                       (3)
```

Borel first-exit restrictions only replace a cell by a subset and preserve
(3).  Every application of the two-frame direct-sum inequality therefore
sums all initial-cell descendants at that time with no cell-count factor.

## 3. Vertical rank ownership

On a retained quantitative-drift chain, the `U` cells

```text
g_0(I_i), g_1(I_i), ..., g_(n-1)(I_i)              (4)
```

are pairwise disjoint by the ordered-cell theorem.  Their spectral
projections for the same local operator `U` are mutually orthogonal.  If the
canonical packet at a site is nonzero, its `U` spectral projection is
nonzero and consumes rank at least one.  Therefore

```text
n<=rank(I_local)<=d.                                (5)
```

This is a per-chain bound.  It does not assert that the sum of all chain
lengths is at most `d`, and the reverse endpoint theorem does not require
such an assertion.

## 4. The only two multiplicities

At one response time, (3) makes packet-error energy additive.  There are at
most `d` good response times by (5), so reusing the global response debt costs
at most `d`.

At one exit time, terminal packets again satisfy (3).  Grouping by first-exit
time gives at most `d` groups, so reusing the charged near/far/discard mass
also costs at most `d`.  No sum introduces the number of initial cells.

Together with Sprint 1230's reverse endpoint estimate, this proves the
functional-analytic ownership asserted in the upper and lower bills of
Sprints 1231 and 1233.

## 5. Hostile finite model

The independent guard generated 100,000 exact path systems.  It varied local
dimension, initial-cell count, time count, injective moving frames, stopped
chain lengths, exact signed-permutation response models, and packet
perturbations.  It found no closure, horizontal-injectivity, vertical-reuse,
direct-sum, or multiplicity violation.

The finite model is a guard, not the proof.  Equations (1)--(5) are the
functional-analytic reconstruction.

## Boundary

This sprint does not rederive the Bell certificate, contact coercivity,
moving-grid loss, coefficient bounds, or near-fixed closure estimate.  It is
also not epistemically blind: it was written after inspecting the disputed
upstream chain.  The public repository remains unchanged until a genuinely
independent reconstruction checks the entire proof package.
