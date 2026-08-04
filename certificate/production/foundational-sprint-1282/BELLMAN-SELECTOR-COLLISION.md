# Bellman selector collision: distinct profiles, not two proved fixed points

## Registered result

The corrected shooting atlas and the 51,201-node boundary-cap iteration pass
all four instrument gates.  Both are positive, both match the exact plateau
values, and both have three simple numerical drift roots.

They nevertheless meet the preregistered **distinct selector consistent**
classification:

```text
maximum profile discrepancy             1.14558e-3
coordinate of maximum discrepancy       -0.898

shooting roots       -0.86439146  -0.37698922   0.79990479
boundary roots       -0.86615967  -0.37698052   0.80000187
paired differences   1.76821e-3    8.69583e-6   9.70748e-5
```

Thus a drift zero census depends materially on which amplitude normalization
is attached to the characteristic graph.

## Post-run adjudication

A direct Bellman contact check prevents the tempting conclusion that these
are two exact fixed points:

```text
boundary-iteration contact residual     2.97e-8
shooting-atlas contact residual          1.62e-4
```

The check excludes points whose predecessor leaves the common active carrier,
so the shooting residual is not an edge extrapolation artifact.  It is the
normalization defect already warned about in Sprint 1271: exact reversibility
transports a local characteristic, but it does not transport the globally
selected Bellman amplitude for free.

The registered collision remains real.  Its correct meaning is that local
shooting coordinates and globally normalized Bellman values are different
types.  The local atlas's three roots cannot certify the global drift roots.

## Consequence

The direct interval campaign cannot evaluate the drift by gluing the existing
reversible shooting charts naively.  It needs one of two honest instruments:

1. a globally normalized interval atlas whose chart transition constants are
   explicitly carried and certified; or
2. continuous Bellman sub/supersolutions that enclose the global selected
   value without invoking a contraction.

The first is now preferable because the exact characteristic graph already
exists; the missing data are scalar normalization transitions, not geometry.
Those transition constants should be solved on chart overlaps against one
global anchor, then independently checked against Bellman contact.

## Claim boundary

This is a floating-point collision and post-hoc contact audit.  It proves
neither exact Bellman multiplicity nor the global three-root theorem.  The
public I3322 result is unchanged.
