# Exact rational I3322 upper bound near the historical candidate

Status: **rigorous theorem; exact rational witness and exact operator weld**

## Theorem

In the normalization used throughout this repository,

```text
omega_tensor <= omega_commuting <= 0.250876384514.
```

Here `omega_commuting` is the supremum over the standard commuting-projective
model, and `omega_tensor` is the tensor-product supremum.  The upper endpoint
is the exact rational number

```text
125438192257 / 500000000000.
```

It lies approximately `1.000000023e-6` above the displayed domain-wall value.

## Exact scalar certificate

The committed file `bellman-subsolution-candidate.json` contains 6,401
rational knots, each represented by an 18-place decimal string.  Let `G` be
their exact piecewise-linear interpolant on the uniform grid in `[-1,1]`.
The candidate builder uses floating point only to find this witness; it has no
proof authority.

The standard-library-only exact verifier constructs, in rational arithmetic,
the upper envelope

```text
M(x) = max_u [G(u) + (x-1/2)u].
```

On every common linearity interval of `G` and `M`, the Bellman residual is a
rational quadratic divided by the positive function `4G`.  Exact endpoint and
vertex minimization over all 10,902 common intervals proves

```text
G(u) + (1-x^2)/(4G(x))
  <= q_hat + 1 - x/2 - (x-1/2)u
```

for every `(x,u)` in `[-1,1]^2`.  The certified global residual lower bound is

```text
135655437485737999093532062544142506000661225846773637
----------------------------------------------------------------
152585378463848045768764394314910196051595150000000000000000

> 8.890461120944086e-7.
```

## Why this implies the operator bound

Put

```text
b(x) = sqrt(1-x^2)/2,
p(x) = b(x)^2/G(x).
```

Apply the certified Bellman inequality at `(x,u)` and at `(-u,-x)`.  Since
`d(-u,-x)=d(x,u)`, Cauchy gives

```text
a(x)+c(u) <= q_hat-d(x,u),
a(x)=sqrt(p(x)G(-x)),
c(u)=sqrt(G(u)p(-u)).
```

The definitions give the exact product laws

```text
a(x)a(-x)=b(x)^2,
c(u)c(-u)=b(u)^2.
```

Those are precisely the scalar hypotheses of the existing
representation-free I3322 decomposition.  Joint functional calculus makes
the transport remainder positive, the product laws make the two local
response remainders positive, and the three remainders sum identically to

```text
q_hat I - B_I3322.
```

The exact abstract algebra is replayed by `bellman_operator_weld_verify.py`.
No fixed-point equation, concavity, contact uniqueness, wall trajectory, or
shooting-chart normalization is used in this upper-bound theorem.

## Claim boundary

This theorem repairs a rigorous **near-optimal upper bound**, not the frozen
release's exact headline.  It does not prove that the displayed wall value is
the exact supremum; it does not prove finite-dimensional nonattainment at the
true supremum; and it does not prove `C_q != C_qs` or nonclosure.  Those claims
remain open at repository HEAD.
