# Pre-registration: negative Bellman bottleneck classifier

The dense Bellman reconstruction forms an `N x N` matrix even though, for
fixed predecessor node `z`, its candidate is affine in the target `x`:

```text
L_z(x) = q*+1-z/2-(z-1/2)x-(1-z^2)/(4F(z)).
```

Build the lower envelope of these ordered-slope lines by a monotone convex
hull.  This must reproduce the old dense update before it is used to increase
resolution.

Run `N=3201,6401,12801` with the same stopping tolerance and boundary cap.
At each resolution construct a PCHIP interpolant of `F`, minimize the
continuous candidate locally around the discrete owner, and evaluate

```text
g_N = min_{x in [-0.9,0]} [P_N(x)-x],
c_N = [1-P_N(x_N)^2]/[4F_N(P_N(x_N))^2]
```

at the minimizing coordinate `x_N`.

Registered gates and classification:

1. at `N=3201`, the hull and dense fixed points agree uniformly within
   `2e-11` and their discrete predecessor owners disagree at no more than two
   nodes;
2. every measured `g_N` is positive;
3. every bottleneck multiplier `c_N` exceeds `1.1`;
4. call the evidence **strict-transit consistent** only if
   `g_12801>3e-4` and `|g_12801-g_6401|<1e-4`;
5. call it **parabolic-contact consistent** only if
   `g_12801<3e-4` and `g_12801/g_6401<0.8`;
6. otherwise report **unresolved**.  Do not move these thresholds after the
   run.

No classification is a theorem about the continuum Bellman fixed point.
Even a clean strict-transit signal requires interval sub/supersolutions and a
certified lower bound for `P(x)-x`; a parabolic signal requires a certified
zero and a multiplier obstruction at that zero.
