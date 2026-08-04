# Pre-registration: max-plus Lyapunov contraction of the Bellman derivative

This registration follows one unregistered 1601-node diagnostic and precedes
the two-resolution engine.

At the global Bellman fixed point, the linearized response is the weighted
composition operator

```text
(L delta)(u)=c(u) delta(P(u)),
c(u)=[1-P(u)^2]/[4F(P(u))^2].                       (1)
```

Local amplification is allowed.  On a finite sampled predecessor graph, put
an edge `u -> nearest(P(u))`.  The obstruction to a weighted contraction is
the largest geometric mean of `c` around a directed cycle.

Run independent 1601- and 3201-node Bellman reconstructions on the same
3601-point `[-0.9,0.9]` carrier.  Register:

1. the unweighted maximum multiplier exceeds one;
2. each functional graph has exactly one directed cycle;
3. its maximum cycle geometric mean is below `0.9`;
4. there exists a positive weight `w` satisfying

   ```text
   c(u)w(P(u))/w(u)<=0.9+1e-12                     (2)
   ```

   at every sampled point;
5. `max(w)/min(w)<10` at both resolutions.

Passing is a numerical feasibility theorem for the finite graphs, not a
continuous Bellman contraction.  The continuous proof would still need an
interval predecessor enclosure and a piecewise weight with (2) on every
cell.
