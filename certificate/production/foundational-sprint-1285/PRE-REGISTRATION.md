# Pre-registration: wide-bracket Arb amplitude exclusion

Reuse Sprint 1284's exact connection `C` box, fixed `t1`, and initial `t2`
bracket.  Do **not** narrow or solve for `t2`.

The original four-step target coordinate is strictly monotone on the certified
graph piece (Sprint 1192).  Sprint 1284 already found strict opposite signs of

```text
y4(t2)+y4(t1)
```

at the two bracket faces.  Continuity and monotonicity therefore give a unique
matched-coordinate root somewhere in the complete bracket.

Evaluate with Arb over that entire `t2` bracket:

```text
B(t2)-A,

A     = reflected local source amplitude at t1,
B(t2) = original target amplitude over the t2 bracket.
```

Registered gates:

1. the existing exact invariant-graph receipt certifies monotonicity on the
   central four-step piece;
2. both bracket-face coordinate residuals retain strict opposite signs;
3. every square-root and amplitude denominator interval is strictly positive;
4. the complete wide-bracket interval `B(t2)-A` excludes zero with lower
   absolute bound above `5e-5`.

If all four gates pass, the unique matched-coordinate root necessarily has a
nonzero amplitude mismatch.  This certifies a load-bearing normalization gap
without requiring a correlated narrow root box.
