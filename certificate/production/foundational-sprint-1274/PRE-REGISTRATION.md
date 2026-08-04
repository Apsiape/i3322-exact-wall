# Pre-registration: lower-envelope selection of folded characteristics

Sprint 1269 propagated local shooting charts through the reflection region and
found multiple incompatible characteristic sheets.  It glued those sheets by
a median, which has no Bellman justification.  The fixed-point equation is a
minimum principle, so register the alternative selector:

```text
at each target x, choose the positive chart candidate with least F(x),
and inherit P(x) from that same chart.                         (1)
```

No coordinate from one sheet may be combined with the value from another.

On `[-0.9,0.9]`, the selected atlas must satisfy all of:

1. complete coverage;
2. `min diff(P)>-1e-4` on the 7201-point sample;
3. exactly three log-free discriminant roots;
4. roots within `2e-3` of the Sprint-1268 registered targets;
5. maximum `F` disagreement below `2e-3` against an independently rebuilt
   1601-node global Bellman profile;
6. maximum `P` disagreement below `2e-2` against that profile.

Failure means that “take the least characteristic sheet” is not the missing
global normalization rule.  Passing is still numerical: a theorem would need
interval sheet ordering, exact switching boxes, and proof that the selected
envelope obeys the Bellman fixed point globally.
