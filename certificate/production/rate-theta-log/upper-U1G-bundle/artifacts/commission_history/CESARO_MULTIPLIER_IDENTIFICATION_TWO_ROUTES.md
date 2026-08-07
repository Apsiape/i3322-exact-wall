# R1 Identification Lemma — independent derivation (synthesizer track)

STATUS: proof sketch at commission level, written INDEPENDENTLY of the
worker's U1e attempt, for comparison. Every consumed receipt is named.
Nothing here is promoted; the merged version goes through the gate.

## Claim

Let λ = (λ_j) be the Schmidt amplitudes of the Theorem (S) carrier and
ρ± the outward two-step ratio limits consumed by the endpoint-Cesàro
receipt. Then

    ρ+ = ρ− = q*  ∈  (0.860375661, 0.860376163),

the PROMOTED certified algebraic tail multiplier. In particular
ρ± ≤ 8604/10000 < 1, hence κ± = −log ρ± > 0 and κ_eff > 0, with NO
return-sector construction, NO quarter-ceiling-at-the-endpoint step,
and kill #12 never engaged.

## The chain (four promoted receipts + continuity)

1. TAIL MONOTONICITY + BOUNDEDNESS ⟹ CONVERGENCE. The carrier's
   scalar component is a nonfixed ORDERED response orbit [receipt: the
   promoted equality-module statement consumed as [E1] throughout the
   lower campaign: "every exact maximizing scalar component is a
   nonfixed ordered response orbit"]. Each tail of the label sequence
   (c_j) is therefore monotone; G1 confines it to the fixed compact
   corridor K = −K ⊂ (−1,1) [receipt: G1, promoted]. Monotone +
   bounded ⟹ each tail CONVERGES to a limit label t_∞±.

2. THE LIMIT IS AN INTERIOR RESPONSE-FIXED CLOSURE, AND SELECTION
   NAMES IT. The limit of a monotone response tail is an interior
   response-fixed closure; the tail-closure quantization theorem
   [receipt: sextic tail-closure, promoted-corpus, twice
   independently re-derived in blind (envelope algebra AND resultant
   route)] lists the possible closures as {S-branch, y−, y+}, and the
   tail-selection theorem [receipt: wall-comparison selection,
   blind-verified robust in 9 configurations, survivor margin never
   crossing zero] excludes all but y+. Hence t_∞± = ±t*, the
   algebraic label with t*² = y+, |t*| ≈ 0.87827 — interior. [THIS
   SIMULTANEOUSLY DISCHARGES OPEN RECEIPT E1: the four endpoint
   limits lie at ±t*, an exact interior pair — stronger than "some
   compact subinterval".]

3. THE RATIO LIMIT IS THE MULTIPLIER AT THE LIMIT LABEL. The
   amplitude transport is multiplicative in the labels:
   λ_{j+1}/λ_j = m_j where m_j is the RN transport multiplier
   evaluated at (c_j, c_{j+1}) [receipt: the RN transport laws of the
   Theorem (S) package, S1-audited]. On the corridor the multiplier
   functions are CONTINUOUS with denominators uniformly bounded away
   from zero (g ≥ m_g > 0, b ≥ b_0 > 0) [receipt: G1 §4, the m_g
   uniformity — "could not break this repair"]. Labels → ±t* by step
   2, so the two-step ratio λ_{2n+2}/λ_{2n} converges (plain limit,
   hence Cesàro) to the two-step multiplier evaluated AT the fixed
   label.

4. THE MULTIPLIER AT THE FIXED LABEL IS THE CERTIFIED q*. The
   two-step transport multiplier at the y+ fixed state is the
   h = r^{−2} eigenvalue of the current characteristic map [receipt:
   hyperbolicity package; the blind round independently CONFIRMED
   "q* = 0.860376050505... as the h = r^{−2} eigenvalue matching the
   certified bracket"], with the exact rational bracket
   q* ∈ (0.860375661, 0.860376163) [receipt: exact guard-carried
   bracket, replayed]. Hence ρ± = q* < 8604/10000 < 1. (Both tails:
   the reflection structure maps one tail to the other; the OUTWARD
   multiplier at −t* equals the outward multiplier at +t* by the
   r(t)r(−t) = 1 reciprocity — equivalently, decay at both ends is
   the normalizability of λ, and the certified value is the same.)

## The confirmation that the identification is right

RETRACTION-BLOCK-BEGIN — retired numerics below quoted as historical
evidence only; the retraction stands.

With ρ± = q*, both tail rates are equal: κ = −log q* per two-step,
so κ_eff = κ/2 per index and

    1/κ_eff = 2/(−log q*).

Evaluating on the CERTIFIED BRACKET (mpmath, 30 digits; to be carried
as exact directed rounding in the bundle guard):

    κ per two-step ∈ [0.150385586528, 0.150386169994]
    1/κ_eff = 2/κ ∈ [13.2990952564, 13.2991468542]

— which CONTAINS the historically-scouted, retracted coefficient
13.2991468418 (within 1.2e-8 of the bracket's upper edge). The retraction stands (the numeric is not claimed; the
constant remains existential in the theorem statement). But the
identification EXPLAINS the scout: the old numeric was 1/κ_eff
evaluated at q*, computed before anyone could justify it. The banked
program memory recorded exactly this ("κ_eff bracket contains
historical log R = 0.0751929") — the numbers knew before the proof
did. This is strong independent evidence the identification types.

RETRACTION-BLOCK-END

## What this closes and what remains

CLOSES: B1/F1/F7 (the KILL — strictness via certified bracket, no
(1.1)-(1.2) exhibition needed); E1/F6 (endpoint interiority, with the
exact labels); the trichotomy question (ρ± = q* > 0 exactly — no
superexponential branch exists for THIS carrier).

REMAINS (unchanged from the commission): R2 (carrier STRUCTURE into
the live chain — my step 3 consumes the RN transport laws, which are
S1-audited but the diagonal/block representation still needs its real
anchor + mini-gate); R3 (error accounting: the retained-endpoint
diagonal charge λ_a² ≤ R_max·B_I with R_max = sup r on K, finite by
G1 — one line once R_max is named; C_B derivation from block
structure; the three-line T_I geometric bound: for any q' ∈ (q*, 1),
λ_{2n} ≤ C q'^n eventually, so Σ_{j>R} λ_j² ≤ C' q'^R — with the
per-index/per-two-step bookkeeping stated once); R4 (define S_d and
D_upper; the every-d split L = round((d−1)κ_eff/κ−); the limsup
form); R5 (hygiene list as commissioned).

## Comparison protocol

When the worker's U1e lands: diff the two derivations step-for-step.
Divergences to watch: (a) whether they route via the return-sector
fallback instead (if so, BOTH routes can ship — belt and suspenders);
(b) their treatment of the minus-tail multiplier (reciprocity step 4
— if they derive a DIFFERENT value for ρ−, stop and reconcile before
anything ships); (c) whether their step-1 monotonicity receipt matches
mine ([E1] nonfixed-ordered) or uses something weaker.
