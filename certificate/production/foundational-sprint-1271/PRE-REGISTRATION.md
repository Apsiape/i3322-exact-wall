# Pre-registration: reciprocal Bellman normalization and drift factorization

Sprint 1270 proves the exact characteristic reverser

```text
M(z,x,u)=(x,y,v),
R(z,x,u)=(-x,-z,1/v),
R M R=M^-1.                                         (1)
```

Before using this symmetry in the dimension campaign, test whether the
normalization of the selected Bellman graph really glues across the reflected
branch.  With

```text
b(x)=sqrt(1-x^2)/2,
F(z)=b(z)u,
F(x)=b(x)v,                                         (2)
```

the candidate identities are

```text
F(x)F(-x)=b(x)^2,
p(x):=b(x)^2/F(x)=F(-x),                            (3)
A(x)=sqrt(p(x)F(-x))=F(-x),
B(x)=sqrt(F(x)p(-x))=F(x).                          (4)
```

For a contact state with predecessor `z=P(x)`, define

```text
H(x)=log(F(x)/F(-x)),
chi(x)=H(x)+H(P(x)).                                (5)
```

The registered factorization is

```text
H(x)=2 log v,
chi(x)=2 log(uv),
chi(x)=0  iff  uv=1.                                (6)
```

The sprint passes only if:

1. all identities follow symbolically from the displayed characteristic and
   reverser formulas;
2. the graph-coverage argument identifies the reversed values with the same
   globally normalized `F`, rather than an independently rescaled branch;
3. the existing corrected atlas satisfies (3) numerically on every overlap;
4. no public theorem is widened merely from this simplification.

Failure of global branch normalization kills (3)--(6), even if the local
symbolic algebra is correct.
