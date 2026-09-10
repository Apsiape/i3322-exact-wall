/-
Selected cores of the replacement lower proof, 2026-09-10.
The potential is an explicit hypothesis, NOT an assumed conclusion about
every graph. Its existence from SCC separation, the analytic predictor,
quantum response estimates, and their composition are not formalized here.
No theorem below proves the full I3322 dimension bound by itself.
-/
import Mathlib.Tactic

namespace I3322Kernel.WeightedFlow

/-- Every occupied edge contributes; there is no path/branch selection. -/
theorem all_edges {V : Type*} [Fintype V]
    (w : V → V → ℝ) (R f : V → ℝ)
    (hw : ∀ x y, 0 ≤ w x y)
    (hf : ∀ x y, 0 < w x y → 1 ≤ R x * f x - f y) :
    (∑ x, ∑ y, w x y) ≤
      ∑ x, ∑ y, w x y * (R x * f x - f y) := by
  apply Finset.sum_le_sum
  intro x _
  apply Finset.sum_le_sum
  intro y _
  by_cases hz : w x y = 0
  · simp [hz]
  · have hp : 0 < w x y := lt_of_le_of_ne (hw x y) (Ne.symm hz)
    nlinarith [hf x y hp]

/-- Incoming and outgoing sums give the correctly oriented residual. -/
theorem balance_identity {V : Type*} [Fintype V]
    (w : V → V → ℝ) (R f : V → ℝ) :
    (∑ x, ∑ y, w x y * (R x * f x - f y)) =
      ∑ x, f x * (R x * (∑ y, w x y) - ∑ y, w y x) := by
  simp_rw [mul_sub, Finset.sum_sub_distrib]
  congr 1
  · apply Finset.sum_congr rfl
    intro x _
    rw [← Finset.sum_mul]
    ring
  · rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro x _
    rw [← Finset.sum_mul]
    ring

/-- Dual l-infinity/l-one estimate; signed potentials are allowed. -/
theorem signed_work_bound {V : Type*} [Fintype V]
    (f d : V → ℝ) (B : ℝ) (hf : ∀ x, |f x| ≤ B) :
    (∑ x, f x * d x) ≤ B * ∑ x, |d x| := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro x _
  calc f x * d x ≤ |f x * d x| := le_abs_self _
    _ = |f x| * |d x| := abs_mul _ _
    _ ≤ B * |d x| := mul_le_mul_of_nonneg_right (hf x) (abs_nonneg _)

/-- Quantitative flow inequality, conditional on a bounded edge potential. -/
theorem mass_le_residual {V : Type*} [Fintype V]
    (w : V → V → ℝ) (R f : V → ℝ) (B : ℝ)
    (hw : ∀ x y, 0 ≤ w x y)
    (he : ∀ x y, 0 < w x y → 1 ≤ R x * f x - f y)
    (hf : ∀ x, |f x| ≤ B) :
    (∑ x, ∑ y, w x y) ≤
      B * ∑ x, |R x * (∑ y, w x y) - ∑ y, w y x| := by
  calc _ ≤ _ := all_edges w R f hw he
    _ = _ := balance_identity w R f
    _ ≤ _ := signed_work_bound f _ B hf

/-- Low-cycle internal edge, with a negative potential. -/
theorem low_internal (R c g : ℝ) (hc : 0 < c)
    (hr : R ≤ 1 - c) (hg : 1 / c ≤ g) :
    1 ≤ R * (-g) - (-g) := by
  have hcg : 1 ≤ c * g := (div_le_iff₀ hc).mp hg |>.trans_eq (mul_comm g c)
  have hg0 : 0 ≤ g := le_trans (le_of_lt (one_div_pos.mpr hc)) hg
  nlinarith

/-- High-cycle internal edge, with a positive potential. -/
theorem high_internal (R c f : ℝ) (hc : 0 < c)
    (hr : 1 + c ≤ R) (hf : 1 / c ≤ f) :
    1 ≤ R * f - f := by
  have hcf : 1 ≤ c * f := (div_le_iff₀ hc).mp hf |>.trans_eq (mul_comm f c)
  have hf0 : 0 ≤ f := le_trans (le_of_lt (one_div_pos.mpr hc)) hf
  nlinarith

/-- Edge entering the negative region; forward closure forbids its reverse. -/
theorem entering_low (R rmin f g : ℝ) (hrmin : 0 < rmin)
    (hr : rmin ≤ R) (hf : 1 / rmin ≤ f) (hg : 0 ≤ g) :
    1 ≤ R * f - (-g) := by
  have hprod : 1 ≤ f * rmin := (div_le_iff₀ hrmin).mp hf
  have hf0 : 0 ≤ f := le_trans (le_of_lt (one_div_pos.mpr hrmin)) hf
  nlinarith

/-- The three positive terms in the final deficit assembly cannot all be small. -/
theorem assembly_alternative (a b c : ℝ) (h : 1 - a ≤ b + c) :
    1 / 2 ≤ a ∨ 1 / 4 ≤ b ∨ 1 / 4 ≤ c := by
  by_contra hn
  push Not at hn
  linarith

/-- Coupling-weighted boundary flux pays the two endpoint masses. -/
theorem weighted_endpoint_payment (x y left right k : ℝ)
    (hx : x ≤ k * left) (hy : y ≤ k * right) :
    x + y ≤ k * (left + right) := by nlinarith

/-- Strict rounding slack, not a rounded equality at the limiting exponent. -/
theorem upper_rounding_slack :
    (2 : ℝ) / (8367827985 / 100000000000) < 239010650 / 10000000 := by
  norm_num

end I3322Kernel.WeightedFlow
