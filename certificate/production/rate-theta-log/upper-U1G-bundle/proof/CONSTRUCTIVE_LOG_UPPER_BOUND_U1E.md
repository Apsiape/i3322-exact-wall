SUPERSEDED STAMP (2026-08-07, U1G round): this document is now
HISTORICAL IN ITS ENTIRETY. Its sections 4-7 were live-by-incorporation
during the U1F round; CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md is fully
self-contained and nothing here is live any longer (ledger entry 17).
The original U1F-era supersession header follows as history.

# The Constructive Logarithmic Upper Bound (U1E — post-gate repair)

SUPERSESSION HEADER (2026-08-07, after the U1E gate DENIED): §§0-3 of
this document are SUPERSEDED by CONSTRUCTIVE_LOG_UPPER_BOUND_U1F.md
(the A8 strictness route; ledger entries 10-15). §§4-7 (truncation,
error accounting, allocation, limsup) remain LIVE, incorporated by
reference from the U1F document with the corrections listed in U1F §5
(C_diag safe bound 20; flux-identity citation to the full Cesàro
source). The §3.6 retrodiction below is retained under its retraction
block as history; its "9e-11" figure was corrected to 8.9e-13 in the
ledger.

STATUS: §§0-3 historical; §§4-7 live-by-incorporation.
Supersedes proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1.md (retained in this
directory as historical; its gate verdicts and repairs are ledgered).
Every consumed receipt is named with file and, where load-bearing,
quoted. Constants are existential throughout; no numerical rate
coefficient is claimed.

## 0. Definitions (gate finding B5/F14)

Let B denote the fixed I3322 Bell operator in the Collins–Gisin
normalization used throughout this repository (classical bound 0;
displayed form: marginals −A2 − B1 − 2B2; eight joint ±1 terms).

    S_d := sup { <psi| B |psi> : dim H_A <= d, dim H_B <= d,
                 six projection-valued binary measurements acting on
                 H_A, H_B respectively, psi a unit vector of
                 H_A (x) H_B }.

NO DILATION: the supremum ranges over strategies whose operators act
on the d-dimensional local factors themselves. Schmidt rank in larger
ambient spaces plays no role anywhere in this document.

    D_upper(eps) := min { d in N : S − S_d <= eps }.

S denotes the common quantum value, known through its certified
window (0.2508753845015185, 0.250875388108398].

## 1. Carrier authority (repair R2)

Promoted Theorem (S) supplies the exact spatial carrier, INCLUDING its
structural form. The authority is the public certificate directory
certificate/production/theorem-S-spatial-attainment-at-S/ of the
repository (release v3.1.0; concept DOI 10.5281/zenodo.21782008),
whose proof document constructs in §10 the normalized positive
diagonal amplitude vector and states in §12 that the construction
consumes "the alternating rank-one projector blocks and the
no-endpoint block-to-Jacobi value identity", installing the two
alternating nearest-neighbour matchings on two copies of l2(Z), the
state psi_S = sum_j lambda_j e_j (x) e_j, and six bounded projection
measurements attaining Bell value S. The S1 referee independently
rebuilt this interface in exact rational arithmetic (Gate 5 of the
referee verdict). Current content hashes (verified on the repository
working tree, 2026-08-07):

    15e444229b80173986cc5c68fcff42d464e8b08d0c8f60d3a624ec86f40d66b0
      CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md
    7978e7caad9ce9f5c1f47404ca0f183c15a8b378a005b3fc696eeedafe4ae900
      THEOREM_S_SIGNED_PUBLIC_STATEMENT.md
    14dcfd479d524d1ca741a38b8bdf06bf19d7918876e12c59b0a7590f4c01c759
      V1_V9_EXECUTION_LEDGER.md
    f07821d781bf6092bfc454c95c9722a3ba7514eb0d2ecf4242100ec0f62134c1
      STATUS.json   (post-2026-08-07 reconciliation, public commit
      0292314; the certificate manifest was refreshed accordingly)
    25c1b4f3db0553eaa19d64ea0d9497ee61297b863ed5a4bc886d31fbb0a06c59
      review/SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md

The one-step amplitude transport law of the promoted proof:

    lambda_{j+1} / lambda_j = g(c_j) / b(c_j)                    (1.1)

with (c_j) the scalar labels of the carrier.

## 2. Corridor and interiority (G1, conditional only)

From the promoted G1 receipt (dependencies/G1_PROMOTED_UPPER_RECEIPT
.md, consumed ONLY through its conditional endpoint-product logic and
its consequences): the full-zero locus Z = R0^{-1}(0) is compactly
interior, Z ⊂⊂ (−1,1)²; the critical storage satisfies g >= m_g > 0
on [−1,1]; hence on the fixed reflection-symmetric corridor K = −K
containing the carrier labels, the coefficient functions b, g and the
transport multiplier r = g/b are continuous with denominators
uniformly bounded below (b >= b_0 > 0 away from the endpoint collar,
whose state mass is paid at O(eps) by the collar receipt). The killed
unconditional identity g(1)g(−1) = 0 is not used; see the marked
retraction block in the G1 receipt.

## 3. Tail limits, the identification rho± = q*, and kappa_eff
   (repair R1A/R1B — the gate KILL, closed by two independent routes)

3.1 TAIL CONVERGENCE. The carrier's scalar component is a nonfixed
ordered response orbit (promoted equality-module receipt). Each tail
of (c_j) is monotone and confined to K, hence converges. The limit of
a monotone response tail is an interior response-fixed closure; the
sextic tail-closure quantization lists the closures as {S-branch,
y−, y+}, and the wall-comparison selection theorem excludes all but
y+. Hence the two tail limits are the algebraic labels ±t*, with
t*² = y+ and |t*| interior. [This discharges receipt E1 with the
exact labels — stronger than any compact-subinterval statement.]

3.2 THE IDENTIFICATION (primary route). The endpoint-Cesàro receipt
defines rho+ = lim lambda_{2n+2}/lambda_{2n} and states the outward
ratio as the product of transport multipliers at the endpoint labels;
one response step equals two characteristic steps. With the forward
tail alternating between the labels (−t*, −(+t*)) per the carrier
orientation (+t* → −t*), the forward endpoint pair is asymptotically
(−t*, −t*), so

    rho+ = r_B(−t*)² = g(−t*)/g(t*) = q*                          (3.1)

where q* is the promoted selected-tail outward two-characteristic
multiplier. At the negative end, outward motion reverses the
characteristic index, giving rho− = r_B(t*)^{−2} = g(−t*)/g(t*) = q*.

3.3 THE IDENTIFICATION (independent confirmation route). By 3.1 the
labels converge to ±t*; by (1.1) and continuity of r = g/b on K with
denominators bounded below (§2), the two-step ratio converges (plain
limit, hence Cesàro) to the two-step multiplier evaluated at the
fixed label — which is the h = r^{−2} eigenvalue of the current
characteristic map, blind-confirmed equal to q* within the certified
bracket. Both routes yield rho± = q*; the minus-tail values agree
(orientation reversal = reflection reciprocity r(t)r(−t) = 1).

3.4 STRICTNESS FROM THE CERTIFIED BRACKET. The promoted exact bracket

    0.860375661183927 < q* < 0.860376162879071                    (3.2)

(retained as live by the hostile correction audit for the EXACT
carrier — the kill in that audit concerned only transfer of these
constants to arbitrary near-maximizers, which this proof never does)
gives immediately

    0 < rho± = q* < 8604/10000 < 1,   kappa± := −log rho± > 0.   (3.3)

Neither F(q), nor the RHO_Q orientation artifact, nor any endpoint
quarter-ceiling mechanism is invoked; permanent kill #12 (raw-gain
substitution into F) is bypassed, not repaired. No tail
classification is needed or claimed: r is continuous and positive at
the endpoint labels, so rho± > 0, excluding superexponential decay
for THIS carrier.

3.5 INDEX BOOKKEEPING (the factor-of-two, displayed). rho± is a
two-index amplitude ratio: lambda_{2n} ~ rho^n gives per-index decay
lambda_j ~ rho^{j/2}. The tail MASS sums squares:

    lambda_j² ~ (rho^{1/2})^{2j} = rho^j = e^{−kappa± j},         (3.4)

so kappa± = −log rho± operates PER INDEX in every tail-mass estimate
below: the amplitude square exactly cancels the half.

3.6 RETRODICTION (evidence, not a claim).
RETRACTION-BLOCK-BEGIN — the retired numeric below is quoted as
historical evidence; it is not asserted and remains retracted.
With equal tails, kappa_eff = kappa/2 (see 6.2) and
1/kappa_eff = 2/(−log q*). Evaluating on (3.2):
1/kappa_eff ∈ [13.2990952753, 13.2991468418]. The historically
scouted and RETRACTED coefficient 13.2991468418 is EXACTLY the
bracket's upper-endpoint evaluation 2/(−log q_hi) rounded to its ten
stated decimals (|difference| ≈ 9e−11): the old scout was computed
at the bracket endpoint, before any derivation licensed it. The
retraction stands — the constant remains existential — but the
identification explains the scout to rounding precision. See
guards/guard_kappa_bracket_retrodiction.py, whose naive "contains"
predicate initially FAILED by 9e−11 and was corrected to this
sharper, honest statement.
RETRACTION-BLOCK-END

## 4. The truncation (construction; repair verified at the gate)

For I = [−L, R] ∩ Z: keep every full 2×2 rank-one block of each
matching whose paired indices both lie in I; at a severed endpoint
pair replace the block by the one-dimensional projector on the
retained index (complementary outcome takes the complement). All six
operators remain exact projections (direct sums of orthogonal
rank-one blocks and 1-dim projectors; verified symbolically for
arbitrary block angles, both matchings, m = 3..8, complements
included — the second-engine guard); the truncated state is
psi_I = M_I^{−1/2} sum_{j in I} lambda_j e_j (x) e_j with
M_I = sum_{j in I} lambda_j²; and the LOCAL DIMENSION IS EXACTLY
d = |I| — no dilation, no padding.

## 5. Error accounting (repair R3)

5.1 PRINCIPAL COMPRESSION FIRST. Let v_I be the value of the
principal Jacobi compression on I. The endpoint-Cesàro receipt gives
the EXACT flux identity

    S − v_I = [ b(c_{a−1}) lambda_{a−1} lambda_a
              + b(c_b) lambda_b lambda_{b+1} ] / M_I,             (5.1)

i.e. only the two cut edges are unpaid, and b <= 1/2 gives
S − v_I <= (1/2) B_I / M_I with B_I := |lambda_{a−1}lambda_a| +
|lambda_b lambda_{b+1}|.

5.2 FROM COMPRESSION TO THE STRATEGY: THE THREE-ROW TABLE. Let V_I be
the Bell value of the §4 strategy. Relative to the principal
compression, the endpoint completion changes exactly three things:

    row 1: the two cut-bond OFF-DIAGONAL terms  → already and only
           accounted by the flux identity (5.1); NOT charged again.
    row 2: the two RETAINED ENDPOINT DIAGONALS  → coefficient change
           of modulus <= 1 per affected Bell term, at sites a and b;
           charged in 5.3.
    row 3: everything else                      → unchanged, exactly.

5.3 THE ENDPOINT-DIAGONAL PAYMENT. Define

    R_max := sup_{t in K} max{ r(t), r(t)^{−1} } < infinity        (5.2)

(finite by §2). By the transport law (1.1),
lambda_a² <= R_max |lambda_{a−1} lambda_a| and
lambda_b² <= R_max |lambda_b lambda_{b+1}|, so

    lambda_a² + lambda_b² <= R_max · B_I.                          (5.3)

The fixed Bell operator has marginal coefficients of absolute sum 4
and eight joint coefficients of modulus 1; all six measurement
operators are projections, hence contractions, so each affected
diagonal coefficient has modulus at most one and

    |V_I − v_I| <= C_diag · R_max · B_I / M_I,   C_diag = 12.      (5.4)

5.4 THE NAMED CONSTANT. Combining (5.1) and (5.4):

    0 <= S − V_I <= C_B · B_I / (1 − T_I),
    C_B := 1/2 + 12 R_max < infinity,                              (5.5)

with T_I := sum_{j not in I} lambda_j² the omitted tail mass.

5.5 THE TAIL AND BOND ESTIMATES (derived, not cited). By (3.4), for
every eta > 0 eventually lambda_j² <= C_eta e^{−(kappa_+ − eta) j}
on the right tail, so the geometric sum gives

    T_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)},          (5.6)

and the boundary products obey the same logarithmic rates:

    B_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)}.          (5.7)

Hence, absorbing C_B and (1 − T_I)^{−1} = 1 + o(1) into the o(·):

    S − V_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)}.      (5.8)

## 6. Every dimension, the balance, and the rate (repair R4)

6.1 ALLOCATION. For every sufficiently large integer d set

    L_d := floor( kappa_+ (d−1) / (kappa_− + kappa_+) ),
    R_d := d − 1 − L_d,                                            (6.1)

so |I| = L_d + R_d + 1 = d EXACTLY: the strategy of §4 has local
dimension exactly d, for every d.

6.2 BALANCE. kappa_− L_d = kappa_eff d + O(1) and kappa_+ R_d =
kappa_eff d + O(1) with

    kappa_eff := (1/kappa_− + 1/kappa_+)^{−1}
              = kappa_− kappa_+ / (kappa_− + kappa_+) > 0.         (6.2)

(With rho± = q* the two rates are equal and kappa_eff = kappa/2.)

6.3 THE RATE, FOR EVERY d. Substituting (6.1) into (5.8):

    S − S_d <= S − V_{I_d} <= exp( −kappa_eff d + o(d) ).          (6.3)

## 7. The theorem

For every 0 < eta < kappa_eff, (6.3) gives eventually
S − S_d <= e^{−(kappa_eff − eta) d}; choosing
d(eps) = max{ d_eta, ceil( log(1/eps) / (kappa_eff − eta) ) } and
letting eta ↓ 0 in the limsup:

    limsup_{eps ↓ 0} D_upper(eps) / log(1/eps) <= 1/kappa_eff.     (7.1)

    THEOREM (U1E). D_upper(eps) = O( log(1/eps) ),
    with existential constant 1/kappa_eff > 0.                     (7.2)

## 8. Conditional corollary (scope-fenced)

IF AND ONLY IF this U1E gate promotes, then together with the
already-promoted lower bound D_lower(eps) = Omega(log(1/eps)):

    D(eps) = Theta( log(1/eps) )

at local-dimension scope, existential constants. This corollary is
not an independently promoted claim of this document.

## 9. Claim boundaries

Local Hilbert-space dimension only; no Schmidt-rank reading. All
constants existential; the retrodiction note (3.6) is evidence, not a
numerical claim. S known only through its certified window. The
exact-carrier constants (q*, t*) are consumed for the EXACT carrier
only; nothing here transfers them to near-maximizers.
