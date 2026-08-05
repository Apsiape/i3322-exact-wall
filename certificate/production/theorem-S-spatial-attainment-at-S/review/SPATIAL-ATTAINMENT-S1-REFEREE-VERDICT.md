# Referee verdict S1 — spatial attainment at the current `S` by scalar-orbit extraction

Referee: independent, blinded to the authors' working notes. Refutation-first.
Prior report by the same referee: `THEOREM-N-ROUND3-VERDICT.md` (nonattainment,
promoted).

Consulted: `candidate/` (all four documents, both artifacts) and the public
repository `i3322-exact-wall` — `certificate/production/theorem-N-four-receipts-at-S/`
(assembly, zero-set reduction, convex-envelope completion), and sprints 1195,
1197, 1198, 1206, 1285, 1287, 1292, 1294, 1295.

Own scripts, written and run here (nothing imported from the authors' code):
`s1_carrier.py`, `s1_geom.py`, `s1_orbit.py`, `s1_tail.py`, `s1_fixed.py`,
`s1_final.py`. The authors' two candidate artifacts were run by me; Sprint
1206's `spatial_realization_verify.py` was run in a **copy** (`repocopy/`) so
that the public repository was not modified.

---

## 0. Overall verdict

**PROMOTE — conditional on five mandatory repairs (V1–V6 below), two of which
(V1, V2) are genuine holes in the written proof rather than prose. I supply the
complete repair for each and have verified them.**

**The primary question of this assignment answers in the negative: nothing
decertified re-enters.** The Sprint-1195 bi-infinite profile, its `ℓ²` tail, and
its eigen-equation — the three objects Sprint 1206's own guard names as
"analytic inputs from Sprint 1195" — are each independently reconstructed, and
the global amplitude-compatibility equation whose failure decertified the old
route (Sprint 1285) is **dissolved rather than re-solved**. That dissolution is
the load-bearing novelty of this candidate and it is sound:

> Sprint 1195 had to **construct** an amplitude vector from the two response
> cocycles and then check that the construction closed; on an orbit where the
> reflection identifies two indices, that check is an equation, and it failed by
> more than `1.4e-4`. The candidate never constructs the amplitudes. It reads
> them off the masses `μ_t({u_n})`, `μ_t({-u_n})` of a conditional measure that
> **already exists**, and *derives* the cocycle. Consistency is then automatic,
> and `λ ∈ ℓ²` is automatic too, because a conditional measure of a
> disintegration is a probability measure on a countable orbit. No normalisation
> equation is ever posed, hence none can fail.

I attacked every gate and could not break the theorem. Three independent
consistency checks that had no obligation to succeed did succeed (§7 below), the
sharpest being that the amplitude ratio `r_B` measured at the two ends of the
reconstructed contact set has **exactly** the two signs that `ℓ²` summability
requires (`r_B(α)=0.9276<1<1.0768=r_B(β)`, per-step decay `0.86`), so the decay
that Sprint 1195 asserted is real and is here a theorem rather than an input.

---

## Gate 1 — GNS limit passage — **DISCHARGED, after V2**

* **Is `R_A = A(X) − b(X)K_A` positive in the certified weld form, and is
  `A ≥ b` needed?** No, `A ≥ b` is neither true nor needed. The certified object
  is 1197 (9), `R_A = t_A I − α(X) − Y(B_3 − I/2)`, i.e. `R_A = A(X) − W` with
  `W := Y(B_3 − I/2)`. I give an operator proof that needs no CS fibration and
  no endpoint care:

  > `W² = Y²(B_3−I/2)² = (I−X²)/4 = b(X)²` and `WX = −XW`, hence
  > `Wf(X) = f(−X)W`. Put `T = A(X) − W`, `T' = A(−X) + W`. The product law
  > `A(x)A(−x) = b(x)²` gives `TT' = T'T = 0`, and `T + T' = A(X) + A(−X) =: D ⪰ 0`
  > commutes with `T` with `T² = TD`. On the joint spectrum `t(t−d)=0` with
  > `d ≥ 0`, so `t ≥ 0`. **`R_A ⪰ 0`.**

  The product law holds *exactly* at every `n`:
  `A_n(x)A_n(−x) = √(p_n(x)g_n(−x)p_n(−x)g_n(x)) = b(x)²`, independently of any
  property of `g_n` beyond positivity — and `g_n ≥ q_n − S > 0` on all of
  `[−1,1]` (1295 §3), so `A_n, B_n` are continuous on the **closed** interval and
  `A_n(±1) = B_n(±1) = 0`. Verified numerically to `1.1e-16` (`s1_geom.py`).

* **Uniform norm bound.** `A_n(x) ≤ (p_n(x)+g_n(−x))/2 ≤ (q_n − d(x,−x))/2 ≤ (q_n+3)/2`
  by Bellman feasibility at the reflected target, and likewise
  `B_n(u) ≤ (q_n − d(−u,u))/2` by the second Bellman inequality. So
  `sup_n ‖R_{A,n}‖ < ∞`. Correct as written.

* **`‖R_nΩ‖² ≤ ‖R_n‖⟨Ω,R_nΩ⟩ → 0`.** Correct: `R² ⪯ ‖R‖R` for `R ⪰ 0`, and
  `Σ_ν⟨Ω,R_{ν,n}Ω⟩ = q_n − ω_*(𝓑) = q_n − S → 0` with each term `≥ 0`. **No
  finite-dimensionality and no spectral cut-off is used** — this is precisely the
  step where Theorem (N)'s Receipt (i) had to say "because `ρ` is
  finite-dimensional, choose `c<1`", and the substitution is legitimate.

* **Fatou for the scalar remainder.** Correct. `φ_n ≥ 0`, `φ_n → φ` pointwise on
  `(−1,1)²` (uniform `g_n → g` plus interior positivity), `∫φ_n dμ ≤ q_n − S → 0`,
  so `∫φ dμ ≤ liminf ∫φ_n dμ = 0` and `φ = 0` `μ`-a.e.

* **Endpoint-atom exclusion transferred to the GNS spectral measures.** Correct
  and, unlike the Theorem-(N) version, state-independent: Receipt (iii) gives
  `φ_n ≥ m_±/2 > 0` uniformly for `q_n ≤ S_+` on `{x=±1} ∪ {u=±1}`, so
  `(m/2)·μ(E) ≤ ∫φ_n dμ → 0` forces `μ(E) = 0` for **any** state.

* **`A_n(X)Ω → A(X)Ω`.** Correct by dominated convergence
  (`|A_n| ≤ C`, `A_n → A` `μ_X`-a.e. since `μ_X({±1}) = 0`). One point the text
  must make explicit: `A_n(±1) = 0` for every `n`, while
  `lim_{x→±1} A(x)` may be strictly positive. `A` is therefore the *interior*
  limit and is generally **discontinuous** at `±1`; this is harmless (the
  endpoints are `μ_X`-null) but it must be said, because a reader who assumes
  `A` continuous will wrongly conclude from Receipt (iii) that the zero locus is
  compactly contained in the open square.

* **Existence of the maximizing commuting state.** Correct and cheap:
  the state space of the universal commuting `C*`-algebra is weak-`*` compact and
  `ω ↦ ω(𝓑)` is weak-`*` continuous. Note the asymmetry with Theorem (N) which
  is worth stating in the paper: Theorem (N) *assumes* a maximizer for
  contradiction, this proof *has* one, and it is exactly this that makes the
  zero locus nonempty.

**Repair required: V2.** `K_A = J_A ⊗ S_B` with `J_A = Y/(2b(X))` **need not
exist** on the GNS space. The `C*`-algebra of two projections decomposes `H_A`
into two-dimensional fibres plus four commuting corners; on the corners
`A_1 = A_2 = I` and `A_1 = A_2 = 0` one has `Y = 0`, and a self-adjoint unitary
anticommuting with `X` must carry the `X = +1` eigenspace onto the `X = −1`
eigenspace — impossible when their multiplicities differ (e.g.
`A_1 = A_2 = diag(1,1,0)` on `ℂ³`). Compressing by `1_{(−1,1)}(X)` does not fix
this, because that projection does not commute with `S_B`. **The boxed identities
`R_{A,n} = A_n(X) − b(X)K_A` and `K_AΩ = r_A(X)Ω` are therefore not licensed as
written, and "all divisions occur `μ`-a.e. in the endpoint-free interior" is not
an argument** (it does not establish that `r_A(X)Ω` is even a vector, i.e. that
`∫r_A² dμ_X < ∞`).

**The repair — use `W`, never `K_A`.** `A(X)Ω = WΩ` is what the limit actually
gives. Then for every bounded Borel `f`,

```
⟨WΩ, f(X)WΩ⟩ = ⟨Ω, W f(X) W Ω⟩ = ⟨Ω, b(X)² f(−X) Ω⟩ = ∫ b(x)² f(−x) dμ_X ,
⟨WΩ, f(X)WΩ⟩ = ⟨A(X)Ω, f(X)A(X)Ω⟩            = ∫ A(x)² f(x)  dμ_X ,
```

an exact identity with no division, no `K_A`, and no CS decomposition. Taking
`f` supported in a compact subset of `(−1,1)` and dividing the *scalar integrand*
by `b²` gives §5's law directly, and monotone convergence extends it (`μ_X`
gives no mass to `±1`). Everything downstream is unchanged. The same substitution
with `W_B := (A_3 − I/2)V` (`W_B² = b(U)²`, `W_BU = −UW_B`) handles `R_B`.

---

## Gate 2 — Radon–Nikodym orientation — **DISCHARGED**

I checked both orientations explicitly and the document's is the correct one.

* `(−id)_*μ_X = r_A²·μ_X` means `∫f(−x)dμ_X = ∫f(x)r_A(x)²dμ_X`. This is what
  the `W`-computation above yields. The inverted convention
  `(−id)_*μ_X = r_A^{−2}μ_X` is refuted by the two-fold consistency test:
  applying the law twice returns `μ_X` iff `r_A(x)r_A(−x) = 1`, which is the
  exact identity `A(x)A(−x)=b(x)²` — it holds in the document's orientation and
  fails in the inverted one.
* The three product identities are exact and require **no** zero-locus
  membership: `r_A(t)r_A(−t) = 1`, `r_B(t)r_B(−t) = 1`, and
  `r_A(t)r_B(t) = A(t)B(t)/b(t)² = 1` since `A(t)B(t) = √(p(t)p(−t)g(t)g(−t)) = b(t)²`.
  Reproduced numerically to `1.0e-13` (`s1_geom.py`).
* The transfer to §6's `μ_U`-form is correct. Using `μ_X = P_*μ_U` (legitimate
  because `μ` is carried by the graph) and `P(a(u)) = −P(u)`, the test function
  `f = 1_{P(E)}` gives `μ_U(aE) = ∫_E r_A(P(u))² dμ_U` — density evaluated at
  `u`, not at `a(u)`, exactly as boxed. Self-consistency: applying twice gives
  `r_A(P(u))·r_A(P(a(u))) = r_A(x)r_A(−x) = 1`. ✔
* **The orientation is load-bearing, and I confirmed it is.** With the inverted
  law the amplitude ratio becomes `λ_{j+1}/λ_j = 1/r_B(c_j)` and the Jacobi
  quotient becomes `d(c_{j−1},c_j) + p(c_j) + g(c_{j−1})` — the Bellman
  functional with source and target exchanged, which is not `S`. Measured
  numerically on the reconstructed storage: correct orientation gives an
  interior eigen-residual `1.2e-5` and Rayleigh quotient tracking `q`; the
  flipped orientation gives residual `2.1e-2` and Rayleigh quotient `0.208`
  (`s1_orbit.py`). A silent inversion would have been caught.

---

## Gate 3 — Borel transversal and disintegration — **DISCHARGED, after V3**

* **Measurability on the actual support.** `Z = {φ = 0} ∩ (−1,1)²` is relatively
  closed, hence σ-compact, hence `Y = π_2(Z)` is Borel and `P` — monotone with
  closed graph — is Borel. Fine.
* **The transversal.** The construction is correct. For `u ∈ Y_+` the orbit
  `τ^n(u)` is strictly increasing (τ is increasing — see V4), `α < β` strictly,
  `α, β` are orbit invariants and Borel, the first-rational choice `q(u)` is
  Borel and orbit-constant, and because the orbit is strictly monotone with
  `inf = α < q < β = sup` there is exactly one `n` with
  `τ^n(u) ≤ q < τ^{n+1}(u)`. So `D_+` meets each increasing orbit once. The
  reflection acts on `τ`-orbits by `bτb = τ^{-1}`, so `b` preserves `Y_+`; the
  induced map on `D_+` is `r∘b` with `r` the (Borel) representative selector, and
  "lesser of the two representatives" gives a transversal for the full
  infinite-dihedral relation. Smoothness follows.
* **Fibrewise inheritance.** Correct, and the normalisation step should be
  written out (V7): `b` preserves fibres so `π∘b = π` and `b_*μ_U` disintegrates
  over the *same* base measure `ν` with conditionals `b_*μ_t`; comparing with
  `r_B²μ_U`, whose base density is `c(t) = ∫r_B²dμ_t`, uniqueness forces
  `c ≡ 1` and `b_*μ_t = r_B²μ_t` for `ν`-a.e. `t`. Same for `a`.
* **Atomicity.** The conditionals are supported on countable orbits, hence purely
  atomic with total mass 1 — this is the structural pivot of the whole proof and
  the document should say so in one sentence. It is also what makes `φ = 0`
  `μ`-a.e. usable pointwise: `μ(N) = 0` gives `μ_t(N) = 0` for `ν`-a.e. `t`, and
  an atomic measure that gives `N` mass zero has **no atom in `N`**, so every
  point of the selected orbit is genuinely on the zero locus.
* **Support is the whole orbit.** Correct: positivity and finiteness of the
  transport densities on `(−1,1)` (interior positivity of `g`) propagate positive
  mass along the orbit.

**Repair required: V3.** `a(u) = P^{-1}(−P(u))` requires `−P(u) ∈ range(P)`, i.e.
`P(u) ∈ Y`. The dual-tie involution gives only `range(P) = −Y`; it does **not**
give `range(P) = Y`, so `a` is *not* defined on all of `Y`, and §6 defines it as
if it were. The repair is §5's own content: `(−id)_*μ_X ∼ μ_X` (both densities
`r_A^{±2}` are positive and finite on the interior), so `μ_X`-a.e. `x` has
`−x ∈ range(P)`; intersecting the countably many conull sets indexed by the
(countable) group `D_∞` produces a Borel, `a`- and `b`-invariant, `μ_U`-conull
set `Y_0 ⊆ Y` on which the whole action is defined. Every later statement must be
read on `Y_0`. Routine, but it must be written, because the naive reading is false.

---

## Gate 4 — interleaving and Jacobi indexing — **DISCHARGED, after V4/V5**

I checked the index conventions ruthlessly and they are right.

* **`P(c_{j+1}) = c_j` for every `j`.** Even `j = 2n`: `P(−P(−u_n)) = u_n` by the
  dual-zero involution at `−u_n`. Odd `j = 2n+1`: `u_{n+1} = τ(u_n) = a(−u_n) = P^{-1}(−P(−u_n))`,
  so `P(u_{n+1}) = −P(−u_n) = c_{2n+1}`. Both exact. Equivalently
  `c_{2n+1} = P(u_{n+1})`, so every label is simultaneously a full-zero **target**
  and a full-zero **source**, which is what makes the alternation coherent.
* **Every adjacent pair is a full-zero pair,** hence carries the Bellman
  *equality* — this is the substance of gate 5's sub-question about zero-locus
  membership of the disintegrated orbit. It holds because (i) the even labels are
  atoms of `μ_t`, hence in `Y`; (ii) the odd labels are in `Y` by the involution
  `−P(Y) ⊆ Y`; (iii) `Z` is the graph of `P`.
* **The ratio law.** Verified in both directions.
  `λ̃_{2n+1}/λ̃_{2n} = r_B(u_n) = r_B(c_{2n})` from `b_*μ_t = r_B²μ_t`. For the
  odd step, `a(u_{n+1}) = −u_n`, so `a_*μ_t = r_A(P(·))²μ_t` at `{u_{n+1}}` gives
  `μ_t({−u_n}) = r_A(c_{2n+1})²μ_t({u_{n+1}})`, hence
  `λ̃_{2n+2}/λ̃_{2n+1} = 1/r_A(c_{2n+1}) = r_B(c_{2n+1})` by `r_Ar_B = 1`. The
  document's alternative route via `r_A(P(−u_n)) = r_B(−P(−u_n))` gives the same
  number by `r_A(t)r_A(−t)=1`. Uniform in `j`. ✔
* **`1 ≤ Σλ̃² ≤ 2`.** Correct. The full response orbit is `{u_n} ∪ {−u_n}`
  (`bτ^n = τ^{-n}b`), the `u_n` are pairwise distinct, and the two `τ`-orbits are
  disjoint (sum `= 1`) or identical (sum `= 2`). **`λ ∈ ℓ²` is therefore free.**
  This is the exact point at which the decertified route needed a global
  normalisation equation, and it is gone.
* **Jacobi convention.** `H_{jj} = d(c_{j−1},c_j)`, `H_{j−1,j} = b(c_{j−1})` is
  Sprint 1206's convention under `ĉ_j = c_{j−1}`, and I verified in exact rational
  arithmetic that the shift is genuinely harmless — see gate 5.
* **The recurrence.** `(Hλ)_j/λ_j = b(c_{j−1})²/g(c_{j−1}) + d(c_{j−1},c_j) + g(c_j)
  = p(c_{j−1}) + d(c_{j−1},c_j) + g(c_j) = S`, the last step being the first
  Bellman equality at the full-zero pair `(c_{j−1}, c_j)` with `c_{j−1}` in the
  **source** slot — which matches 1295 §2's placement convention exactly. `H` is
  bounded, so `Hλ = Sλ` holds in `ℓ²`. ✔

**Repair required: V4.** The document never states that `τ = a∘b` is
**increasing** (a composition of two decreasing maps). This is needed three
times: to rule out periodic orbits of period `> 1` (an increasing injection has
no non-fixed periodic points, so "finite orbit" = "fixed point"); to make §7's
`Y_±` unions of orbits; and to make the `u_n` distinct in §9.

**Repair required: V5.** §10 asserts "on the full-zero locus, `K(t) = 1`, so
`B(t) = g(t)`" and applies it at **every** label. Two one-line facts are needed
and missing: (i) the odd labels `−P(−u_n)` are themselves full-zero *targets*
(the involution again); (ii) `K(t) = 1 ⟺ g(t)g(−t) = b(t)²` is invariant under
`t ↦ −t`, so `K(x) = 1` at a source transfers to `−x`. Without (i)–(ii),
`r_B(c_j) = g(c_j)/b(c_j)` is only justified at half the labels.

---

## Gate 5 — the finite-to-infinite extension — **DISCHARGED, after V6. Nothing decertified re-enters.**

This was the primary target. My conclusion is that the extension is clean, but
the citation is not.

* **What the limit argument needs, exactly.** `λ ∈ ℓ²` with `Hλ = Sλ`, the six
  operators bounded, and absolute convergence of
  `⟨ψ, M⊗N ψ⟩ = Σ_{r,s} λ_rλ_s M_{rs}N_{rs}` for two-banded `M, N`. The diagonal
  sums are dominated by `Σλ_j²` and the neighbour sums by Cauchy–Schwarz, so the
  finite block identity passes to `ψ_S` term by term with no limit-exchange
  hypothesis. This is Sprint 1206 §3 and it is sound.
* **Which finite identity is available.** Two different statements live in the
  repository and they must not be conflated. Sprint 1295 §5 proves the **open**
  Pál–Vértesi word identity — endpoints `1, −1`, odd carrier, padding — and that
  identity's hypotheses do **not** hold for the interleaved labels `c_j`, which
  are an arbitrary bi-infinite word in `(−1,1)` with no endpoints. What the
  candidate needs is the **no-endpoint alternating** identity, which exists as
  the `cyclic_blocks`/`cyclic_jacobi_score` fixture of
  `foundational-sprint-1206/spatial_realization_verify.py`. That fixture is the
  right one and it passes (I ran it in `repocopy/`: 24 fixtures, 12 open + 12
  cyclic, `all_gates_pass: true`).
* **I replicated it independently** (`s1_carrier.py`, exact `Fraction`
  arithmetic, 60 cyclic fixtures at `n = 4,6,8,10,12`, random rational cosine
  labels and random rational amplitudes), building the Bell operator from the
  **Sprint-1197 reparameterisation** `𝓑 = XU + X/2 − U/2 − I + Y(B_3−I/2) + (A_3−I/2)V`
  rather than from the Collins–Gisin coefficient list. Results: all six blocks
  are exact projections; the 1197 value equals the Collins–Gisin value exactly
  (an independent cross-check of the two functional presentations); and both
  equal `Σ_j d(c_j,c_{j+1})λ_j² + Σ_j √(1−c_j²)λ_{j−1}λ_j` exactly.
* **The "harmless global index shift" is genuinely harmless, and I found the
  reason.** The identity holds for **both** assignments of the alternating
  matchings to Alice and Bob (verified for both parities, 60/60 fixtures),
  whereas the source/target orientation is **not** free — the swapped diagonal
  `d(c_{j+1},c_j)` fails on every fixture. The parity-blindness is an exact
  symmetry of the functional: exchanging the matchings sends
  `X ↦ −U, U ↦ −X, Y ↦ V, V ↦ Y, A_3 ↔ B_3` (because `P_B^±(t) = P_A^±(−t)`),
  under which `𝓑` is invariant term by term. This should be recorded, since it is
  what licenses the shift.
* **Does any Sprint-1195 input re-enter? No.** Sprint 1206's guard states its own
  boundary: "the certified bi-infinite profile, `ℓ²` tail, and eigen-equation
  remain analytic inputs from Sprint 1195". The candidate replaces all three:
  the profile by the interleaved orbit `c_j`, the `ℓ²` tail by
  `Σλ̃² ≤ 2`, and the eigen-equation by the Bellman contact equality along the
  orbit. Only §§2–4 of 1206 (blocks + value identity) are consumed, and those are
  free of 1195. I also confirmed that the candidate's `g`, `P`, endpoint
  receipts, weld and strict-graph inputs all come from the Theorem-(N) package
  (1287/1295 + Assembly V1 + the completion document), not from 1195.
* **No overshoot.** A pleasant consistency check the document should adopt: every
  finite principal block of the bi-infinite `H(c)` **is** a Sprint-1295 word
  matrix `J_x` for the sub-word `(c_{j_0},…,c_{j_1+1})` (verified symbolically on
  200 random words, `s1_final.py`), so `H ⪯ S` by 1295 §2. With `Hλ = Sλ` this
  makes `λ` a top eigenvector and pins the value at exactly `S` — it cannot
  exceed `S`, which would have contradicted the promoted upper bound.

**Repair required: V6.** The candidate's dependency list must cite **Sprint 1206
§§2–4 / the no-endpoint cyclic fixture only**, never "Sprint 1206" as a theorem:
that document's §1 is titled "Certified input" and imports Sprint 1195
explicitly, and its status line still reads "analytic consequence of the
certified bi-infinite wall". Citing it wholesale would re-import the decertified
object by reference and would, on its face, make the new theorem look like a
restatement of the old one. The public repository must retire or clearly mark
`foundational-sprint-1206/SPATIAL-ATTAINMENT-THEOREM.md` before this candidate is
published beside it.

---

## Gate 6 — fresh eyes — **ONE MORE GAP FOUND (V1), plus V7–V9**

Assuming there is one more gap was the right instruction. It is in §6, and the
sentence as written is **false**, not merely under-argued.

### V1 — the fixed-point exclusion is circular, and its unqualified form is false

§6 concludes "the current full-zero locus contains no state-carrying finite
response orbit" from "a fixed point of `τ` … satisfies the multiplicity-uniform
quarter ceiling". At that point in the argument there are no atoms: `μ_U` may be
purely non-atomic, and Sprint 1198's amplitude holonomy (13)–(14) is a statement
about **component norms**, i.e. it needs `‖E_uΩ‖ > 0`. Atoms appear only in §8,
whose disintegration is built on §7's transversal, whose `Y_± = {τ(u) ≷ u\}`
partition presupposes fixed-point-freeness. The chain §6 → §7 → §8 → §6 closes on
itself.

Worse, the *unqualified* claim is false. My reconstruction shows that `τ` **does**
have fixed points on the zero locus: the contact set is a compact interval
`Y ≈ [α, β] = [−0.8783, +0.8778]` (stable in grid and in `q`; `m(u)` rises to
`1.5e-4` at `u = 0.888` and `5.8e-3` at `u = 0.928`), `τ(u) < u` strictly inside,
and the displacement `τ(u) − u` tends to `0` at **both** ends (`−5e-5` and
`−3.3e-3` at the finest setting, shrinking under refinement). Those two boundary
fixed points are exactly the accumulation points of every bi-infinite orbit — the
construction *needs* them to exist. What must be excluded is only that they
**carry mass**.

**The repair, in full, verified by me.** It needs neither atoms nor the
disintegration, and it may be placed before §7:

> Let `F = {u ∈ Y_0 : τ(u) = u}`. On `F`, `a(u) = −u = b(u)`, and `F` is Borel and
> invariant under both `a` and `b`. For Borel `E ⊆ F` we have `aE = bE`, so the
> two transport laws give `∫_E r_A(P(u))² dμ_U = ∫_E r_B(u)² dμ_U` for every such
> `E`, i.e. `r_A(P(u)) = r_B(u)` for `μ_U`-a.e. `u ∈ F`. Write `x = P(u)`;
> `τ(u) = u` gives `P(−u) = −x`, so `(x,u)` and `(−x,−u)` are both full-zero
> pairs. Zero-set localization gives `K(x) = K(u) = 1`, i.e. `g(x)g(−x) = b_x²`
> and `g(u)g(−u) = b_u²`; with `ρ := r_A(x) = r_B(u)` this is 1198 (14):
> `g(−x) = ρ b_x`, `g(x) = b_x/ρ`, `g(u) = ρ b_u`, `g(−u) = b_u/ρ`. The two
> Bellman equalities then give `S − d(x,u) = ρ(b_x+b_u)` and
> `S − d(−x,−u) = (b_x+b_u)/ρ`; adding and subtracting yields 1198 (16)–(17), and
> (18)–(20) give `S ≤ −t + √t ≤ 1/4` with `t = 1 − xu ≥ 0`. This contradicts
> `S > 1/4` (Sprint 1292). Hence `μ_U(F) = 0`.

I re-derived (16)–(20) symbolically; they are exact. The repaired statement is
strictly weaker than the document's ("`F` is `μ_U`-null", not "`F` is empty") and
strictly sufficient: §7's `Y_±` then partition a conull set, which is all the
transversal needs.

Independent corroboration that the repair is the right one and that the package
is *not* inconsistent: at the two boundary fixed points the two transport
densities visibly **disagree** — `r_A(P(α)) = 1.0766` versus `r_B(α) = 0.9276`,
gap `0.149`, stable under refinement — so the measure cannot charge them, and
the quarter-ceiling contradiction correctly does **not** fire in their absence.
Had those two numbers agreed, `S ≤ 1/4` would have followed with no state at all
and the entire package would have collapsed.

### V7 — disintegration normalisation

Write out the `c(t) ≡ 1` step of §8 (given under gate 3).

### V8 — three further things fresh eyes should record

* The document should state that the *only* place finiteness entered Theorem (N)
  — "two decreasing bijections of a finite ordered set coincide" — is replaced
  here by the `D_∞` orbit structure, and that this is the whole difference
  between a contradiction and a construction.
* `‖ψ_S‖ = 1` and the well-definedness of its `I3322` value should be stated
  explicitly (they follow from `Σλ_j² = 1` and the two-banded absolute
  convergence), since §11 currently asserts the value in one line.
* The `μ`-a.e. qualifiers are missing throughout §§5–10. With V3's conull
  invariant `Y_0` in hand they are cheap; without it the statements are literally
  false.

### V9 — binding conditions on the public wording

1. The theorem is **spatial attainment at the certified `S`**, and `S` is known
   only to lie in `(0.2508753845015185, 0.250875388108398]`. The text must not
   assert that `S` equals the historical Pál–Vértesi decimal, nor that the
   Pál–Vértesi construction is optimal — the wording condition W7.1 of my
   round-3 verdict continues to bind.
2. The separation `C_qs(3,3;2,2) \ C_q(3,3;2,2) ≠ ∅` must be stated as
   *conditional on Theorem (N)*, with Theorem (N) cited, since it is the
   nonattainment half that excludes `p_*` from `C_q`.
3. The historical claim of the same separation (Sprint 1206) was **decertified**
   (Sprint 1285). The public text must say so and must say precisely what is new:
   the profile, the `ℓ²` tail and the eigen-equation are now derived from the
   maximizing commuting state rather than imported from Sprint 1195, and the
   global amplitude-compatibility equation is dissolved, not repaired. Anything
   less will read as a re-issue of a retracted claim.
4. Both candidate artifacts must be described as algebraic-identity and
   finite-synthetic guards. They are honest about this in `STATUS.json` and
   `README.md`; the published artifact README must repeat it. Note for the record
   that `scalar_orbit_algebraic_guards.py` is close to vacuous — its second and
   third assertions are tautologies (`X − X == 0`, and `(ra*rb).subs(ra,1/rb)`),
   and no assertion in either script touches a step of the theorem. They should
   be strengthened or demoted to "smoke tests".

---

## 7. Consistency checks that had no obligation to succeed

Recorded because they are the strongest evidence available short of proof. All
are my own reconstruction (`s1_geom.py`, `s1_tail.py`, `s1_fixed.py`), value
iteration on the terminal-pivot operator in Legendre form, grids to `N = 200001`,
`q` down to `0.25087539`; the Legendre step was cross-validated against brute
force to `4.4e-16` and the weld floor `min_{x,u} φ ≥ 0` holds at `7.0e-14`.

| Check | Could have failed | Result |
|---|---|---|
| `r_B < 1` at the forward orbit limit **and** `r_B > 1` at the backward limit — the exact condition for the amplitudes to decay at *both* ends | Yes; if `g` were symmetric at `±β` both ratios would be `1`, `Σλ̃²` would diverge, and no probability measure could satisfy the transport laws on an infinite orbit | **Holds.** `r_B(α) = 0.9276`, `r_B(β) = 1.0768`, product `0.9989 ≈ 1` (consistent with `r_B(t)r_B(−t)=1` and `α = −β`), per-step decay `0.86`. The `ℓ²` decay Sprint 1195 asserted is real |
| `range(P) = −Y` (the dual-tie involution as a statement about sets) | Yes | **Holds.** `Y = [−0.8791, 0.8790]`, `P(Y) = [−0.8785, 0.8785]`; `max|P(−P(u)) + u| = 2e-4` at grid spacing `3.3e-5` |
| `K = g(t)g(−t)/b(t)² ≥ 1`, with `K = 1` on the contact set | Yes | **Holds.** `K ∈ [1.0000, 1.00046]` on `Y`; the discretized `g` over-estimates the infimum so `K` is under-estimated, and `K → 1` from the correct side under refinement |
| `r_A(P(u)) ≠ r_B(u)` at the boundary fixed points | Yes — equality would give `S ≤ 1/4` with no state and destroy the package | **Holds**, gap `0.149`, stable |
| Bell value `=` Jacobi form for *both* matching parities, and `≠` for the swapped source/target diagonal | Yes | **Holds**, exactly, 60/60 rational fixtures |
| Every finite principal block of `H(c)` is a 1295 word matrix, so `H ⪯ S` | Yes | **Holds**, 200/200 random words |

---

## 8. Findings ledger

| ID | Severity | Finding |
|---|---|---|
| **V1** | **Blocking for the text; repaired here** | §6's `τ`-fixed-point exclusion is circular (needs §8's atoms, which need §7, which needs §6) and its unqualified form is false — fixed points exist at both ends of the contact set. Replace by the invariant-set Radon–Nikodym comparison on `F = {τ = id}`, concluding `μ_U(F) = 0`. |
| **V2** | **Blocking for the text; repaired here** | `K_A`, `K_B` need not exist as global self-adjoint unitaries (unequal multiplicities on the `X = ±1` CS corners). §4's boxed remainder identities and the unjustified division by `b(X)` are not licensed. Replace by `W = Y(B_3−I/2)`, `W_B = (A_3−I/2)V`, using only `W² = b(X)²` and `WX = −XW`. |
| **V3** | Must fix | `a` is defined only where `P(u) ∈ Y`; the involution gives `range(P) = −Y`, not `Y`. Construct the Borel `D_∞`-invariant `μ_U`-conull `Y_0` from §5's quasi-invariance and state all of §§5–10 on it. |
| **V4** | Must fix | State that `τ = a∘b` is increasing; used to exclude higher-period orbits, to make `Y_±` orbit-unions, and to make the `u_n` distinct. |
| **V5** | Must fix | §10 needs the two one-liners: odd labels are full-zero targets, and `K(t)=1` is invariant under `t ↦ −t`. |
| **V6** | Must fix before publication | Cite Sprint 1206 §§2–4 / the **no-endpoint cyclic** identity only, never "Sprint 1206", whose §1 imports the decertified Sprint 1195; and distinguish it from 1295 §5's open-word identity, whose hypotheses the labels `c_j` do not satisfy. Retire or mark `SPATIAL-ATTAINMENT-THEOREM.md` in the public repository. |
| **V7** | Should fix | Write out the disintegration normalisation (`c(t) ≡ 1`) and the atomicity sentence. |
| **V8** | Should fix | `μ`-a.e. qualifiers; `‖ψ_S‖ = 1` and well-definedness of the value; the discontinuity of the limit `A` at `±1`; the "no overshoot" remark `H ⪯ S`. |
| **V9** | **Binding on public wording** | See gate 6. Especially: name the decertification and say exactly what is new. |

None of V1–V9 is a mathematical obstruction. V1 and V2 change the proof rather
than the prose; both repairs are forced, short, and verified above.

---

## 9. The theorem I sign

Conditional on V1–V6 being executed as specified:

> **Theorem (S).** Let `I` be the I3322 Bell functional in the normalisation used
> throughout the repository (classical bound `0`; qubit and qutrit maximum
> exactly `1/4`), and let
> `S := ω_tensor(I3322) = ω_commuting(I3322) ∈ (0.2508753845015185, 0.250875388108398]`
> be its quantum supremum. Then `S` is **attained by a normal spatial strategy**:
> there exist six orthogonal projections — three on each of two copies of
> `ℓ²(ℤ)` — and a unit vector `ψ_S ∈ ℓ²(ℤ) ⊗ ℓ²(ℤ)` with
> `⟨ψ_S, 𝓑_{3322} ψ_S⟩ = S`. Consequently the correlation `p_*` it produces lies
> in `C_qs(3,3;2,2)`, and by Theorem (N) not in `C_q(3,3;2,2)`, so
>
> ```text
> C_qs(3,3;2,2) \ C_q(3,3;2,2) ≠ ∅.
> ```

**Exact dependency list, as I would sign it.**

*From the candidate (all audited here):*
1. §2 — existence of a maximizing state on the universal commuting `C*`-algebra
   (weak-`*` compactness) and its GNS triple.
2. §3 — Fatou passage: `φ = 0` `μ`-a.e., with endpoint atoms excluded by
   Receipt (iii) **uniformly in the state**.
3. §4 **as repaired by V2** — uniform bounds on `A_n, B_n, R_{A,n}, R_{B,n}`;
   `‖R_nΩ‖² ≤ ‖R_n‖⟨Ω,R_nΩ⟩ → 0`; `A(X)Ω = WΩ`, `B(U)Ω = W_BΩ`.
4. §5 — the two scalar Radon–Nikodym laws and the three exact product identities.
5. §6 **as repaired by V1, V3, V4** — the response maps on a conull invariant
   `Y_0`, `τ` increasing, and `μ_U{τ = id} = 0`.
6. §7 — the first-rational Borel transversal; smoothness of the `D_∞` relation.
7. §8 **with V7** — disintegration; atomic conditionals inheriting both transport
   laws.
8. §9 **with V4** — the interleaved labels, the one-step cocycle, `1 ≤ Σλ̃² ≤ 2`,
   hence `λ ∈ ℓ²`.
9. §10 **with V5** — `Hλ = Sλ` via the Bellman contact equality at every adjacent
   pair.
10. §11 **with V6** — the no-endpoint alternating block-to-Jacobi identity;
    two-banded absolute convergence.

*From the promoted Theorem-(N) package:*
11. Assembly V1 Receipt (i) — the limiting storage `g` (uniform bound,
    `3/2`-Lipschitz, Arzelà–Ascoli, concavity, interior positivity, Bellman
    feasibility at `S`). *The finite-dimensional spectral cut-off of Receipt (i)
    is **not** used and must not be cited.*
12. Assembly V1 Receipt (iii) — the exact endpoint margins `m_±` and the uniform
    endpoint `R_0`-gap `≥ m_±/2` for all `q ≤ S_+`.
13. `CRITICAL_ZERO_SET_REDUCTION` §§2, 4, 5, 6 — concavity, `K ≥ 1`, zero-set
    localization (`K(x) = K(u) = 1`, `p(x) = g(−x)`, `p(−u) = g(u)`), strict Monge.
14. `CONVEX_ENVELOPE…COMPLETION` §§1–9 **as repaired by round-3 W1–W4** — the
    open-interval envelope, both plateau exclusions, the dual-tie involution, and
    the strict graph theorem `R_0^{-1}(0) ∩ D²` one-to-one and strictly increasing.
15. Sprint 1198 §4 (16)–(20) — the quarter ceiling, used **only** inside V1's
    repair.
16. Sprint 1197 — the Bell-operator reparameterisation and the weld form of
    `R_0, R_A, R_B`. *(Independently replicated in `s1_carrier.py`.)*
17. Sprint 1287 — the generic operator weld at each `q_n`.
18. Sprint 1295 — `P = S`; the storages `g_q` with `g_q ≥ q − S`, feasibility and
    common modulus of continuity; §2's source/target placement convention.
19. Sprint 1292 — `S > 0.2508753845015185 > 1/4`.
20. Sprint 1294 — `S ≤ S_+`, fixing the `q`-window of Receipt (iii).
21. Sprint 1206 **§§2–4 only**, i.e. the alternating rank-one projector blocks and
    the no-endpoint block-to-Jacobi value identity. *(Verifier run in a copy and
    independently replicated in exact arithmetic in `s1_carrier.py`.)*
22. **Theorem (N)** — for the separation corollary only.

*Standard mathematics:* weak-`*` compactness of the state space; GNS; joint
spectral theory and Borel functional calculus for a commuting pair; Fatou and
dominated convergence; Lusin–Souslin; Rokhlin disintegration over a smooth
countable Borel equivalence relation.

**Explicitly NOT used:** the Sprint-1195 global Bellman fixed point, its
bi-infinite cosine profile, its geometric `ℓ²` tail and its eigen-equation
(all decertified by Sprint 1285); Sprint 1206 §1 and its status line; the
global amplitude-compatibility equation in any form; any square factorization of
`R_A, R_B`; norm convergence of the weld on the whole GNS space; a compact
interior spectral carrier; direct-integral decomposition of the operator
representation; any operator-multiplicity classification; any pre-existing Jacobi
alignment; the DOC-C shooting/heteroclinic artifacts; the conditional
dimension-necessity campaign (Sprints 1208–1265).

---

## 10. Reproduction

Candidate artifacts (run here, both PASS):

```
python candidate/artifacts/scalar_orbit_algebraic_guards.py
python candidate/artifacts/scalar_orbit_hostile_controls.py
```

Repository verifier (run in `repocopy/`, never in place):

```
foundational-sprint-1206/spatial_realization_verify.py    all_gates_pass: true
```

Referee's own scripts:

```
python s1_carrier.py   # exact-rational replication of the no-endpoint PV
                       # block-to-Jacobi identity from the 1197 reparameterisation;
                       # both matching parities; swapped-diagonal control
python s1_geom.py      # Legendre-form reconstruction of g_q; weld floor;
                       # product laws; contact set and P
python s1_orbit.py     # K on the contact set; orbit, interleaved labels,
                       # Jacobi residual, flipped-orientation control
python s1_tail.py      # r_B at the two ends: the ell^2 decay condition
python s1_fixed.py     # boundary fixed points of tau; the rho vs rho' gap
python s1_final.py     # principal blocks are 1295 word matrices, so H <= S
```

---

## 11. Closing note

Round 3 said the decisive move on Theorem (N) was "weakening the receipts until
they were true". This candidate does the same thing once more, in the one place
that had killed the program before. Sprint 1195 tried to *build* the amplitudes
and had to solve a global compatibility equation; it did not close, by
`1.4e-4`. This proof never poses that equation — it takes an object that already
exists (a maximizing commuting state), disintegrates only its **scalar** joint
spectral measure over the countable response relation, and reads the amplitudes
off the resulting atoms. Summability, consistency and geometric decay all become
consequences of "a conditional measure is a probability measure". That is the
right shape for a repair, and it is why I am signing.

The residues are of the same species as W1 was: §6 excludes a set of fixed points
that demonstrably is **not** empty (only null), and §4 rewrites the certified
remainder through an operator `K_A` that need not exist. Both are artefacts of
carrying finite-dimensional habits — a finite ordered support, a global CS
involution — into a setting that no longer supplies them. Fix those two, add the
conull-invariance hygiene, cite 1206 by section rather than by name, and this is
a proof.
