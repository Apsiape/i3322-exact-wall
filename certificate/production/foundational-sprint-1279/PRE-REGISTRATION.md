# Pre-registration: grid-phase and deep-refinement attack

Sprint 1278's `N=12801` transit gap may be a favorable alignment between the
putative contact and the uniform node lattice.  Attack that possibility before
building any interval proof.

Use the same monotone lower-envelope Bellman operator and continuous local
minimizer.  Run the phase ensemble

```text
N = 12797, 12798, ..., 12805
```

and the deeper refinements `N=25601,51201`.  Construct the final affine hull
once per resolution so continuous predecessor evaluations locate their owner
by binary search rather than rescanning all nodes.

Register:

1. every measured transit gap is positive;
2. every bottleneck coordinate lies within `0.001` of `-0.8782`;
3. every bottleneck multiplier exceeds `1.15`;
4. classify the parabolic signal as **phase-robust** only if every phase-
   ensemble gap is below `2.5e-4` and both deep-refinement gaps are below
   `1.5e-4`;
5. classify **strict transit reopened** only if every phase-ensemble and both
   deep-refinement gaps exceed `3e-4`;
6. otherwise classify **unresolved**.

The thresholds will not move after the run.  A phase-robust result remains
floating-point evidence: it does not prove that the limiting gap is zero.
