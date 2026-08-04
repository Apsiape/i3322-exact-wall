# The inactive sliver is a saturated boundary cell

Status: **300-bit interval certificate plus analytic global coercivity
theorem**

## 1. Quantitative outer-tail certificate

Let `I=P([-1,1])=[-x_*,x_*]`. Sprint 1194 defines the outer stationarity
extension `S(x)` and proves `S(x_*)=1` and `dS/dx>0` on the right inactive
tail, with reflection on the left. The new 300-bit Arb pass certifies on all
32,768 inherited tiles

```text
dS/dx>1/100.                                        (1)
```

The measured lower enclosure is `6.427794009447098`.

If `G(x)=L_x(1)-F(1)` is the endpoint support gap, the Sprint 1194 identities
give `G'(x)=S(x)-1` and `G(x_*)=0`. Twice integrating (1) yields

```text
G(x)>=(x-x_*)^2/200,       x>=x_*.                  (2)
```

Reflection gives the same estimate on the left tail.

## 2. Saturated predecessor coordinate

Define

```text
Pi_I(x)=min(x_*,max(-x_*,x)),
Y(x)=P^-1(Pi_I(x)).                                  (3)
```

`Y` is increasing, `10`-Lipschitz, and equals the ordinary inverse
predecessor coordinate on `I`. On the two tails it is the corresponding
endpoint `+1` or `-1`.

For the forward Bellman gap `Delta_+(x,u)`, strong concavity gives the usual
tangent estimate when `x in I`. When `x` is inactive, Sprint 1194's slope
ordering places `L_x` above the endpoint tangent, while (2) prices the
vertical excess. Therefore, on the complete rational response box,

```text
Delta_+(x,u)
 >=(u-Y(x))^2/20+dist(x,I)^2/200.                   (4)
```

Apply the reflected statement to the second Bellman gap:

```text
Delta_-(x,u)
 >=(x+Y(-u))^2/20+dist(u,I)^2/200.                  (5)
```

The geometric-mean/Cauchy step used in Sprint 1217 is global and gives

```text
r_0>=(Delta_++Delta_-)/2.                           (6)
```

Consequently

```text
r_0(x,u)
 >=[(u-Y(x))^2+(x+Y(-u))^2]/40
   +[dist(x,I)^2+dist(u,I)^2]/400.                  (7)
```

Equation (7) is the global quadratic contact theorem that Sprint 1231
needed. There is no fixed positive gap on the full sliver; the gap vanishes
quadratically at its boundary and is now priced correctly.

## 3. Exact moving partitions survive saturation

Use `Y(x)` rather than `P^-1(x)` to label the `X` cells. The boundary cell
simply contains the corresponding inactive tail. On exact contact,
`Y(P(u))=u`. Moreover sign reversal obeys

```text
Y(-P(u))=a(u),                                      (8)
```

including the endpoint values. Thus the moving-frame address identities are
unchanged. Points in the inactive sliver contribute an additional mean
coordinate error controlled by (7), hence by `sqrt(epsilon_0)`, with no
density assumption.

The far endpoint region outside `[-9/10,9/10]` is separated from `I` by the
fixed distance `9/10-x_*>0`; (7) gives it a genuine positive gap. It may be
discarded while the sliver between `x_*` and `9/10` remains inside the
saturated boundary cell, where all response weights retain the Sprint 1216
lower bounds.

## Consequence

Sprint 1231's use of a fixed `kappa_out` on the whole inactive sliver is
retracted. Replace it by the saturated coordinate and (7). Every resulting
rounding/weight error has the same `O(sqrt(epsilon))` rate already present in
the global ledger, so the explicit base `312^4` is unchanged.

