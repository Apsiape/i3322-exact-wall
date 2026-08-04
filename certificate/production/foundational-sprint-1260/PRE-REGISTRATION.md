# Pre-registration: one grid for every queried tail

Sprint 1256 commonized the core band `[-H,0]`.  The finite flow also queries
shifted tails, so register the stronger target before reusing that grid.

For every `K>0`, the canonical joint coupling restricted to
`{zeta>=-K}` must satisfy

```text
integral |y-u|^2 dPi <=120 epsilon_0 [exp(3K)+2].
```

Consequently one width-`h` shifted order grid must put all but

```text
sqrt(120 d epsilon_0 [exp(3K)+2])/h
```

of that entire upper-tail mass into common Alice/Bob cells.

The proof must separately integrate the `t<=1` and `t>=1` resolvent regimes.
It may not extrapolate the `t^-3` estimate to infinity, assume a smallest
Schmidt coefficient, or commonize only the eventual core.

