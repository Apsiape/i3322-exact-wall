# Prospective v1.3.0 release notes

This revision adds a two-sided quantitative dimension law for the certified
spatial wall. It is not yet a tagged archival release; DOI and citation
metadata remain those of v1.2.0 until release.

## New theorem

Compressing the normal spatial maximizer to the centered principal section of
local dimension `d=2L+1` gives an exact two-boundary flux formula. The
certified geometric tails imply

```text
lim -log(q_*-v_L)/d = log R,
R = 1.07809205080209208....
```

Consequently the unrestricted dimension-`d` optimum, with binary POVMs
allowed, satisfies

```text
0 < q_*-Q_d <= exp[-d log R+O(1)].
```

Equivalently, `log(1/epsilon)/log R+O(1)` local dimension is sufficient to
reach deficit `epsilon`.

A separate robust-certificate argument proves that every tensor-product
strategy with both local dimensions at most `d`, allowing arbitrary mixed
states and binary POVMs, satisfies

```text
q_*-Q_d >= kappa d^-4 Gamma^-d,
Gamma = 312^4 = 9,475,854,336,
kappa = 4.2946546143314459987...e-52.
```

The prefactor and exponential base are explicit but intentionally crude.
Combining necessity and achievability shows that the minimum local dimension
required for deficit `epsilon` is `Theta(log(1/epsilon))`.

## Verification added

- an exact-rational production guard for the principal-section flux identity;
- an independent SymPy reconstruction with missing-boundary controls;
- an independent `mpmath.iv` derivation and enclosure of `R` and `log R`;
- a same-dimension pure/projective reduction for arbitrary binary POVMs;
- a complete production chain for robust response localization, moving-frame
  transport, packet ancestry, finite-rank exit, and the dimension lower bound;
- a sealed 19-source blind reconstruction of the lower bound;
- a post-verdict exact SymPy audit of every final constant and absorption;
- release-level replay and semantic gates for both receipts.

## Claim boundary

The lower bound is device-independent within the standard bipartite
tensor-product model with no communication and local dimensions bounded by
`d`. It is not a sharp asymptotic constant, a statement about experimental
noise, a commuting-operator dimension bound, or a claim that the centered
truncations are finite-dimensional optimizers.
