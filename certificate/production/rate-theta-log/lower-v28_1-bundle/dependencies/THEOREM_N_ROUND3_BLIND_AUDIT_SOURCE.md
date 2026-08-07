# Round-3 referee verdict — THE PROMOTION AUDIT of Theorem (N)

Referee: independent, blinded to the authors' working notes. Refutation-first.
Prior reports by the same referee: `ROUND1-VERDICT.md`, `ROUND2-VERDICT.md`.

Consulted: the round-3 package
`package/production/theorem-N-four-receipts-at-S/` (all nine documents and all
five artifacts) and the public repository `i3322-exact-wall` at HEAD — sprints
1197, 1198, 1206, 1287, 1292, 1294, 1295, `paper/CERTIFICATE-MAP.md`,
`paper/CERTIFICATE-STATUS-ALERT.md`, `review/ADJUDICATION.md`, `README.md`.
Literature: Pál–Vértesi, *Phys. Rev. A* **82**, 022116 (2010) / arXiv:1006.3032,
and a 2025–2026 sweep for a resolution.

Own scripts, written and run here (nothing imported from the authors' code):
`r3_storage.py`, `r3_envelope.py`, `r3_kink.py`, `r3_exact.py`,
`r3_carrier.py`. The authors' five artifacts were run by me; the four
load-bearing repository verifiers were run in a **copy** (`repocopy/`) so that
the public repository was not modified.

---

## 0. Overall verdict

**PROMOTE — with four mandatory textual repairs, one of which is a genuine
(but fully repairable, and here repaired) hole in the written proof.**

I attacked every step named in the assignment and could not break the theorem.
The convex-envelope plateau-exclusion theorem is correct; the dual-tie
involution is an exact derived identity, not an assertion; the reflection-gluing
defect `K ≥ 1` checks out against Sprint 1295's actual history definition; the
endpoint receipts are exactly what they claim; the limiting-weld substitute is
sound; and no step needs uniformity in `q` that the limit does not supply. My
round-2 score of **1 of 4 receipts certified is now 4 of 4**.

The one real finding is **W1**: the completion document builds the convex
minorant on an *"endpoint-excluded compact source interval"* with **no receipt
that sources outside that interval are inactive**. As literally written, §§3–5
therefore characterise activity for a *restricted* minimisation, while an
occupied `R_0`-zero pair is only known to be active for the *full* source
domain. This is not a mathematical obstruction — I give below the complete
repair (take the source domain to be the **open** interval `(-1,1)`, where the
minorant exists because `C ≥ g(0) > 0` follows from Bellman feasibility at
`u = 0`), and I have verified every step of the repaired argument. But the
document as it stands does not close, and must not be published as it stands.

Three further repairs (W2, W3, W4) fix justifications that are false on a
non-compact domain but whose conclusions have clean one-line proofs. W7 is a
binding condition on the **public wording**.

---

## 1. Task 1 — the convex-envelope theorem, line by line

Notation as in the document: `g` the limiting critical storage,
`b(x)² = (1-x²)/4`, `p = b²/g`, `C(x) = S+1-x/2-p(x)`, and the first Bellman
inequality in envelope form `g(u) ≤ C(x) + (1/2-x)u`.

### (c) The downward-corner lemma (2.1) — **CORRECT**

`g` concave and finite on `[-1,1]` has finite one-sided derivatives at every
interior point, and `g > 0` on `(-1,1)` (Assembly V1, verified in §5 below), so
`p` and `C` have finite one-sided derivatives on all of `(-1,1)`. The identity

```text
C'_+(x) - C'_-(x) = (b(x)²/g(x)²)·(g'_+(x) - g'_-(x)) ≤ 0
```

is exact (re-derived symbolically in `r3_exact.py`; also the authors'
`convex_envelope_plateau_exclusion_verify.py` gate). Existence of the one-sided
derivatives is where interior positivity of `g` is load-bearing, and it is
supplied. **No attack succeeds.**

### (a) The reduction (3.1) — **CONCLUSION CORRECT, JUSTIFICATION WRONG (W2)**

The document argues via "each point of `H` is either a contact point with `C`,
or lies on a chord between two contact points". On a **non-compact** domain a
component of `{H<C}` need not have contact points at both ends, so this
justification fails. The conclusion is nonetheless immediate and
domain-independent:

> Let `m = inf_y [C(y)-uy]`. The affine map `y ↦ uy+m` is a convex minorant of
> `C`, hence `≤ H`, so `inf_y[H(y)-uy] ≥ m`; and `H ≤ C` gives `≤ m`.

This is the correct proof and must replace the chord argument.

### (b) "Active ⟺ `u ∈ ∂H(x)`" — **THE USED DIRECTION IS CORRECT; the "⟺" is
false in general (W4)**

If `x` minimises `C(·)-u·` over the domain `D`, then
`C(x)-ux = m ≤ H(x)-ux ≤ C(x)-ux`, so **`H(x) = C(x)`** and `x` minimises
`H(·)-u·`, i.e. `u ∈ ∂H(x)`. The converse fails wherever `H(x) < C(x)`. Only
"⟹" is used in Theorem 5.1, so this is a wording defect, not an error. Note
that `C = H` at active points is *derived*, not assumed — the audit question is
answered affirmatively.

### (d) The kink-contradiction chain — **CORRECT**

At a contact point `x₀` put `F = C-H ≥ 0`, `F(x₀)=0`; both one-sided
derivatives of `F` exist, so `F'_-(x₀) ≤ 0 ≤ F'_+(x₀)`, i.e.
`C'_-(x₀) ≤ H'_-(x₀) ≤ H'_+(x₀) ≤ C'_+(x₀)`. With (2.1) this forces **equality
throughout**. The document's chain is valid, and in fact proves more than it
claims:

> **Strengthened form (referee's, recommended as the published statement):**
> at every contact point of `H` with `C`, `C` is differentiable and `H' = C'`.
> Consequently a *strict downward corner of `C` is never active*, and `H` is
> differentiable everywhere on the interior.

This matches the zero-set document's own remark that "an active seam is either
smooth or inactive", and is the cleanest way to state the result.

Numerically confirmed in `r3_kink.py`: for six concave piecewise-linear
storages with violent knots (slope jumps up to 60), the corner jump of `C` is
downward in every case and **the knot is never a vertex of the lower convex
hull** (`C-H` at the knot ranges from `7.8e-4` to `1.2`).

### (e) BOUNDARY BEHAVIOUR — **THE ONE REAL FINDING (W1), plus W3**

Two distinct issues hide here.

**W3 (justification).** §4's "on such a component, the greatest convex minorant
is the chord between its boundary contact points, hence is affine" again
presupposes contact endpoints. The needed statement — *`H` has no kink at a
point where `H < C`* — has a direct proof that is immune to the boundary:

> Suppose `H(x₀)<C(x₀)` and `H'_-(x₀)<H'_+(x₀)`. Take `ℓ` affine with
> `ℓ(x₀)=H(x₀)` and slope strictly between the two one-sided derivatives; then
> `ℓ ≤ H` with equality only at `x₀`, and `H-ℓ` grows at least linearly on both
> sides, so `U_ε := {H < ℓ+ε}` shrinks to `{x₀}`. For `ε` small,
> `C > ℓ+ε` on `U_ε` by continuity of `C` at `x₀`, hence `max(H, ℓ+ε)` is a
> convex minorant strictly above `H` at `x₀` — contradicting maximality.

**W1 (the hole).** The document takes `H` to be the greatest convex minorant on
"the endpoint-excluded compact source interval". No receipt in the package
excludes sources in `(x_R, 1)` or `(-1, x_L)`; the exact receipts exclude only
`x = ±1` themselves, and Assembly V2's Receipt U4 (which would have supplied
the wing exclusion) is explicitly listed as **OPEN** and is superseded, not
delivered. On a strictly smaller source interval, "x is active" means active for
a restricted minimisation, whereas what an `R_0`-zero pair delivers is
minimality over the **whole** admissible source set. The published argument
therefore does not connect.

**The repair, in full, verified by me.** Take the source domain to be the open
interval `D = (-1,1)`. Then:

1. `g > 0` and concave on `D`, so `C` is continuous on `D` with finite
   one-sided derivatives, and (2.1) holds at **every** point of `D`.
2. `C` is **bounded**: feasibility at `u = 0` reads
   `p(x)+g(0) ≤ S-d(x,0) = C(x)+p(x)`, hence `C(x) ≥ g(0) > 0` on `D`
   (`r3_exact.py` §5 checks the algebra; and `p ≥ 0` gives `C ≤ S+3/2`).
   Therefore the constant `g(0)` is a convex minorant and `H` is finite.
   *(Numerics agree exactly: reconstructed `C ∈ [0.50008, 1.75088]`, with
   `S+3/2 = 1.750875…` attained at `x=-1` and `g(0)=1/2` forced by `K(0)=1`.)*
3. Every point of `D` is interior, so no boundary contact point is ever needed
   and no chord can run to an excluded endpoint region.
4. Theorem 4.1 (with W2/W3's replacements) and Theorem 5.1 then hold verbatim
   on `D`, and an `R_0`-zero pair `(x,u)` with `x,u ∈ D` gives exactly
   `C(x)-ux = min_{y∈D}[C(y)-uy]`, hence `u = H'(x)`.

Endpoint exclusion is then needed **only** to place the occupied spectrum inside
`D` — which is precisely what Receipt (iii) does. The repaired argument is
strictly stronger than the written one and needs no wing receipt at all.

Worth recording: the boundary is *not* dangerous, and the reason is structural.
If `g(±1)=0` then concavity gives `g(x) ≥ (1∓x)·g(x₀)/(1∓x₀)` near the endpoint,
so `p = b²/g` stays **bounded**; `C` cannot blow down, and no convex minorant
can be destroyed. This is the fact the document should state instead of
excluding the endpoints by fiat.

### Countermodel search — **failed, as the theorem predicts**

`r3_envelope.py` and `r3_kink.py` searched for a concave positive `g` on an open
interval whose `C` has a convex minorant with an interior kink: random concave
piecewise-linear storages (3–12 knots), square-root storages, tent storages
vanishing at **both** endpoints, one-sided storages vanishing at one endpoint,
grids up to 64,001, and six adversarial hand-built knot families. Every apparent
"kink" was a hull-vertex slope jump with **bounded** jump/spacing ratio, i.e.
smooth-but-large curvature (`jump/spacing ≈ 1.25 … 275`, stable under
refinement), never a surviving kink. No countermodel exists, consistently with
the proof.

---

## 2. Task 2 — the dual-tie involution

**DERIVED, not asserted. Compatible with an asymmetric storage. CORRECT.**

* `B(u) = A(-u)` is a *definitional* identity, not a symmetry hypothesis:
  `A(x) = √(p(x)g(-x))` gives `A(-u) = √(p(-u)g(u)) = B(u)`.
* `d(-u,-x) = d(x,u)` is an exact polynomial identity (checked independently in
  `r3_exact.py` and by both authors' scripts).
* Hence `R_0(-u,-x) = S-d(x,u)-A(-u)-B(-x) = S-d(x,u)-B(u)-A(x) = R_0(x,u)`.
  **No use of `g(-t)=g(t)`** — the identity survives the asymmetric active range
  `[-0.8936, +0.8981]` that both the authors and I measure.
* The involution maps the **full** equality locus to itself, because the two
  constraints swap: the second Bellman inequality at `(x,u)` *is* the first
  Bellman inequality at `(-u,-x)`, and the Cauchy tie
  `p(x)p(-u) = g(u)g(-x)` is symmetric under the swap. So `R_0=0` at `(x,u)`
  iff at `(-u,-x)`, with both Bellman equalities and the Cauchy tie preserved.
* Consequently Theorem 6.1 is valid: two sources for one zero-target reflect to
  one source with two zero-targets, contradicting Theorem 5.1.

Structural note worth publishing: the vertical tie really *does* occur for the
raw first-contact correspondence (whenever `H` has a chord region, both of its
endpoints are active for the same target). Theorem 6.1 does not deny that; it
says at most one of the two can lie on `R_0^{-1}(0)`. The written text should
say so, or a reader will think Theorem 6.1 contradicts the geometry.

---

## 3. Task 3 — the zero-set reduction theorems

All four re-derived independently. Both authors' verifiers run and PASS; as
expected they check only algebraic identities, so I audited the connective
logic separately.

| Statement | Verdict |
|---|---|
| **Thm 1.1**, `g_q = T_q g_q` (both directions) | **CORRECT.** `≤` is 1295's extension inequality. `≥`: a one-edge pivot `q-d(i,j)` dominates `q-d(i,j)-b(i)²/g_q(i)`; a longer history has preceding pivot `p ≥ g_q(i)` and `p ↦ q-d(i,j)-b(i)²/p` is increasing. (Not actually needed downstream — see §7, F3.) |
| **§2 concavity** | **CORRECT.** `d(i,j)` is affine in `j` and every terminal pivot is `A_{h,i}(q)-d(i,j)`; an infimum of affine functions is concave, and a uniform limit of concave functions is concave. Independently confirmed numerically: max second difference of the reconstructed `g` is `4.4e-16` at `N = 2001…8001`. |
| **Thm 4.1**, `K ≥ 1` via 2×2 gluing | **CORRECT, and it checks out against 1295's actual definition.** I reconstructed the gluing explicitly. For a word `x=(x_0,…,x_n)`, 1295 sets `(J)_{k,k}=d(x_k,x_{k+1})` and `(J)_{k-1,k}=b(x_k)`. Reflecting *and* reversing a history ending at `-t` gives a word starting at `t` whose Jacobi matrix is the index-reversal of the original (uses `d(-y,-x)=d(x,y)` **and** `b(-x)=b(x)`), so its pivot onto its first coordinate is `r`. Concatenating history-1 (ending at `t`) with it produces a word whose coordinates `m-1, m` are coupled by `-b(t)`; Schur-complementing the rest is exactly the LDL elimination from each end, leaving `[[p,-b(t)],[-b(t),r]]`. Schur complements are operator-monotone, so `qI-J ⪰ δI` descends, giving `(p-δ)(r-δ) ≥ b(t)²`; independent infima are legitimate since both factors are `≥ 0`. Numerics: `min K = 1.0000069, 1.0000043, 1.0000004` at `N=2001,4001,8001` — approaching `1` from **above**, as `K ≥ 1` requires. |
| **Thm 5.1**, `R_0=0 ⟹ K(x)=K(u)=1`, `p(x)=g(-x)`, `p(-u)=g(u)` | **CORRECT.** Cauchy equality is `p(x)p(-u)=g(u)g(-x)`, i.e. `K(x)K(u)=1`; with `K ≥ 1` both are `1`. Both factors `≤ h` and their geometric mean `= h` forces both `= h`, so both Bellman inequalities are equalities. |
| **§6 strict Monge** | **CORRECT.** Own equalities + two cross inequalities give `h(x_1,u_1)+h(x_2,u_2) ≤ h(x_1,u_2)+h(x_2,u_1)`, which for I3322 is exactly `(x_1-x_2)(u_1-u_2) ≥ 0`. |

**Steps the verifiers do not cover, audited by hand:** the gluing *construction*
(above); the inference chain `R_0=0 ⟹` both Bellman equalities `⟹` C-activity;
the passage from `K_q ≥ 1` at each `q` to `K ≥ 1` at the limit; and the
assembly of Monge + both plateau exclusions into the strict graph theorem
(§7 of the completion document) — all correct.

---

## 4. Task 4 — the assembly chain, step by step, with receipts

| # | Step | Receipt | Verdict |
|---|---|---|---|
| 0 | Projectivisation of a POVM maximiser | 1198 §1 / 1197 §5 (finite dilation, or extreme-effect replacement) | **DISCHARGED.** Both routes preserve finite dimension, tensor split and value. |
| 1 | Limiting equality module at `S` | Assembly V2 §receipt (i) = Assembly V1 Thm 1 | **DISCHARGED** with a presentational gap (W6). Uniform bound: one-edge histories give `g_q ≤ q+3/2`; `3/2`-Lipschitz from `|∂_j d| = |i-1/2| ≤ 3/2`; Arzelà–Ascoli. Interior positivity: `g(x)=0` with `b(x)>0` drives `g_n(j) → -∞` against `g_n ≥ q_n-S>0`. Weld passage: `Σ_ν Tr(ρR_{ν,n}) = q_n-S → 0`, each term `≥ 0`, coefficients converge on the finite occupied interior spectrum, limits are PSD with zero trace against `ρ`, so `R_{ν,∞}ρ = 0`. |
| 2 | Endpoint exclusion (exact rational margins) | Assembly V1 Receipt (iii); `four_receipts_at_S_endpoint_and_scout.py` | **DISCHARGED.** Independently re-derived exactly in `r3_exact.py`: `L_+^q(u)-p_1 = r[(2-r)/(4q+2r) - (u+1/2)]` and `L_-^q(u)-p_1 = r[(u+1/2) + (2-r)/(4q+6r)]`; both are strictly decreasing in `q` (worst case `q=S_+`) and monotone in `u` (worst cases `u=+1`, `u=-1`). I reproduce `m_+ = 23686917837403/3008753881083980` and `m_- = 274562305945801/4008753881083980` **exactly**. The `g_q ≤ p_1` domination step is exactly 1295 (7): `g_q(j)` is the infimum of terminal pivots over *all* finite histories, and `(1,1-r,u)`, `(-1,-1+r,u)` are legitimate histories with `p_0 = q+r/2 > 0`, `p_0 = q+3r/2 > 0`. |
| 3 | "one Bellman sum ≤ `h-m_±`, the other ≤ `h`" ⟹ `R_0 ≥ m_±/2` | Assembly V1 Receipt (iii) | **DISCHARGED.** `p(±1)=0`, so the first sum is `g_q(u) ≤ h(±1,u)-m_±`; the second is feasibility. `h-√(h(h-m)) ≥ m/2` reduces to `(h-m/2)² - h(h-m) = m²/4 ≥ 0`, valid since `h ≥ q > 1/4 > m_±`. The target cases `u=±1` follow from the exact identities `h(x,+1)=h(-1,-x)`, `h(x,-1)=h(+1,-x)` (checked). Reconstructed numerics give the *actual* gaps `0.0522` and `0.2094`, comfortably above `m_+/2 = 0.003936` and `m_-/2 = 0.034245`. |
| 4 | Occupied support ⊆ `R_0^{-1}(0)` | `R_{0,∞} = φ(X,U) ⪰ 0` with `φ ≥ 0`, joint spectral theory | **DISCHARGED** (round-2 R1). |
| 5 | **Envelope binding:** occupied support lies in the ACTIVE CONTACT of THIS `C` from THIS `g` | completion doc §§1,5 | **DISCHARGED ONLY AFTER W1's REPAIR.** With `D=(-1,1)`: `R_0=0` gives `g(u)=C(x)+(1/2-x)u` while feasibility gives `g(u) ≤ C(y)+(1/2-y)u` for **all** `y ∈ D`; hence `x` attains `min_{y∈D}` and `u = H'(x)`. With the document's restricted compact interval, this step does **not** close. |
| 6 | Horizontal plateau exclusion (Thm 5.1) | completion doc §§2–5 | **DISCHARGED** (§1 above). |
| 7 | Vertical plateau exclusion (Thm 6.1) | completion doc §6 | **DISCHARGED** (§2 above). |
| 8 | Strict graph theorem | completion doc §7 | **DISCHARGED.** Monge `≥ 0` plus both exclusions gives a one-to-one strictly increasing partial function on the interior. |
| 9 | Unitary transports, totality, component equations (10a) | 1198 §3, round-2 audit | **DISCHARGED.** `K_A = J_A⊗S_B` is a self-adjoint unitary (`J_A=Y/(2b(X))`, `J_A²=I`, `J_AX=-XJ_A`, `S_B²=I`); `R_{A,∞}ψ=0` gives `K_Aψ = r_A(X)ψ` with `b(X)` invertible on the occupied set; the graph property makes `E_x^Xψ` the *whole* joint component, so `K_Aψ_u = r_A(-x)ψ_{a(u)} ≠ 0`. **Only the weaker zero-locus statement is consumed** — see §6. |
| 10 | One decreasing bijection of a finite ordered set ⟹ `a = b_map` | 1198 §3 | **DISCHARGED.** `a` is decreasing because the graph relation is strictly increasing on the occupied set; `Σ` is finite; both maps are bijections of `Σ`. |
| 11 | Multiplicity-uniform amplitude elimination and quarter ceiling | 1198 §4 | **DISCHARGED.** Re-derived from the new zero-set identities: `K(x)=1` gives `r_A(-x)=b(x)/g(-x)`, so `ρ = g(-x)/b(x) = √(g(-x)/g(x))` — 1198 (13)–(14) are now *consequences* of `p(x)=g(-x)`, not an extra fixing step. (16)–(20) re-verified symbolically in `r3_exact.py`: `(b_x+b_u)²+(x-u)²/4 = (1-xu+s_xs_u)/2`, `(1-xu)²-s_x²s_u²=(x-u)²`, `1/4-(-t+√t)=(√t-1/2)²`. The transport coefficient is a **scalar** functional-calculus factor between complete fibres, so arbitrary finite multiplicity is harmless. |
| 12 | `S > Q_127 > 1/4` | 1292 (exact 255-dim strategy) + 1287/1295 | **DISCHARGED.** `ω_tensor > 0.2508753845015185` (verifier run, all gates pass); `ω_commuting ≤ S` from 1287+1295 §3; hence `S > 1/4`. Note this direction needs only `ω_tensor ≤ S`, not the harder `ω_tensor ≥ S`. The completion document's label `Q_127` refers to the Sprint-1288 127-dimensional strategy; the current strongest receipt is Sprint 1292's dimension-255 bound. Harmless, but the published text should cite 1292. |
| 13 | `S ≤ S_+ = 0.250875388108398` (needed for the `q`-window of step 2) | 1294 exact 25,601-knot witness | **DISCHARGED.** Verifier run; `certificate_closed: true` (its `all_gates_pass:false` is the separately-recorded *performance wager*, not a theorem gate). |
| 14 | `ω_tensor = ω_commuting = S` (needed for the headline reading) | 1295 §5 + the Pál–Vértesi principal-block carrier (Sprint 1206) | **DISCHARGED, and independently replicated by me.** `r3_carrier.py` builds the six PV blocks from the published recipe, forms the Bell operator via the *Sprint-1197 reparameterisation*, and evaluates it on `Σλ_i|ii⟩ ∈ C^n⊗C^n`: the value equals the Jacobi quadratic form to machine zero (`0`–`1.1e-16`) for random label words at `n = 5,7,9,11,15,21,31`, with all six blocks exact projections. The padding step is confirmed (`J` of the padded word contains the raw word's `J` as a principal block). This closes the last link neither prior round audited. |

**No step's receipt is missing or weaker than consumed**, except step 5, whose
consumed statement (activity for the *full* source domain) is stronger than what
the written envelope construction supplies — the W1 hole, repaired above.

---

## 5. Task 5 — uniformity and limit hygiene

**Clean. The round-2-era uniformity concern is now moot, and I could not
resurrect it.**

* No step needs uniformity in `q` of a contact structure. The convex-envelope
  argument runs **at the limiting `g`**, using only: concavity, interior
  positivity, and feasibility at `S`. Assembly V2 §1.1's uniform-`q` demand
  belonged to the superseded tiling route.
* The two places `q` still enters are both uniform **by exact monotonicity**,
  which I verified symbolically rather than numerically:
  `∂_q(L_±^q - p_1) = r(r-2)/(2q+r)²` resp. `r(r-2)/(2q+3r)²`, both `< 0`, so
  `q ≤ S_+` is the worst case and the margins `m_±` hold for the whole window.
  The `K ≥ 1` gluing holds at each `q` with `δ = q-S`, and `δ_n → 0` passes to
  the limit.
* The subsequential-limit construction matches 1295's stated properties: `g_q`
  is an infimum of the affine-in-`j` family `constant(history,i)-d(i,j)`
  (1295 (9)); the one-edge histories give the uniform bound
  `g_q(j) ≤ q - max_i d(i,j) ≤ q+3/2`; `|∂_j d(i,j)| = |i-1/2| ≤ 3/2` gives the
  common Lipschitz constant; Arzelà–Ascoli gives a uniformly convergent
  subsequence; concavity, feasibility and `K ≥ 1` all pass to the limit.
* **The argument never needs `g = T_S g` at the limit** (F3 below), so no
  fixed-point property has to survive the limit.
* **W6 (presentational).** "All scalar functional-calculus coefficients converge
  on the occupied finite spectra" is morally right but under-argued. The clean
  form: choose `c<1` with the finite occupied spectrum inside `[-c,c]` and set
  `Π = 1_{[-c,c]}(X) ⊗ 1_{[-c,c]}(U)`. Because `[-c,c]` is symmetric, `Π`
  commutes with `X, U, J_A, J_B, S_A, S_B`, hence with all three remainders;
  `Πρ = ρ`; and `A_n → A` uniformly on `[-c,c]` gives norm convergence of
  `ΠR_{ν,n}Π`. Then PSD-ness and `Tr(ρ·)=0` pass to the limit and
  `R_{ν,∞}ρ = 0`. This paragraph should be written out.

---

## 6. Task 6 — updated receipt table (round-2 interface, re-scored)

| Input (round-2 numbering) | Round-2 status | **Round-3 status** | Receipt |
|---|---|---|---|
| **(i)** `S·I-B = R_0+R_A+R_B ⪰ 0` with the 1197 local structure, at `S` | NOT CERTIFIED | **DISCHARGED** — and the round-2 obstruction is *dissolved*, not solved: attainment of the 1295 infimum is **never needed**. A hypothetical finite maximiser carries the exact equality module by the limiting-weld substitute, even if `g(±1)=0`. My round-2 finding N5 (interior positivity by the `-∞` argument) is exactly the authors' route; the endpoint boundary layer I flagged as "the single highest-value next step" is bypassed rather than closed. | Assembly V1 Thm 1 + 1287 generic weld + 1295 `g_q` (W6: write out the spectral cut-off) |
| **(ii)** contact uniqueness + strictly increasing predecessor | NOT CERTIFIED at any value | **DISCHARGED in the weaker, sufficient form** (see below) | completion doc Thms 4.1/5.1/6.1/§7 + zero-set doc §§4–6 (W1/W2/W3/W4 repairs mandatory) |
| **(iii)** `range(P)` strictly interior | NOT CERTIFIED | **DISCHARGED — and no longer required.** After W1's repair the envelope is built on all of `(-1,1)`, so no interiority of the active range is used. What *is* used and *is* certified is the strictly weaker statement that the **occupied spectrum** avoids `x,u = ±1`, by the exact margins `m_±`. My round-2 items N2/N6 are superseded: the two explicit endpoint lines are now used to exclude endpoint *atoms*, not to bound `range(P)`. | Assembly V1 Receipt (iii), exact rationals, re-derived here |
| **(iv)** `S > 1/4` | CERTIFIED | **CERTIFIED** (unchanged; verifier re-run) | 1292 + 1287 + 1295 |

**Score: 4 of 4.**

**Is the replacement of receipt (ii) sufficient for the 1198 mechanism?**
**Yes.** My round-2 formulation demanded a globally single-valued, strictly
increasing first-contact predecessor `P` on all of `[-1,1]`. What 1198 actually
consumes is only:

1. *(no-cancellation / "a member of `Σ` identifies the complete occupied pair")*
   — needs the occupied support to lie in a **one-to-one** relation, so that the
   `X = x` spectral component of `ψ` is a single joint component. The full-zero-
   locus graph theorem gives exactly this;
2. *(`a(u)` well defined)* — needs `-x` to be an occupied source with a unique
   occupied target. Existence comes from **unitarity** of `K_A`, not from `P`;
   uniqueness comes from the graph theorem;
3. *(`a` decreasing)* — needs the relation to be strictly **increasing** on the
   occupied set, which the Monge step plus both plateau exclusions supply.

Nothing in 1198 requires `P` to be defined off the zero locus, and the
round-2-era worry that a tie at an inactive `x` would destroy the graph property
is now *provably irrelevant*: the reflection-gluing theorem shows every tie with
`K>1` lies outside the equality module. The replacement is strictly weaker and
strictly sufficient. **Round-2 items 2, 3, 5 of §5 are withdrawn; item 4 (the
reflected left wing) is withdrawn as a threat** — the asymmetric wing
`[-0.8936, +0.8981]` is reproduced by me at five resolutions and is now
irrelevant to the proof, since no wing enclosure is used.

---

## 7. Task 7 — fresh eyes (things neither round named)

**F1 (the finding). W1 above.** The unjustified compact source-domain
restriction. Found only by asking what "the endpoint-excluded compact source
interval" is licensed by, and discovering that the receipt that would license it
(Assembly V2 Receipt U4) is the one the supersessions dropped. It is repairable,
and I have repaired it — but it is exactly the kind of residue that survives
when the authors and the adjudicator converge on a new argument and carry over a
phrase from the abandoned one.

**F2 (structural, in the authors' favour).** `C` is **bounded** on `(-1,1)`
whatever the endpoint behaviour of `g`: bounded above by `S+3/2` because
`p ≥ 0`, and below by `g(0) > 0` by feasibility at `u=0`. Moreover, concavity
alone forces `p = b²/g` to stay bounded even when `g(±1)=0` (chord bound
`g(x) ≥ (1∓x)g(x₀)/(1∓x₀)`). So the endpoint boundary layer that dominated
round 2 cannot damage the envelope at all. This should be a lemma in the paper;
it is what makes the open-interval formulation legitimate.

**F3 (dependency pruning).** The zero-set document's Theorem 1.1 (`g_q=T_qg_q`)
and §2's fixed-point framing are **not used** by the final chain. Only
feasibility, concavity and interior positivity of the limit are consumed. The
published dependency list should say so; it removes an entire theorem from the
critical path.

**F4 (over-claim risk in the write-up).** The vertical tie is *real* for the raw
first-contact correspondence — every chord region of `H` has two active sources
for one target. Theorem 6.1 must be stated as "not both on `R_0^{-1}(0)`", never
as "the first-contact correspondence has no vertical plateau", which is false.
The authors' own STORAGE_REPRESENTATION_BRANCH_VERDICT §3 already stumbled once
in this area (it asserted a plateau mechanism with the sign reversed, corrected
later); the same paragraph should not be resurrected.

**F5 (package hygiene, W8).** The package simultaneously ships
`FOUR_RECEIPTS_AT_S_ASSEMBLY_V2.md` §6 ("uniform full-coverage contact
uniqueness and strict increase: **OPEN**"),
`STORAGE_REPRESENTATION_BRANCH_VERDICT.md` §9 ("the final promotion gate is now
… build a uniform, full-coverage, nonsmooth contact tiling"), a fail-closed
`receipt_ii_certificate_schema.json` marked `SCHEMA_ONLY_NOT_A_CERTIFICATE`, a
`validate_receipt_ii_certificate.py` with nothing to validate, and a `README.md`
stating the package does **not** contain a completed Receipt (ii) — against two
supersession notes and a completion document that close it by a completely
different route. A reader cannot tell the status from the package. This must be
reconciled (retire or clearly mark the superseded documents and dead artifacts)
before anything is published.

**F6 (verifier scope, W9).** All three authors' verifiers PASS when I run them,
and I reproduce every number they print. But they check *algebraic identities
only*: derivative-jump identity, reflection identity, Monge identity,
subgradient identity, the 2×2 determinant, `K_xK_u=1`, and the two exact
endpoint margins. **None of them tests a single one of the theorem's logical
steps** — not the minorant construction, not the no-kink argument, not the
envelope binding, not the limiting weld. The package is honest about this, but a
public reader will assume otherwise from the "PASS" banners. The published
artifact README must say what the scripts do and do not certify.

**F7 (normalisation, independently reconfirmed).** My own see-saw over the
functional as built from the 1197 reparameterisation gives **exactly
`0.25000000`** at local dimension 3, matching the literature statement that the
I3322 maximum is `0.25` in `C²⊗C²` and `C³⊗C³` while the true maximum is
`≈ 0.2509`. This is an independent confirmation, from outside the repository,
that the `1/4` in the quarter ceiling and the `S ≈ 0.25088` of the certificates
live in the same normalisation. Round 1's framing correction (classical bound
`0`, `1/4` = qubit ceiling) stands and is already correct in the repository.

**F8 (priority).** A literature sweep finds no resolution of the Pál–Vértesi
conjecture. It remains listed as open; the 2010 paper's conjecture is precisely
"measuring finite dimensional quantum systems is not enough to achieve the true
quantum maximum". So the theorem, if published, is new.

---

## 8. Findings ledger

| ID | Severity | Finding |
|---|---|---|
| **W1** | **Blocking for the text; repaired here** | Convex minorant built on an unjustified "endpoint-excluded compact source interval". Replace by `D=(-1,1)`; add the lemma `C ≥ g(0) > 0`. |
| **W2** | Must fix | §3's chord justification of (3.1) is invalid on a non-compact domain. Replace by the affine-minorant one-liner. |
| **W3** | Must fix | §4's "the chord between its boundary contact points" likewise. Replace by the direct lifting argument. |
| **W4** | Should fix | §5's "active **exactly when** `u ∈ ∂H(x)`" — only "⟹" holds and only "⟹" is used. |
| **W5** | Recommended | Publish the strengthened form: at any contact point `C'_-=C'_+=H'`, so a strict downward corner of `C` is never active. |
| **W6** | Should fix | Assembly V1's limiting weld needs the explicit symmetric spectral cut-off `Π` for the norm-convergence step. |
| **W7** | **Binding on public wording** | See §9. |
| **W8** | Must fix before publication | Package ships mutually contradictory status documents and dead Receipt-(ii) artifacts. |
| **W9** | Must fix before publication | Artifact README must state that the verifiers check algebraic identities only. |
| **W10** | Minor | The completion document cites `Q_127` (Sprint 1288); the current receipt is Sprint 1292's dimension-255 bound. |

None of W1–W10 is a mathematical obstruction. W1 is the only one that changes
the proof rather than the prose, and its repair is forced, short, and verified.

---

## 9. THE THEOREM I SIGN

Conditional on W1–W4 and W6 being executed as specified above, I certify:

> **Theorem (N).** Let `I` denote the I3322 Bell functional in the
> Collins–Gisin normalisation used throughout the repository (classical bound
> `0`; qubit and qutrit maximum exactly `1/4`), and let
>
> ```text
> S := ω_tensor(I3322) = ω_commuting(I3322)
> ```
>
> be its quantum supremum, certified to lie in
> `(0.2508753845015185, 0.250875388108398]`.
> Then **no finite-dimensional quantum strategy attains `S`**: for every finite
> dimension `d`, every state `ρ` on `C^d ⊗ C^d` (pure or mixed) and every triple
> of binary measurements per party (projective or POVM),
>
> ```text
> ⟨I⟩_ρ < S.
> ```
>
> Equivalently, `sup` over finite-dimensional strategies is approached but never
> reached, and the finite-dimensional quantum correlation set `C_q(3,3;2,2)` is
> not closed.

This is the operative content of the Pál–Vértesi conjecture (2010).

**Exact dependency list.**

*Analytic, in the round-3 package (all audited here):*
1. Assembly V1 Theorem 1 — limiting-weld substitute (subsequential limit `g` of
   `g_{q_n}`; uniform bound, `3/2`-Lipschitz, Arzelà–Ascoli; interior
   positivity; passage of the weld on the finite occupied interior spectrum,
   **with W6's spectral cut-off**).
2. Assembly V1 Receipt (iii) — exact endpoint margins `m_±` and the uniform
   endpoint `R_0`-gap `≥ m_±/2`, for all `q ≤ S_+`.
3. `CRITICAL_ZERO_SET_REDUCTION` §2 (concavity), §4 (reflection-gluing
   `K ≥ 1`), §5 (zero-set localisation), §6 (strict Monge).
   *(Theorem 1.1 is **not** on the critical path — F3.)*
4. `CONVEX_ENVELOPE…COMPLETION` §2 (downward corners), §3–§5 (envelope
   reduction, no-kink, horizontal plateau exclusion) **as repaired by W1–W4**,
   §6 (dual-tie involution, vertical plateau exclusion), §7 (strict graph).

*Repository, at HEAD:*
5. Sprint 1197 — Bell-operator reparameterisation, CS fibres,
   `‖B_3-I/2‖ ≤ 1/2` determinant. *(Independently replicated in `r3_carrier.py`.)*
6. Sprint 1287 — generic operator weld: any positive continuous Bellman-feasible
   `G` at `q` yields `qI-B = R_0+R_A+R_B ⪰ 0`. *(Verifier run.)*
7. Sprint 1295 — `P = S`; the terminal-pivot storage `g_q` for every `q>S` with
   `g_q ≥ q-S`, Bellman feasibility, and the common modulus of continuity; and
   the Pál–Vértesi principal-block padding. *(Verifier run.)*
8. Sprint 1206 — the finite Pál–Vértesi block-to-Jacobi identity, giving
   `ω_tensor ≥ S`. *(Verifier run **and independently replicated** in
   `r3_carrier.py`: exact agreement at `n = 5…31` for random label words. Only
   the **finite** identity is used; the bi-infinite profile and `ℓ²` tail, which
   remain analytic inputs from the decertified Sprint 1195, are **not**.)*
9. Sprint 1294 — exact 25,601-knot rational witness: `S ≤ 0.250875388108398`.
   *(Verifier run; `certificate_closed: true`.)*
10. Sprint 1292 — exact 255-dimensional strategy: `S > 0.2508753845015185 > 1/4`.
    *(Verifier run; all gates pass.)*
11. Sprint 1198 — equality-kernel mechanism: unitary transports and totality,
    component equations (10a), one-decreasing-bijection, multiplicity-uniform
    amplitude elimination, quarter ceiling (13)–(20). *(Audited in round 2;
    (16)–(20) re-verified symbolically here.)*

*Standard mathematics:* Naimark dilation / extreme-effect replacement;
Arzelà–Ascoli; operator monotonicity of the Schur complement; joint spectral
theory for a commuting pair; elementary convex analysis on an open interval.

**Explicitly NOT used:** the Sprint-1195 global Bellman fixed point and its
amplitude normalisation (decertified by Sprint 1285); any reflected left wing;
any `C¹` or curvature assumption on the storage; global uniqueness of the first
Bellman contact; any interiority bound on `range(P)`; attainment of the
Sprint-1295 infimum at `S`; the DOC-C shooting/heteroclinic/relabeling
artifacts; spatial attainment; the conditional dimension-necessity campaign
(Sprints 1208–1265), whose `Q_d` localisation gap remains open and is untouched
by this theorem.

**W7 — binding conditions on the public wording.**

1. The claim is **nonattainment of the quantum supremum in finite dimension**.
   The public text must **not** assert that `S` equals the historical
   Pál–Vértesi decimal `0.2508753845139765…`, nor that the Pál–Vértesi
   construction is optimal. `S` is identified only to within
   `(0.2508753845015185, 0.250875388108398]` (width `3.61e-9`). The half of the
   2010 conjecture that is resolved is the finite-dimensional half.
2. The normalisation must be stated: classical bound `0`, qubit/qutrit maximum
   `1/4`, `S ≈ 0.2509`. Presenting `1/4` as "the classical bound" (as the round-1
   circulated statement did) is false and would misrepresent the theorem.
3. The asymmetry of the active predecessor range (`≈ [-0.8936, +0.8981]`) versus
   the `u ↦ -u` symmetry of a hypothetical occupied orbit must be stated
   explicitly, as Assembly V2 §1.3 already requires — they are different
   objects, and the left wing must never be described as reflected.
4. The artifact scripts must be described as algebraic-identity guards, not as
   verifications of the theorem (W9).
5. The nonclosure corollary may be stated, but its dependence on
   `sup_{C_q} = S` (Sprints 1287/1295) should be cited, and it must not be
   conflated with the stronger `C_qs \ C_q` separation, which rests on spatial
   attainment and is **not** promoted by this audit.

---

## 10. Reproduction

Authors' artifacts (run in the package, all PASS, all numbers reproduced):

```
python artifacts/convex_envelope_plateau_exclusion_verify.py
python artifacts/critical_zero_set_reduction_verify.py
python artifacts/four_receipts_at_S_endpoint_and_scout.py
```

Repository verifiers (run in `repocopy/`, never in place):

```
foundational-sprint-1287/bellman_operator_weld_verify.py         all gates pass
foundational-sprint-1287/exact_rational_bellman_subsolution.py   all gates pass
foundational-sprint-1292/exact_dimension_255_lower_bound.py      all gates pass
foundational-sprint-1294/exact_endpoint_clustered_threshold.py   certificate_closed
foundational-sprint-1295/bellman_path_equivalence_verify.py      all gates pass
foundational-sprint-1206/spatial_realization_verify.py           all gates pass
foundational-sprint-1198/equality_kernel_verify.py               all gates pass
```

Referee's own scripts:

```
python r3_storage.py    # independent critical storage; concavity, K>=1, R0>=0,
                        # endpoint gaps, C bounded, predecessor geometry
python r3_envelope.py   # countermodel search for an interior kink of H
python r3_kink.py       # corner-sign lemma; knots are never contact points
python r3_exact.py      # exact re-derivation of m_+, m_-, the R0-gap step,
                        # monotonicity in q and u, C >= g(0), (16)-(20)
python r3_carrier.py    # independent replication of the 1197 reparameterisation
                        # and the PV block-to-Jacobi identity; d=3 ceiling 0.25
```

---

## 11. Closing note

Three rounds: an unsound restoration (round 1), a valid mechanism with three of
four receipts missing (round 2), and now a complete chain. The decisive move was
not closing the receipts I demanded but **weakening them until they were true** —
the equality module is obtained by a limiting substitute rather than by attaining
an infimum, contact uniqueness is replaced by plateau exclusion on the zero
locus, and interiority of `range(P)` is dropped entirely. Each replacement is
strictly weaker and strictly sufficient. That is the right shape for a repair,
and it is why I am signing.

The one residue is the phrase "endpoint-excluded compact source interval",
carried over from the abandoned tiling route into an argument that neither needs
nor is entitled to it. Fix it, fix the package's contradictory status documents,
and this is a proof.
