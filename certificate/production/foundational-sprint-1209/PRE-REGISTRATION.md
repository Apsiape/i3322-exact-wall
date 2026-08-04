# Sprint 1209 pre-registration -- response debt as measure asymmetry

Date: 2026-08-03

## Wager

The robust response theorem of Sprint 1208 can be pushed from vectors to
spectral measures without selecting eigenvectors or rounding multiplicities.
For a sign-symmetric good cutoff, the local remainder expectation should
upper-bound the total-variation defect between the weighted spectral measure
and its reflected pushforward.

## Registered predictions

1. If `w=E sqrt(A(X)) psi`, `KXK=-X`, and
   `delta=||(I-K)w||`, then for every bounded real `f`,

   ```text
   |<w,f(X)w>-<w,f(-X)w>| <= 2 ||f||_infinity ||w|| delta.
   ```

2. The identity preceding Cauchy--Schwarz is exact and uses only
   `K f(X) K=f(-X)`.
3. With `m=||w||^2`, the normalized reflected-measure defect is at most
   `2 delta/sqrt(m)` in the dual total-variation norm.
4. Sprint 1208 therefore gives the explicit bound

   ```text
   2 sqrt(2 epsilon_A/[eta(1-theta_A)])
   ```

   whenever the bad-cutoff state mass is at most `theta_A<1`.
5. The result will not yet compose Alice and Bob transports: the two weighted
   measures differ, and their Radon--Nikodym cocycle must be retained rather
   than normalized away.

## Failure conditions

- the reflected pushforward requires discrete spectrum;
- the cutoff fails to commute with the reflection;
- multiplicity enters the bound;
- normalization introduces an uncontrolled small denominator despite the
  good-mass estimate;
- or the cocycle can be discarded without changing the finite-section rate.
