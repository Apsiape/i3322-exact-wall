/-
Combinatorial cores of the dimension-rate analysis (machine-checked).

Two finite lemmas:

1. `staircase_card_le` — an inversion-free bipartite relation on
   `Fin m × Fin n` has at most `m + n - 1` edges. Proof: on an
   inversion-free edge set the coordinate sum `(a,c) ↦ a + c` is
   injective. This is the edge-budget core: after far-inversion
   deletion, each parity class of the retained cell support is
   inversion-free, so its size is controlled linearly by the number of
   occupied marginal cells.

2. `min_point_pseudocycle` — a cyclic δ-pseudo-orbit of a monotone map
   on ℝ contains a δ-approximate fixed point at its minimum. This is
   the exactification core: a repeated cell cycle with uniformly small
   step defect localizes an approximate fixed point of the response
   map with the SAME accuracy, independent of cycle length.

Plus the elementary product bound `prod_le_two_pow_sum` used by the
branch-selection estimate (∏ D_k ≤ 2^{Σ D_k}).

CLAIM BOUNDARY: these are the combinatorial cores only. The response
theory, transport typing, and assembly are NOT formalized here.
-/
import Mathlib.Tactic

namespace I3322Kernel

/-- On an inversion-free edge set, the coordinate sum is injective:
    distinct edges have distinct sums. -/
theorem staircase_sum_injOn {m n : ℕ}
    (E : Finset (Fin m × Fin n))
    (hE : ∀ p ∈ E, ∀ q ∈ E, p.1 < q.1 → p.2 ≤ q.2) :
    Set.InjOn (fun p : Fin m × Fin n => (p.1 : ℕ) + (p.2 : ℕ)) E := by
  intro p hp q hq hsum
  have hsum' : (p.1 : ℕ) + (p.2 : ℕ) = (q.1 : ℕ) + (q.2 : ℕ) := hsum
  clear hsum
  by_contra hne
  -- Distinct edges: compare first coordinates.
  rcases lt_trichotomy p.1 q.1 with h1 | h1 | h1
  · have h2 : p.2 ≤ q.2 := hE p hp q hq h1
    have : (p.1 : ℕ) + p.2 < (q.1 : ℕ) + q.2 :=
      Nat.add_lt_add_of_lt_of_le h1 h2
    omega
  · -- Equal first coordinates: second coordinates must differ.
    have h2 : p.2 ≠ q.2 := by
      intro h2eq
      exact hne (Prod.ext h1 h2eq)
    have : (p.2 : ℕ) ≠ (q.2 : ℕ) := fun hc => h2 (Fin.ext hc)
    have h1' : (p.1 : ℕ) = q.1 := congrArg Fin.val h1
    omega
  · have h2 : q.2 ≤ p.2 := hE q hq p hp h1
    have : (q.1 : ℕ) + q.2 < (p.1 : ℕ) + p.2 :=
      Nat.add_lt_add_of_lt_of_le h1 h2
    omega

/-- The staircase edge budget: an inversion-free bipartite relation on
    `Fin m × Fin n` has at most `m + n - 1` edges. -/
theorem staircase_card_le {m n : ℕ}
    (E : Finset (Fin m × Fin n))
    (hE : ∀ p ∈ E, ∀ q ∈ E, p.1 < q.1 → p.2 ≤ q.2) :
    E.card ≤ m + n - 1 := by
  rcases E.eq_empty_or_nonempty with rfl | ⟨p₀, hp₀⟩
  · simp
  -- The sum map is injective on E and lands in {0, …, m+n-2}.
  have hminj := staircase_sum_injOn E hE
  have hmn : 0 < m ∧ 0 < n := ⟨Fin.pos_iff_nonempty.mpr ⟨p₀.1⟩,
    Fin.pos_iff_nonempty.mpr ⟨p₀.2⟩⟩
  have hcard : E.card = (E.image (fun p : Fin m × Fin n =>
      (p.1 : ℕ) + (p.2 : ℕ))).card :=
    (Finset.card_image_of_injOn hminj).symm
  have hsub : E.image (fun p : Fin m × Fin n => (p.1 : ℕ) + (p.2 : ℕ))
      ⊆ Finset.range (m + n - 1) := by
    intro s hs
    obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hs
    have h1 : (p.1 : ℕ) ≤ m - 1 := Nat.le_sub_one_of_lt p.1.isLt
    have h2 : (p.2 : ℕ) ≤ n - 1 := Nat.le_sub_one_of_lt p.2.isLt
    have := hmn.1; have := hmn.2
    exact Finset.mem_range.mpr (by omega)
  calc E.card = _ := hcard
    _ ≤ (Finset.range (m + n - 1)).card := Finset.card_le_card hsub
    _ = m + n - 1 := Finset.card_range _

/-- Elementary branch-selection bound: a product of positive degrees is
    at most two to their sum. -/
theorem prod_le_two_pow_sum (s : Finset ℕ) (D : ℕ → ℕ) :
    ∏ k ∈ s, D k ≤ 2 ^ (∑ k ∈ s, D k) := by
  calc ∏ k ∈ s, D k ≤ ∏ k ∈ s, 2 ^ (D k) :=
        Finset.prod_le_prod (fun _ _ => Nat.zero_le _)
          (fun k _ => (Nat.lt_two_pow_self).le)
    _ = 2 ^ (∑ k ∈ s, D k) := by
        rw [Finset.prod_pow_eq_pow_sum]

/-- Rate-route band algebra (i): the elementary ceiling
    s(1-s) ≤ 1/4 for every real s. -/
theorem s_mul_one_sub_s_le_quarter (s : ℝ) : s * (1 - s) ≤ 1 / 4 := by
  nlinarith [sq_nonneg (s - 1 / 2)]

/-- Rate-route band algebra (ii): the band identity. For t² ≤ 1 with
    s = √(1-t²): D(t) + 2·b(t) = t² - 1 + s = s(1-s). -/
theorem band_identity {t : ℝ} (ht : t ^ 2 ≤ 1) :
    t ^ 2 - 1 + Real.sqrt (1 - t ^ 2)
      = Real.sqrt (1 - t ^ 2) * (1 - Real.sqrt (1 - t ^ 2)) := by
  have hs : Real.sqrt (1 - t ^ 2) ^ 2 = 1 - t ^ 2 :=
    Real.sq_sqrt (by linarith)
  nlinarith [hs]

/-- Rate-route band algebra (iii): the band quarter ceiling.
    For t² ≤ 1: D(t) + 2·b(t) = t² - 1 + √(1-t²) ≤ 1/4. -/
theorem band_quarter_ceiling {t : ℝ} (ht : t ^ 2 ≤ 1) :
    t ^ 2 - 1 + Real.sqrt (1 - t ^ 2) ≤ 1 / 4 := by
  rw [band_identity ht]
  exact s_mul_one_sub_s_le_quarter _

/-- Rate-route band algebra (iv): the amplitude bound b(t) ≤ 1/2. -/
theorem amplitude_b_le_half {t : ℝ} (ht : t ^ 2 ≤ 1) :
    Real.sqrt (1 - t ^ 2) / 2 ≤ 1 / 2 := by
  have h : Real.sqrt (1 - t ^ 2) ≤ 1 := by
    calc Real.sqrt (1 - t ^ 2) ≤ Real.sqrt 1 :=
          Real.sqrt_le_sqrt (by nlinarith [sq_nonneg t])
      _ = 1 := Real.sqrt_one
  linarith

/-- The minimum-point pseudo-cycle lemma: a cyclic δ-pseudo-orbit of a
    monotone map on ℝ has a δ-approximate fixed point at its minimum.
    Cyclicity is encoded by periodicity `u (k + L) = u k`; the length
    `L` never enters the bound. -/
theorem min_point_pseudocycle
    (f : ℝ → ℝ) (hf : Monotone f)
    (u : ℕ → ℝ) (L : ℕ) (hL : 0 < L)
    (hper : ∀ k, u (k + L) = u k)
    (δ : ℝ)
    (hstep : ∀ k, |u (k + 1) - f (u k)| ≤ δ)
    (j : ℕ) (hmin : ∀ k, u j ≤ u k) :
    |f (u j) - u j| ≤ δ := by
  -- Lower bound: the successor is ≥ the minimum.
  have hsucc := hstep j
  rw [abs_le] at hsucc
  have hlow : u j - δ ≤ f (u j) := by
    have := hmin (j + 1)
    linarith [hsucc.2]
  -- Upper bound: the predecessor (via periodicity) is ≥ the minimum,
  -- and monotonicity transports the step bound back to `u j`.
  have hpred := hstep (j + L - 1)
  have hidx : j + L - 1 + 1 = j + L := by omega
  rw [hidx, hper j, abs_le] at hpred
  have hmono : f (u j) ≤ f (u (j + L - 1)) := hf (hmin (j + L - 1))
  have hhigh : f (u j) ≤ u j + δ := by linarith [hpred.1]
  rw [abs_le]
  constructor <;> linarith

end I3322Kernel
