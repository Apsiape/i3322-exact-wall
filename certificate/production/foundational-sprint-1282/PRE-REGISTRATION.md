# Pre-registration: Bellman selector collision

Compare two independently constructed profiles at the same certified `q*`:

1. the corrected shooting atlas assembled from the exact plateau
   parameterization, four certified central iterates, two certified wing
   iterates, and their reversible charts;
2. the 51,201-node monotone Bellman iteration initialized at the boundary cap.

Use the common active carrier `[-0.898,0.898]`.  Neither construction may use
the other's values.  Evaluate the log-free drift discriminant and its three
roots on each profile.

Registered instrument gates:

1. shooting-chart overlap spread remains below `1e-12`;
2. both profiles are positive on the carrier;
3. both produce exactly three simple numerical drift roots;
4. both agree with the exact plateau values at `+/-C` within `2e-5`.

Registered classification:

- **same selector consistent** only if the uniform profile discrepancy is
  below `5e-5` and every paired root differs by less than `2e-4`;
- **distinct selector consistent** only if the uniform profile discrepancy is
  above `1e-4` and at least one paired root differs by more than `5e-4`;
- otherwise **unresolved**.

A distinct-selector result does not by itself prove two exact Bellman fixed
points: the shooting atlas is a high-accuracy floating reconstruction of an
exact certified graph, while the boundary iteration remains a discrete
approximation.  It would, however, invalidate treating the drift roots as
canonical until the selector ancestry is resolved exactly.
