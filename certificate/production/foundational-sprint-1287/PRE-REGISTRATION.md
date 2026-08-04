# Pre-registration: exact rational Bellman subsolution

## Target

Construct a globally normalized Bellman certificate without using the failed
shooting-chart amplitude weld.

Fix

```text
q_hat = 0.250876384514
```

exactly.  This is about `1.000000023e-6` above the displayed shooting center.

## Candidate construction

1. Reconstruct the zero-offset boundary Bellman profile on the uniform
   `N=6401` grid with the ordered lower-envelope iteration.
2. Stop at sup update below `1e-13`.
3. Round each profile value to exactly 18 digits after the decimal point using
   round-half-even, and thereafter treat every knot as a rational number.
4. Let `G` be the exact rational piecewise-linear interpolant of those knots.

The floating iteration chooses a candidate only.  It carries no proof
authority after step 3.

## Exact reduction

For fixed `x`, the maximum of

```text
G(u)+(x-1/2)u
```

over a piecewise-linear `G` occurs at a knot.  Construct the exact rational
upper envelope `M(x)` of those knot lines.  On every common interval where

```text
G(x)=a x+b,    M(x)=m x+c,
```

the Bellman residual has the sign of the quadratic

```text
N(x)=4(ax+b)[q_hat+1-c-(1/2+m)x]-(1-x^2),
```

provided `ax+b>0`.  Check its exact minimum on the closed interval using the
two endpoints and its rational vertex when the vertex lies inside.

## Registered gates

1. the candidate iteration converges before 5,000 steps;
2. every rational knot of `G` is strictly positive;
3. the exact upper envelope covers `[-1,1]` with ordered breakpoints;
4. every common interval has a strictly positive denominator;
5. every exact quadratic minimum is strictly positive;
6. the global Bellman residual lower bound, obtained by dividing the minimum
   numerator by a rigorous upper bound for `4G`, exceeds `5e-7`.

If all gates pass, the scalar inequality

```text
G(u)+(1-x^2)/(4G(x))
 <= q_hat+1-x/2-(x-1/2)u
```

holds for every `(x,u)` in `[-1,1]^2`.  Combined with the already exact
operator decomposition, this certifies the rigorous near-exact upper bound

```text
omega_tensor <= omega_commuting <= 0.250876384514.
```

It does **not** restore exact equality at `q_*`, nonattainment, spatial
separation, or nonclosure.
