# Local Morse type does not reconstruct the global Bellman branch

Status: **registered selector rejected at coverage**

The proposed selector retained only shooting sheets with

```text
dP_j/dx>0,
```

then chose the least positive value among them.  It fails before any root or
profile comparison: at the first sampled target `x=-0.9`, none of the thirteen
propagated sheets has the required local type.

This does not contradict the certified global Bellman proposition, whose
predecessor is increasing everywhere.  It shows that the arbitrarily
forward-propagated local shooting family does not contain the correctly typed
global boundary sheet at every target.  A pointwise Morse sign cannot create
the missing sheet or encode its boundary condition.

Combined with Sprint 1274, the conclusion is sharp:

- value alone does not select the branch;
- local second variation alone does not select the branch;
- the globally normalized Bellman solution requires a boundary/action or
  viscosity condition.

The characteristic-atlas shortcut is therefore closed.  The next rigorous
route should enclose the already certified global Bellman fixed point directly
with interval sub/supersolutions, then evaluate the Sprint-1273 discriminant
`D` on those global enclosures.
