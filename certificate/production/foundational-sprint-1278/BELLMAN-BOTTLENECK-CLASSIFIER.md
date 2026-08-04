# The negative bottleneck is parabolic-contact consistent

## Instrument gate

The ordered-line lower-envelope engine reproduces the old dense 3201-node
Bellman fixed point to `8.89e-16` uniformly, with zero discrete predecessor
owner disagreements.  The high-resolution results therefore use a faster
implementation of the same discrete operator, not a changed equation.

## Registered classification

```text
nodes    minimum P(x)-x       coordinate          multiplier c
 3201    3.3701243468e-4      -0.8780240686        1.1590602577
 6401    3.7044488061e-4      -0.8779901026        1.1586938176
12801    5.4616959234e-5      -0.8782315598        1.1617528825
```

The final gap is below `3e-4` and is `0.14744` times the 6401-node gap.  This
meets the preregistered **parabolic-contact consistent** classification.  All
measured gaps remain positive, and every multiplier exceeds the registered
`1.1` threshold.

## Why this matters

Sprint 1277 showed that nearby predecessor reconstructions spend different
numbers of iterates near this same negative bottleneck, changing the
accumulated Lyapunov debt by `0.25235`.  Sprint 1278 supplies a mechanism: the
transit gap appears to be collapsing while the local derivative multiplier
remains strictly above one.

If the limiting predecessor has a fixed point `P(x_*)=x_*` here, then any
finite positive weight cancels around that one-point orbit:

```text
c(x_*) w(P(x_*))/w(x_*) = c(x_*) > 1.
```

Consequently no bounded positive weighted sup norm can turn this derivative
into a contraction.  That conditional statement is elementary; the missing
premise is the certified limiting fixed point and a certified lower bound on
its multiplier.

## Next gate

The numerical classification must be attacked in two ways before it can
carry proof architecture:

1. extend the memory-safe resolution ladder and test whether the small gap is
   stable or oscillatory under node refinement;
2. derive interval Bellman sub/supersolutions that enclose both `F` and the
   minimizer equation near the bottleneck.

A validated parabolic contact would not prove the desired dimension lower
bound.  It would prove that the previously proposed Banach-contraction route
is structurally unavailable and that the three-root theorem must be obtained
by a noncontractive method (monotone order bounds, degree, or a local normal
form).

## Claim boundary

The hull/dense comparison and all table entries are floating-point facts.
“Parabolic-contact consistent” is the preregistered numerical classification,
not a theorem that the continuum contact exists.  The public I3322 theorem is
unchanged.
