# Pre-registration: charged common-cell descent

Use the canonical joint order-resolution measure of Sprint 1254, restricted
to the vertical core `[-H,0]`.  Before choosing a grid, register the target:
for every width `h>0`, some shifted interval grid places all but

```text
sqrt(120 d epsilon_0 [exp(3H)-1])/h
```

of the core mass into cells in which the Alice and Bob order coordinates
share one address.

The proof must average the actual joint measure over the grid shift.  It may
not restrict a response vector, delete a coarse complement, assume a density,
or choose matching spectral atoms.

Falsifiers:

1. the integrated contact cost has a worse power than `exp(3H)`;
2. shifted-grid separation costs more than `|y-u|/h` on average;
3. the Cauchy step introduces an unowned mass; or
4. the claimed common-cell measure is not positive.

