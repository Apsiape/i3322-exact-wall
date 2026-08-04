# The parabolic signal survives grid phase and deep refinement

## Verdict

The Sprint-1278 bottleneck collapse is not a lucky alignment of one uniform
grid.  All nine preregistered neighboring node counts and both deeper
refinements satisfy every instrument gate.

```text
phase ensemble N=12797..12805:
  gap range       [2.3025e-5, 1.2222e-4]

deep refinement:
  N=25601         6.9507e-5
  N=51201         2.1794e-5

all coordinates  within 1.05e-4 of -0.8782
all multipliers  > 1.1616
```

The registered classification is **phase-robust parabolic signal**.

## What changed

The memory-safe affine-hull engine was extended so that a final predecessor
owner is located by binary search on the exact discrete lower envelope.
Continuous local minimization then uses only the owner's neighboring cells.
The 51,201-node reconstruction completes without an `N x N` allocation.

The neighboring-grid gaps vary, as expected for a contact sampled at changing
lattice phase, but none reopens the preregistered strict-transit scale.  The
location and multiplier are substantially more stable than the gap itself.

## New algebraic target

At a differentiable active contact with `P(x)=x`, the envelope theorem gives
`F'(x)=1/2-x`.  Combining Bellman equality with predecessor stationarity
reduces the candidate to a finite algebraic system.  A preliminary symbolic
elimination factors through

```text
4x^4-(4q+5)x^2+(q+2)=0.
```

Its outer negative root at the certified `q*` is approximately
`-0.87827294518`, inside every refined bottleneck cluster.  This observation
was made after the phase experiment and is not counted as a registered gate.
It defines the next exact campaign: derive the conditional normal form, verify
the branch factors symbolically, and certify that the global Bellman minimizer
actually realizes the algebraic candidate.

## Claim boundary

Grid-phase robustness is stronger numerical evidence, not a proof of zero
gap.  The displayed polynomial is a necessary condition under explicitly
stated differentiability, activity, uniqueness, and fixed-predecessor
hypotheses.  It does not by itself establish any of those hypotheses.  The
public I3322 theorem and the conditional dimension-law boundary are unchanged.
