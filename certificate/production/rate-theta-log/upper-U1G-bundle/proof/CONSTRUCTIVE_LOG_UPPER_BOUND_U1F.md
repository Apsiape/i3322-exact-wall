SUPERSEDED STAMP (2026-08-07): the U1F round-3 gate DENIED this
document (verdicts on disk in audit_archive/). Superseded ENTIRELY by
CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md, which is fully self-contained.
Retained as history only; nothing here is live.

# The Constructive Logarithmic Upper Bound (U1F)

STATUS: promotion candidate for the external upper-only gate.
Supersedes CONSTRUCTIVE_LOG_UPPER_BOUND_U1E.md (retained, historical)
after the U1E gate (DENIED; verdicts in the program record). The
strictness route is the elementary Bellman-band argument supplied
constructively by the U1E proof auditor (finding A8), verified and
adopted; it consumes ONLY anchored material. Constants existential;
one explicit numerical BOUND (not a rate claim) is derived and
guard-checked.

## 0. Definitions

Let B denote the fixed I3322 Bell operator in the Collins–Gisin
normalization (classical bound 0), displayed:

    B = −A2 − B1 − 2 B2
        + A1B1 + A1B2 − A1B3 + A2B1 + A2B2 + A2B3 − A3B1 + A3B2,

three binary projection-valued measurements PER PARTY.

    S_d := sup { <psi| B |psi> : dim H_A <= d, dim H_B <= d,
                 three projection-valued binary measurements per
                 party acting on H_A, H_B respectively, psi a unit
                 vector of H_A (x) H_B }.

NO DILATION: operators act on the d-dimensional local factors
themselves; Schmidt rank in larger ambient spaces plays no role.

    D_upper(eps) := min { d in N : S − S_d <= eps }.

S is the common quantum value, known through its certified window
(0.2508753845015185, 0.250875388108398]. THE CERTIFIED FACT S > 1/4
IS CONSUMED by this proof (§3); the machine-checked kernel carries
both backbone inequalities (the scalar quarter ceiling s(1−s) <= 1/4
and 1/4 < S_LO) as Lean theorems.

## 1. Carrier authority

Promoted Theorem (S): public certificate directory
certificate/production/theorem-S-spatial-attainment-at-S/ (release
v3.1.0; concept DOI 10.5281/zenodo.21782008). Its proof document —
"Spatial Attainment at the Current I3322 Supremum by Scalar-Orbit
Extraction"; THIS IS THE SCALAR-ORBIT DOCUMENT, promoted — constructs
the normalized positive diagonal amplitude vector (§10) and installs
the alternating rank-one blocks with the no-endpoint block-to-Jacobi
value identity (§12); the S1 referee rebuilt this interface in exact
rational arithmetic (Gate 5). DISCLOSED RESIDUAL RISK: the
certificate's own status materials record that its Sections 6–9
(conull invariant set, Borel transversal, uniqueness of
disintegration) carry the residual proof risk, with full expanded
write-up scheduled; §10 consumes those sections. This proof inherits
that disclosed risk through its [P] root and says so.

Current content hashes (verified on the public working tree,
2026-08-07, after the header reconciliation at public commit e50bfec):

    090aecebe7d5c1502bbe93961e40821179cc9a4c592de841316a33a4871a4141
      CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md  (header reconciled to
      PROMOTED v3.1.0 with the residual-risk note, 2026-08-07)
    7978e7caad9ce9f5c1f47404ca0f183c15a8b378a005b3fc696eeedafe4ae900
      THEOREM_S_SIGNED_PUBLIC_STATEMENT.md
    14dcfd479d524d1ca741a38b8bdf06bf19d7918876e12c59b0a7590f4c01c759
      V1_V9_EXECUTION_LEDGER.md
    f07821d781bf6092bfc454c95c9722a3ba7514eb0d2ecf4242100ec0f62134c1
      STATUS.json
    25c1b4f3db0553eaa19d64ea0d9497ee61297b863ed5a4bc886d31fbb0a06c59
      review/SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md

Consumed from the certificate: the amplitude transport law

    lambda_{j+1} / lambda_j = g(c_j) / b(c_j)                    (1.1)

(§11 verbatim); the Bellman value identity at carrier labels

    S = d(c_j, c_j') + g + b²/g   at the fixed-label form,        (1.2)

with d(x,u) = xu + (x−u)/2 − 1 and b(t) = sqrt(1−t²)/2 (the paper's
displayed cost and amplitude functions; b is EVEN); and §1's certified
input that the full interior zero locus is a ONE-TO-ONE STRICTLY
INCREASING relation.

## 2. Corridor

From the promoted G1 receipt (conditional consumption only; the
retraction block in the dependency copy carries the killed
unconditional identity's notice): Z = R0^{-1}(0) is compactly
interior and g >= m_g > 0 on [−1,1]. All carrier labels lie in Z, a
compact subset of a fixed corridor K = −K ⊂⊂ (−1,1); hence on K the
functions b, g, r = g/b are continuous with b >= b_0 > 0 and
r bounded with bounded inverse (no collar payment is needed: the
labels are IN Z, which is interior; compactness of K alone gives the
bounds).

## 3. Tail limits and strictness (the A8 route — anchored material only)

3.1 TAIL MONOTONICITY AND CONVERGENCE. The label sequence is linked
through the zero-locus relation, which is one-to-one and STRICTLY
INCREASING (certificate §1, quoted above). Hence, by induction along
the chain, each tail of (c_j) is monotone: if c_{j+1} >= c_j then
applying the increasing relation preserves the order at the next
link, and the base ordering is fixed by the carrier orientation.
Monotone + confined to compact K ⟹ each tail CONVERGES to a limit
label t_inf(±) ∈ Z (Z closed). Single-valuedness of the limit and
the pairing identity (the u-limit and the x-limit coincide with the
graph relation at the limit) follow from the same strictly-increasing
one-to-one structure — this is the discharge of the Cesàro source's
§9 pairing warning, stated as such.

3.2 THE LIMIT RATIO EQUATION. The Cesàro receipt (full source,
dependencies/ENDPOint_CESARO_CARRIER_RATE_THEOREM.md) defines
rho± as the outward two-index amplitude ratio limits. In the limit
the Jacobi recurrence at the (constant) limit label t gives, for the
one-step ratio x = lim lambda_{j+1}/lambda_j:

    b(t) (x + 1/x) = S − D(t),   D(t) := d(t,t) = t² − 1,        (3.1)

i.e. x + 1/x = mu := (S − D)/b. By (1.1)-(1.2), mu = r + 1/r with
r = g/b evaluated at t — the roots of (3.1) are exactly the transport
multiplier and its reciprocal. Positivity of lambda and lambda ∈ l²
select the DECAYING root x < 1 whenever mu > 2; then rho± = x².

3.3 STRICTNESS FROM THE CERTIFIED WINDOW (A8). For every label t,
with s := sqrt(1−t²) ∈ [0,1]:

    D(t) + 2 b(t) = t² − 1 + s = −s² + s = s(1−s) <= 1/4          (3.2)

(the scalar quarter ceiling — machine-checked in the Lean kernel).
The certified window gives S >= S_LO > 1/4 (also Lean-checked:
quarter_lt_window_lower). Hence

    mu − 2 = (S − D − 2b)/b >= (S − 1/4)/b >= 2 (S − 1/4) > 0     (3.3)

using b <= 1/2. Equivalently, by the Bellman identity (1.2),
S − (D + 2b) = (g − b)²/g >= 0 with equality iff g = b — excluded by
(3.3). Therefore x < 1 STRICTLY, uniformly over all labels:

    mu >= 2 + 2(S_LO − 1/4) = 2.001750769...                      (3.4)
    rho± = x² <= 0.9197271...  < 1                                 (3.5)
    kappa± = −log rho± >= 0.0836782... > 0   (per index, §3.5)     (3.6)
    kappa_eff >= 0.0418391...,  1/kappa_eff <= 23.9010649...       (3.7)

The displayed decimals are BOUNDS (guard-checked exact-rational /
high-precision in guards/guard_a8_strictness.py), not rate claims;
the theorem's constant remains existential. This route consumes ONLY:
the certificate (§1, §10-§12, (1.1)-(1.2)), G1's corridor, the Cesàro
receipt's rho definition, and certified S > 1/4. The distorted-return
functional, the return-quotient orientation, and the endpoint
return-sector mechanism are none of them invoked (kill #12 governs
normalized-gain substitution into the distorted-return functional,
which never appears here — the quarter-ceiling ALGEBRA s(1−s) <= 1/4
is the Lean-checked scalar lemma, not the return-sector theorem); no
selection theorem, no sextic, no hyperbolicity, no numerical bracket.

3.4 INDEX BOOKKEEPING. rho± is a two-index ratio: lambda_{2n} ~ rho^n
gives lambda_j ~ rho^{j/2} per index, and tail MASS sums squares:
lambda_j² ~ rho^j = e^{−kappa j} — the amplitude square exactly
cancels the half; kappa acts per index in every estimate below.

3.5 CONSISTENCY NOTE (non-load-bearing; no evidential weight).
RETRACTION-BLOCK-BEGIN — retired numerics quoted as history only. The
sharper identification rho± = q* = g(−t*)/g(t*) with the historical
selected-tail bracket was verified independently by the U1E proof
auditor to ~10 digits (their finding A7) via the same ratio equation
at the plateau label; and the retracted scout coefficient
13.2991468418 equals the bracket's upper-endpoint evaluation
2/(−log q_hi) to 8.9e−13 — which shows the scout and that bracket are
THE SAME COMPUTATION (provenance entanglement), and is therefore a
consistency note carrying no independent evidential weight. Neither
the identification nor any bracket is consumed by this proof.
RETRACTION-BLOCK-END

## 4. The truncation

Unchanged from U1E §4 (endpoint-projector completion; all six
operators exact projections — second-engine verified symbolically at
arbitrary block angles; local dimension exactly d = |I|).

## 5. Error accounting

Unchanged from U1E §5 with three corrections: (a) the flux identity
(5.1) is cited to its actual source — the FULL Cesàro theorem
document now carried in dependencies/ (§2 there), not the former
extract; (b) the coefficient bound: C_diag <= 20 by the two-sided
product bound (a joint term's diagonal is a product of two projector
diagonals, |a'b' − ab| <= 2), and C_diag = 12 holds under the
one-sided count; the proof uses the SAFE bound C_B := 1/2 + 20 R_max
(constants existential; the change is absorbed); (c) rows and
payments as in the three-row table, R_max := sup_K max{r, 1/r} finite
by §2.

    0 <= S − V_I <= C_B · B_I / (1 − T_I),  C_B = 1/2 + 20 R_max  (5.5')

    T_I, B_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)}     (5.6')

derived from §3.4 exactly as in U1E (5.6)-(5.7).

## 6.–7. Allocation, every d, limsup — unchanged from U1E

Floor allocation L_d = floor(kappa_+ (d−1)/(kappa_− + kappa_+)),
R_d = d − 1 − L_d gives |I| = d exactly for every sufficiently large
d; balance gives kappa_eff = (1/kappa_− + 1/kappa_+)^{−1} > 0; and

    S − S_d <= exp(−kappa_eff d + o(d))                            (6.3)

    limsup_{eps↓0} D_upper(eps)/log(1/eps) <= 1/kappa_eff          (7.1)

    THEOREM (U1F). D_upper(eps) = O(log(1/eps)), existential
    constant 1/kappa_eff > 0; moreover the anchored uniform bound
    (3.7) gives 1/kappa_eff <= 23.9010649... unconditionally.       (7.2)

## 8. Conditional corollary

IF AND ONLY IF this U1F gate promotes: with the promoted lower bound,
D(eps) = Theta(log(1/eps)) at local-dimension scope. Not an
independently promoted claim of this document.

## 9. Claim boundaries

Local dimension only. The residual risk of the [P] root's Sections
6-9 is inherited and disclosed (§1). S consumed only through its
window and the Lean-checked S > 1/4. All constants existential except
the explicit UPPER bound in (3.7)/(7.2), which is a derived
inequality, guard-checked, and claims no sharpness.
