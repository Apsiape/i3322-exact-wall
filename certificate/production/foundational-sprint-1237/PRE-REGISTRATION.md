# Pre-registration -- fixed-d optimizer reduction

The sprint passes only if it proves:

1. `Q_d` is attained in the mixed-state/binary-POVM parameter space;
2. with all effects fixed, a maximizing state may be replaced by a pure top
   eigenstate on the same `d x d` space;
3. holding the state and every other effect fixed, a maximizing binary effect
   may be replaced by an extreme point of `[0,I]` without lowering the value;
4. the extreme points of `[0,I]` are exactly orthogonal projections;
5. replacing the six effects sequentially preserves the global optimum and
   never changes local dimension; and
6. a lower bound for the projective optimum implies the same deficit bound
   for every dimension-`d` POVM strategy.

At least 50,000 exact-rational multilinear hostile fixtures must verify the
finite sequential-replacement logic.  A proof that uses dilation fails.
