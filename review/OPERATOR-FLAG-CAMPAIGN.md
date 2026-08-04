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
10. **Exact skew action and boundary averaging (Sprints 1250--1251).** The two
    response actions compose with the certified cocycle orientation on the
    event measure.  Averaging logarithmic cuts charges every response boundary
    crossing and supplies a cut with flux `O(d/H)`; no complement is deleted.
11. **Quantitative order coalescence (Sprint 1252).** One-dimensional monotone
    transport converts contact, response, and cut flux into a grid-free bound
    for the retained integral of `|a(u)+u|`.
12. **Order-or-resolution wall (Sprint 1253).** The weighted closure theorem
    gives the pointwise scalar dichotomy

    ```text
    q_*-1/4 <=84|a(u)+u|+(17/10)|log C(u)|.
    ```

    This eliminates the need to identify response-specific Hilbert fibres.
13. **Canonical joint lift (Sprint 1254).** The positive blocks
    `||E_A sqrt(t)D(t+D*D)^-1 F_B||_HS^2` couple the complete Alice and Bob
    event measures exactly.  Near contact, their quadratic order mismatch is
    at most `360 epsilon_0/t^3`.  Multiplicity provenance is now carried by a
    canonical positive object rather than chosen packet targets.
14. **Finite monotone skew flow (Sprint 1255).** A finite decreasing two-flow
    decomposes into paths and fixed points.  Paths pay an endpoint; fixed
    points pay a vertical translation.  For at most `d` source atoms, the
   abstract core-mass bill is explicit and polynomial in `d`.
15. **Charged common-cell descent (Sprint 1256).** Averaging the actual
    canonical joint measure over shifted order grids retains a common-cell
    core.  Every rejected event is billed by the integrated quadratic contact
    defect; no Hilbert vector or unpriced complement is localized.
16. **Stable coarse wall (Sprint 1257).** The sharper quarter-wall coefficients
    survive a common cell with exact diameter tax `41769 h/50`.  At
    `h<=25m_0/41769`, every retained event still owes half the wall margin in
    actual horizontal response displacement or log-resolution translation.
17. **Transport-type collider (Sprint 1258).** Total variation on moving atoms
    is discontinuous, while ordinary joint Wasserstein can swap two nearby
    fibres and erase a fixed vertical debt.  Monotone-fibre transport retains
    the complete ordered-flag address and exactly equals the integrated
    horizontal-plus-vertical response bill.
18. **Synchronized-prefix recovery (Sprint 1259).** Complete cumulative tails
    recover the vertical fibre bill with coefficient `2d`, independent of
    atom spacing and multiplicity.  This isolates one remaining analytic
    receipt: control of synchronized Alice/Bob prefixes on the canonical
    carrier.
19. **Upper-tail commonization (Sprint 1260).** The contact coupling is
    integrable above resolution zero as well as below it. One shifted source
    grid therefore covers every tail queried by the flow, with bill
    `120 epsilon_0[exp(3K)+2]` before Cauchy--Schwarz.
20. **Sign-coherent source cells (Sprint 1261).** Horizontally near-matched
    events have a fixed vertical gap. The certified source width is small
    enough that its sign cannot change inside a cell; horizontally large
    events and their possible cancellation are explicitly billed.
21. **Trace-normalized upper cap (Sprint 1262).** The event mass above `S` is
    at most `exp(-S)`, independent of rank. This prices the upper band
    interface, while logarithmic averaging owns the lower one.
22. **Two-stage address (Sprint 1263).** Independent shifted source/output
    grids buy both addresses with additive first-moment bills. This theorem is
    valid but not by itself sufficient for the response triangle, which needs
    one numerical prefix.
23. **Output-cell sign coherence (Sprint 1264).** The Alice reversal has
    inverse Lipschitz constant `20`; the vertical shift oscillates by at most
    `574 delta` in a common output cell. The registered width therefore
    prevents cross-source cancellation inside one output address.
24. **One-grid correction (Sprint 1265).** One shared grid applied to
    `y,u,a(y),-u` supplies the same prefix before and after both responses,
    losing at most the sum of source-contact and horizontal-response first
    moments divided by the grid width.
25. **One-sided prefix flux (Sprint 1266).** Querying only cuts below the
    selected core boundary makes every exterior contaminant an inbound
    response crosser and every lost core interval an outbound crosser.  The
    resulting boundary bill has coefficient `2B/g`, independent of the number
    of occupied fibres; only the synchronized-prefix discrepancy pays the
    linear rank factor.
26. **Cancellation-preserving localization (Sprint 1267).** Full response
    prefixes are finite-differenced into cell residuals before the common
    carrier is restricted.  The exact four-term telescope then charges every
    address-bad event at most twice at source and twice at output.  Its cost is
    `4W M_bad`, independent of the number of grid cells.
27. **Intrinsic drift-chamber scout (Sprint 1268).** Independent 1601- and
    3201-node Bellman reconstructions find exactly three simple zeros of
    `chi=q-p` in the registered boxes.  Every root is numerically separated
    from horizontal coalescence by more than `1/20`.  This is a numerical
    target, not a theorem; interval zero exclusion is the live gate.
28. **Wrong-chart rejection (Sprint 1269).** A direct shooting reconstruction
    was preregistered as an independent ancestry test and failed five of six
    targets: overlapping charts disagreed by about `0.195`, the composite
    predecessor ceased to be monotone, and eleven apparent roots appeared.
    This reproduces Sprint 1192's warned-against error of propagating a local
    chart forward past its reflection section.  The failed construction and
    its receipt are retained.
29. **Exact reverser and repaired atlas (Sprint 1270).** The shooting map has
    the exact involutory reverser `R(x,y,u)=(-y,-x,1/v)` and satisfies
    `R M R=M^-1`; all three symbolic residuals vanish.  Restricting to the
    certified pre-section charts and their reversible images yields 18 charts
    whose maximum overlap spread is `1.2e-15`, with monotone predecessor and
    the same three roots to the registered tolerance.  The numerical atlas is
    only an ancestry check.  The inactive outer sliver is separately typed by
    Sprint 1217, and interval root exclusion remains open.
30. **Normalization-defect audit (Sprint 1271).** The exact reverser suggested
    `F(x)F(-x)=b(x)^2`, which would collapse the balanced response weights and
    make the drift a raw reflection-section residual.  The preregistered atlas
    guard rejects that identification: chart overlaps agree to `1.2e-15`, but
    the reciprocal residual reaches `8.1e-5` at the origin.  Defining
    `K(x)=F(x)F(-x)/b(x)^2` gives the corrected exact law
    `chi=2 log(uv)-log K(x)-log K(P(x))`.  Thus the missing datum is a
    branch-gluing normalization field, not another root of the local map.

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

The source descent and pointwise coarse wall are now proved.  A direct descent
to the Sprint-1255 total-variation flow is rejected because that topology is
discontinuous under output motion.  The replacement gate is:

```text
canonical Alice--Bob order--resolution coupling
+ controlled off-diagonal contact cost
+ two operator response-rectangle bounds
=> one synchronized-prefix bound on the same ordered carrier
=> controlled monotone-fibre transport.
```

Sprints 1260--1267 now construct the common carrier, remove cellwise
cancellation, prevent the lower response flux from acquiring the prefix rank
factor, and localize the full Sprint-1249 response rectangles without giving
bad addresses a cell-count factor.  The remaining obstruction is quantitative
and explicit: the localization theorem pays the bad-address mass times the
finite cut-window length.  That term contains the horizontal output mismatch
from Sprint 1265 and must be absorbed without forcing a superlinear cut depth.
Until the complete parameter ledger or a bounded-complexity sign partition is
proved and independently replayed, the public theorem boundary is unchanged.

The bounded-complexity option is now concrete: Sprints 1268--1270 predict four
intrinsic drift chambers by two independent numerical constructions, while
the second construction's reversibility is exact.  Certifying exactly three
roots and their horizontal separation would replace the artificial fine grid
by three fixed response prefixes.  No use of the numerical zero census is
permitted in a theorem before the interval certificate lands.  Sprint 1271
also rules out certifying the roots from `uv-1` alone: the interval engine must
carry the normalization defect `K` or evaluate the global Bellman profiles
directly.
