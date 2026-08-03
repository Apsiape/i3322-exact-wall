# Technical supplement: the validated Bellman/domain-wall certificate

**Seth Douglas** ·
[ORCID 0009-0007-4708-3252](https://orcid.org/0009-0007-4708-3252) ·
[apsiape@gmail.com](mailto:apsiape@gmail.com)

This supplement states the computer-assisted input used by *A rigorously
characterized I3322 quantum wall and finite-dimensional nonattainment* at a
level suitable for reproduction. The analytic operator certificate and the
finite-support contradiction are in the main manuscript. No foundational
interpretation from the surrounding repository is used.

## S1. Arithmetic model and theorem boundary

All rigorous numerical inequalities use Arb real balls through `python-flint`.
Symbolic identities use exact SymPy arithmetic. A printed decimal is never a
gate: a gate passes only when a ball excludes zero with the required sign or
an exact residual is identically zero.

The computer proves the **Certified Bellman proposition** in the main text:
there exist the stated `q_*`, a positive concave `F`, and a strictly increasing
predecessor `P` for which the global Bellman inequality has a unique contact.
It also proves that finite truncations of the selected orbit approach `q_*`.
Everything after that proposition is analytic.

The enclosure is

```text
q_* in [0.250875384513976535514,
        0.250875384513976536486].
```

It is a validated shooting constant, not an asserted elementary closed form.

## S2. Characteristic recurrence

Write a characteristic state as `(x,y,u)`, put

```text
sx = sqrt(1-x^2),     sy = sqrt(1-y^2),
D  = xy + (x-y)/2 - 1,
v  = 2(q-D-sx/(2u))/sy,
z  = ((1-2x)+2yv/sy)/(2v^2) - 1/2.
```

The forward characteristic map is

```text
M_q(x,y,u) = (y,z,v).                           (S2.1)
```

It is obtained by imposing equality and stationarity in the Bellman equation,
with `u` the adjacent amplitude ratio. Direct symbolic substitution proves
that the Bellman residual vanishes along (S2.1).

The map has an exact reversal symmetry. The required orbit leaves a positive
fixed plateau, crosses a two-equation reflection section after four and five
iterates, and returns along the reflected branch. This converts the infinite
domain wall into a finite shooting problem plus validated tails.

## S3. Algebraic plateau and hyperbolicity

The positive plateau `(C,C,R)` lies on the branch

```text
R = sqrt(1-C^2)(2C-1)/((1-C)(2C+1)),
q = (4C^4-5C^2+2)/(4C^2-1),
sqrt(3)/2 < C < 1.                              (S3.1)
```

Exact elimination isolates this branch and proves the relevant root count.
At the selected point the derivative of `M_q` has two stable multipliers and
one unstable multiplier. Reference midpoints are

```text
5.8379840653..., 0.8603760495..., 0.1473755392....
```

The certificate proves separation from the unit circle by interval bounds;
the decimals only identify the branch.

## S4. Analytic local unstable manifold

The local unstable curve is represented analytically as `P(t)` and normalized
by

```text
M_q(P(t)) = P(mu t).                            (S4.1)
```

A high-order polynomial approximation is corrected by a graph transform on a
complex ball. The validated bounds are:

- 400 complex boundary tiles;
- real radicand margin greater than `0.22545`;
- denominator margin greater than `1.0726`;
- graph-transform contraction at most `0.180945557`;
- correction at most `1.859e-26` in adapted coordinates and
  `2.213e-25` in original coordinates.

Thus the true analytic unstable curve exists uniquely inside the tube used by
the shooting proof.

## S5. The two-dimensional shooting zero

The unknowns are the plateau coordinate `C` and unstable parameter `t`. The
two shooting residuals are evaluated after the fourth and fifth iterates:

```text
crossing[0] + crossing[1] = 0,
after[2] - 1/crossing[2] = 0.                  (S5.1)
```

They encode the reflection section and amplitude reversal. A preconditioned
Miranda argument validates one zero in

```text
C in 0.8782729451808124521 +/- 4.86e-20,
t in 0.0037582873342893243 +/- 4.36e-20.
```

Propagating this rectangle through (S3.1) gives the stated `q_*` enclosure.
Every opposite face has the registered strict sign after including the local
manifold and propagation error. Tail allowances are below `1.9e-23` and
`9.95e-25` in the two preconditioned residuals.

Miranda proves existence. Branch isolation, hyperbolicity, and the strict graph
certificates below supply the uniqueness needed by the Bellman construction.

## S6. Exact contact covariance

Let `R(x,y,u)=0` denote Bellman equality and let

```text
beta = dF(x) - (1/2-y) dx.
```

Exact symbolic calculation gives

```text
M_q^* beta = beta/u_next^2.                    (S6.1)
```

All coefficient residuals reduce to zero. Because the local unstable tangent
lies in `ker(beta)`, (S6.1) transports the Bellman envelope relation over the
entire certified orbit. This is the exact bridge between the shooting dynamics
and the scalar function `F`; it is not inferred from plotting or interpolation.

## S7. Global invariant graph

The central orbit is covered by 300-bit Arb boxes:

- 8,192 local plateau tiles;
- four central pieces of 32,768 tiles each;
- zero failed tiles.

On every tile the projected derivatives satisfy strict signs giving a
single-valued graph with `dx/dt<0` and `dy/dt<0`; the interval pivots are
strictly positive. Reflection supplies the other half. Consequently the
predecessor `P` is strictly increasing and contact is unique in the active
central region.

An earlier literal six-forward-piece parametrization failed. The corrected
cover is plateau-to-section plus reflection. The failed parametrization is
retained in the receipt so that the accepted geometry cannot silently inherit
the wrong coordinate convention.

## S8. Boundary wing and inactive exterior

The active right wing begins at the unique root in a width-`2e-14` bracket
around

```text
t = -0.003719358976358651...
```

The residual derivative is below `-34.725`; endpoint signs are opposite. Two
pieces of 32,768 boxes certify the wing to the endpoint, whose terminal
predecessor is enclosed near `0.898116482394039`. Reflection gives the left
wing.

The remaining outer interval is divided into 32,768 boxes. Successor
monotonicity and the stationarity-target derivative exclude any additional
contact; the reconstructed Bellman value has lower bound greater than
`0.2104`. The first attempted guard—strict monotonicity of a line derivative—
fails at the calibrated endpoint for a structural reason. The accepted guard
uses successor monotonicity, and the receipt records both the failure and the
repair.

## S9. Positivity, concavity, and finite truncations

The contact relation defines `F` on the invariant graph. Equation (S6.1), the
strict derivative signs, and the inactive exclusion imply:

1. `F>0` on `[-1,1]`;
2. the contact slope is monotone, hence `F` is concave;
3. each `u` has exactly one active predecessor `P(u)`; and
4. every other `x` lies strictly above the tangent contact, yielding the global
   Bellman inequality.

The hyperbolic plateau provides square-summable tails. Cutting the two-sided
orbit at finite distance and normalizing produces finite tensor-product
strategies. Boundary errors decay to zero, so their Bell values converge to
`q_*`. This is an approximation statement; the separate equality-kernel proof
shows that no finite cut can attain the limit.

## S10. Analytic upper certificate and equality audit

The main paper combines the Bellman inequality with its reflection to obtain
scalar functions `a,c` satisfying

```text
a(x)+c(u) <= q_*-d(x,u),
a(x)a(-x)=b(x)^2,
c(u)c(-u)=b(u)^2.                              (S10.1)
```

Functional calculus turns (S10.1) into three positive operators whose sum is
`q_* I-B_3322`. This works for arbitrary commuting projective measurements.

The finite-support equality argument has two implementations. The theorem
engine follows the spectral-kernel proof. An independently written audit
reconstructs the decreasing-bijection lemma by rank tables and separately
eliminates the amplitude ratio. Both end at

```text
q_* <= -t+sqrt(t) <= 1/4,
```

contradicting the certified lower endpoint of `q_*`.

## S11. What is and is not independently checked

The release verifier freezes hashes, checks semantic gates, and can rerun all
engines. The production path is deterministic reproducibility. A second path
under `independent/` reconstructs every computer-assisted Bellman gate with
`mpmath.iv`, a locally implemented rectangular complex-interval layer, and no
imports from the Arb/FLINT production modules. Its arithmetic harness passes
18,000 rational-enclosure checks. It independently certifies the plateau and
degree-12 invariant series, analytic graph transform, Miranda shooting zero,
8,192-tile central graph, endpoint wing, and inactive exterior. All eight
registered gates pass.

The independent shooting interval is

```text
[0.2508753845139765355147934110068914495...,
 0.2508753845139765357198798108850040972...].
```

It overlaps the production Arb interval and both directed endpoints round to
the displayed 18-place value. The independent analytic-tail allowance is
`2.2592334301979876e-25`, only `1.020883...` times the production allowance.
The nonattainment proof separately has two exact symbolic implementations.
This is method-independent internal reconstruction, not evidence about
physical enactment or a claim that implementation diversity proves a theorem
without the analytic arguments stated in the paper.

The numerical finite-carrier sequence is consistent with
`q_*-Q_n = Theta(R^{-n})`, with the fitted asymptotic exponent agreeing with
`log R` to about `8e-7`. The current exact reversal proof is discontinuous and
does not give a robust defect estimate. Therefore no quantitative
device-independent dimension lower bound is claimed.

## S12. Reproduction

From the repository root:

```powershell
python certificate/release/verify_release.py
python certificate/release/verify_release.py --full
```

The first command checks custody and committed receipts. The second
deterministically regenerates the proof stack. Exact file ownership, hashes,
and individual commands are in `CERTIFICATE-MAP.md` and
`release/release-manifest.json`.
