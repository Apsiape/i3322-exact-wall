# Pre-registration: Morse-filtered characteristic envelope

At each target `x`, every shooting chart candidate carries `(F_j(x),P_j(x))`.
Register the local stability filter

```text
candidate j is admissible only if dP_j/dx>0.          (1)
```

This is the differential type of the certified Bellman graph and is
equivalent to `F_j''<0` through `F'=1/2-P`.

Among admissible candidates choose the least positive `F_j`, inheriting `P_j`
from the same sheet.  On `[-0.9,0.9]` require the same fixed gates as Sprint
1274:

1. complete coverage;
2. selected `min diff(P)>-1e-4`;
3. exactly three log-free discriminant roots;
4. root error below `2e-3`;
5. maximum `F` disagreement below `2e-3` against the independent 1601-node
   Bellman reconstruction;
6. maximum `P` disagreement below `2e-2`.

Failure means local Morse type is not enough: sheet selection depends on a
global action, boundary condition, or viscosity rule not carried by the local
characteristic state.
