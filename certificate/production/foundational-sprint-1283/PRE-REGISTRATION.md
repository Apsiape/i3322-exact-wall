# Pre-registration: global Bellman amplitude consistency audit

The exact wall argument uses two claims simultaneously:

1. every shooting transition carries local values
   `F_local(x)=sqrt(1-x^2)u/2` and
   `F_local(y)=sqrt(1-y^2)v/2` satisfying Bellman equality exactly;
2. all target charts assemble one global function `F`.

The missing compatibility check is whether the locally carried source value
equals the globally assembled target value at the same coordinate:

```text
F_global(x) = F_local(x).                           (1)
```

Rebuild the complete corrected atlas at parameterization orders 12, 14, and
16.  For every original and reverser-generated transition whose source and
target lie in `[-0.898,0.898]`, evaluate the mismatch in (1).  Also evaluate
the raw local Bellman equality before any global interpolation.

Registered gates and classification:

1. raw local Bellman residual is below `1e-12` at every order;
2. target-chart overlap spread is below `1e-12` at every order;
3. **persistent global mismatch** if every maximum source mismatch exceeds
   `5e-5` and the order-16 maximum differs from the order-12 maximum by less
   than 10% of the order-12 maximum;
4. **truncation artifact** if the order-16 maximum is below `1e-6` and each
   order increase reduces the maximum by a factor below `0.2`;
5. otherwise **unresolved**.

No theorem is retracted from a floating-point persistence result alone.  A
persistent result opens an Arb interval audit at the maximizing transition
and demotes any theorem assembly that assumes (1) without certifying it.
