# Preregistration 2 -- geometric Bellman symmetrization

Date: 2026-08-03

The false reflection shortcut and the exploratory geometric repair in
`CORRECTION.md` are frozen inputs.

## Prospective checks

1. Exact symbolic algebra must prove
   `A(x)A(-x)=B(x)B(-x)=b(x)^2` from `p=b^2/F`, without assuming any symmetry
   of `F`.
2. The forward Bellman inequality at `(x,u)` and the reflected inequality at
   `(-u,-x)` must have the same cost `d(x,u)`.
3. A polynomial Cauchy identity must prove the geometric transport bound from
   those two inequalities.
4. Replacing the false potentials by `A,B` must leave the complete
   three-remainder Bell-operator proof valid, including endpoints and
   one-dimensional CS blocks.
5. The frozen 32,001-guard hull should place the symmetrized dual ceiling
   within `1e-10` of the exact wall; this is a numerical guard, not the proof.
6. A direct held-out complex-matrix engine using the certified rational
   `Q_cert` hull must assemble all three remainder operators independently,
   keep each minimum eigenvalue above `-1e-10`, and reproduce
   `Q_cert I-B` below `1e-11`.

Any residual, use of `F(x)F(-x)=b^2`, or dual excess above `1e-10` kills the
repair.
