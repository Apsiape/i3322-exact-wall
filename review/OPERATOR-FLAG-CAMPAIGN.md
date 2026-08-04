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
7. **Operator-valued resolution (Sprint 1246).** Without any commutation,
   congruence by a response multiplier replaces scalar resolution `tI` by the
   anisotropic metric `tC^-2`. The scalar log-scale translation is its
   commuting shadow.
8. **Order-resolution event measure (Sprints 1247--1248).** Logarithmically
   differentiating the soft-support filtration produces a positive measure on
   contact order and resolution. Its total mass is exactly Schmidt rank, its
   first vertical moment is the flag-localized log determinant, and every soft
   flag is a rectangle of this one measure. Resolution truncation now exposes
   the missing boundary flux rather than deleting it.
9. **Square-root response transport (Sprint 1249).** A preregistered negative
   control failed: `1/sqrt(t)` stability survived. Self-adjoint dilation then
   proved

   ```text
   ||W_t(M)-W_t(N)||_HS
   <=[3 sqrt(6)/(8 sqrt(t))]||M-N||_HS.
   ```

   Individual response debts therefore control all full event rectangles with
   no Schmidt-basis choice and no response-multiplier norm.

## What is and is not new

The individual ingredients are neighboring established mathematics:
regularized determinants and capacity are central in
[operator scaling](https://arxiv.org/abs/1511.03730), while approximate
operator-algebra representations are used in
[robust game-algebra self-testing](https://arxiv.org/abs/2411.03259) and
[constant-sized unbounded-dimension self-tests](https://arxiv.org/abs/2103.01729).
The general functional-calculus identities in Sprints 1240, 1242, and
1245--1249
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

Prove or refute a robust finite-measure theorem of the form

```text
two controlled response pushforwards of the event measure
+ nontrivial order-resolution skew drift
+ total event mass d and normalized first moment
=> a charged boundary flux depending on d.
```

Only after this is combined with Sprints 1208, 1232, and 1243 can a universal
lower bound on `q_*-Q_d` be restored. The present work changes the architecture
of the open problem; it does not change the public theorem boundary.
