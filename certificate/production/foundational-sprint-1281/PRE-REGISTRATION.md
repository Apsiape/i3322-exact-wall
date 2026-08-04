# Pre-registration: exact reversed-plateau obstruction

The Sprint-1280 algebraic candidate appears to be the negative reversible
image of the already certified Sprint-1115 high plateau.  Test that ancestry
exactly rather than building a redundant interval contact proof.

Let

```text
s=sqrt(1-C^2),
R=s(2C-1)/[(1-C)(2C+1)],
q=(4C^4-5C^2+2)/(4C^2-1).
```

Verify symbolically:

1. the Sprint-1280 quartic vanishes at `x=-C`;
2. the reverser sends `(C,C,R)` to `(-C,-C,1/R)` and the latter is fixed
   whenever the former is fixed;
3. the negative Bellman value is
   `F(-C)=s/(2R)=(1-C)(2C+1)/(2(2C-1))`, exactly the Sprint-1280 low branch;
4. the Bellman derivative multiplier there is
   `(1-C^2)/(4F(-C)^2)=R^2`;
5. on `sqrt(3)/2<C<1`,
   `R^2-1=-2C(4C^2-3)/[(C-1)(2C+1)^2]>0`.

Require the existing exact plateau, reverser, global graph, and global Bellman
assembly receipts to pass unchanged.

If all gates land, state the scoped no-go: for any bounded positive weight
with finite nonzero value at `-C`, the weighted composition derivative

```text
(L delta)(x)=c(x) delta(P(x))
```

has norm at least `R^2>1` on the fixed one-point orbit.  Hence this derivative
cannot be made contractive by any such weighted sup norm.

This kills a proof architecture, not the I3322 theorem or the prospective
dimension lower bound.
