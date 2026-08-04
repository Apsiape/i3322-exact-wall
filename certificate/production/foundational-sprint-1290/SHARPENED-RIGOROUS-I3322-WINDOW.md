# Sharpened rigorous I3322 window

Status: **unconditional theorem; exact rational fixed-witness optimization**

## Theorem

In the normalization used by this repository,

```text
0.25087519579012 < omega_tensor
                   <= omega_commuting <= 0.250875494588345.
```

The upper endpoint is the exact rational number

```text
50175098917669 / 200000000000000.
```

Together with the exact finite-strategy lower certificate from Sprint 1288,
the rigorous window has exact width recorded in
`exact-fixed-witness-threshold.json` and decimal width

```text
2.9879822277405625e-7.
```

## What was optimized

No new Bellman profile was fitted. The 6,401 rational knots committed in
Sprint 1287 were held fixed. For each trial rational `q`, the standard-library
verifier rebuilt the complete exact support-line envelope, intersected its
partition with every linear segment of the profile, and minimized the exact
quadratic Bellman numerator on all 10,902 common intervals.

A binary search over the `10^-15` grid proves that

```text
q = 0.250875494588345  passes,
q = 0.250875494588344  fails.
```

Both decisions are exact `Fraction` statements. The result is sharp only at
that resolution for this fixed piecewise-linear witness.

## Interpretation

The previous width `1.1887e-6` was mostly a deliberately conservative safety
lift. Removing that padding contracts the certified uncertainty by a factor
of about four. The remaining window is now only about `2.988e-7`, but it is
not thereby proved to be a physical, operator-algebraic, or dimensional gap.

Sprint 1289 supplies the right anatomy for the next test: any gap between a
Bellman upper witness and a finite Jacobi lower strategy decomposes into
nonnegative contact slack plus nonnegative Hellinger marginal-balance slack.

## Claim boundary

This theorem does not identify the exact optimum. It does not prove equality
at the historical wall candidate, finite-dimensional nonattainment at the
true optimum, `C_q != C_qs`, or nonclosure. It improves the unconditional
numerical enclosure and nothing beyond that enclosure is inferred from its
small width.
