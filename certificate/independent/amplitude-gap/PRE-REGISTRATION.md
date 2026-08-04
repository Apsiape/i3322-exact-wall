# Pre-registration: independent global-amplitude-gap reconstruction

## Purpose

Reconstruct Sprint 1285's negative result with the repository's independent
`mpmath.iv` arithmetic and independently implemented series/map code.  The
engine must not import FLINT, Arb, or any production module.

The production result is already known, so this is an independent-engine
reconstruction rather than a blind discovery.  Its numerical thresholds and
classification are fixed here before the engine is written.

## Fixed input

Use the same published `C` enclosure, degree-12 unstable parameterization,
fixed source parameter

```text
t1 = 0.0015293272133344497,
```

and complete target bracket

```text
t2 in [0.0015874649714962908, 0.001588503145749181].
```

Propagate both charts by four map steps.  Define

```text
r(t2) = y4(t2) + y4(t1),
A      = sqrt(1-y4(t1)^2)/(2 v5(t1)),
B(t2) = sqrt(1-y4(t2)^2) v5(t2)/2.
```

## Registered gates

1. no production or FLINT/Arb module is imported;
2. interval differentiation proves `r'(t2)<0` on every tile of a complete
   cover of the target bracket;
3. the left face of `r` is strictly positive and the right face strictly
   negative, proving one and only one matched coordinate;
4. every radicand and amplitude denominator is strictly positive;
5. a mean-value interval cover proves `B(t2)-A` is strictly positive over the
   complete bracket, with lower bound above `1e-4`.

If all five gates pass, the independent engine certifies the same theorem as
Sprint 1285: the unique coordinate-matched point cannot satisfy the global
amplitude compatibility equation.

## Independence boundary

The engine may import only `certificate/independent/iv_core.py`, standard
library modules, and `mpmath`.  It must not read the production JSON when
forming its verdict.  A separate post-verdict concordance check may compare
the two receipts only after the independent JSON exists.
