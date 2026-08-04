# The dimension-`d` optimum has a pure projective representative

Status: **analytic finite-dimensional theorem plus 50,000 exact-rational
multilinear guards**

## Theorem

Fix local Hilbert spaces `H_A,H_B` with dimensions at most `d`.  The maximum
of any finite binary-output Bell functional over density operators and binary
POVMs on these spaces is attained by a pure state and orthogonal-projection
effects on the same spaces.

No dilation is used.

## Proof

The density matrices and six effect intervals

```text
0<=E<=I
```

are compact in finite dimension.  The Bell value is continuous, so a global
maximizer exists.

Hold all effects fixed.  The objective has the form `Tr(rho B)` for one
Hermitian Bell operator `B`.  Replacing `rho` by a rank-one projection onto a
top eigenvector of `B` cannot lower the value.  Because the starting point was
globally maximizing, the value remains the global maximum.  The local spaces
are unchanged.

Now hold the state and five effects fixed.  As a function of the remaining
effect `E`, the value is

```text
constant+Tr(C E)                                   (1)
```

for a Hermitian coefficient `C` on that party's original local space.  The
maximum of (1) over `0<=E<=I` is attained by the spectral projection of `C`
onto its positive eigenspace, with any projection choice on the zero
eigenspace.  This replacement cannot lower the value and does not change
dimension.  Repeat for all six effects.  Every intermediate point remains a
global maximizer, so after finitely many replacements the state is pure and
all measurements are projective.

For completeness, the extreme points of `[0,I]` are precisely projections.
If `E` has an eigenvalue strictly between zero and one, perturbing that
eigenvalue up and down writes `E` as the midpoint of two distinct effects.  If
`P` is a projection and `P=(E_1+E_2)/2`, saturation on `ran(P)` and vanishing
on `ker(P)` force `E_1=E_2=P`.

## Consequence for `Q_d`

Let `Q_d` allow arbitrary mixed states and binary POVMs.  The theorem gives a
pure projective dimension-`d` strategy with value exactly `Q_d`.  Therefore a
deficit lower bound proved for every pure projective dimension-`d` strategy
also bounds `q_*-Q_d`.  Moreover every individual dimension-`d` POVM strategy
has value at most `Q_d`, so it inherits the same lower deficit.

This closes the quantifier without the dimension-increasing Naimark route.

## Guard

The exact common-denominator engine tested 50,000 six-variable multilinear
objectives.  Sequential endpoint replacement never lowered the value; a
held-out subset independently enumerated all 64 vertices.  The guard checks
the finite replacement logic.  The matrix spectral argument above is the
proof.

## Boundary

This is a standard finite-dimensional convexity reduction, not a new Bell
theorem.  It supplies a missing explicit dependency to the blind packet; it
does not validate the packet/discard assembly.
