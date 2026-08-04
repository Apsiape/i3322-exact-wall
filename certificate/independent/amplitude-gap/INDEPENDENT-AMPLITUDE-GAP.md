# Independent reconstruction of the global-amplitude gap

## Result

A separately implemented `mpmath.iv` engine reconstructs Sprint 1285 without
importing FLINT, Arb, or any production module.  All five preregistered gates
pass.

```text
largest upper bound on matched-coordinate derivative   -285.9509470
left face residual                                      > 0.0001722853520
right face residual                                     < -0.0001276904740
amplitude difference over complete bracket
  [0.00014027599579792882, 0.00017894040323422364]
```

The strict derivative sign and opposite face signs prove that the coordinate
matching equation has exactly one root in the bracket.  The amplitude interval
excludes zero everywhere in that same bracket, so in particular it excludes
zero at the unique root.

## Independence

The reconstruction uses `certificate/independent/iv_core.py`, which contains
its own degree-12 parameterization, dual-number differentiation, interval map,
and recurrence implementation.  It does not read the production receipt when
forming its verdict.  The later concordance script only compares the two
already-written JSON receipts.

The independent and production amplitude intervals overlap.  Their lower
bounds differ by less than `7.1e-11`; their upper bounds differ by less than
`7.2e-11`.

## Consequence

The normalization gap is no longer a single-engine finding.  The current
Bellman theorem assembly is open under two interval stacks with separate
arithmetic and map implementations.

This still does not prove the published numerical candidate false.  It proves
that the documented global normalization is not established by the current
local-chart assembly.

## Reproduction

```text
python certificate/independent/amplitude-gap/amplitude_gap_mpmath.py
python certificate/independent/amplitude-gap/amplitude_gap_concordance.py
```
