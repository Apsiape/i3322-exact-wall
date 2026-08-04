# The shooting value is a numerical global-Bellman positivity threshold

## Result

The preregistered ordered-hull experiment passed all six gates.

For each of `N=801,1601,3201,6401`, direct Bellman iteration from the affine
boundary cap was run without a positivity floor.  The classification is
uniform across all four resolutions:

```text
q-q_center       result
-1e-4            collapse to F<=0
-1e-5            collapse to F<=0
-1e-6            collapse to F<=0
 0               positive fixed profile
+1e-6            positive fixed profile
+1e-5            positive fixed profile
+1e-4            positive fixed profile
```

At zero offset,

```text
N=3201  min F = 0.053006945780839754
N=6401  min F = 0.053006292806481614
difference       6.529743581396019e-7.
```

No run was unresolved.  Negative offsets collapsed in 45--129 iterations;
the zero-offset profiles converged in 144--148 iterations.

## Interpretation

This is the first evidence for a repair architecture that does not reuse the
failed normalization:

```text
shooting/wall construction  -> lower bound at q_*
global Bellman positivity   -> upper bound at q_*
```

The two objects can meet at the same scalar without being the same local
characteristic chart.  The numerical result suggests that the shooting value
is the critical parameter at which the globally selected Bellman envelope
first remains positive.

That interpretation is stronger and cleaner than repairing the reflected
chart by an ad hoc scale factor.  It also explains why the boundary iteration
had a tiny Bellman contact residual while the reversible shooting atlas did
not: they are different theorem owners.

## What is not proved

This is a deterministic floating-point scout, not an interval theorem.  It
does not prove:

- exact equality of the shooting root and the Bellman positivity threshold;
- existence of a positive continuous fixed point at every exact `q` in the
  shooting interval;
- a global Bellman inequality at `q_*`;
- nonattainment, spatial separation, or nonclosure.

The current public theorem remains under correction.

## Exact repair target

The next proof should avoid characteristic gluing entirely.  Construct a
positive continuous concave function `G` such that

```text
G(u) + (1-x^2)/(4G(x))
    <= q + 1 - x/2 - (x-1/2)u
```

for every `(x,u)` in `[-1,1]^2`, with `q` enclosed by the validated shooting
interval.  Such a subsolution directly gives the Bellman upper bound.  A
piecewise-polynomial or piecewise-rational `G` obtained from the boundary
fixed point can be checked rectangle by rectangle with interval arithmetic;
no reflected amplitude identification is needed.

Only after that upper bound lands should uniqueness/contact be rebuilt for
finite-dimensional nonattainment.
