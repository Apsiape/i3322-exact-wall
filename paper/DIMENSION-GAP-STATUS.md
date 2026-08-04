# Quantitative dimension approximation: proved achievability and open necessity

## Proved wall-truncation theorem

For the certified positive wall, let `v_L` be the value obtained by compressing
all local effects and the state to indices `{-L,...,L}` and normalizing. With
`d=2L+1`, the exact principal-section identity is

```text
q_*-v_L = [h_-L lambda_-L-1 lambda_-L
            + h_(L+1) lambda_L lambda_(L+1)] / S_L.
```

The analytic wall tails then give

```text
lim -log(q_*-v_L)/d = log R,
R = 1.07809205080209208...,
log R = 0.07519285919570202....
```

If `Q_d` is the unrestricted tensor-product optimum in local dimension at
most `d`, allowing binary POVMs, this proves the achievability bound

```text
0 < q_*-Q_d <= exp[-d log R+O(1)].
```

Thus `log(1/epsilon)/log R+O(1)` local dimension is sufficient. Both the exact
flux identity and the plateau exponent were reconstructed by a second engine
that imports no production module.

## Numerical finite-section audit

The centered Pal--Vertesi carrier values satisfy

| local dimension | value | gap to `q_*` |
|---:|---:|---:|
| 31 | 0.250492717483438 | 3.82667e-4 |
| 63 | 0.250850779989507 | 2.46045e-5 |
| 127 | 0.250875195790122 | 1.88724e-7 |
| 191 | 0.250875382981378 | 1.53260e-9 |
| 255 | 0.250875384501519 | 1.24575e-11 |

The last three ratios agree with the proved exponential rate. Numerically,

```text
log(R) = 0.075193...,
fitted -log(gap)/dimension slope = 0.07653....
```

The table illustrates the theorem; it is not used to infer its exponent.

## What remains open

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

Until one of these lands, the public quantitative theorem is achievability,
not a device-independent dimension lower bound. In particular, the wall
truncations cannot establish a lower bound for arbitrary strategies.
