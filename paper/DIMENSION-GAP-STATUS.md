# Quantitative dimension law at the I3322 wall

## Definition

Let `Q_d` be the optimum of the normalized I3322 functional over
tensor-product strategies whose two local Hilbert spaces have dimensions at
most `d`. Mixed states and arbitrary binary POVMs are allowed. Let `q_*` be the
certified infinite-dimensional wall value.

Compactness and multilinear extremality imply that `Q_d` has a pure-state,
projective-measurement representative on the same local spaces. No Naimark
dilation or increase in dimension is used.

## Constructive upper bound on the deficit

For the certified positive wall, let `v_L` be the value obtained by compressing
all local effects and the state to indices `{-L,...,L}` and normalizing. With
`d=2L+1`, the exact principal-section identity is

```text
q_*-v_L = [h_-L lambda_-L-1 lambda_-L
            + h_(L+1) lambda_L lambda_(L+1)] / S_L.
```

The analytic wall tails give

```text
lim -log(q_*-v_L)/d = log R,
R = 1.07809205080209208...,
log R = 0.07519285919570202....
```

Since `Q_d>=v_L`, this proves

```text
0 < q_*-Q_d <= exp[-d log R+O(1)].
```

Thus `log(1/epsilon)/log R+O(1)` local dimension is sufficient.

## Universal lower bound on the deficit

The robust equality-certificate argument supplies explicit constants

```text
Gamma = (20*78/5)^4 = 312^4 = 9,475,854,336,
kappa = 4.294654614331445998753374519792940851...e-52
```

such that, for every `d>=1`,

```text
q_*-Q_d >= kappa d^-4 Gamma^-d.
```

The proof localizes the three positive certificate remainders, charges the
near-fixed and inactive-tail sectors, follows canonical packets through a
finite sequence of moving spectral frames, and compares the resulting upper
energy ledger with a finite-rank reverse-endpoint lower bound. Every frame,
exit-time, and response-debt multiplicity is explicit.

The proof was reconstructed blindly from a sealed 19-source packet and then
audited in a separate exact-arithmetic pass. The public certificate retains
both routes.

## Complexity consequence

Let `D(epsilon)` be the least `d` for which some allowed strategy has deficit
at most `epsilon`. The two inequalities imply

```text
[log(1/epsilon)-O(log log(1/epsilon))]/log Gamma
    <= D(epsilon)
    <= log(1/epsilon)/log R+O(1).
```

Therefore

```text
D(epsilon) = Theta(log(1/epsilon)).
```

This is the asymptotic-order statement. The large gap between `log Gamma` and
`log R` remains open, so the optimal exponential rate and prefactor are not
known.

## Numerical illustration of the constructive sequence

| local dimension | value | gap to `q_*` |
|---:|---:|---:|
| 31 | 0.250492717483438 | 3.82667e-4 |
| 63 | 0.250850779989507 | 2.46045e-5 |
| 127 | 0.250875195790122 | 1.88724e-7 |
| 191 | 0.250875382981378 | 1.53260e-9 |
| 255 | 0.250875384501519 | 1.24575e-11 |

The table illustrates the upper construction only; no fit from these values
enters either theorem.

## Scope

The necessity theorem is device-independent within the standard bipartite
tensor-product model with no communication and both local dimensions bounded
by `d`. It does not establish a dimension witness under signaling, network
resources, postselection, or an alternative operator-algebraic notion of
dimension. It also does not prove that the centered truncations attain `Q_d`.
