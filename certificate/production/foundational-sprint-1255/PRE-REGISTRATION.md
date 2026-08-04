# Pre-registration: finite monotone skew-flow theorem

The joint coupling of Sprint 1254 reduces the remaining rank issue to a
finite transport graph.  Register an abstract theorem before using any I3322
constants.

For at most `d` ordered source atoms, let two strictly decreasing injections
send atom `i` to horizontal outputs `A_i,B_i`, while translating its vertical
tail function by `p_i,q_i in [-B,B]`.  The difference of the two pushed tail
measures is `sigma_L` at log cut `L`.

Common output points define a partial increasing map of source indices, so
its components must be paths or fixed points.  If every fixed point has
`|p_i-q_i|>=g`, the target is

```text
M_core <= [3 d^3+(H+2B)/g] sup_L ||sigma_L||_TV,
```

where `M_core` is the vertical event mass in `[-H,0]` and the supremum uses
the explicitly enlarged cut interval.

Falsifiers:

1. a common-output component can contain a nontrivial cycle;
2. path propagation needs an unbounded coefficient;
3. fixed-point translations can hide core mass; or
4. the displayed polynomial factor is too small.

