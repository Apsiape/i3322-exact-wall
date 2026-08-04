# Independent finite-strategy reconstruction

## Independence boundary

Reconstruct the Sprint-1288 finite-strategy value using `mpmath.iv` directly
from the committed public candidate. Do not import the production exact
verifier, its rational square-root routine, or any production Bellman engine.

## Registered gates

1. the profile and vector dimensions are `128` and `127`;
2. every interval radicand `1-c_j^2` is positive;
3. direct interval evaluation of the normalized finite Jacobi quotient has
   lower endpoint above `0.25087519`;
4. the interval width is below `1e-80` at 160 decimal digits;
5. the independent interval contains the production exact rational lower
   certificate or lies strictly above it because the production proof uses
   deliberately floored square roots;
6. the candidate payload hash agrees before evaluation.

This is an implementation-independent arithmetic reconstruction of the same
finite witness, not an independent discovery of the witness and not a repair
of the historical exact-optimum theorem.
