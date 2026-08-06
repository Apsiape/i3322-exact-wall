/-
L1 — The quarter-ceiling algebra (machine-checked).

Formalizes Sprint 1198 (16)–(20), the paper's central displayed chain:
for x, u ∈ [-1, 1] with b_x = √(1-x²)/2, b_u = √(1-u²)/2, t = 1 - x·u:

  (a) (b_x+b_u)² + (x-u)²/4 = (1 - x·u + √((1-x²)(1-u²)))/2
  (b) (1-x·u)² - (1-x²)(1-u²) = (x-u)²          [pure ring identity]
  (c) hence (b_x+b_u)² + (x-u)²/4 ≤ t
  (d) -t + √t ≤ 1/4 for t ≥ 0
  (e) conclusion: x·u - 1 + √((b_x+b_u)² + (x-u)²/4) ≤ 1/4

This is the amplitude-elimination ceiling: any closed (a = b)
finite-dimensional strategy has value ≤ 1/4 < S.

CLAIM BOUNDARY: this is the algebraic core only. The reduction of a
finite-dimensional maximizer to this two-variable form (kernel
equations, W-operator anticommutation, the closure step) is NOT
formalized here.
-/
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

namespace I3322Kernel

open Real

variable {x u : ℝ}

/-- (b): the discriminant identity — a pure ring identity. -/
theorem discriminant_identity (x u : ℝ) :
    (1 - x * u) ^ 2 - (1 - x ^ 2) * (1 - u ^ 2) = (x - u) ^ 2 := by
  ring

/-- (a): the amplitude expansion. -/
theorem amplitude_expansion (hx : x ^ 2 ≤ 1) (hu : u ^ 2 ≤ 1) :
    (Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
      + (x - u) ^ 2 / 4
    = (1 - x * u + Real.sqrt ((1 - x ^ 2) * (1 - u ^ 2))) / 2 := by
  have hx' : (0 : ℝ) ≤ 1 - x ^ 2 := by linarith
  have hu' : (0 : ℝ) ≤ 1 - u ^ 2 := by linarith
  have hxs : Real.sqrt (1 - x ^ 2) ^ 2 = 1 - x ^ 2 := Real.sq_sqrt hx'
  have hus : Real.sqrt (1 - u ^ 2) ^ 2 = 1 - u ^ 2 := Real.sq_sqrt hu'
  have hmul : Real.sqrt (1 - x ^ 2) * Real.sqrt (1 - u ^ 2)
      = Real.sqrt ((1 - x ^ 2) * (1 - u ^ 2)) :=
    (Real.sqrt_mul hx' _).symm
  nlinarith [hxs, hus, hmul]

/-- The square-root comparison at the heart of (c):
    √((1-x²)(1-u²)) ≤ 1 - x·u on the square. -/
theorem sqrt_prod_le (hx : x ^ 2 ≤ 1) (hu : u ^ 2 ≤ 1) :
    Real.sqrt ((1 - x ^ 2) * (1 - u ^ 2)) ≤ 1 - x * u := by
  have ht : (0 : ℝ) ≤ 1 - x * u := by nlinarith
  have hsq : (1 - x ^ 2) * (1 - u ^ 2) ≤ (1 - x * u) ^ 2 := by
    nlinarith [sq_nonneg (x - u)]
  calc Real.sqrt ((1 - x ^ 2) * (1 - u ^ 2))
      ≤ Real.sqrt ((1 - x * u) ^ 2) := Real.sqrt_le_sqrt hsq
    _ = 1 - x * u := by rw [Real.sqrt_sq ht]

/-- (c): the amplitude bound. -/
theorem amplitude_le (hx : x ^ 2 ≤ 1) (hu : u ^ 2 ≤ 1) :
    (Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
      + (x - u) ^ 2 / 4
    ≤ 1 - x * u := by
  rw [amplitude_expansion hx hu]
  have := sqrt_prod_le hx hu
  linarith

/-- (d): the scalar quarter ceiling — for t ≥ 0, -t + √t ≤ 1/4. -/
theorem scalar_quarter_ceiling {t : ℝ} (ht : 0 ≤ t) :
    -t + Real.sqrt t ≤ 1 / 4 := by
  have hs : Real.sqrt t ^ 2 = t := Real.sq_sqrt ht
  nlinarith [sq_nonneg (Real.sqrt t - 1 / 2)]

/-- (e): the quarter ceiling — the paper's displayed conclusion.
    Any closed strategy value is capped at 1/4. -/
theorem quarter_ceiling (hx : x ^ 2 ≤ 1) (hu : u ^ 2 ≤ 1) :
    x * u - 1
      + Real.sqrt
          ((Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
            + (x - u) ^ 2 / 4)
    ≤ 1 / 4 := by
  set E := (Real.sqrt (1 - x ^ 2) / 2 + Real.sqrt (1 - u ^ 2) / 2) ^ 2
    + (x - u) ^ 2 / 4 with hE
  have hEt : E ≤ 1 - x * u := amplitude_le hx hu
  have ht : (0 : ℝ) ≤ 1 - x * u := by nlinarith
  have hsqrt : Real.sqrt E ≤ Real.sqrt (1 - x * u) := Real.sqrt_le_sqrt hEt
  have hceil : -(1 - x * u) + Real.sqrt (1 - x * u) ≤ 1 / 4 :=
    scalar_quarter_ceiling ht
  linarith

/-- Strictness against the window: 1/4 is strictly below every point of
    the certified window, whose lower endpoint is
    0.2508753845015185 = 2508753845015185/10^16. -/
theorem quarter_lt_window_lower :
    (1 : ℚ) / 4 < 2508753845015185 / 10 ^ 16 := by
  norm_num

end I3322Kernel
