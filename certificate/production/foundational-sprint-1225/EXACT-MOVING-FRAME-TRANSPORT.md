# Moving contact frames have exact addresses and approximate amplitudes

Status: **exact two-frame packet theorem; near-fixed charging remains open**

## Later correction

The exact theorem and address identities below survive. The sentence in
Section 4 that the complete drift-side structural chain was already closed
was premature: a transport-closed path/endpoint family had not yet been
written. Sprints 1228--1230 replace that claim with a one-initial-slice
forward-exit theorem. No part of the abstract two-frame estimate is retracted.

## 1. Two-frame packet transport

Let `{E_i}` and `{E'_i}` be complete orthogonal PVMs and let `K` be unitary
with

```text
K E_i K*=E'_i.                                      (1)
```

Choose fine projections `G_i<=E_i` and `G'_i<=E'_i`, and put

```text
G=sum_i G_i,
G'=sum_i G'_i.                                      (2)
```

For every vector `w`, define

```text
delta=||Kw-w||,
gamma_s=||(I-G)w||,
gamma_t=||(I-G')w||,
D^2=sum_i ||K G_iw-G'_i w||^2.                     (3)
```

Then

```text
D<=delta+gamma_s+gamma_t,                           (4)
D^2<=3(delta^2+gamma_s^2+gamma_t^2).               (5)
```

### Proof

For each index,

```text
K G_iw-G'_i w
 =K(G_i-E_i)w
  +[K E_iw-E'_i w]
  +(E'_i-G'_i)w.                                    (6)
```

The three indexed families occupy orthogonal target coarse blocks. Their
direct-sum norms are `gamma_s`, `delta`, and `gamma_t`, since

```text
K E_iw-E'_i w=E'_i(Kw-w).                           (7)
```

Minkowski proves (4), and the three-term square inequality proves (5). No
number-of-cells, dimension, rank, atom, or multiplicity factor appears.

## 2. Exact addresses in the contact dynamics

At frame `g`, the paired cells are

```text
U: g(I_i),
X: P(g(I_i)).                                       (8)
```

For Alice's nonlinear reflection `a=P^-1(-P)`,

```text
-P(g(I_i))=P(a g(I_i)).                             (9)
```

The sign relation of `K_A` therefore maps the source `X` coarse block exactly
to the same-index `X` block in frame `ag`. For Bob,

```text
-g(I_i)=b g(I_i),                                   (10)
```

so `K_B` maps the source `U` block exactly to the same-index block in frame
`bg`.

The fine projections also impose the paired cell of the other party. They
need not be conjugated exactly; their failure to transport is precisely the
packet error `D`, controlled by (4)--(5). Thus:

```text
coarse address: exact,
fine paired amplitude: approximate and paid.        (11)
```

## 3. Coordinate error is retired

Sprint 1224 introduced a provisional coordinate-step error `eta`. Equations
(9)--(11) show that no such geometric approximation is present: surviving
same-index ancestry follows the exact moved interval. Response debt and
off-contact/rank discard enter only as Hilbert norm error.

The ordered temporal-rank condition therefore sharpens to

```text
Delta>2H.                                           (12)
```

With `H<=20^n h`, it suffices to choose

```text
h<=Delta/(4*20^n).                                  (13)
```

The complete ancestry chain on a drift component then consumes at most `d`
local spectral ranks, while its recurrence residual is bounded by the sum of
response and two-frame discard energies.

## 4. Remaining assembly

The drift-side structural chain is now complete modulo collecting constants:

```text
contact coercivity
 -> paired moving cells
 -> Schmidt-rank compression
 -> exact-address packet transport
 -> <=d ordered sites
 -> endpoint/recurrence energy.                     (14)
```

The irreducible remaining sector is near-fixed contact. It must be converted
from small base displacement plus small packet debt into the scalar closure
residuals of Sprint 1211, or charged directly by nonneutral Bellman holonomy.
The inactive predecessor strip and final constant optimization also remain.
