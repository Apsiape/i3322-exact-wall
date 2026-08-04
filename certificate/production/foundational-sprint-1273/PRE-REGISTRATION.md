# Pre-registration: the log-free global drift discriminant

For the globally normalized Bellman function and predecessor map, define

```text
chi(x)=log(F(x)/F(-x))+log(F(P(x))/F(-P(x))),        (1)

D(x)=F(x)F(P(x))-F(-x)F(-P(x)).                     (2)
```

Because every factor is positive, register the exact equivalence

```text
sign chi(x)=sign D(x),
chi(x)=0 iff D(x)=0.                                 (3)
```

In terms of the characteristic ratios and the normalization defect,

```text
D(x)=b(x)b(P(x))/(uv)
     * [(uv)^2-K(x)K(P(x))].                         (4)
```

The sprint passes only if:

1. (3)--(4) reduce symbolically to zero;
2. the 1601- and 3201-node global Bellman reconstructions have no sign
   disagreement between `chi` and `D` away from numerical zeros;
3. `D` has exactly the same three registered roots as `chi`, within `1e-8`
   inside each reconstruction;
4. the result is typed only as a replacement interval target, not a root-count
   theorem.

Failure means the previous drift implementation or the proposed algebraic
typing is inconsistent.  Passing does not certify the zero count until Arb
enclosures cover the full domain.
