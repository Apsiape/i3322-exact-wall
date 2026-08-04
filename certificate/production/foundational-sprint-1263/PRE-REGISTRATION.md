# Pre-registration: two-stage common addresses

Start with a positive joint event measure on a finite vertical band.  Suppose
the Alice/Bob source-order mismatch has first moment `C_src`, and the two
actual response outputs have first moment mismatch `D_out`.

Before choosing either grid, register the target: for every source width `h`
and output width `delta`, some pair of independent shifts retains a positive
submeasure with one common source cell and one common output cell, losing at
most

```text
C_src/h + D_out/delta.
```

The second shift must be chosen after the first restriction and must use the
actual response outputs, not representatives.  Every omitted event must be
counted exactly once or safely overcounted.

