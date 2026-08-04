# Exact reversed-plateau obstruction

## The hidden identity

The apparent new contact of Sprints 1277--1280 is not a new point.  It is the
negative reversible image of the high plateau certified in Sprints
1115--1195.

Let

```text
s=sqrt(1-C^2),
R=s(2C-1)/[(1-C)(2C+1)],
q=(4C^4-5C^2+2)/(4C^2-1),
sqrt(3)/2<C<1.
```

Sprint 1115 proves that `(C,C,R)` is the high plateau fixed state.  Sprint
1270 proves the exact reverser

```text
R_map(x,y,u)=(-y,-x,1/v),
R_map M R_map = M^-1.
```

Therefore its image `(-C,-C,1/R)` is also fixed.  Direct substitution into
the shooting map verifies both fixed coordinates exactly.

## The Sprint-1280 polynomial was already the plateau law

Substituting `x=-C` into

```text
4x^4-(4q+5)x^2+(q+2)=0
```

is exactly equivalent to the displayed formula for `q(C)`.  The negative
Bellman value is

```text
F(-C)=s/(2R)
     =(1-C)(2C+1)/(2(2C-1)),
```

which is exactly Sprint 1280's low-value branch.  The global characteristic
graph and Bellman fixed-point receipts in Sprints 1192--1195 already certify
that this fixed characteristic belongs to the global wall.

Thus the numerical argmin failure in Sprint 1280 was not missing existence.
It was the expected ill-conditioning of sampling an already exact parabolic
fixed characteristic.

## Exact contraction no-go

The Bellman derivative multiplier at the reversed plateau is

```text
c(-C)=(1-C^2)/(4F(-C)^2)=R^2.
```

Moreover

```text
R^2-1 = -2C(4C^2-3)/[(C-1)(2C+1)^2] > 0
```

on `sqrt(3)/2<C<1`.

For a bounded positive weight `w` with finite nonzero `w(-C)`, the weighted
composition multiplier on the fixed one-point orbit is

```text
c(-C) w(P(-C))/w(-C) = R^2 > 1.
```

Hence the Bellman derivative cannot be a contraction in any such weighted
sup norm.  This is an exact obstruction, not a numerical warning.

## Meaning for the campaign

The failed continuous weight in Sprint 1277 and the phase-robust gap collapse
in Sprints 1278--1279 are now explained by old certified structure.  The
sampled finite graphs contracted because discretization replaced the exact
expanding fixed characteristic by a finite transit or split rounded loops.
Their weights cannot converge to a bounded continuous weight.

The three-root campaign must abandon global Banach contraction.  Its viable
proof mechanisms are now monotone enclosure of the already certified
characteristic graph, interval degree/sign topology, or a parabolic normal
form that explicitly separates the two plateau ends.

This result kills a proof architecture only.  It does not weaken the exact
I3322 wall, change the public theorem, or prove the prospective universal
dimension lower bound.
