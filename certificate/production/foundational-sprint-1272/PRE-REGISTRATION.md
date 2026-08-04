# Pre-registration: normalization-defect geometry and symmetrization tariff

Define

```text
K(x)=F(x)F(-x)/b(x)^2,
b(x)=sqrt(1-x^2)/2.                                  (1)
```

For a Bellman contact state `M(z,x,u)=(x,y,v)`, put

```text
a=b(z)/u=p(z),
c=b(x)v=F(x).                                        (2)
```

Before running a new profile reconstruction, register the exact candidate
laws

```text
K(-x)=K(x),
A(z)=a sqrt(K(z)),
B(x)=c/sqrt(K(x)),                                   (3)

r_sym(z,x)=a+c-A(z)-B(x)
          =a[1-sqrt(K(z))]+c[1-1/sqrt(K(x))],        (4)

r_ref(z,x)=a+c-F(-z)-p(-x)
          =a[1-K(z)]+c[1-1/K(x)].                   (5)
```

The numerical predictions are:

1. `K` is at least one, up to the registered reconstruction tolerance;
2. `K` has a unique maximum at zero and is strictly decreasing on `[0,0.9]`;
3. `max(K)-1 < 1/2 (q_*-1/4)`;
4. the exact tariff formulas (4)--(5) agree with direct evaluation;
5. the zeros of `r_sym` coincide with the three Sprint-1268 drift zeros.

Prediction 5 is a hostile identification test.  Its failure means the
normalization defect and cocycle drift are distinct structures even though
both enter the same response architecture.  No monotonicity or zero-set claim
is promoted from a floating-point run.
