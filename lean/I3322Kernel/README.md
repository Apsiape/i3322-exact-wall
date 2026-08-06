# I3322Kernel — machine-checked algebraic cores

Lean 4 + Mathlib formalization of the small, self-contained algebraic
cores of the paper *"The I₃₃₂₂ quantum value is attained spatially but
not in finite dimension"* (`paper/resolution.pdf`, this repository).

**Claim boundary, stated first:** these are the paper's *algebraic
cores*, not its theorems. The measure-theoretic chain (weak-\* limits,
disintegration, RN transport), the operator-algebraic chain (kernel
equations, W-operator anticommutation, the reduction of a
finite-dimensional maximizer to the two-variable form), and the
interval-arithmetic window certification are **not** formalized here.
What is formalized is exactly the set of displayed formulas a referee
would otherwise check by hand.

## Contents

| File | Lemma | Paper statement formalized |
|---|---|---|
| `I3322Kernel/QuarterCeiling.lean` | L1 | The amplitude-elimination chain (Sprint 1198 (16)–(20)): the expansion identity, the discriminant ring identity, the bound `(b_x+b_u)² + (x−u)²/4 ≤ 1−xu`, the scalar ceiling `−t+√t ≤ 1/4` for `t ≥ 0`, and the conclusion `xu−1+√(…) ≤ 1/4`. Plus `1/4 <` the certified window's lower endpoint (exact rationals). Together: any *closed* (`a = b`) strategy value is capped strictly below `S`. |
| `I3322Kernel/EndpointMargins.lean` | L2 | The exact endpoint margins of Receipt (iii): with `q = 250875388108398/10¹⁵`, `r = 1/10`, the margins equal `23686917837403/3008753881083980` and `274562305945801/4008753881083980`, both `> 0`, both exceeding the paper's displayed decimals (`0.00787`, `0.0684`), and both formulas antitone in the level on `(1/4, ∞)` — so the certified upper endpoint is the worst case over the window. |
| `I3322Kernel/FiniteClosure.lean` | L4 | The finite-closure lemma: a strictly monotone self-map of a finite linear order is the identity; hence two strictly antitone bijections of a finite linear order coincide. This is the single point where finite dimension enters Theorem (N). |

L3 (the corner-sign lemma for one-sided derivatives of concave
functions) is commissioned but not yet formalized.

## Verification

```
lake exe cache get   # prebuilt Mathlib oleans
lake build           # must complete with no errors, no sorry
```

Axiom hygiene: every theorem should report only the standard axioms
(`propext`, `Classical.choice`, `Quot.sound`) under `#print axioms`.

Toolchain pinned in `lean-toolchain`; Mathlib pinned in `lakefile.toml`.
