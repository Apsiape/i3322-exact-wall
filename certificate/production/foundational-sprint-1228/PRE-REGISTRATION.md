# Sprint 1228 pre-registration

The verifier will test only the following frozen inequalities.

For positive packet RMS weights `p,p'`, packet norms `z,z'`, and transport
error `e`,

```text
|p z-p' z'| <= e
  implies
|z'-(p/p')z| <= e/p'.
```

If a positive scalar weight `ell` lies in `[m,M]`, and its oscillation from
chosen source/target representatives is at most `omega`, then

```text
|p/p'-ell_s/ell_t|
 <= omega(1/m+M/m^2).
```

The tests will use exact rational scalar fixtures and independent random
Euclidean packet fixtures. No I3322 conclusion is registered merely from
these inequalities.

