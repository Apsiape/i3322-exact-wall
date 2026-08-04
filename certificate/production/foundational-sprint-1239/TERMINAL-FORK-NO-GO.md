# A terminal packet does not canonically commonize

Status: **exact finite countermodel to the proposed terminal shortcut**

## Countermodel

Let `H=R^3` with basis `e_0,e_1,e_2`, and use the unnormalised fixed vector

```text
w=e_0+e_1+e_2.
```

Let `K_A` swap `e_0,e_1` and let `K_B` swap `e_0,e_2`. Both are
self-adjoint involutions and

```text
K_A w=w,                    K_B w=w.                (1)
```

Take the localized source packet `G=|e_0><e_0|` and response-specific target
packets

```text
G'_A=|e_1><e_1|,            G'_B=|e_2><e_2|.       (2)
```

Then

```text
K_A G w=G'_A w=e_1,
K_B G w=G'_B w=e_2.                                (3)
```

Thus both fine packet errors vanish. Put `E'=span{e_1,e_2}` and assign one
coarse spectral label to this two-dimensional block. Both targets in (2) lie
below the same coarse block, but

```text
G'_A G'_B=0.                                       (4)
```

There is no nonzero common fine target. If instead the complete coarse target
`G'_c=E'` is used, then

```text
||K_A G w-G'_c w||=1,
||K_B G w-G'_c w||=1.                              (5)
```

The missing components cancel against the complementary packet equations:
for Alice, for example,

```text
K_A(I-G)w=(I-G'_A)w=e_0+e_2.                       (6)
```

Hence the global zero response defect contains no positive local bill that
can be assigned to the common fork.

## Shared-factor realization

The obstruction is not removed by the formal I3322 factor types.  Take
four-dimensional local spaces.  On Alice use the coarse sign operator

```text
X=diag(+1,-1,-1,+1),
```

let `J_A=(0 1)(2 3)`, and let `S_A=(0 2)(1 3)`.  On Bob use the same coarse
sign pattern for `U`, let `S_B=(0 1)(2 3)`, and let
`J_B=(0 2)(1 3)`.  Then

```text
J_A X J_A=-X,              J_B U J_B=-U.            (7)
```

Define

```text
K_A=J_A tensor S_B,        K_B=S_A tensor J_B.      (8)
```

The uniform vector on the sixteen product basis states is fixed by both
involutions.  The source basis packet `|0,0>` is sent to `|1,1>` by `K_A`
and to `|2,2>` by `K_B`.  Both targets have the same joint coarse label
`(X,U)=(-1,-1)`, but they are orthogonal multiplicity fibres.

Thus the shared-factor form and exact coarse sign relations do not forbid the
fork.  A stronger theorem must use the quantitative contact remainder `R_0`
and retain the fibre provenance on which it acts.

## Consequence

The proposed terminal repair after Sprint 1238 is not implied by the current
abstract packet data. An explicit drift endpoint does not by itself remove
the fibre-multiplicity ambiguity. The same cancellation that invalidated the
former near-fixed restriction reappears when two response-specific targets
are forced into one scalar amplitude.

This does **not** refute the coupled-sector theorem of Sprint 1238. It shows
only that its remaining terminal gate cannot be closed by scalar
commonization.

## Revised architecture

Any successful continuation must retain branch provenance. Two candidates
remain:

1. an I3322-specific operator/contact identity stronger than the shared
   factors and sign relations already tested here; or
2. a PSD/Gram-valued flow whose edge data remain orthogonal until energy is
   summed, as anticipated by the reciprocal-holonomy spoof of Sprint 1220.

The scalar packet route, with only norms and coarse labels, is now exhausted.
