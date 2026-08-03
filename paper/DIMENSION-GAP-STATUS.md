# Quantitative dimension gap: honest status

## Result of the first campaign

The centered Pal--Vertesi carrier values satisfy

| local dimension | value | gap to `q_*` |
|---:|---:|---:|
| 31 | 0.250492717483438 | 3.82667e-4 |
| 63 | 0.250850779989507 | 2.46045e-5 |
| 127 | 0.250875195790122 | 1.88724e-7 |
| 191 | 0.250875382981378 | 1.53260e-9 |
| 255 | 0.250875384501519 | 1.24575e-11 |

The last three ratios are consistent with exponential convergence at the
positive plateau rate. Numerically,

```text
log(R) = 0.075193...,
fitted -log(gap)/dimension slope = 0.07653....
```

This is useful asymptotic evidence and agrees with the geometrically decaying
domain-wall tails. It is not a dimension witness.

## Why the current proof does not yield a robust bound

The nonattainment theorem uses finiteness once and sharply: two decreasing
bijections of one finite ordered support must be the same reversal. Near
equality supplies approximate kernel equations, but it does not immediately
supply:

1. a common finite support after small spectral leakage;
2. an approximate bijection separated from collisions;
3. a dimension-uniform lower bound for disagreement of the two transports.

Without those estimates one cannot infer a valid function

```text
q_*-Q_d >= f(d)>0
```

from the exact contradiction. Fitting the aligned lower sequence would reverse
the required inequality and would not control arbitrary strategies.

## Precise next theorem

A quantitative strengthening should prove one of the following equivalent
forms.

- **Robust transport form:** Bell deficit `epsilon` forces the two decreasing
  response transports to agree outside weight `g(epsilon)`.
- **Finite-rank remainder form:** for every rank-`d` state, the sum of the
  three certificate remainders is at least `f(d)`.
- **Spectral packing form:** a rank-`d` joint spectral measure cannot support
  an approximate nonclosing Bellman orbit with defect below `f(d)`.

Until one of these lands, the public theorem is exact nonattainment, not a
quantitative device-independent dimension lower bound.
