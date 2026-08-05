# Pre-registration: independent Bellman--path theorem audit

## Independence contract

Reconstruct the theorem from its displayed definitions without importing the
Sprint 1295 verifier.  The audit may inspect the older Sprint 1287 input
contract and the exact Pal--Vertesi block definitions only after its abstract
proof verdict is fixed.

## Required attacks

1. **Index reversal:** derive the quadratic-form Young bound independently and
   reject the theorem if the source `b(i)^2/g(i)` or target `g(j)` appears on
   the wrong edge.
2. **Pivot-floor attack:** search exact rational positive-definite
   tridiagonal fixtures for a final Schur pivot below the spectral lower
   bound.  Any counterexample kills the uniform-pivot lemma.
3. **Infimum attack:** verify that extending histories gives
   `g(j)<=q-d(i,j)-b(i)^2/g(i)`, including nonattained infima; reverse
   orientation kills the theorem.
4. **Continuity attack:** prove or refute that all terminal-pivot functions
   have one endpoint modulus and that their infimum preserves it.
5. **Carrier attack:** reconstruct an odd-dimensional endpoint-constrained
   Pal--Vertesi block fixture containing an arbitrary smaller Jacobi word as a
   principal block.  Padding must preserve the Rayleigh value exactly.
6. **Weld typing:** confirm that the older operator theorem accepts arbitrary
   positive Bellman storage and does not silently require the failed shooting
   orbit, concavity, unique contact, or attainment of the infimum.

## Registered verdicts

- If every attack passes, accept
  `omega_tensor(I3322)=omega_commuting(I3322)=P=S`.
- If only the abstract theorem passes but carrier or weld typing fails, retain
  `P=S` and reject the I3322 consequence.
- No outcome identifies the common value with the historical decimal or
  restores nonattainment/nonclosure.
