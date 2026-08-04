# A one-sided prefix window keeps boundary flux outside the rank factor

Status: **proved abstract transport theorem; response-prefix localization
remains open**

## 1. Setup

Let `mu` be a finite positive measure of events.  Every address-good event
has an ordered fibre `i in {1,...,n}`, a vertical coordinate `zeta`, and two
shifts

```text
p,q in [-B,B].                                      (1)
```

Fix a cut depth `L` and call `zeta>=-L` the core.  Address-bad core mass is
denoted by `M_bad`; those events are not assigned a common fibre.

Among the address-good core events, split the mass into `M_S+M_L`.  On the
small sector `S`, require

```text
|p-q|>=g,                                           (2)
```

and require the sign of `p-q` to be constant within each fibre.  No sign or
gap condition is imposed on the large sector.

For every good fibre define the **full**, not core-restricted, shifted-tail
difference

```text
r_i(ell)
 =integral_(fibre i)
   [1_{zeta+p>=-ell}-1_{zeta+q>=-ell}] dmu,         (3)

R_j(ell)=sum_(i<=j) r_i(ell).                       (4)
```

Only the one-sided cut window is queried:

```text
E_L=integral_(-infinity)^L max_j |R_j(ell)| d ell. (5)
```

Finally let `Phi_L` be the sum of the two full response fluxes across the cut
`-L`:

```text
Phi_L=integral [
 |1_{zeta>=-L}-1_{zeta+p>=-L}|
+|1_{zeta>=-L}-1_{zeta+q>=-L}|] dmu.               (6)
```

## 2. The one-event boundary fact

For one event, the two indicators in (3) differ on the interval between

```text
-zeta-p  and  -zeta-q,                              (7)
```

whose full length is `|p-q|<=2B`.

If the event is in the core, the part of (7) above `L` can be nonempty only
if at least one shifted copy crosses out through `-L`.  If the event is
outside the core, (7) can meet `(-infinity,L]` only if at least one shifted
copy crosses in.  Therefore:

```text
core event:
  integral_^L |indicator difference|
  >=|p-q|-2B (crossing count),                      (8)

exterior event:
  integral_^L |indicator difference|
  <=2B (crossing count).                            (9)
```

There is no unrecorded shell mass in either statement.

## 3. Coherent fibres and prefix recovery

On the small core of one fibre, all indicator differences have the same
pointwise sign.  Hence their `L1` norms add.  The large core can cancel at
most `2B M_L`, and every exterior contaminant is charged by (9).  The reverse
triangle inequality gives

```text
sum_i integral_^L |r_i|
 >=g M_S-2B M_L-2B Phi_L.                          (10)
```

Finite differencing of (4), exactly as in Sprint 1259, gives

```text
sum_i integral_^L |r_i|<=2n E_L.                  (11)
```

Combining (10)--(11), adding `M_L`, and restoring the address-bad core proves

```text
boxed:
M_core
 <=M_bad
   +(2n/g) E_L
   +(1+2B/g) M_L
   +(2B/g) Phi_L.                                  (12)
```

The prefix discrepancy pays the fibre-count factor.  The physical boundary
flux does not.

If horizontal displacement is at least `theta` on the large sector and its
core first moment is `D_L`, then `M_L<=D_L/theta`, so

```text
boxed:
M_core
 <=M_bad
   +(2n/g) E_L
   +[(1+2B/g)/theta] D_L
   +(2B/g) Phi_L.                                  (13)
```

## 4. I3322 consequence and remaining gate

Sprints 1261 and 1264 supply the sign and gap hypotheses with

```text
g=25m_0/169,
B=2 log(13/2),
n<=2d.                                             (14)
```

Sprint 1251 can select `L` with dimension-independent `Phi_L` by averaging
over an interval of length proportional to `d`.  Equation (13) shows that
this flux remains dimension-independent after vertical recovery; the feared
extra factor of `d` was an artifact of restricting the shifted-tail measure
before applying the response receipt.

One gate remains.  The cumulative quantities `R_j` in (5) are formed on the
address-good common carrier, whereas Sprint 1249 controls full response
rectangles.  Passing from the full rectangles to (5) must preserve the
four-term telescoping cancellation; bounding four discarded complements
separately would recreate a cut-window factor.  This theorem does not make
that localization step and does not promote a universal dimension bound.

