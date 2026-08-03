# Independent interval reconstruction -- preregistration

Date: 2026-08-03

## Independence contract

The second engine may use Python's standard library, SymPy for exact
cross-checks, and `mpmath.iv`. It may not import `flint`, any Sprint-1115--1200
Python module, or any production JSON receipt. Mathematical formulas may be
transcribed from the paper and technical supplement. Production outputs are
consulted only after the second verdict is frozen.

The complex layer must be implemented locally from rectangular real intervals;
`mpmath.iv` has no usable complex square root in this environment. The
principal square root on `Re(z)>0` will be computed by

```text
p=sqrt((|z|+Re(z))/2),  q=Im(z)/(2p).
```

## Registered gates

1. **Arithmetic:** at least 10,000 exact-rational fixtures for `+,-,*,/` are
   enclosed; square-root outputs satisfy exact lower/upper square tests.
2. **Plateau/series:** the positive plateau is hyperbolic and the independently
   generated degree-12 parameterization satisfies the invariance equations
   through degree 12.
3. **Analytic tail:** a complex-domain graph-transform calculation proves
   contraction `<1` and an original-coordinate correction below `3e-25` on
   `|t|<=0.01`.
4. **Shooting:** all four preconditioned Miranda faces retain strict opposite
   signs after the independently propagated analytic-tail allowance.
5. **Central graph:** every local and central tile has `dx<0`, `dy<0`, and
   positive pivot.
6. **Boundary wing:** the endpoint residual changes sign, its derivative is
   strictly negative, and every wing tile has the graph signs.
7. **Inactive exterior:** every tile passes successor monotonicity,
   stationarity-target monotonicity, and positivity.

## Registered verdicts

- `7/7`: independent reconstruction of the entire computer-assisted Bellman
  input.
- `1--6/7`: partial replication only; the theorem package keeps an explicit
  second-engine debt at the first failed layer.
- A disagreement in a strict sign or exact formula triggers theorem quarantine
  until the discrepancy is explained.

Matching rounded decimals is never a gate. No tolerance will be chosen after
looking at the production receipt; subdivisions may increase, but domains and
claim predicates may not change without a correction entry.
