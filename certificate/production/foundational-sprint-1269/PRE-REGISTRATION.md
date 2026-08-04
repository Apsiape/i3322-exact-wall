# Pre-registration: reconstruct the drift from shooting charts alone

Sprint 1268 used a min-plus Bellman iteration.  Register a methodologically
different reconstruction from the certified shooting parameterization.

For a shooting state `(x,y,u)` and its successor `(y,z,v)`, record

```text
F(x)=sqrt(1-x^2) u/2,
F(y)=sqrt(1-y^2) v/2,
P(y)=x.                                             (1)
```

Propagate overlapping positive-manifold charts through the reflection region,
merge them by the monotone order coordinate, and reconstruct `F` and `P`
without importing any Bellman profile from Sprint 1268.

Registered comparison targets:

1. the overlap spread in reconstructed `F` is below `1e-4` on the active box;
2. the shooting atlas finds exactly three zeros of `chi=q-p`;
3. those roots lie within `2e-3` of the Sprint-1268 roots; and
4. the smallest reconstructed `|a(r)+r|` remains above `1/20`.

This remains a floating-point ancestry test.  Passing it licenses construction
of the interval inverse atlas; it does not itself certify a zero count.

