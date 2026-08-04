# The drift has a log-free global discriminant

Status: **exact sign/root equivalence; numerical three-root ancestry only**

Let

```text
H(x)=log(F(x)/F(-x)),
chi(x)=H(x)+H(P(x)).                                 (1)
```

Define instead

```text
D(x)=F(x)F(P(x))-F(-x)F(-P(x)).                     (2)
```

Since all four Bellman values are positive,

```text
exp(chi(x))-1
 =D(x)/[F(-x)F(-P(x))].                             (3)
```

Therefore, exactly,

```text
sign chi(x)=sign D(x),
chi(x)=0 iff D(x)=0.                                (4)
```

Writing `z=P(x)`, `F(z)=b(z)u`, `F(x)=b(x)v`, and
`K(t)=F(t)F(-t)/b(t)^2` also gives

```text
D(x)=b(x)b(z)/(uv) * [(uv)^2-K(x)K(z)].             (5)
```

Both symbolic residuals reduce to zero.

Independent 1601- and 3201-node Bellman reconstructions have zero sign
disagreements between (1) and (2) away from their numerical zero boxes.  In
each reconstruction, `D` and `chi` have the same three roots with discrepancy
below `3.3e-9`, passing the preregistered `1e-8` gate.  The first implementation
interpolated `D` and `chi` separately on a `5e-4` mesh and missed that gate by
two orders of magnitude.  The gate was held fixed and both roots were then
solved by continuous Bellman/PCHIP evaluation inside the same detected
brackets.

Equation (2) is the correct interval target.  It uses the globally normalized
Bellman function directly, avoids logarithmic interval widening, and does not
mistake the local characteristic reverser for a normalization law.

No three-root theorem is claimed here.  The next proof must enclose `F` and
`P` with Arb on the complete target domain and certify the sign of (2) outside
three root boxes, plus transversality inside them.
