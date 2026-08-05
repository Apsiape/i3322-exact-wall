# Pre-registration: endpoint-clustered Bellman collider

## Observation held fixed

The 6,401- and 25,601-knot exact certificates have their worst common cell
near `x=-0.893`, while the active envelope owner moves toward the endpoint
`u=-1` (from approximately `-0.991` to `-0.994`).  Fourfold uniform
refinement reduced the upper tax by approximately a factor of sixteen.

## Wager

The remaining upper tax is dominated by resolution of an endpoint/contact
pair rather than by a global tensor-versus-commuting obstruction.

## Frozen construction

Use exactly 25,601 symmetric rational grid points.  Before decimal
quantization their search coordinates are

```text
x(t) = (2t-1 - cos(pi*t))/2,       t=i/25600.
```

Thus the grid is the equal blend of the uniform and Chebyshev--Lobatto grids.
Construct the left half, quantize it to 18 decimal places, and obtain the
right half by exact sign reflection so symmetry is not a floating accident.
Run the same ordered Bellman-envelope iteration and commit the resulting
18-place positive rational knot values.  The floating search has no proof
authority.

The theorem engine must independently use exact `Fraction` arithmetic on the
stored nonuniform grid, reconstruct its support-line hull, form every common
linearity cell, and locate the first passing `10^-15` grid point.

## Registered predictions

1. the exact candidate is positive and covers `[-1,1]` strictly increasingly;
2. the exact threshold is below `0.250875387500000`;
3. the exact window against the dimension-255 lower bound is below `3e-9`;
4. the immediate `10^-15` predecessor fails;
5. either the worst receipt remains in the registered endpoint/contact region
   (`x in [-0.91,-0.87]`, owner below `-0.98`) or the new receipt explicitly
   identifies the bottleneck displaced by endpoint clustering.

## Failure value

Failure of predictions 2 or 3 rejects the simple endpoint-resolution account
at fixed witness size.  A displaced worst receipt is not repaired post hoc;
it becomes the datum for deciding whether a global adaptive mesh or a genuine
continuum regularity theorem is needed.

## Claim boundary

Passing would provide a stronger fixed-witness upper bound and evidence about
the discretization mechanism.  It would not identify the exact optimum,
prove an `h^2` theorem, establish flow-to-path realizability, or restore the
historical nonattainment and correlation-set corollaries.
