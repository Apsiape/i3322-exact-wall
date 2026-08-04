# Pre-registration -- packet-path audit

Define for each moved frame `g_k` and initial cell `I_i` the canonical packet

```text
G_(k,i)=1_(P(g_k I_i))(X) 1_(g_k I_i)(U).
```

The sprint passes only if it proves all of the following.

1. **Closure.** Choosing `G_(k,i)` as source and the canonically addressed
   `G_(k+1,i)` as target is legal in the two-frame theorem.  Consequently the
   target norm at step `k` is literally the source norm at step `k+1`; no
   fibre identification is invoked.
2. **Horizontal orthogonality.** For each fixed `k`, the family
   `{G_(k,i)}` is orthogonal, including after Borel first-exit restrictions.
3. **Vertical rank.** Along each retained drift chain, the `U` cells are
   pairwise disjoint.  Every nonzero site consumes rank at least one of one
   fixed local operator, so a chain has length at most `d`.
4. **Multiplicity.** Direct-sum response energy is charged once at each time;
   endpoint mass is charged once at each exit time.  Since no chain has more
   than `d` sites, neither global bill is reused more than `d` times.  There
   must be no factor equal to the number of initial cells.
5. **Hostile finite model.** At least 100,000 exact-rational randomized path
   systems must verify closure, horizontal injectivity, vertical no-reuse,
   the direct-sum packet inequality, and the `d` multiplicity cap.

Passing proves packet ownership only.  It does not independently derive the
contact tube bounds, response remainders, cocycle coefficient bounds, or
near-fixed mass estimate.
