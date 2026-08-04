# Contact and horizontal debt buy two common addresses

Status: **proved positive-measure two-stage descent; operator receipt assembly
remains open**

## 1. Abstract two-grid theorem

Let `Gamma` be a finite positive measure carrying source coordinates `(y,u)`
and actual response-output coordinates `(A,B)`.  Put

```text
C_src=integral |y-u| dGamma,
D_out=integral |A-B| dGamma.                         (1)
```

For a width-`h` source grid averaged over its shift, the separation identity
of Sprint 1256 gives

```text
average_s Gamma(source cells differ)<=C_src/h.       (2)
```

Choose one shift satisfying (2), and restrict to its common-source set
`G_src`.  On that positive restriction, average an independent width-`delta`
grid over output shifts.  Since restriction can only decrease a positive
integral,

```text
average_r Gamma|_(G_src)(output cells differ)
 <=D_out/delta.                                     (3)
```

Thus some pair of shifts retains

```text
G=G_src intersect G_out                             (4)
```

with

```text
boxed:
Gamma(G)>=Gamma(all)-C_src/h-D_out/delta.            (5)
```

Every retained event has both a common source address and a common output
address.  The grids may have unrelated widths and shifts.

## 2. I3322 ownership

On the finite vertical band:

- Sprints 1256 and 1260 bound `C_src` from the canonical joint coupling;
- Sprint 1252 bounds the horizontal response cost that owns `D_out`;
- Sprint 1257 fixes a source width small enough to retain half the pointwise
  quarter wall;
- Sprint 1261 uses that same source address to prevent vertical sign
  cancellation; and
- Sprint 1262 prices the upper vertical boundary, while Sprint 1251 prices
  the lower one.

The output address is the missing typing datum for Sprint 1259.  A cumulative
union of output cells is now literally the same measurable output set for the
Alice and Bob response measures.  Consequently the two response rectangle
receipts can be compared at common output prefixes after adding the explicit
source, output, and vertical-interface bills.

## 3. Scope

Equation (5) is a positive-measure theorem; it never localizes a response
vector.  It proves the geometric carrier needed by the final receipt
assembly, not the assembly itself.  In particular, the response errors must
still be integrated over the chosen vertical cut range with their
`t^-1/2` cost.  No universal dimension lower bound is claimed here.

