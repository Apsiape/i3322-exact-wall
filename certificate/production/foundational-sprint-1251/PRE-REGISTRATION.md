# Pre-registration: logarithmic cut averaging

The packet proof failed because a restricted sector could exchange uncharged
mass with its complement.  The event measure gives that complement a literal
vertical boundary.  Average the location of that boundary rather than fixing
it in advance.

Registered theorem:

For a finite measure `mu` of mass `d` and vertical shifts `h_j` satisfying
`|h_j|<=B_j`, define the crossing flux at depth `L` by

```text
Flux_j(L)=integral |1_{zeta>=-L}-1_{zeta+h_j(u)>=-L}| dmu.
```

Then for every `H>0` there is `L in [0,H]` with

```text
sum_j Flux_j(L)<=d(sum_j B_j)/H.
```

For a normalized Schmidt state, the retained upper tail at that cut must have
mass at least `1/2`.  With the I3322 response box and `H=kappa d`, the two
response fluxes must be bounded by `4 log(13/2)/kappa`, while Sprint 1249's
response error is at most `(9/2)sqrt(d epsilon) exp(kappa d/2)` per response.

Failure conditions:

- an atom crosses a moving cut for more than `|h|` units of depth;
- total event mass cannot replace a number-of-packets count;
- or the selected cut loses the dimension-independent retained core.

