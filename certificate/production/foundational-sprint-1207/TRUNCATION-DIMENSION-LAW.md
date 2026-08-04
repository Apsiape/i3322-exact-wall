# The spatial wall has an exact logarithmic truncation law

Status: **analytic achievability theorem; not a dimension lower bound**

## Theorem

Let `q_*`, `H(c)`, and the normalized positive vector
`lambda in ell^2(Z)` be the certified I3322 wall:

```text
H(c) lambda = q_* lambda,
H_(j-1,j) = h_j = sqrt(1-c_j^2)/2.
```

For `L>=0`, put `I_L={-L,...,L}` and
`S_L=sum_(j in I_L) lambda_j^2`. Compress all six spatial binary effects to
`span{e_j:j in I_L}`. Compression of a projection is a positive contraction,
hence a valid binary effect. With the normalized truncated state, the
dimension-`d=2L+1` strategy has value `v_L` satisfying

```text
q_*-v_L = [h_(-L) lambda_(-L-1)lambda_(-L)
            +h_(L+1)lambda_L lambda_(L+1)] / S_L.       (1)
```

For the certified positive-plateau ratio

```text
R=1.07809205080209208...,
```

one has

```text
lim_(L->infinity) -log(q_*-v_L)/(2L+1) = log R.         (2)
```

Consequently, if `Q_d` is the unrestricted tensor-product optimum with local
dimensions at most `d`, then along odd dimensions

```text
0 < q_*-Q_d <= q_*-v_((d-1)/2)
              = exp[-d log R+O(1)].                    (3)
```

Even dimensions inherit the estimate by padding with an unused summand.
Accuracy `epsilon` is therefore achievable with

```text
d <= log(1/epsilon)/log(R)+O(1),
1/log(R)=13.2991351931... .                            (4)
```

## Proof

Compression leaves every expectation on the truncated state equal to its
expectation before compression. The Bell-to-Jacobi identity therefore turns
the compressed Bell expectation into the Rayleigh quotient of the principal
Jacobi block.

Multiply the wall eigenvalue equation by `lambda_j` and sum over `I_L`.
Every diagonal and internal off-diagonal term is present in the principal
quadratic form. The only omitted terms are the two edges crossing the section
boundary, giving (1).

The certified analytic wall approaches its two constant plateaux
exponentially, and its positive eigenvector obeys

```text
lambda_(j+1)/lambda_j -> 1/R       as j -> +infinity,
lambda_(j-1)/lambda_j -> 1/R       as j -> -infinity.
```

The crossing coefficients tend to positive constants and `S_L->1`. Hence the
numerator of (1) is `exp[-(2L+1)log(R)+O(1)]`, proving (2)--(4).

The production engine checks (1) over exact rational fixtures. A separate
symbolic/interval engine reconstructs the identity and independently encloses
`R` and `log R` without importing production modules.

## Scope

This theorem proves that logarithmic dimension is **sufficient**. It does not
prove necessity or any positive lower bound for `q_*-Q_d`. Such a bound must
control every dimension-`d` strategy, not only wall truncations.
