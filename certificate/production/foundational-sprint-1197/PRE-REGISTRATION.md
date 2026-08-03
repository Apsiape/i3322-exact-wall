# Preregistration -- unrestricted I3322 Bellman dual

Date: 2026-08-03

## Frozen input

Sprints 1195--1196 supply a positive Bellman fixed point `F` at `q_*`, its
reflection construction, and exact aligned open/periodic lower sequences.
The exploratory potential in `DISCOVERY-LOG.md` is known.

## Prospective checks

1. A fresh symbolic expansion of the original nine-term I3322 projector
   functional must reproduce the displayed `(X,Y,U,V)` Bell operator with
   every constant and sign exact.
2. The scalar transport dual residual must reduce identically to
   `q_*-d(x,u)-F(-x)-F(u)`, hence to the Sprint 1195 Bellman residual.
3. On every nondegenerate CS block and for every response eigenvalue
   `z in [-1/2,1/2]`, both local remainder determinants must be
   nonnegative solely from `F(x)F(-x)=(1-x^2)/4`.
4. The one-dimensional CS degeneracies at `x=+/-1` and at `x=0,Y=+/-1`
   must obey the same operator inequalities without division by a sine.
5. The three remainder operators must add exactly to
   `q_*I-B_I3322`. A separate random complex-matrix engine must reproduce the
   original/reparameterized Bell operators below `1e-12` on held-out ranks.

## Kill conditions

Any sign mismatch, failure at a one-dimensional CS block, dependence on
Schmidt alignment, or use of a trace inequality not implied by the operator
remainders kills the unrestricted theorem.

## Claim boundary

Passing proves the tensor-product quantum **supremum**. Finite-dimensional
nonattainment is a separate equality-kernel theorem and is not preregistered
here.
