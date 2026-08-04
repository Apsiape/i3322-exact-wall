# Sprint 1233 pre-registration

Let `t=sqrt(epsilon)`, `A=20^2`, `M=78/5`, and suppose

```text
L_d<=lambda A^d t,
W_D>=1-alpha t-L_d,
B_lower>=W_D/[(d+1)M^(2d)],
B_upper<=beta[d t+L_d].
```

Register that these four lines alone imply

```text
epsilon>=c d^-4 (20M)^(-4d)
```

for some positive `c` depending only on `alpha,beta,lambda`. The verifier
will attack both the large-loss and small-loss cases over exact rationals.

