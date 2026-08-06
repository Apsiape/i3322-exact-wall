/-
L2 — The exact endpoint margins (machine-checked).

Formalizes the endpoint-margin receipts of the I3322 nonattainment
certificate (`theorem-N-four-receipts-at-S`, Receipt (iii)): with the
certified upper window endpoint `q = 250875388108398/10^15` and probe
width `r = 1/10`, the two endpoint-line margins are the stated exact
rationals and are strictly positive; and both margin formulas are
antitone in the level `q` on `(1/4, ∞)`, so the stated `q` is the
worst case over the certified window.

CLAIM BOUNDARY: these are the algebraic cores only. The analytic and
measure-theoretic chains of the theorems are NOT formalized here.
-/
import Mathlib.Tactic

namespace I3322Kernel

/-- The certified upper endpoint of the value window, as an exact rational. -/
def q : ℚ := 250875388108398 / 10 ^ 15

/-- The probe width. -/
def r : ℚ := 1 / 10

/-- Right-endpoint margin formula. -/
def mPlus : ℚ := r * ((2 - r) / (4 * q + 2 * r) - 3 / 2)

/-- Left-endpoint margin formula. -/
def mMinus : ℚ := r * (-(1 / 2) + (2 - r) / (4 * q + 6 * r))

/-- The right margin equals the exact rational of the certificate. -/
theorem mPlus_eq : mPlus = 23686917837403 / 3008753881083980 := by
  norm_num [mPlus, q, r]

/-- The left margin equals the exact rational of the certificate. -/
theorem mMinus_eq : mMinus = 274562305945801 / 4008753881083980 := by
  norm_num [mMinus, q, r]

/-- The right margin is strictly positive. -/
theorem mPlus_pos : 0 < mPlus := by
  rw [mPlus_eq]; norm_num

/-- The left margin is strictly positive. -/
theorem mMinus_pos : 0 < mMinus := by
  rw [mMinus_eq]; norm_num

/-- The paper's displayed decimal lower bound for the right margin. -/
theorem mPlus_gt : (787 : ℚ) / 100000 < mPlus := by
  rw [mPlus_eq]; norm_num

/-- The paper's displayed decimal lower bound for the left margin. -/
theorem mMinus_gt : (684 : ℚ) / 10000 < mMinus := by
  rw [mMinus_eq]; norm_num

/-- Right-margin formula as a function of the level. -/
def mPlusAt (s : ℚ) : ℚ := r * ((2 - r) / (4 * s + 2 * r) - 3 / 2)

/-- Left-margin formula as a function of the level. -/
def mMinusAt (s : ℚ) : ℚ := r * (-(1 / 2) + (2 - r) / (4 * s + 6 * r))

/-- The right margin is antitone in the level on `(1/4, ∞)`:
    the certified upper endpoint is the worst case over the window. -/
theorem mPlusAt_antitone {s₁ s₂ : ℚ} (h₁ : 1 / 4 < s₁) (h : s₁ ≤ s₂) :
    mPlusAt s₂ ≤ mPlusAt s₁ := by
  unfold mPlusAt r
  have hd₁ : (0 : ℚ) < 4 * s₁ + 2 * (1 / 10) := by linarith
  have hd₂ : (0 : ℚ) < 4 * s₂ + 2 * (1 / 10) := by linarith
  have key : (2 - 1 / 10) / (4 * s₂ + 2 * (1 / 10))
      ≤ (2 - 1 / 10) / (4 * s₁ + 2 * (1 / 10)) := by
    apply div_le_div_of_nonneg_left (by norm_num) hd₁
    linarith
  linarith

/-- The left margin is antitone in the level on `(1/4, ∞)`. -/
theorem mMinusAt_antitone {s₁ s₂ : ℚ} (h₁ : 1 / 4 < s₁) (h : s₁ ≤ s₂) :
    mMinusAt s₂ ≤ mMinusAt s₁ := by
  unfold mMinusAt r
  have hd₁ : (0 : ℚ) < 4 * s₁ + 6 * (1 / 10) := by linarith
  have hd₂ : (0 : ℚ) < 4 * s₂ + 6 * (1 / 10) := by linarith
  have key : (2 - 1 / 10) / (4 * s₂ + 6 * (1 / 10))
      ≤ (2 - 1 / 10) / (4 * s₁ + 6 * (1 / 10)) := by
    apply div_le_div_of_nonneg_left (by norm_num) hd₁
    linarith
  linarith

end I3322Kernel
