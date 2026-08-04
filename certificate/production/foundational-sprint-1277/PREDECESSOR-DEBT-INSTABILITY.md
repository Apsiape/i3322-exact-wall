# Continuous predecessor debt: the stability gate fails

## Verdict

The canonical finite-horizon potential

```text
h(u)=max_(0<=n<=200) sum_(j=0)^(n-1)
     [log c(P^j(u))-log(0.9)]
```

does enforce the desired weighted multiplier inequality separately on both
tested Bellman reconstructions.  It does **not** stabilize between them.
Four of the five preregistered gates pass; the uniform two-resolution gate
fails by a factor greater than fifty.

```text
maximum weighted multiplier       0.9000000000000005
weight dynamic range              5.23
latest maximizing partial sum     step 10
maximum increment, steps 181--200 -0.0449

registered uniform h tolerance    0.005
measured uniform disagreement     0.252350499959
```

The largest discrepancy occurs at `u=-0.8875`.  The 1601-node reconstruction
maximizes at step 9 with `h=1.3900059675`; the 3201-node reconstruction
maximizes at step 10 with `h=1.6423564675`.

## Mechanism

At that point the two continuously interpolated predecessor maps initially
disagree by only about `4.64e-5`, but both trajectories linger near the
negative bottleneck around `u=-0.878`.  There the derivative multiplier is
approximately `1.16`, above both one and the registered contraction target.
The fine orbit remains in the locally expanding region for one additional
iterate, adding approximately `0.25` to the accumulated debt.  A tiny change
in the reconstructed predecessor therefore becomes an order-one change in
the canonical weight.

This is not nearest-grid rounding: Sprint 1277 iterates shape-preserving
continuous predecessor profiles.  Nor is the failure repaired by the
negative 200-step tail.  The problem is the finite transient residence time
before that tail begins.

## Consequence

Sprint 1276's sampled functional-graph weights remain valid facts about those
finite graphs.  They no longer justify calling the continuous weighted-norm
route viable.  The straightforward canonical lift is resolution-unstable and
must not be intervalized as if it were already a continuous object.

The next question is narrower and more decisive: does the exact Bellman
predecessor have a genuine negative parabolic contact, or does it have a
strict but very small transit gap?  In the first case every bounded positive
weighted sup norm is obstructed if the contact multiplier exceeds one.  In
the second case a weight may exist, but its conditioning is controlled by a
quantitative lower bound on that transit gap.  A higher-resolution,
memory-safe continuous Bellman reconstruction must decide between those two
possibilities before any contraction theorem is attempted.

## Claim boundary

All displayed data are finite-resolution, finite-horizon floating-point
results.  They refute the registered stability claim.  They do not prove a
parabolic fixed point, nonexistence of every continuous Lyapunov weight, or
any change to the public I3322 theorem.
