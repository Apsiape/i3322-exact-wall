# The inactive endpoint gap is globally additive

Status: **exact symbolic theorem plus 200,000 exact-rational signed checks**

The Bellman support line is affine in its target:

```text
L_x(y)=b(x)+(1/2-x)y.
```

Let `L_*` be the active right-endpoint line, whose predecessor is `x_*` and
whose contact target is `1`.  Exact subtraction gives

```text
L_x(y)-L_*(y)
 =[L_x(1)-L_*(1)]+(x-x_*)(1-y).                    (1)
```

For `x>=x_*` and `y in [-1,1]`, the second term is nonnegative.  Therefore
the complete line separation is at least its endpoint separation.  On the
left, anchoring at `-1` gives

```text
L_x(y)-L_-*(y)
 =[L_x(-1)-L_-*(-1)]+(-x_*-x)(y+1),                (2)
```

again with nonnegative remainder for `x<=-x_*`.

Combining (1)--(2) with Sprint 1232's certified endpoint estimate gives, on
either inactive tail,

```text
L_x(y)-L_endpoint(y)>=dist(x,I)^2/200.              (3)
```

The endpoint line is the active tangent, so its already-certified strong-
concavity gap adds independently.  Thus the inactive half of Sprint 1232's
saturated contact inequality is valid exactly; it does not rely on a sampled
two-variable surface or an implicit convexity inference.

The verifier deliberately treats the line intercepts as arbitrary symbols.
The result depends only on the slope law `1/2-x`.  It passed both symbolic
identities and 200,000 exact-rational signed fixtures.

## Boundary

This sprint does not recertify the endpoint Arb bound or the active tangent
gap.  It certifies the specific additive arrow between them.  Packet ancestry
and discard ownership remain separate.
