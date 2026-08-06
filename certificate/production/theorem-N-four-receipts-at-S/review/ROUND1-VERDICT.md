# Referee verdict — Theorem (N), I3322 finite-dimensional nonattainment

Referee: independent, blinded to authors' working notes. Refutation-first.
Files consulted: `PROOF-UNDER-AUDIT.md`, `DOC-C-CLASSIFICATION.md`,
`DOC-C-CLAIM-LEDGER.md`, `artifacts-inspection-only/*`. Own scripts:
`check3_normalization.py`, `check4_countermodel.py` (plus the pre-existing
`check1.py`, `check2.py` found in the directory).

## Overall verdict

**UNSOUND AS WRITTEN — one decisive gap that carries essentially the entire
theorem. A repair route exists and is identified below, but the repair *is* the
mathematical content of (N), not a formality.**

I am **not** claiming Theorem (N) is false. I am claiming the text does not
prove it. The single inference on which everything rests —

> finite-dimensional maximizer ⟹ the scalar support is a **finite set invariant
> under the total involutions `a` and `b`**

— is asserted in one unproved sentence (DOC-C §1) and is exactly the statement a
truncated chain violates. I exhibit an explicit model in which **every relation
the proof invokes holds exactly** (`a` and `b` decreasing involutions,
`a = P^{-1}(-P(·))`, `b = -id`, `τ = ab` increasing, `τ = P^{-2}` of (17),
`P(-P(u)) = -u` of (2)) and in which a finite support exists with **no
common-return point at all**. In that model §3's contradiction never fires.
See `check4_countermodel.py`, Part II.

The failure mode is not exotic: the finite set is a **truncated open chain**,
which is precisely the shape of the known finite-dimensional Pál–Vértesi
strategies that climb toward `S` (literature: local dimension ≥ 12 is needed to
exceed 1/4; the cited `Q_127` is presumably one of these). The proof must
distinguish "exact maximizer with finite support" from "near-maximizer with
finite support", and the *only* thing that does so is total invariance at the
terminal atoms — which is where the argument is silent.

## Framing error found in the theorem statement itself

The assignment states "Collins–Gisin normalization, where the classical bound is
0.25". **This is false.** For the CG functional actually used by the authors'
own artifact (`bell_symmetry_collider.py`, identical to `check1.py`):

- exhaustive deterministic local maximum = **0** (`check1.py`, `check3`);
- see-saw maximum over projective strategies for local dimension d = 2,3,4,5,6 =
  **0.2500000000** in every case (`check3_normalization.py`);
- literature confirms 1/4 is the **two-qubit** maximum and that local dimension
  ≥ 12 is required to beat it; the classical bound is 0.

So `1/4` is the **qubit ceiling**, not the classical bound. This is not fatal —
it actually makes the architecture *more* coherent (a "common-return / closure"
sector is a qubit-like closed sector, so H's quarter ceiling is the qubit
bound) — but the statement of the theorem as circulated misdescribes its own
normalization, and any reader who accepts "classical bound 0.25" will
misjudge what H is.

## Per attack surface

### 1. Dihedral orbit argument (DOC-C §2) — **SURVIVES-ATTACK**

The mathematics is correct. `a(u) = P^{-1}(-P(u))` is total and well defined
(the range `[-x*,x*]` is symmetric, so `-P(u)` is always in the range), `b` is
total, both are decreasing involutions, `τ = ab` is increasing. If `τ(u) > u`
then monotonicity gives a strictly increasing forward chain, so no return;
periodic ⟹ fixed. Fixed ⟹ `a(b(u)) = u` ⟹ (apply `a`) `a(u) = b(u)`.

Strengthened form the proof actually needs, and which is also true: a **finite**
`⟨a,b⟩`-orbit is a finite `τ`-invariant totally ordered set, and a strictly
increasing self-bijection of a finite chain is the identity, so *every* point of
a finite orbit satisfies `a(u) = b(u)`. Verified exhaustively for n ≤ 7 in
`check4_countermodel.py` Part I (0 non-identity increasing permutations).

Edge cases checked and harmless: orbits meeting a fixed point of `a` or `b`;
even/odd length (a finite orbit has size ≤ 2, since `τ = id` on it); the
endpoints `u = ±1`, where in fact `a(1) = b(1) = -1` automatically, so endpoints
are *already* common-return points at the scalar level — see surface 4 for why
that does **not** dispose of them.

**Caveat that must be recorded:** the lemma is about orbits of the **total**
group action. It says nothing about a set closed under a *partial* transport.
The proof uses it in exactly the partial situation.

### 2. Support-invariance step (DOC-C §1) — **GAP (two sub-gaps), and the
Jacobi-independence claim is REFUTED**

DOC-C §1: "an exact maximizing state annihilates `R_0,R_A,R_B`. Its
state-carrying joint spectral support is therefore contained in the
double-contact zero set Z ... and the two response kernels make the supported
measure class invariant under the `a` and `b` transports. This statement uses
neither finite dimension nor the aligned Jacobi form."

**(2a) The scalar reduction is not licensed as stated.** "Joint spectral
support" presupposes a commuting family of self-adjoint operators whose joint
spectrum carries the coordinate pair `(P(u), u)`. For an arbitrary
finite-dimensional maximizer the natural operators (`A_1,A_2,A_3`,
`B_1,B_2,B_3`) do **not** commute — non-commutation is the whole point of I3322
— and no operator is named anywhere in DOC-C or the proof whose spectral
measure is the "scalar spectral measure". Getting from `R_A ψ = 0` (a kernel
membership) to "spectral support ⊆ Z" requires `R_A = f(X)` for a single
self-adjoint `X` with zero set `Z`. That identification is available in the
aligned Jacobi/tridiagonal presentation and nowhere else in these documents.

**Missing statement (2a):** *For every finite-dimensional maximizer there exist
commuting self-adjoint `X_A`, `X_B` (or a single `X`) on the occupied block such
that `R_0, R_A, R_B` are functions of them, and such that the maximizer is
unitarily equivalent to one in aligned Jacobi form with respect to `X`.*

The claim "uses neither finite dimension nor the aligned Jacobi form" is
**refuted by the proof's own language**: `PROOF-UNDER-AUDIT` §3 writes "forces
every occupied **edge** into the critical equality kernels". "Edge" is a Jacobi
off-diagonal. The argument is stated in the Jacobi form while claiming
independence from it.

**(2b) Invariance is asserted, never derived, and totality is the crux.** "the
two response kernels make the supported measure class invariant" is a single
sentence with no derivation. What a kernel relation actually delivers is a
*recurrence*: the three-term relation at an occupied site links neighbouring
spectral weights. That yields invariance **only where the linking coefficient is
nonzero**. In the authors' own Jacobi normalization (their §1) the off-diagonal
is `b(x) = √(1-x²)/2`, which **vanishes exactly at `x = ±1`** — the endpoints.
So the derivation, when actually carried out, produces a *partial* transport
with a possible terminal atom, not a total group action.

**Missing statement (2b):** *For an exact maximizer with atomic scalar spectral
measure μ, for every atom u with μ({u}) > 0 one has μ({a(u)}) > 0 and
μ({b(u)}) > 0 — with no terminal exception.*

DOC-C's own concession ("in the non-atomic case ... constructing that measurable
lift is a later gate") is correctly irrelevant to (N), since finite dimension
forces atomicity. That part of the interface is clean.

### 3. W0 exhaustion (PROOF §3) — **GAP (inherits 2), individual steps survive**

Attacked each step; three survive, one does not.

- **Purification: SURVIVES.** A mixed finite-dimensional `ρ_AB` attaining `S`
  purifies to `|ψ⟩ ∈ H_A ⊗ H_B ⊗ H_E`; assign `H_E` entirely to one party and
  let its measurements act as `A_i ⊗ 1_E`. Correlations, value, tensor
  structure and finite dimension are all preserved. No attack goes through.
- **POVM / Naimark: SURVIVES but is UNSTATED.** The certificate contact
  argument is a projective-measurement statement; a maximizer with genuine
  POVMs needs dilation. It works — dilate the three binary POVMs per party on
  `H ⊗ C² ⊗ C² ⊗ C²` with ancillas in `|0⟩`, one ancilla per setting — and it
  preserves finite dimension, the tensor split and the value, so the dilated
  strategy is again an exact maximizer. But the proof never mentions it, and
  the dilated strategy is the object the rest of the argument must be applied
  to. **Repairable, one paragraph.**
- **Block restriction: SURVIVES but is UNSTATED.** The Bell operator commutes
  with the centre of the algebra generated by the local observables, hence is
  block diagonal, hence `⟨W⟩_ψ = Σ_k w_k ⟨W⟩_{ψ_k}` is a convex combination; if
  the total is `S = sup`, every positive-weight block attains `S`. Fine, but
  the affineness argument is not given, and the *same* argument is needed later
  (see surface 4, multi-orbit decomposition) where it is likewise not given.
- **"Finite pure-point scalar spectral support": NOT ESTABLISHED.** Trivially
  true *once* a scalar operator is identified — and that identification is
  precisely gap (2a). As written this sentence assumes its own hardest premise.

There is also an internal tension: §3 restricts to an *irreducible* block
(which would be the natural way to control multiplicity), while §4 asserts that
multiplicity is unclassified but harmless. Irreducibility of the algebra
generated by both parties' observables does **not** imply that the contact
operator `X` has simple spectrum, so §3's restriction does not in fact retire
the multiplicity issue of §4.

### 4. The assembly (PROOF §3) — **GAP, decisive; explicit counter-model**

This is the failure point.

**Attack (successful).** `check4_countermodel.py`, Part II. Let
`g(s) = tanh(0.35 s)`, `c_j = g(j + 1/2)`, and set

```
b(u) = -u                      (so b(c_j) = c_{-1-j})
a(u) = g(2 - g^{-1}(u))        (so a(c_j) = c_{1-j})
tau  = a∘b                     (so tau(c_j) = c_{j+2})
P(u) = g(g^{-1}(u) - 1)
```

Verified numerically to 1e-12: `a` and `b` are decreasing involutions, `τ` is
increasing, `a = P^{-1}(-P(·))`, `τ = P^{-2}` (DOC-C (17)), and
`P(-P(u)) = -u`, i.e. **the whole line lies in the double-contact zero set Z**
of (2). Every structural hypothesis the proof invokes holds exactly.

Now take the finite support `F = {c_{-5}, …, c_{4}}`. Output:

```
|F| = 10   b-invariant: True
a-escapes at j = [-5, -4]   tau-escapes at j = [3, 4]
points of F with a(u)=b(u) (common return): []
```

`F` is finite, fully `b`-invariant, and closed under `a` and `τ` at every atom
except the two terminal ones — and **contains no common-return point
whatsoever**, because `a(c_j) = c_{1-j}` and `b(c_j) = c_{-1-j}` are equal for
no `j`. Therefore "finite scalar support ⟹ every orbit finite ⟹ common return
⟹ `S ≤ 1/4`" is **not a valid inference from the premises the proof states**.
Only total invariance rescues it, and total invariance is exactly what a
truncated chain fails and what the proof never proves (gap 2b).

This is the same object as `check2.py`'s Part (B) observation, made faithful to
the full certified structure.

Sub-findings inside surface 4:

- **Set vs measure class: NOT a problem.** For an atomic measure, invariance of
  the measure class gives `μ({u}) > 0 ⟺ μ({a(u)}) > 0`, so the finite support
  is invariant as a set. This attack fails; the step is fine *conditional on
  invariance holding at all*.
- **Multi-orbit decomposition: UNSTATED, repairable.** A finite support may
  split into several common-return sectors. `S ≤ 1/4` on each does not
  syntactically give `S ≤ 1/4` overall; one needs the same affineness /
  central-decomposition argument as in surface 3. Routine, but absent.
- **Endpoint atoms: NOT EXCLUDED within the stipulated inputs.** At `u = ±1`
  the scalar orbit lemma is vacuously satisfied (`a(1) = b(1) = -1`), so the
  endpoint sector is formally "common return" — but H cannot be applied there,
  because in the authors' own normalization the amplitude coefficient
  `b(x) = √(1-x²)/2` vanishes at `x = ±1`, so "the two amplitude ratios" of H
  are `0/0`. The endpoint sector therefore genuinely needs an independent
  exclusion. `PROOF` §3 item 5 asserts it; DOC-C §4 attributes it to "the
  released equality audit" (not stipulated, not reproduced here); DOC-C §8
  argues it from continuum branch geometry ("a wing that reaches an endpoint in
  finite characteristic time"), which is a statement about the *certified
  branches*, not about the atoms of an arbitrary finite-dimensional maximizer.
  **This is a load-bearing import with no proof in the audited material** —
  and it is the same vanishing coefficient that creates gap (2b). The two are
  one gap.
- **Does "common-return sector" match H's hypothesis? MISMATCH FLAGGED.** The
  stipulation given to me reads "on a common-return (fixed/closure) sector".
  DOC-C §8, describing what prior result 1210 actually proved, calls it "the
  **neutral fixed-point** quarter ceiling". Neutrality is a dynamical condition
  (multiplier 1) on the shooting map; a `τ`-fixed scalar atom with `a(u) = b(u)`
  need not be a neutral fixed point of anything. If H's real hypothesis is
  neutrality, applying it to an arbitrary common-return atom is an overreach.
  The referee cannot settle this without H's proof; it is recorded as an
  interface finding.

### 5. Multiplicity boundary (PROOF §4) — **GAP**

The dismissal is too quick. It is true that operator multiplicity does not
change the *set* of scalar values in the support, so if the exclusion depended
only on that set, §4 would be sound. But the exclusion runs through H, and H is
stipulated in terms of "**the two amplitude ratios**" — scalar objects. On a
common-return sector carrying multiplicity `m > 1`, the transport is
matrix-valued and "the two amplitude ratios" are `m × m` blocks; nothing in the
audited material shows the `≤ 1/4` ceiling survives that replacement. So the
sentence "a finite-dimensional carrier has finite scalar support and is already
excluded by the orbit theorem" is only valid if H is multiplicity-uniform.

**Missing statement (5):** *H holds on a common-return sector of arbitrary
finite multiplicity, not only on a multiplicity-one (rank-one transport)
sector.*

Combined with the §3/§4 tension noted above (irreducibility does not give
simple spectrum), this is a second genuine hole, independent of gap 2/4.

### 6. Nonclosure corollary (PROOF §5) — **SURVIVES-ATTACK (conditional on (N))**

Checked for equivocation and found none. Behaviors for (3,3;2,2) live in a
bounded subset of a finite-dimensional real space; a sequence of finite-dim
tensor behaviors with values → `S` has a convergent subsequence; the Bell
functional is linear, hence continuous, so the limit `p*` has value exactly `S`.
`p* ∈ closure(C_q)`. If `C_q` were closed then `p* ∈ C_q`, i.e. some
finite-dimensional tensor strategy realizes `p*` and attains `S`, contradicting
(N). The identification "strategy attains `S`" ⟺ "some behavior in `C_q` has
value `S`" is exact, since every `C_q` behavior comes from some finite-dim
tensor strategy. `sup_{C_q} = S` is supplied by T0.

Two notes, neither an error: (i) the argument needs `S` to be the sup over
`C_q` specifically, which is T0's finite-dim/commuting common value — used
correctly; (ii) the corollary is only as strong as (N), so it inherits every gap
above. For calibration: nonclosure of `C_qs` is known for 5 inputs / 2 outputs
(Dykema–Paulsen–Prakash) and by Slofstra in large scenarios; a (3,3;2,2)
nonclosure would be strictly stronger than anything in the literature, and the
Pál–Vértesi conjecture that (N) resolves is, as of this audit, **open**.

### 7. Interface audit of stipulated inputs — five overreaches

Points where the proof needs T0/LB/H to say more than stipulated:

1. **T0 → scalar reduction.** T0 stipulates a Bellman DP structure with a
   predecessor homeomorphism "on a scalar coordinate" and a kernel-contact
   extraction. The proof needs, in addition, that *every* finite-dimensional
   maximizer's occupied block is unitarily equivalent to a strategy in which
   that scalar coordinate is a genuine commuting spectral variable and
   `R_0,R_A,R_B` are functions of it. Not stipulated. (= gap 2a.)
2. **T0 → totality of transport.** Stipulated: the state annihilates the
   remainders. Needed: the induced transport is total on the support, including
   terminal atoms. Not stipulated. (= gap 2b, the decisive one.)
3. **H → endpoint sectors.** Needed at `u = ±1`, where H's "two amplitude
   ratios" degenerate (`√(1-x²)/2 → 0`). Not stipulated, and the substitute
   ("the released equality audit") is not in the audit package.
4. **H → multiplicity uniformity.** (= gap 5.)
5. **H → additivity over several sectors.** Needed when the finite support
   splits into more than one common-return component. Routine but unstated.

`LB` is used correctly and minimally (only as `S > 1/4`). The `§§1–2` material
(the determinant-compensated multiplier `m̂ > 1`) is **genuinely not used** by
§3–§5: I found no reference to `m̂`, `E`, `v_1`, `v_2` or the Riccati matrices
anywhere in the (N) argument. **The dependency audit's claim of independence
from §§1–2 checks out.** The word "edge" in §3 is a residue of the same Jacobi
picture, but that is a presupposition (surface 2), not a dependence on §§1–2's
numerics.

### 8. Internal consistency of DOC-C — **FINDING (dependency audit incomplete)**

- DOC-C §8 is candid that §§1–3 are *recovery* of prior result 1210, so (N)'s
  items 1–4 reduce to that prior result plus H. Consistent.
- But `PROOF` §3's **item 5** ("endpoint atoms and nontrivial finite cycles are
  excluded") is *not* covered by the five inputs listed in the dependency audit.
  "Nontrivial finite cycles" is fine (it follows from the orbit lemma). "Endpoint
  atoms" is not: it rests on DOC-C §8, which in turn rests on external results
  **S1 and S2** and on "the released equality audit" — none of which are
  stipulated, present, or proved here. **The dependency audit is therefore
  incomplete as written.**
- DOC-C §10's "scalar rigidity theorem" (every exact normal spatial maximizer
  sits on the certified *bi-infinite* orbit) would imply (N) immediately. The
  proof correctly declines to use it — but a reader should notice that (N) is
  either a corollary of a stronger unstipulated theorem, or an independent
  weaker route; the text presents it as the latter without saying so.
- **Artifact inspection.** All seven scripts in `artifacts-inspection-only/`
  bear on DOC-C §§7, 10, 11 — the shooting/heteroclinic/relabeling material
  that the dependency audit explicitly says (N) does not need. **Not one
  artifact tests any load-bearing step of (N)** (no test of support invariance,
  the quarter ceiling, endpoint exclusion, purification/Naimark, or the
  assembly). The load-bearing steps are structural rather than numerical, so
  this is not itself an error — but the "certified / exact / Arb-verified" aura
  of the artifact set does **not** transfer to Theorem (N), and a reader will
  wrongly assume it does. Separately, `bell_symmetry_collider.py`'s "positive
  fixture checks" are hollow: they verify `1/2 + (sum of positive rationals) >
  1/2` on invented `λ` sequences with cyclic wraparound, which is a tautology,
  not a test that these are the maximizer's marginals. (Bears on §11 only.)

## Three weakest load-bearing points, ranked

1. **Totality of the support transport at terminal atoms** (DOC-C §1's one
   unproved sentence + `PROOF` §3 item 5's imported endpoint exclusion). This
   single statement *is* Theorem (N): everything else in the argument is either
   stipulated or elementary. It fails precisely for truncated chains, which are
   the shape of the actual finite-dimensional near-maximizers.
   **Repair route:** show the equality kernels give a three-term recurrence with
   off-diagonal coefficient `√(1-x²)/2` nonvanishing on the occupied support,
   and prove independently that no exact maximizer has an atom at `x = ±1`.
   Both halves must be proved for an arbitrary finite-dimensional maximizer, not
   for the certified branch geometry.
2. **The operator→scalar reduction for an arbitrary maximizer** (gap 2a), which
   DOC-C claims needs neither finite dimension nor the aligned Jacobi form. The
   only visible derivation of everything downstream goes through the Jacobi
   form, and the proof's own word "edge" concedes it. Without a named commuting
   family, "joint spectral support" is undefined.
3. **Multiplicity-uniformity of the quarter ceiling H** (gap 5), together with
   the H-hypothesis mismatch ("common-return sector" as stipulated vs "neutral
   fixed-point ceiling" as DOC-C §8 describes the source result). §4's
   dismissal of multiplicity addresses the support set but not the object H
   actually bounds.

## What would change my verdict

Supply, for an arbitrary finite-dimensional exact maximizer (post-purification,
post-Naimark, restricted to a positive-weight block): (i) the commuting family
defining the scalar coordinate and the proof that `R_0,R_A,R_B` are functions of
it; (ii) the recurrence proof that the atomic support is invariant under `a` and
`b` with **no** terminal exception, including the exclusion of `x = ±1` atoms;
(iii) H at arbitrary finite multiplicity. Given those three, surfaces 1, 3, 4
and 6 close and the theorem stands as stated.
