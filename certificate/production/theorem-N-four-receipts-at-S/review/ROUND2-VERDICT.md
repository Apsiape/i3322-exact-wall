# Round-2 referee verdict — Theorem (N), I3322 finite-dimensional nonattainment

Referee: independent, blinded to the authors' working notes. Refutation-first.
Round-1 report by the same referee: `ROUND1-REFEREE-REPORT.md`.

Consulted: `BLIND-SPEC-ROUND2.md`, `REPAIR-CLAIM.md`, `ORIGINAL-PROOF-ROUND1.md`,
`round1_countermodel.py`, and the public repository `i3322-exact-wall` at HEAD —
in particular `certificate/production/foundational-sprint-1198/`
(`FINITE-DIMENSIONAL-NONATTAINMENT.md`, `PRE-REGISTRATION.md`,
`equality_kernel_verify.py`), sprints 1192/1193/1194/1195/1197/1199/1200,
1285/1286/1287/1289/1291/1292/1294/1295, `paper/MANUSCRIPT.md`,
`paper/CERTIFICATE-MAP.md`, `paper/CERTIFICATE-STATUS-ALERT.md`,
`paper/TECHNICAL-SUPPLEMENT.md`, `paper/DIMENSION-GAP-STATUS.md`,
`paper/NORMALIZATION-CONCORDANCE.md`, `README.md`, `review/ADJUDICATION.md`.

Own scripts, written and run in this directory:
`r2_check_algebra.py`, `r2_interface_probe.py`, `r2_critical.py`,
`r2_endpoint_lines.py`.

---

## 0. Overall verdict

**CONDITIONAL.** Two separable questions must not be conflated, and the authors'
own summary conflates them:

1. **Is the sprint-1198 mechanism valid mathematics?** — **YES.** I attacked
   every step named in task 1 and could not break any of them. Given four
   explicitly nameable hypotheses (H1)–(H4) below, Theorem (N) follows, and the
   round-1 countermodel is genuinely excluded. My round-1 verdict "UNSOUND AS
   WRITTEN" is **superseded**: it was a verdict on the restoration document,
   which had replaced this argument with a strictly weaker orbit summary.
   R1, R2, R3 are **DISCHARGED at the level of mechanism**.

2. **Does the repository currently certify (H1)–(H4)?** — **NO. One of four.**
   Only `S > 1/4` is certified at the current common value `S`. The other three
   are certified *nowhere at HEAD, at any value*, because the object they all
   come from — the sprint-1195 globally normalized Bellman fixed point — is the
   object sprint 1285 exactly excludes.

The authors state the interface as "sprint 1198 establishes its mechanism at the
historical certificate value `q_*`, and the repaired theorem must bind those
equations to `S`". **That understates it.** Sprint 1198's own pre-registration
says "the promoted result must use the exact Sprint-1195 Bellman fixed point",
and sprint 1197 — the sole source of 1198's equation (1) — is stamped
"conditional on the validated Bellman fixed-point construction of Sprint 1195".
Sprint 1285 decertified precisely that construction. So the required work is
**not a re-binding of certified equations from `q_*` to `S`; it is a first proof
of those equations at any value at all.**

Consequently Theorem (N) is **not restored**, and the authors are right not to
relabel it. But its status has changed materially: it is now a theorem with a
**short, finite, explicitly enumerable list of missing analytic receipts**,
none of which is the diffuse "prove the support is invariant" of round 1.

---

## 1. Per-obligation verdicts

### R1 — Scalar reduction / operator→scalar licensing: **DISCHARGED**

Round 1 demanded a named commuting family with `R_0, R_A, R_B` functions of it.
The authors' correction (that `R_A, R_B` are decomposable kernels, not scalar
functions) is right, and the actual situation is **cleaner than they claim**:

* `X ⊗ I` and `I ⊗ U` commute (opposite parties). `R_0 = α(X)⊗I + I⊗β(U) − G(X,U)`
  is a genuine function of that commuting pair, and it is `≥ 0`. Hence
  `R_0 ψ = 0` ⟹ `ψ` is supported in the zero set of its symbol
  `q − d(x,u) − A(x) − B(u)`. This is legitimate joint spectral theory, needs no
  Jacobi form, no alignment, no finite dimension. **Round-1 gap (2a) is closed.**
* `R_A` and `R_B` need **not** be functions of the pair, and 1198 never uses
  that. What it uses is the exact substitution
  `Y = 2b(X)J_A` with `J_A := Y·(2b(X))^{-1}` on the spectral subspace `|X| < 1`.
  From the projector relations alone (`X²+Y²=I`, `XY+YX=0`) one gets
  `J_A* = J_A`, `J_A² = I`, `J_A X = −X J_A` — a self-adjoint unitary reversing
  `X`. No Halmos/CS two-projection theorem is even needed for the operator
  identity, only for the intuition. Then
  `R_A = A(X)⊗I − b(X)(J_A ⊗ S_B)` identically, so `R_A ψ = 0` **is** the kernel
  equation (8). Same for `R_B`.
* Round-1's complaint that the word "edge" concedes a Jacobi presupposition is
  answered: the 1198 text never uses an edge; the restoration document did.
* Two round-1 sub-items dissolve rather than needing repair:
  - **Purification is unnecessary.** For a mixed maximizer `ρ`, `Tr(ρR_i)=0` with
    `R_i ≥ 0` gives `R_i ρ = 0`, so every vector in `range(ρ)` is annihilated.
  - **POVM/Naimark** is stated in 1198 §1 and is correct in both of its forms
    (finite local dilation; or "replace each binary effect by an extreme
    maximizer of its linear objective", where extreme effects are projections and
    the global bound forbids the value from rising).

**Sufficiency for every downstream step: yes.** I found no later step that needs
`R_A` to be a function of a commuting operator.

### R2 — Totality of the transport + endpoint-atom exclusion: **DISCHARGED**

This was round 1's decisive gap. It is now genuinely closed, by a mechanism
that is *stronger* than the authors' own description of it.

* **Totality.** From `R_Aψ = 0`, `K_A ψ = r_A(X) ψ` with `r_A = A/b` (division
  licensed because `b(x) ≠ 0` on the occupied set — see interiority). Because
  the support lies in the one-to-one graph `x = P(u)`, the `X = x` spectral
  component of `ψ` is the *whole* occupied component `ψ_+`, and `K_A` maps the
  `X = x` subspace onto the `X = −x` subspace. Projecting gives exactly (10a):
  `K_A ψ_+ = r_A(−P(u)) ψ_{a(u)}`. Since `K_A = J_A ⊗ S_B` is a **self-adjoint
  unitary**, `‖K_A ψ_+‖ = ‖ψ_+‖ ≠ 0`, so the right side is nonzero, so
  `ψ_{a(u)} ≠ 0`. **Totality follows from unitarity alone**; strict positivity
  and finiteness of `r_A` are not needed here (they are needed later, to make
  `ρ ∈ (0,∞)`). The same for `K_B` and `b_map(u) = −u`, and the inverse relations
  give both directions.
* The round-1 countermodel is **excluded**. Its escape was a truncated open chain
  whose two terminal atoms had no transported partner. Under a unitary transport
  that is impossible: the transport coefficient cannot vanish at a terminal atom,
  because there is no coefficient — the unitary itself carries the norm. I could
  not repair the countermodel; every variant I tried has to break either
  unitarity of `K_A` (i.e. `S_B² ≠ I`, i.e. `B_3` not a projection) or
  interiority (i.e. an occupied atom at `x = ±1`).
* **Answering the spec's explicit probes.** Can `r_A` vanish or blow up on an
  occupied contact? `r_A(x) = A(x)/b(x) = √(p(x)F(−x))/b(x)`. On an occupied
  contact `|x| ≤ x_* < 1`, so `b(x) > 0`; and `F > 0` on `[−1,1]` gives
  `0 < r_A < ∞`. Both conditions are consequences of (H1)+(H3), **not** extra
  assumptions — which is the right structure. Can the occupied support fail to
  lie on the contact graph? No: that is `R_0ψ = 0` plus joint spectral theory
  (R1 above), and it is the only place finite dimension is not used.
* **Endpoint exclusion.** Correct, and in fact stronger than 1198 claims. Zero of
  the `R_0` symbol forces equality in *both* Bellman inequalities, hence
  `x = P(u)` **and** `−u = P(−x)`. The second forces `−u ∈ range(P)` as well as
  `x ∈ range(P)`. So the occupied set lies in
  `range(P) ∩ (−range(P))` **in both coordinates** — strictly interior as soon as
  `range(P) ⊆ [−x_*, x_*]`, `x_* < 1`. No branch-wing geometry, no `0/0`
  ceiling, no "released equality audit" import. Round-1's item 7.3 and its
  §8-dependency complaint are both retired.
* **Round-1's "multi-orbit decomposition" worry dissolves.** The argument never
  decomposes into orbits: `Σ` is the *entire* occupied `u`-set of the single
  vector `ψ`, and `a`, `b_map` are bijections of all of `Σ`. One totally ordered
  set, one decreasing bijection, `a = b_map` on all of `Σ`. No additivity lemma
  is needed. (Round-1 item 7.5 withdrawn.)

### R3 — Multiplicity-uniform quarter ceiling: **DISCHARGED**

The authors are right and round 1 was wrong here. The transports are
`K ψ_+ = (scalar) ψ_-` where the scalar is `r_A(−x)`, a *scalar* functional
calculus coefficient, and `K` is unitary between complete fibres of arbitrary
finite rank. Taking norms gives one scalar `ρ = ‖ψ_-‖/‖ψ_+‖` however large the
multiplicity. There is no `m × m` block anywhere. No simple spectrum, no
rank-one transport, no invariant line, no irreducibility is used — so the §3/§4
tension round 1 flagged (irreducibility ⇏ simple spectrum) is also moot.

The **H-hypothesis mismatch flagged in round 1 is resolved in the authors'
favour**: `CERTIFICATE-MAP.md` puts "Finite support reversal", "Amplitude
elimination (6.1)–(6.5)" and "Quarter ceiling (6.6)–(6.8)" in the *main analytic
chain*, owned by sprints 1198/1200, while the "neutral-cycle margin" of sprints
1211–1212 sits in the separate *conditional dimension-necessity campaign*. The
ceiling used is not the neutral-fixed-point ceiling. Round-1 item 7.4 withdrawn.

---

## 2. Line-by-line audit of sprint 1198

Verified independently in `r2_check_algebra.py` (sympy + hostile numerics),
without importing or reading the authors' `equality_kernel_verify.py` result.

| Step | Attack | Result |
|---|---|---|
| §1 projectivization / finite dilation | POVM maximizer ⟹ projective maximizer? value preserved? tensor split preserved? | **SURVIVES** (both routes valid) |
| §1 CS-fibre identities (3) | is `J_A` well defined and unitary without a CS/Halmos decomposition? at `x=0` 1-dim summands with `Y=±1`? at `x=±1`? | **SURVIVES**; `J_A = Y/(2b(X))` on `|X|<1`, the `x=0` summands give `J_A = Y` there, endpoints are excluded downstream anyway |
| §2 contact analysis (4)–(7) | does the symbol zero really force *both* Bellman equalities *and* Cauchy equality? | **SURVIVES**: `A+B ≤ √(PQ) ≤ q−d` with `P,Q ≤ q−d`; equality throughout forces `P = Q = q−d` and the Cauchy tie |
| §2 interiority of every occupied zero pair | can an occupied pair sit at `x=±1` or `u=±1`? | **SURVIVES *given* `range(P)` interior** — and is strictly stronger than stated (both coordinates confined to `range(P) ∩ −range(P)`). Reduces entirely to hypothesis (H3) |
| §3 component equations (10a) | does `K_A ψ_+` land in a *single* `(−x,−u)` component, given `S_B` need not preserve `U`-eigenspaces? | **SURVIVES**: `K_Aψ = r_A(X)ψ` is supported on the graph, and `K_A` maps `X=x` onto `X=−x`; the `u`-coordinate is then forced. This is the step round 1 could not see |
| §3 no-cancellation / injectivity | can two distinct sources cancel? | **SURVIVES** (`P` injective ⟹ distinct `X`-eigenspaces after the flip) |
| §3 unique decreasing bijection (11) | any finite chain with two distinct decreasing bijections? | **SURVIVES** (elementary; re-verified) |
| §4 amplitude elimination (13)–(17) | is (14) *forced* or merely *consistent*? | **SURVIVES and is forced.** From `ρ² = F(−x)/F(x) = F(u)/F(−u)` + Cauchy equality + the two Bellman equalities, the difference of the two Bellman sums factors as `(b_x+b_u)(b_x−ρf_x)(b_x+ρf_x)/(b_x f_x)`; the unique positive root is `f_x = b_x/ρ`. Verified symbolically |
| §4 (16)→(17) elimination of `ρ` | correct root chosen? | **SURVIVES**; residual `= 0` exactly with the positive root |
| §4 ceiling algebra (18)–(20) | identities and the final square | **SURVIVES**; `(b_x+b_u)²+(x−u)²/4 = (1−xu+s_xs_u)/2 ≤ t`, `(1−xu)²−s_x²s_u² = (x−u)²`, `1/4 −(−t+√t) = (√t−1/2)²`. Hostile sweep of 4·10⁶ random `(x,u)`: max `0.24999913 ≤ 1/4` |

**Load-bearingness measurement (new).** To confirm that the finite-closure step
`a = b_map` is not decorative, I removed it: if the partner of `(x,u)` were an
arbitrary other occupied pair `(x',u')` sharing only the norm ratio `ρ`, the two
amplitude equations `q−d(x,u)=ρ(b_x+b_u)`, `q−d(x',u')=(b_{x'}+b_{u'})/ρ`
permit `q` up to **0.30884**. So the entire theorem rests on the closure step,
i.e. round 1 attacked exactly the right place — and the repaired argument now
holds it.

**Conclusion of the line-by-line audit: I could not break sprint 1198.**
Every premise I could satisfy without its conclusion turned out to be
unsatisfiable once unitarity of `K_A, K_B` and interiority were on the table.

---

## 3. THE INTERFACE — receipt list (the decisive deliverable)

The exact hypotheses sprint 1198 consumes, stated at the current common value
`S = ω_tensor = ω_commuting` of sprint 1295:

* **(H1)** a **positive** (continuous) `F : [−1,1] → (0,∞)` with
  `p(x)+F(u) ≤ S − d(x,u)` for all `(x,u)`, giving
  `S·I − B = R_0 + R_A + R_B`, `R_• ≥ 0`, with the 1197 local structure;
* **(H2)** for every `u`, equality in that inequality at a **unique** `x = P(u)`,
  with `P` **strictly increasing**;
* **(H3)** `range(P) ⊆ [−x_*, x_*]` with `x_* < 1` (strict interiority);
* **(H4)** `S > 1/4`.

| Input | Status at `S` | Receipt / missing receipt |
|---|---|---|
| **(i)** `S·I − B = R_0+R_A+R_B ≥ 0` with the 1197 local remainder structure | **NOT CURRENTLY CERTIFIED AT `S`** | The *generic weld* is certified: sprint 1287 `bellman_operator_weld_verify.py` turns **any** positive continuous `g` Bellman-feasible at `q` into exactly this decomposition (product laws `a(x)a(−x)=b(x)²`, `c(u)c(−u)=b(u)²` follow definitionally; `R_A,R_B ≥ 0` follows from them plus `‖B_3−I/2‖≤1/2`). **What is missing is the witness at `q = S`.** Sprint 1295 proves `P = S` where `P` is an **infimum** over positive continuous storages and constructs a feasible `g` only for each `q > S` (with `g ≥ δ = q−S`, §3). **Attainment of that infimum is never proved.** Every certified witness in the repository (1287/1290/1293/1294) is a strict subsolution at `q̂ > S` with certified residual `> 8.89e-7`, hence has **empty contact set** and cannot support any equality-kernel argument. Missing receipt: *"the infimum in 1295 (1) is attained by a positive continuous storage at `q = S`"* (or a limiting-certificate substitute). Sprint 1291 explicitly warns the limiting primal may drive `G(−1) → 0`, which is the precise way this can fail. See §4, finding N7/N8 |
| **(ii)** Bellman equalities with **contact uniqueness** and strictly increasing predecessor `P` | **NOT CURRENTLY CERTIFIED AT `S`** (nor at `q_*`) | The only source is sprints 1192–1194 welded by 1195 §§2–3, whose global amplitude normalization sprint 1285 **exactly excludes** (mismatch enclosed in `[1.4028e-4, 1.7894e-4]`, zero excluded, two independent engines). `CERTIFICATE-MAP.md` marks the "Bellman theorem assembly" row **OPEN**. Sprint 1287's weld advertises that it uses **no contact uniqueness** — so the current upper-bound route deliberately does not produce this object. Additionally, even the historical receipt is weaker than the prose: 1194's own claim boundary yields only `L_x(y) ≥ F(y)` for inactive `|x| > x_*` and records `literal_strict_line_derivative_test: false`, while supplement S9(4) says "every other `x` lies **strictly** above the tangent contact" and 1200 §A says "every inactive outer predecessor is excluded". **A tie at an inactive `x` destroys the graph property that (10a) and `a(u)=P^{-1}(−P(u))` require.** Missing receipts: (a) existence of the contact structure for the storage of (i) at `S`; (b) *strict* inactive exclusion |
| **(iii)** `range(P)` strictly interior | **NOT CURRENTLY CERTIFIED AT `S`** | Same provenance (1195 §3: `x_* = 0.898116482394039`, supplement S8; left wing "by reflection"), hence same decertification. **Worse: this hypothesis is not even in the manuscript's own stipulated input.** The "Certified Bellman proposition" (`MANUSCRIPT.md` §2) states `P : [−1,1] → [−1,1]` — no interiority — yet §5 silently works "on the occupied interior support". Missing receipt: *`range(P) ⊆ [−x_*,x_*]`, `x_* < 1`, for the storage of (i) at `S`*. See finding N2 for a clean equivalent form that makes this cheap to certify |
| **(iv)** `S > 1/4` | **CURRENTLY CERTIFIED AT `S`** | Sprint 1292 `exact_dimension_255_lower_bound.py` (exact rational profile/state, certified rational square-root floors) gives `ω_tensor > 0.2508753845015185`, independently reconstructed at 160-digit interval precision in `certificate/independent/dimension-255/`; sprint 1295 gives `ω_tensor = ω_commuting = S`. Hence `S > 1/4` unconditionally. Normalization concordance (`NORMALIZATION-CONCORDANCE.md`, Pál–Vértesi Eqs. (9)–(14)) confirms the `1/4` in (20) is in the same normalization |

**Score: 1 of 4 certified.** The three that are missing are all the *same*
object — a critical (not near-critical) Bellman storage at `S` together with its
contact geometry — which the repository currently does not have at any value.

---

## 4. New findings (neither round named these)

**N1 — the manuscript's stipulated input is incomplete.** The "Certified Bellman
proposition" omits interiority of `range(P)`, which §5 then uses. Even granting
the whole computer-assisted layer, the analytic chain as written has a hole.
Repair: add (H3) to the proposition.

**N2 — interiority has a clean, cheap equivalent form (previously unnamed).**
The Bellman operator is a lower envelope of the affine family
`L_x(u) = c(x) + m(x)·u` with `c(x) = q+1−x/2−b(x)²/F(x)` and
`m(x) = 1/2 − x`. The two endpoint predecessors give **explicit** lines with no
`F`-dependence at all (because `b(±1)=0`):
```
L_{+1}(u) = q + 1/2 − u/2,        L_{−1}(u) = q + 3/2 + 3u/2.
```
Therefore **`range(P)` is strictly interior ⟺ `F(u) < L_{+1}(u)` and
`F(u) < L_{−1}(u)` strictly on `[−1,1]`.** Sprint 1195 (5) derives only the
*non-strict* cap `F(y) ≤ q_* + (1−y)/2` from `x = 1`, and derives nothing at all
from `x = −1`. Certifying two strict scalar inequalities against two explicit
lines is far cheaper than the wing-geometry route, and my numerics say the
margins are comfortable (below).

**N3 — `P`'s monotonicity is free; only strictness and uniqueness need a
certificate.** In the same envelope picture the slope `m(x) = 1/2 − x` is
strictly decreasing in `x`, so the argmin of a lower envelope of these lines is
**automatically non-decreasing in `u`**. The 32,768-tile Arb certificates of
sprints 1192/1193 are therefore not needed for monotonicity — only for
*single-valuedness* and *strictness*. This narrows what has to be re-proved
after 1285.

**N4 — independent corroboration of the window, with no shooting chart.**
`r2_critical.py` runs min-plus value iteration of `T_q` directly on a grid and
bisects for the critical level:

| grid `N` | grid-critical `q` |
|---:|---|
| 1001 | 0.250874963317… |
| 2001 | 0.250875245499… |
| 4001 | 0.250875299607… |

increasing toward the certified window `[0.2508753845015185, 0.250875388108398]`
from below, as a grid restriction of the minimisation should. This is a genuinely
independent (non-Arb, non-shooting) sanity check that the Bellman critical level
and the certified value agree — and, importantly, that a **positive** critical
storage exists numerically.

**N5 — (H1) looks closable, and here is the missing lemma.** Numerically the
critical storage is strictly positive everywhere including the endpoints
(`min F ≈ 5.3008e-2` at `x=−1`, `F(+1) ≈ 2.1048e-1`, stable over
`N = 1001…8001`). Analytically, the following short argument closes (i) on the
open interval and is *not* in the repository:

> Let `g_q` be the sprint-1295 storage (7) at level `q > S`. The pivot recursion
> is monotone in `q`, so `g_q` is non-decreasing in `q`; set
> `g_S := lim_{q↓S} g_q ≥ 0`. All terminal pivots have the form
> `const(history,i) − d(i,j)`, so the family has one uniform modulus of
> continuity in `j` (1295 §4), which passes to the limit; hence `g_S ∈ C[−1,1]`.
> **Positivity on `(−1,1)`:** suppose `g_S(i_0) = 0` with `b(i_0) > 0`. Pick
> `q_n ↓ S` with `g_{q_n}(i_0) → 0`. Feasibility (8) at `q_n` gives, for any `j`,
> `g_{q_n}(j) ≤ q_n − d(i_0,j) − b(i_0)²/g_{q_n}(i_0) → −∞`, contradicting
> `g_{q_n} ≥ q_n − S > 0`. Hence `g_S > 0` on `(−1,1)`, and feasibility at `S`
> passes to the limit wherever `g_S > 0`.

What this argument does **not** deliver is the two endpoints, where `b(±1) = 0`
makes `b²/g` a `0/0` limit and where sprint 1291 explicitly warns that "an
optimal limiting primal may drive `G(−1)` to zero". So (i)'s missing receipt
reduces to a **boundary-layer statement**: `g_S(±1) > 0`, or a proof that
`b(x)²/g_S(x) → 0` as `x → ±1`. That is a genuinely small, well-posed target,
and it is the single highest-value next step.

**N6 — interiority is numerically robust with a large margin.**
`r2_endpoint_lines.py`, at the window midpoint:

| `N` | `range(P)` | `min(L_{+1} − F)` | `min(L_{−1} − F)` | `min F` |
|---:|---|---|---|---|
| 2001 | `[−0.894000, +0.898000]` | `4.0398e-2` (at `u=+1`) | `1.9786e-1` (at `u=−1`) | `5.3012e-2` |
| 4001 | `[−0.893500, +0.898000]` | `4.0399e-2` | `1.9787e-1` | `5.3008e-2` |
| 8001 | `[−0.893750, +0.898000]` | `4.0399e-2` | `1.9787e-1` | `5.3005e-2` |

So (H3) is not in danger of being *false*; it is merely uncertified, and N2 gives
a cheap route to certifying it.

**N7 — a live discrepancy in the historical left wing (new, and it points at the
same reflection step 1285 killed).** My independently computed active-predecessor
range is **asymmetric**: `≈ [−0.8937, +0.898]`. The right endpoint agrees with
the repository's `x_* = 0.898116482394039` (supplement S8). The **left** endpoint
does **not**: the repository obtains the left wing "by reflection" and places it
at `−0.898116…`, whereas four independent grid resolutions
(`Δ = 2e-3, 1e-3, 5e-4, 2.5e-4`) give `−0.8940, −0.8940, −0.8935, −0.89375`, a
discrepancy of `≈ 4.4e-3` — an order of magnitude above the grid spacing and
stable under refinement. This
matters because **there is no exact reflection symmetry available here**: sprint
1197 §2 itself notes that the naive reflection identity `F(x)F(−x) = b(x)²` is
false ("the endpoint wings disprove it"), and sprint 1285's decertification is
literally a *reflected source/target amplitude* mismatch. My numerics are
suggestive, not decisive (my `F` is a grid value-iteration fixed point at the
window midpoint, not a certified object), but the "reflection supplies the left
wing" step in sprints 1192/1193/1195 should be **re-derived, not reflected**,
before it is reused. I record this as the strongest new independent signal in
this audit.

**N8 — the structural defect `K(x) = F(x)F(−x)/b(x)²` is `≥ 1`, with equality on
the whole central region.** Measured over `|x| < 0.95`: `min K = 1.000000`,
`max K ≈ 1.1536`, with `≈ 93%` of grid points at `|K − 1| < 1e-3`. Sprint 1198's
(14) *derives* `F(x)F(−x) = b_x²` (i.e. `K = 1`) at any occupied pair. Two
consequences worth recording: (a) this is a *derived* local identity, not the
globally false shortcut, so there is no internal contradiction with 1197 §2 —
round 2 clears that suspicion; (b) because `K = 1` holds on a large region, one
cannot hope to get nonattainment cheaply from `K ≠ 1`; the quarter-ceiling route
is doing real work.

**N9 — decertified material silently upstream of 1198 (task 4).** Yes, and more
than the authors acknowledge:
`1198 (1)` **is** `1197 (12)`, whose status line reads "conditional on the
validated Bellman fixed-point construction of Sprint 1195"; `1195 §§2–3` is the
"Bellman theorem assembly" row that `CERTIFICATE-MAP.md` marks **OPEN after
Sprint 1285**; `1192`'s own receipt says "Global Bellman minimality is
separate"; `1198`'s pre-registration mandates the 1195 fixed point by name. So
`1198` is not "valid at `q_*` and needing transport to `S`" — it is currently
valid at **no** certified value. Sprint 1199 (commuting) and 1206 (spatial
witness) inherit the same defect. The `1285` list in
`CERTIFICATE-STATUS-ALERT.md` already names nonattainment as decertified; the
repair claim does not engage with the fact that this decertification hits the
*mechanism*, not just the *value*.

**N10 — normalization.** Round 1's framing correction stands and is already
correct in the repository (`MANUSCRIPT.md`: "Its classical bound is 0. Qubit
strategies attain 1/4"). The authors' restated convention (classical `= 0`,
`1/4 =` qubit / common-return ceiling) is right. Literature agrees the qubit
maximum is `1/4` and that the Pál–Vértesi conjecture is open, so Theorem (N)
would be a genuinely new result — which is exactly why the receipt list must be
complete before it is claimed.

---

## 5. Ranked remaining weakest points

1. **Existence of a critical positive storage at `S`** (interface (i)). Without
   it there is no certificate to annihilate and nothing downstream has meaning.
   Closable on `(−1,1)` by the short limit argument in N5; the residual is the
   **endpoint boundary layer** (`g_S(±1) > 0`, or `b²/g_S → 0` at `±1`), which
   sprint 1291 independently flags as the plausible failure mode.
2. **Contact uniqueness at `S`** (interface (ii)). No receipt exists at HEAD at
   any value; the historical one is inside the decertified 1195 weld, and even
   there the inactive exclusion is certified only non-strictly (1194's own
   claim boundary and `literal_strict_line_derivative_test: false`) while the
   supplement and the 1200 audit both assert strictness. Two separate repairs
   are needed: existence of the contact geometry at `S`, and strictness.
3. **Strict interiority of `range(P)` at `S`** (interface (iii)). Not in the
   manuscript's own proposition; numerically safe with margin `4.0e-2`;
   reducible by N2 to two strict inequalities against two *explicit* lines.
4. **The reflected left wing** (N7). An independent `4.6e-3` discrepancy against
   the repository's `−x_*`, sitting on exactly the reflection step whose global
   normalization sprint 1285 exactly excluded. Must be re-derived rather than
   reflected. If the true active range is genuinely asymmetric, several
   downstream statements phrased as `[−x_*, x_*]` need restating (they remain
   *interior*, so Theorem (N)'s mechanism is unaffected — but the certificates
   are not).
5. **Strictness of `P`** as opposed to monotonicity (N3). Needed for injectivity
   of `P`, hence for "a member of `Σ` identifies the complete occupied pair".
   Cheap relative to 1–4, but currently bundled inside the decertified tile
   certificates.

---

## 6. What would change my verdict to RESTORED

Exactly the four receipts of §3, at `S`, in this order of difficulty:

1. (H1) a positive continuous storage feasible at `S` — attainment of the
   sprint-1295 infimum, plus the endpoint boundary layer (N5 does the interior);
2. (H3) strict separation of that storage from `L_{+1}` and `L_{−1}` (N2);
3. (H2) single-valuedness and strict increase of its contact argmin, with the
   inactive exclusion proved **strictly**;
4. (H4) — already held.

Given those four, sprint 1198's argument as written is, in my judgement, a
correct proof of Theorem (N) for an arbitrary finite-dimensional maximizer
(mixed or pure, POVM or projective, any multiplicity), and the round-1
countermodel is dead. Nothing further about representation, alignment,
irreducibility, or orbit structure is required.

---

## 7. Reproduction

```
python r2_check_algebra.py      # symbolic audit of 1198 (13)-(20) + load-bearingness
python r2_interface_probe.py    # min-plus Bellman scout, contact structure vs q
python r2_critical.py           # grid-critical level, F>0, range(P), K(x)
python r2_endpoint_lines.py     # the two explicit endpoint lines and their margins
```
