/-
L4 — The finite-closure lemma (machine-checked).

The single point where finite dimension enters Theorem (N): a finite
linear order admits at most one strictly antitone bijection onto
itself; hence any two such bijections coincide. In the nonattainment
proof this forces the two decreasing equality transports of a
hypothetical finite-dimensional maximizer to be equal (`a = b` on the
occupied support), which activates the quarter-ceiling elimination.

Proof idea: if `a` and `b` are strictly antitone bijections then
`b⁻¹ ∘ a` is a strictly monotone self-map of a finite linear order,
hence the identity (a minimal element of `{z | f z < z}` would map to
a smaller such element) — so `a = b`.

CLAIM BOUNDARY: this is the combinatorial core only.
-/
import Mathlib.Tactic

namespace I3322Kernel

/-- A strictly monotone self-map of a finite linear order is the
    identity. -/
theorem strictMono_self_eq_id {α : Type*} [LinearOrder α] [Fintype α]
    (f : α → α) (hf : StrictMono f) : f = id := by
  have hwf : WellFounded ((· < ·) : α → α → Prop) := Finite.to_wellFoundedLT.wf
  -- Lower bound `y ≤ f y`: a minimal element of `{z | f z < z}` maps
  -- to a strictly smaller element of the same set — contradiction.
  have hle : ∀ y : α, y ≤ f y := by
    intro y
    by_contra hy
    have hyS : f y < y := not_le.mp hy
    obtain ⟨m, hm, hmin⟩ := hwf.has_min {z | f z < z} ⟨y, hyS⟩
    exact hmin (f m) (hf hm) hm
  -- Upper bound `f y ≤ y`: dually, a maximal element of `{z | z < f z}`
  -- maps to a strictly larger element of the same set.
  have hgt : WellFounded ((· > ·) : α → α → Prop) := Finite.to_wellFoundedGT.wf
  have hge : ∀ y : α, f y ≤ y := by
    intro y
    by_contra hy
    have hyS : y < f y := not_le.mp hy
    obtain ⟨m, hm, hmin⟩ := hgt.has_min {z | z < f z} ⟨y, hyS⟩
    exact hmin (f m) (hf hm) hm
  funext x
  exact le_antisymm (hge x) (hle x)

/-- Two strictly antitone bijections of a finite linear order coincide. -/
theorem decreasing_bijections_coincide {α : Type*} [LinearOrder α] [Fintype α]
    {a b : α → α}
    (hb : Function.Bijective b)
    (haa : StrictAnti a) (hba : StrictAnti b) : a = b := by
  -- `g := b⁻¹` is strictly antitone, so `g ∘ a` is strictly monotone.
  obtain ⟨g, hga, hgb⟩ := Function.bijective_iff_has_inverse.mp hb
  have hbg : ∀ z, b (g z) = z := hgb
  have hg : StrictAnti g := by
    intro x y hxy
    rcases lt_trichotomy (g x) (g y) with h | h | h
    · exfalso
      have hlt := hba h
      rw [hbg x, hbg y] at hlt
      exact lt_asymm hxy hlt
    · exfalso
      have heq : x = y := by rw [← hbg x, ← hbg y, h]
      exact hxy.ne heq
    · exact h
  have hmono : StrictMono (g ∘ a) := fun x y hxy => hg (haa hxy)
  have hid : (g ∘ a) = id := strictMono_self_eq_id _ hmono
  funext x
  have hx : g (a x) = x := congrArg (fun h => h x) hid
  calc a x = b (g (a x)) := (hbg (a x)).symm
    _ = b x := by rw [hx]

end I3322Kernel
