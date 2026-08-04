# The exact reverser does not fix the Bellman normalization

Status: **registered candidate rejected; normalization holonomy remains**

For a characteristic state and its successor write

```text
M(z,x,u)=(x,y,v).
```

The local Bellman reconstruction is

```text
F(z)=b(z)u,             F(x)=b(x)v,
b(x)=sqrt(1-x^2)/2.                                  (1)
```

Sprint 1270's exact reverser sends this state to

```text
R(z,x,u)=(-x,-z,1/v).                                (2)
```

The registered candidate identified the local normalization on the `R` image
with the normalization of the globally assembled Bellman function.  That
would give `F(-x)=b(x)/v`, hence

```text
F(x)F(-x)=b(x)^2,                                    (3)
p(x)=b(x)^2/F(x)=F(-x),
A(x)=F(-x),             B(x)=F(x).                   (4)
```

It would also turn the Sprint-1268 drift into

```text
H(z)=2 log u,             H(x)=2 log v,
chi(x)=H(x)+H(P(x))=2 log(uv),
chi(x)=0 iff uv=1.                                    (5)
```

The symbolic implications (3)--(5) are correct conditional on the
normalization identification.  The identification itself is false.

The corrected 18-chart atlas has maximum overlap disagreement about
`1.2e-15`, but it measures

```text
max |F(x)F(-x)-b(x)^2| = 8.1e-5.                    (6)
```

The mismatch is therefore not chart interpolation or overlapping ancestry.
The exact reverser maps characteristic states, but the locally reconstructed
amplitude on the reflected characteristic carries a nontrivial gluing factor
relative to the globally normalized Bellman function.  The candidate silently
set that factor to one.

This is why the manuscript's geometric symmetrization was not redundant, and
why the drift cannot yet be reduced to the raw section residual `uv-1`.

## The corrected exact factorization

Define the normalization defect

```text
K(x)=F(x)F(-x)/b(x)^2.                              (7)
```

This is not an added degree of freedom; it is an exact observable of the
already certified Bellman function.  Equations (1) and (7) give

```text
F(-x)=K(x)b(x)/v,
p(x)=F(-x)/K(x),
A(x)=F(-x)/sqrt(K(x)),
B(x)=F(x)/sqrt(K(x)).                               (8)
```

Likewise

```text
H(x)=2 log v-log K(x),
H(z)=2 log u-log K(z),
chi(x)=2 log(uv)-log K(x)-log K(P(x)).              (9)
```

Therefore the correct section equation is

```text
chi(x)=0  iff  (uv)^2=K(x)K(P(x)).                 (10)
```

The local reversible atlas sees a gluing discrepancy up to about `1.000325`
on its sampled symmetric carrier.  Sprint 1272 corrects the typing of that
number: it is a local-chart normalization diagnostic, not the global Bellman
`K` range.  A separate min-plus reconstruction finds the global sampled range
reaching about `1.00733` near `|x|=0.9`.  Neither range is interval-certified.
Conceptually, `K` is the precise price of gluing the local reflected
characteristic to the globally normalized Bellman envelope.

## Boundary

Neither reciprocal normalization, the balanced-weight collapse, nor
`chi=2 log(uv)` is claimed.  The defect-corrected identities (7)--(10) are
exact algebra.  The three-root interval campaign must certify `K` together
with the characteristic ratios, or directly interval-evaluate the globally
normalized `F` and `P`.  The final sentence of the historical Sprint 1271
version said the public theorem was unchanged. Sprint 1285 later proved that
this normalization defect is load-bearing for the Bellman assembly; the
public theorem is now under correction as described in
`paper/CERTIFICATE-STATUS-ALERT.md`.
