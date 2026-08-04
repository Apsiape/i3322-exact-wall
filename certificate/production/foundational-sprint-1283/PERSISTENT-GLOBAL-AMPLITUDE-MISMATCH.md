# Persistent global amplitude mismatch

## Registered verdict

The complete corrected atlas was rebuilt at parameterization orders 12, 14,
and 16.  All three runs are numerically identical at the reported scale:

```text
transitions checked per order          42,806
maximum raw local Bellman residual     3.89e-16
maximum target-chart overlap spread    1.17e-15
maximum global source mismatch         1.624859095e-4
order-14 / order-12 mismatch ratio      1.0
order-16 / order-14 mismatch ratio      1.0
```

This satisfies the preregistered **persistent global mismatch** classification.

The maximizing transition is reflected:

```text
source coordinate          -0.0086452416113
target coordinate          -0.636893607718
locally carried F(source)   0.501049932823
assembled F(source)         0.501212418732
```

## What is and is not consistent

Each raw transition satisfies Bellman equality because the shooting map was
constructed from that equality.  Separately, target charts agree wherever
they overlap.  What fails is the cross-role compatibility

```text
locally carried source amplitude = assembled target amplitude
```

when the same coordinate appears in those two roles.  The median mismatch is
only `1.2e-13`, so the failure is not uniform; it is concentrated in a typed
part of the reflected assembly.

This explains Sprint 1282's contact residual and vindicates Sprint 1271's
warning that exact characteristic reversal does not transport global
normalization for free.

## The load-bearing concern

The exact aligned-wall proof uses local Bellman equality and one global
function `F`.  Its machine-readable prerequisite audit checks the invariant
graph, positivity, reflection geometry, and inactive contacts, but does not
explicitly check this source/target amplitude compatibility.  Therefore the
current certificate stack has a normalization gate that is not machine-
closed.

This document does not retract the public theorem.  The present result is
floating-point persistence, albeit with an exact local control and three
stable series orders.  The next sprint must match two chart coordinates with
Arb intervals and show whether their amplitude difference excludes zero.

If Arb excludes zero, the existing theorem assembly must be demoted until a
globally normalized atlas or a different Bellman fixed-point certificate is
supplied.  If Arb contains zero after correct chart matching, this numerical
instrument was mistyped and must be withdrawn.
