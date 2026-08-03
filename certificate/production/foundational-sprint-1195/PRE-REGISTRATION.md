# Preregistration -- contact covariance and envelope completion

Date: 2026-08-03

## Frozen input

The exploratory identity in `DISCOVERY-LOG.md` is known. The exact plateau,
hyperbolicity, unstable parameterization, connection, graph projection,
boundary wing, and inactive-tail certificates from Sprints 1115--1116 and
1192--1194 are also frozen inputs.

## Prospective checks

1. A fresh symbolic engine, written from the displayed shooting map rather
   than copied coefficient formulas, must independently derive the Bellman
   equality, stationarity equation, and `M^* beta = beta/v^2`.
2. On the high plateau branch, the contact multiplier `1/R^2` must equal the
   isolated stable multiplier `D/A`, and hence differ from the unique unstable
   multiplier.
3. The exact local unstable manifold must therefore lie in `ker(beta)`; the
   already-certified global orbit inherits the envelope identity everywhere.
4. The characteristic predecessor map must be increasing, so
   `F'(y)=1/2-P(y)` makes `F` concave. Every active characteristic line is then
   a global support line above `F`.
5. Combined with Sprint 1194's inactive-tail guard, these facts must prove a
   positive fixed point of the continuous Bellman operator at the exact
   connection parameter.

## Failure conditions

Any nonzero symbolic residual, equality of the contact and unstable
multipliers, a gap in the coverage of `[-1,1]`, or use of numerical equality
where an exact identity is required kills the advertised completion.
