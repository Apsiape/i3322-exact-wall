# Prospective v1.3.0 release notes

This revision adds a quantitative achievability theorem for the certified
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

## Verification added

- an exact-rational production guard for the principal-section flux identity;
- an independent SymPy reconstruction with missing-boundary controls;
- an independent `mpmath.iv` derivation and enclosure of `R` and `log R`;
- release-level replay and semantic gates for both receipts.

## Claim boundary

The theorem proves sufficiency only. It neither supplies nor claims a lower
bound on the dimension needed by every near-optimal strategy. That robust
arbitrary-strategy problem remains open.
