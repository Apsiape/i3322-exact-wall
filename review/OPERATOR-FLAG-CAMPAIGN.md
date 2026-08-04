# Operator-flag campaign after the scalar no-go

**Date:** 2026-08-04  
**Release decision:** unchanged -- do not tag or mint v1.3

## Result stack

The replacement campaign deliberately starts before packetization.

1. **Schmidt correspondence (Sprint 1240).** The two response remainders are
   exact Hilbert--Schmidt defects of two-sided transformations of the state
   coefficient operator. Mirsky's inequality controls the complete singular
   spectrum. The regularized volume
   `Phi_t(D)=log det(tI+D^*D)` is stable with explicit constant and telescopes
   to a boundary term on an open shift.
2. **Marginal null (Sprint 1241).** Two distinct finite involutions can preserve
   every marginal singular value, exterior power, determinant, and `Phi_t`
   while producing different targets. Marginal volume is therefore not the
   missing closure invariant.
3. **Regularized flags (Sprint 1242).** The soft support eigenvalues
   `s^2/(t+s^2)` interpolate between mass and rank. Contact intertwiners
   transport their cumulative spectral flags with an explicit bound.
4. **Grid-free I3322 contact (Sprint 1243).** The layer-cake identity and the
   certified global Bellman coercivity yield

   ```text
   integral ||1_{Y(X)<=s}D-D1_{U<=s}^T||_HS^2 ds
   <=sqrt(40 epsilon_0).
   ```

   This retains every complement and uses no spectral partition.
5. **Mixed flag distance (Sprint 1244).** Relative gluing is a weighted
   cumulative-flag distance. For permutations it is exactly a weighted
   Spearman footrule; for branch-mixing kernels it is rowwise one-dimensional
   Wasserstein distance.
6. **Resolution-scale lift (Sprint 1245).** On exact contact, a response
   multiplier `c` translates the regularization scale `t` to `t/c^2`.
   Composing the two response maps reproduces the certified I3322 amplitude
   cocycle. The old skew product is therefore an exact action on a canonical
   operator filtration, not a packet artifact.

## What is and is not new

The individual ingredients are neighboring established mathematics:
regularized determinants and capacity are central in
[operator scaling](https://arxiv.org/abs/1511.03730), while approximate
operator-algebra representations are used in
[robust game-algebra self-testing](https://arxiv.org/abs/2411.03259) and
[constant-sized unbounded-dimension self-tests](https://arxiv.org/abs/2103.01729).
The general functional-calculus identities in Sprints 1240, 1242, and 1245
should not be advertised as new standalone mathematics.

The I3322-specific assembly is the prospective contribution: its certified
Bellman contact graph, two response correspondences, and nontrivial cocycle
act on one regularized ordered flag. The cited robust-self-testing results do
not directly settle this case: their principal frameworks concern robust game
algebras/approximately tracial states, whereas the I3322 wall is a nontracial
weighted infinite-dimensional attainer and the desired result is a dimension
necessity bound, not uniqueness of a finite ideal strategy.

Operator-scaling capacity is a plausible next instrument because its
log-determinant potential detects shrunk subspaces. No completely positive map
or capacity inequality has yet been derived from the I3322 response
remainders, so that connection remains a registered direction rather than a
theorem.

## Exact remaining gate

Prove or refute a robust finite-order theorem of the form

```text
two approximately transported decreasing soft flags
+ nontrivial logarithmic resolution drift
+ Schmidt rank at most d
=> a response/contact boundary charge depending on d.
```

Only after this is combined with Sprints 1208, 1232, and 1243 can a universal
lower bound on `q_*-Q_d` be restored. The present work changes the architecture
of the open problem; it does not change the public theorem boundary.
