# Arb amplitude adjudication: decisive interval, failed preregistration

## Registered verdict

Three of five registered gates pass.  The run is therefore **not** reported as
an all-pass certificate.

```text
initial root faces opposite sign                PASS
final coordinate residual contains zero         PASS
amplitude difference excludes zero by >1e-4     PASS

requested t2 width <1e-15                       FAIL
measured t2 width                                3.87e-15

requested raw Bellman interval width <1e-15     FAIL
measured raw Bellman interval width              2.72e-13
```

The failures are interval-dependency widths, not sign reversals.  Direct
four-step interval propagation carries the common `C` uncertainty through
several repeated expressions and loses correlations.

## Decisive surviving interval

At the narrowed matched-coordinate box, Arb gives

```text
reflected source amplitude
  [0.5010499328226706, 0.5010499328228755]

original target amplitude
  [0.5012124157949853, 0.5012124216671848]

difference
  [0.0001624829721098, 0.0001624888445142]
```

This strongly supports the mismatch, but the narrow box itself missed its
registered width gate.  It should not be used alone to claim a complete
certificate.

## Registered repair

Narrow localization is unnecessary.  The initial `t2` bracket already has
strict opposite coordinate signs.  The exact invariant-graph projection
certifies monotonicity, hence a unique matching root lies inside.  The next
test will evaluate the amplitude difference over the **entire initial
bracket**.  If that wide interval excludes zero, then every possible matching
root has nonzero mismatch and no correlated root enclosure is required.

The raw local Bellman equality is an exact algebraic identity already replayed
in Sprint 1271; its over-wide zero interval need not carry the normalization
comparison.
