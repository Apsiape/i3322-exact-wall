# The Constructive Logarithmic Upper Bound (U1G)

STATUS: promotion candidate for the external upper-only gate (round 6; the round-5 proof surface returned PROMOTE at frozen commit 5c3e9c8b; this round folds in the round-5 integrity blockers and the proof surface auditor's recommended items).
Fully SELF-CONTAINED: supersedes CONSTRUCTIVE_LOG_UPPER_BOUND_U1F.md
and CONSTRUCTIVE_LOG_UPPER_BOUND_U1E.md ENTIRELY (both retained as
history; nothing in either is live-by-incorporation). Gate history:
U1 DENIED, U1E DENIED, U1F DENIED (all verdicts on disk in
audit_archive/). The round-3 proof auditor's closing assessment —
"the mathematics is sound and I could not break it"; every U1F blocker
was an anchoring/exposition/audit-trail defect — is the commission this
document executes. Constants existential; one explicit numerical BOUND
(not a rate claim) is derived and guard-checked.

## 0. Definitions

Let B denote the fixed I3322 Bell operator in the Collins–Gisin
normalization (classical bound 0), displayed:

    B = −A2 − B1 − 2 B2
        + A1B1 + A1B2 − A1B3 + A2B1 + A2B2 + A2B3 − A3B1 + A3B2,

three binary projection-valued measurements PER PARTY. (Marginal
coefficients have absolute sum 4; the eight joint coefficients have
modulus 1 — both counts re-verified by the round-3 proof auditor
against the repository concordance table, its finding F22.)

    S_d := sup { <psi| B |psi> : dim H_A <= d, dim H_B <= d,
                 three projection-valued binary measurements per
                 party acting on H_A, H_B respectively, psi a unit
                 vector of H_A (x) H_B }.

NO DILATION: operators act on the d-dimensional local factors
themselves; Schmidt rank in larger ambient spaces plays no role.

    D_upper(eps) := min { d in N : S − S_d <= eps }.

S is the common quantum value, known through its certified window

    S in (0.2508753845015185, 0.250875388108398]                  (0.1)

(THEOREM_S_SIGNED_PUBLIC_STATEMENT.md lines 7–12, hash in §1). Write
S_LO := 0.2508753845015185; the window is OPEN at its lower endpoint,
so S > S_LO strictly.

## 1. Authorities and anchors (every consumed source, by hash)

1a. THE PROMOTED THEOREM (S) CERTIFICATE [P]. Public directory
certificate/production/theorem-S-spatial-attainment-at-S/ (release
v3.1.0; concept DOI 10.5281/zenodo.21782008). Its proof document —
"Spatial Attainment at the Current I3322 Supremum by Scalar-Orbit
Extraction" — is THE scalar-orbit document, promoted. Current content
hashes (public working tree, 2026-08-07, public commits 7cc1a9b,
0292314, e50bfec):

    090aecebe7d5c1502bbe93961e40821179cc9a4c592de841316a33a4871a4141
      CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md
    7978e7caad9ce9f5c1f47404ca0f183c15a8b378a005b3fc696eeedafe4ae900
      THEOREM_S_SIGNED_PUBLIC_STATEMENT.md
    14dcfd479d524d1ca741a38b8bdf06bf19d7918876e12c59b0a7590f4c01c759
      V1_V9_EXECUTION_LEDGER.md
    f07821d781bf6092bfc454c95c9722a3ba7514eb0d2ecf4242100ec0f62134c1
      STATUS.json
    25c1b4f3db0553eaa19d64ea0d9497ee61297b863ed5a4bc886d31fbb0a06c59
      review/SPATIAL-ATTAINMENT-S1-REFEREE-VERDICT.md

Consumed from the proof document, quoted with lines:

  (i)   §6:446–451: the interior zero locus Z "is Borel and is the
        graph of a strictly increasing one-to-one Borel map P",
        Z = {(P(u), u) : u in Y}.
  (ii)  §10:792–795, boxed: "P(c_{j+1}) = c_j for every j" — ONE map,
        every link; and §10:798: "Every adjacent pair (c_j, c_{j+1})
        is a full-zero source-target pair."
  (iii) §11:929–932, the amplitude transport law:

            lambda_{j+1} / lambda_j = g(c_j) / b(c_j)              (1.1)

  (iv)  §11: the carrier eigen-equation H lambda = S lambda with
        Jacobi entries H_jj = d(c_{j-1}, c_j), H_{j-1,j} = b(c_{j-1}),
        where d(x,u) = xu + (x−u)/2 − 1 (the paper's displayed cost
        function — receipt: certificate/production/
        foundational-sprint-1197/EXACT-I3322-QUANTUM-SUPREMUM.md:66,
        hash-anchored below; round-4 proof R1 noted the definition is
        off the certificate document) and b(t) = sqrt(1−t²)/2
        (certificate line 229; b is EVEN; 2b(t) = sqrt(1−t²)).

    9a5d34fbfb88e13ebe9ec86e27d8c27347cbeaf04336f2d64eb85ff96e7a6c66
      certificate/production/foundational-sprint-1197/EXACT-I3322-QUANTUM-SUPREMUM.md
  (v)   §1:73: "the full interior zero locus is a one-to-one strictly
        increasing relation" (the §6 map in relation form).

DISCLOSED RESIDUAL RISK, INHERITED AND LOCATED: the certificate's
status materials record that its §§6–9 (conull invariant set, Borel
transversal, uniqueness of disintegration) carry the residual proof
risk, with full expanded write-up scheduled. Items (i) and (ii) above
sit INSIDE that range (§6 directly; §10 consumes §§6–9). This proof
therefore inherits the disclosed risk at its foundation, and says so
here rather than in a footnote (round-3 finding F13, recorded as
instructed). Corroboration noted by the round-3 proof auditor
(independently, not claimed by any prior bundle): certificate §7:
594–610 carries the same elimination algebra as §3's ceiling below.

1b. THE LEAN KERNEL [V] — machine-checked backbone, anchored. Public
repository path lean/I3322Kernel/, public commit 6e6adb5 (pushed
2026-08-07), Lean 4 + mathlib, AxiomCheck.lean covers ALL 27 kernel
theorems and each reports only [propext, Classical.choice, Quot.sound]
(staircase_sum_injOn: a subset; stdout receipt at
audit_archive/AXIOMCHECK_RECEIPT_2026-08-07.txt). Source hashes are
COMMIT-BLOB digests — verify via `git cat-file blob 6e6adb5:<path>`,
NOT the working tree, whose checkout line endings may differ
(round-4 proof finding F-03; the hygiene guard's H5 verifies against
the commit blobs):

    029575287691d33f72a6c513b53eef15f64fc9cfea5c19f567bbd66043d9c9b4
      I3322Kernel.lean
    732db6a54fe2f1c6fa5fc8ce7277de76107cb3bda32823b8c517aae05e4176d9
      AxiomCheck.lean
    6d25a672ef760597a232501ae81090a439f6c83088f712faa85b22a5e0d04ade
      I3322Kernel/QuarterCeiling.lean
    7cb878e1acb8987b6bf5d9a242bd689b1f01f99e291dd98b388b9d0513d07304
      I3322Kernel/RateCores.lean
    09d0b726e2e50ee1160abdcb5502e989604c7e30c5f49f9932ce2e8fd265ce28
      I3322Kernel/EndpointMargins.lean
    c4328d8d6a5a68c31c8ad068df6a511a93af3a50b4352680021f26964b74de19
      I3322Kernel/FiniteClosure.lean

Consumed theorems, with EXACT statements:

  band_identity          : t² <= 1  ->  t² − 1 + sqrt(1−t²)
                                        = sqrt(1−t²)·(1 − sqrt(1−t²))
  s_mul_one_sub_s_le_quarter : s·(1−s) <= 1/4          (every real s)
  band_quarter_ceiling   : t² <= 1  ->  t² − 1 + sqrt(1−t²) <= 1/4
  amplitude_b_le_half    : t² <= 1  ->  sqrt(1−t²)/2 <= 1/2
  quarter_lt_window_lower: (1:Q)/4 < 2508753845015185/10^16

HONEST SCOPE OF THE LAST ITEM (round-3 finding F11): the Lean theorem
quarter_lt_window_lower checks ONLY the literal rational comparison
1/4 < S_LO. It does NOT establish S > S_LO — that is the certified
window (0.1), whose authority is the hash-anchored signed public
statement above, NOT the Lean kernel. The composite S > 1/4 therefore
rests on: [window certification, hash-anchored] + [literal comparison,
Lean-checked]. INDEPENDENT SECOND ANCHOR BY EXHIBITION (promoted to
load-bearing for this single fact, as the round-3 auditor directed):
guards/guard_second_engine_projectors.py PART B evaluates explicit
finite-dimensional PV strategies at 110-digit precision with Bell
values 0.2500643651906... (d = 24) and 0.2505605862827... (d = 33);
each exhibits S >= S_d > 1/4 directly, and the guard ASSERTS the
exhibited fact (values at d = 24 and d = 33 strictly exceed 1/4 —
fail-capable, round-4 integrity finding 1). The Jacobi-quotient-to-
Bell-value bridge that makes the eigenvalue a strategy value is the
public certificate document certificate/production/
foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md, anchored:

    514242545b32040e34f0d879dfe8bd745b8a0d24341b071ff93e901763351195
      certificate/production/foundational-sprint-1292/RIGOROUS-DIMENSION-255-LOWER.md
      (the direct Jacobi quotient realized by an explicit legal
      finite strategy)

PART B's construction uses open-endpoint PV padding, NOT this proof's
§4 completion (disclosed in artifacts/small_d_demoted/DISCLOSURE.md);
that caveat does not touch the exhibited VALUES. The existential
theorem needs only S > 1/4 (doubly anchored). The explicit numerical
bound (3.9)/(7.2) needs the full window value S_LO (single anchor:
the window).

1c. G1 [source status: PROVED CANDIDATE] — FULL byte-identical source,
dependencies/G1_ENDPOINT_POSITIVITY_AND_CONDITIONAL_ENDPOINT_PRODUCT.md
(sha256 6dbb19c7d00a9fd5d0535b896ab6565f226ce6ae6fab381ea6f71a5f3fa9598a,
byte-identical to the sealed v28.1 copy). Its own status line (line 3)
is: "PROVED CANDIDATE; promotion audit may attack provenance/typing
but no new frontier input is assumed" — quoted here verbatim, NOT
upgraded (round-3 findings 3 and B5). Its verification record: G1 was
consumed by the promoted lower-bound closeout (v28.1, five external
audit rounds) and its endpoint arithmetic is exact-rational
guard-checked in that sealed bundle. Consumed here: §3:117–123
(boxed): the closed full-zero set Z := R0^{-1}(0) is compactly
interior, Z ⊂⊂ (−1,1)²; §4:129–133: m_g := min_{[−1,1]} g > 0;
§4:172–179: the lawful existential constants 0 < b_0 <= b(t) on the
corridor. G1's endpoint-reserve inputs are provenance-anchored by
dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md (sha256
ec4ffeadf81a33553dfd3a215c2ed4cacaf72f0d226be1068838344183dd4fdc) —
the two rational reserves are family-A coarse inactivity bounds, not
Theorem-(N)'s exact margins (round-3 finding 11 discharged). The 08
document's family-A source — REFLECTION_DUAL_UPPER_ENVELOPE_AND_
ADAPTIVE_TAILS.md, Theorem 4.1 with its exact rational verifier — is
carried as a full byte-identical copy in dependencies/ (sha256
589bb7d804984910cff814a3a7513a94634ce37b8c0e7f2cc49a281bb8b0f216;
round-4 proof finding F-04). TERMINATION STATEMENT (stated plainly,
per the same finding): deeper receipts named inside these sealed
sources — in particular the Theorem-N round-3 blind-audit source
referenced by 08's family B — are NOT carried in this bundle; that
chain terminates in the sealed v28.1 closeout archive (sha256
9ec7cab5e54d2168f27840e1eec581cecd163092dff1bff13c33dc14ed7df192,
quoted in authority/PROMOTED_LOWER_RATE_RECEIPT.md) and is inherited
at that bundle's PROMOTED status, exactly as the lower bound itself
is.

1d. THE ENDPOINT-CESARO SOURCE — FULL byte-identical source,
dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md (sha256
1ed80a067d3afcbd04c58a8792f1c98ae83aff0d783947496f81b7db4b4472b4).
CONSUMED: §2:85–94 ONLY — the boxed exact two-boundary flux identity,
which is two lines of algebra from H lambda = S lambda (re-derived
character-for-character by the round-3 proof auditor, its F14).
EXPLICITLY NOT CONSUMED, BY SECTION NUMBER (round-3 finding 4 and
blocker 4):
  - §6 ("Why 0 < rho± < 1 needs no numerical multiplier certificate"),
    lines 226–292: a RIVAL strictness argument whose hypotheses are
    sourced to a prose-named, unreceipted supplier ("the Sprint-1198
    amplitude-elimination hypotheses"). This proof's strictness is §3
    below, from the Lean-anchored band algebra and the certified
    window; §6 is superseded for every purpose of this bundle. (The
    round-3 auditor observed §6's mechanism coincides with certificate
    §7's audited elimination — corroboration, but this proof still
    does not consume §6.)
  - §9 (lines 455–509): its warning concerns the two-end SYMMETRY
    identity r_A(x_+) = r_B(beta), which this proof NEVER uses — the
    two ends are bounded separately in §3 (round-3 finding F2:
    attribution corrected; dependency removed outright).
  - §3 (lines 101–132): realizes truncations in local dimension at
    most |I|+3 by PV padding. SUPERSEDED by this proof's §4, which
    achieves exactly d = |I| by endpoint-projector completion — a
    strict improvement; the discrepancy is flagged here, not silent
    (round-3 finding 15).
  - §10's numerical scouts: reconnaissance in the source's own words;
    not consumed.
  - §13's conditionality on receipt E1: discharged constructively by
    §3.1 below (the four endpoint labels all lie in the compact
    interior corridor); noted for completeness — the consumed §2 is
    exact algebra and never needed E1.

1e. THE TRUNCATION SOURCES — FULL byte-identical sources:
dependencies/RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md
(sha256
908874eed6fe673c80a4c4ac1481809f62b8f6d716556de34228b8fb4b07c8f9;
provenance for §4's block anatomy) and dependencies/
ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md (sha256
d486e3e33f83afcea41a68b1930f2548e399eaa584e371c7ea03dc619df054bb,
byte-identical to the sealed v28.1 upper_artifacts copy and matching
the U1-round hash anchor; the matching/completion rules PART A of the
second-engine guard is built from — round-4 integrity finding 5). §4
below is self-contained and the completion's exactness is
second-engine verified symbolically.

1f. THE PROMOTED LOWER RECEIPT [P] — authority/
PROMOTED_LOWER_RATE_RECEIPT.md; consumed ONLY by §8's conditional
corollary, never by the upper proof.

## 2. Corridor

By 1a(ii) (§10:798) every adjacent label pair lies in the full-zero
set Z; by G1 (1c, §3:117–123) Z ⊂⊂ (−1,1)². Let K denote the union of
the two coordinate projections of the closure of Z: a COMPACT subset
of (−1,1) containing every label c_j and every label limit. On K:
b(t) = sqrt(1−t²)/2 is continuous with b >= b_0 > 0 (t bounded away
from ±1); g is continuous with g >= m_g > 0 (1c); hence the transport
multiplier r := g/b is continuous on K with

    0 < 2·m_g <= r(t) <= R_max := sup_K max{ r, 1/r } < infinity,  (2.1)

using b <= 1/2 (Lean: amplitude_b_le_half) for the lower bound. No
collar payment is needed: the labels are IN Z, which is compactly
interior; compactness alone gives the bounds.

## 3. Monotone labels, tail ratio limits, and strictness

3.1 SINGLE-MAP MONOTONICITY (round-3 blocker B4, executed). By 1a(ii),
P(c_{j+1}) = c_j for EVERY j — one map, every link. By 1a(i), P is
strictly increasing and one-to-one, so P^{-1} exists on ran(P) and is
strictly increasing. Hence

    c_{j+1} = P^{-1}(c_j)   for every j in Z.                      (3.1)

First, c_1 != c_0: if c_1 = c_0 then by (3.1) and induction the label
sequence is CONSTANT, say c_j = c for all j; then by (1.1) lambda is
exactly geometric with fixed ratio r(c) > 0, which is in l²(Z) in
NEITHER direction if r(c) != 1 and not normalizable if r(c) = 1 —
contradicting the certificate's unit vector. So c_1 != c_0.

If c_1 > c_0: applying the strictly increasing P^{-1} to both sides
of c_j > c_{j-1} gives c_{j+1} > c_j (forward induction), and
applying the strictly increasing P to c_j > c_{j-1} gives
c_{j-1} > c_{j-2} (backward induction); so (c_j) is strictly
increasing on all of Z. If c_1 < c_0, it is strictly decreasing.
Either way the WHOLE sequence is strictly monotone and confined to
the compact K (§2), hence both tail limits exist:

    t_+ := lim_{j -> +infinity} c_j,
    t_- := lim_{j -> -infinity} c_j,     t_± in K ⊂ (−1,1).        (3.2)

(All subsequential limits of a convergent sequence coincide, so in
the response parametrization of the Cesàro source's §4 the four
endpoint labels alpha, beta, x_+, x_- equal t_+ or t_-; that source's
receipt E1 is thereby discharged, though nothing below needs it.)

3.2 THE OUTWARD RATIO LIMITS EXIST — NO FIAT (round-3 finding F4). By
(1.1), lambda_{j+1}/lambda_j = r(c_j) EXACTLY, r is continuous on K
(§2), and c_j -> t_±; therefore

    lim_{j -> +infinity} lambda_{j+1}/lambda_j = r(t_+) =: y_+,
    lim_{j -> -infinity} lambda_{j-1}/lambda_j = 1/r(t_-) =: y_-,  (3.3)

with 0 < y_± < infinity by (2.1). y_+ is the outward one-step
amplitude ratio at the right end; y_- at the left end.

3.3 THE LIMIT RATIO EQUATION (from the eigen-row, both ends). Row j
of H lambda = S lambda (1a(iv)) divided by lambda_j:

    b(c_{j-1})·(lambda_{j-1}/lambda_j) + d(c_{j-1}, c_j)
      + b(c_j)·(lambda_{j+1}/lambda_j) = S.

Let j -> +infinity: both neighbor ratios converge (3.3, with
lambda_{j-1}/lambda_j -> 1/y_+), both labels -> t_+, and b, d are
continuous, so with D(t) := d(t,t) = t² − 1:

    b(t_+)·(y_+ + 1/y_+) = S − D(t_+),  i.e.
    y_+ + 1/y_+ = mu(t_+),   mu(t) := (S − D(t))/b(t).             (3.4)

Let j -> −infinity: identically, y_- + 1/y_- = mu(t_-).

3.4 THE SCALAR BAND BOUND — FOR EVERY INTERIOR t (round-3 finding F3:
the two quantities now cleanly separated; THIS step is scalar algebra
valid for all t, and only (3.4) ties it to the carrier's limits). For
every t in (−1,1), using 2b(t) = sqrt(1−t²):

    D(t) + 2b(t) = t² − 1 + sqrt(1−t²) <= 1/4                      (3.5)

— the Lean theorem band_quarter_ceiling verbatim (via band_identity:
t² − 1 + s = s(1−s), and s_mul_one_sub_s_le_quarter). Hence, with
0 < b(t) <= 1/2 (Lean: amplitude_b_le_half):

    mu(t) − 2 = (S − D(t) − 2b(t)) / b(t)
             >= (S − 1/4) / b(t)
             >= 2·(S − 1/4)                                        (3.6)
             >  2·(S_LO − 1/4)     [S > S_LO, window (0.1); the
                                    literal comparison 1/4 < S_LO is
                                    Lean: quarter_lt_window_lower]

    mu(t) >= mu_min := 2 + 2·(S_LO − 1/4) = 2.001750769003037     (3.7)

(exact terminating decimal), for EVERY interior t simultaneously — in
particular at t_+ and t_-.

3.5 STRICT DECAY AT BOTH ENDS. Fix an end and write y for its outward
ratio, mu for mu(t_±) >= mu_min > 2. By (3.4), y + 1/y = mu, so y is
one of the two positive roots x_dec(mu) < 1 < x_gro(mu) = 1/x_dec(mu)
(distinct since mu > 2 excludes y = 1). l²(Z) excludes the growing
root: an outward ratio limit y > 1 makes lambda grow geometrically
outward, contradicting lambda in l². Hence y = x_dec(mu). In the form

    x_dec(mu) = 2 / ( mu + sqrt(mu² − 4) )                         (3.8)

x_dec is transparently strictly decreasing in mu on (2, infinity), so
mu >= mu_min gives, at BOTH ends,

    y_± <= x_max := x_dec(mu_min) = 0.95902403684... <= 0.9590241,
    y_±² <= x_max² = 0.91972710323... <= 0.9197272 < 1.            (3.9)

All displayed decimals are BOUNDS rounded in the SAFE direction
(upper bounds rounded UP — round-3 finding F5), guard-checked
digit-for-digit exact-rational/high-precision in
guards/guard_a8_strictness.py, and are not rate claims; the theorem's
constant remains existential.

3.6 INDEX BOOKKEEPING (the factor of two, displayed). Tail MASS sums
amplitude SQUARES: at the right end lambda_{j+1}/lambda_j -> y_+
gives, for every eta > 0, eventually lambda_j² <=
C_eta·(y_+ e^eta)^{2j}; the amplitude square exactly cancels the
half-index convention of any two-step accounting. Define the
per-index tail-mass exponents

    kappa_± := −2·log y_± >= −2·log x_max
             = 0.08367827985... >= 0.0836782 > 0                  (3.10)

(lower bound correctly rounded DOWN).

3.7 THE HARMONIC-MEAN STEP, WRITTEN (round-3 finding F7; display
repaired per round-4 proof finding F-02). The map
(a, b) -> (1/a + 1/b)^{-1} is increasing in each argument on
(0, infinity)²: increasing a decreases 1/a, decreases the sum,
increases the inverse. Hence with kappa_± >= K_0 := 0.08367827985
(a DOWN-rounded decimal surrogate — named K_0 to keep it distinct
from the compact set K of section 2 — for −2·log x_max — and the
rounding direction is safe HERE because K_0 appears below only in
K_0/2, rounded down, and in the DENOMINATOR of 2/K_0, where a
down-rounded K_0 makes 2/K_0 an over-estimate, i.e. safe for an
upper display; the shorter
surrogate 0.0836782 of (3.10) is NOT safe in a denominator —
2/0.0836782 = 23.9010877... would overshoot the bound below, the
round-4 F-02 defect — and is never used in this section):

    kappa_eff := (1/kappa_- + 1/kappa_+)^{-1} >= (2/K_0)^{-1} = K_0/2
              >= 0.0418391,
    1/kappa_eff <= 2/K_0 = 23.90106493088... <= 23.9010650.          (3.11)

Exact-rational check of the displayed chain: 2/K_0 =
2/0.08367827985 = 23.90106493088... <= 23.9010650 (TRUE as printed;
the guard's G5 parses EVERY displayed K_0 from this document and
re-verifies the chain in exact rationals — a chain check, not a
token check). The exact value of 2/(−2 log x_max) is
23.90106492878...; the display 23.9010650 is the UP-rounded safe
bound (agrees digit-for-digit with the guard's two-sided assert and
the banner — round-3 finding 8).

## 4. The truncation (exact d = |I|)

For I = [−L, R] ∩ Z: keep every full 2×2 rank-one block of each
matching whose paired indices both lie in I; at a severed endpoint
pair replace the block by the one-dimensional projector on the
retained index (the complementary outcome takes the complement). All
six operators remain exact projections — direct sums of orthogonal
rank-one blocks and 1-dim projectors; verified SYMBOLICALLY for
arbitrary block angles, both matchings, m = 3..8, complements
included, by guards/guard_second_engine_projectors.py PART A. The
truncated state is psi_I = M_I^{−1/2} sum_{j in I} lambda_j e_j (x)
e_j with M_I = sum_{j in I} lambda_j². The LOCAL DIMENSION IS EXACTLY
d = |I| — no dilation, no padding. (The Cesàro source's §3 achieves
only |I|+3 by PV padding; superseded, see 1d.)

## 5. Error accounting

5.1 PRINCIPAL COMPRESSION FIRST. Let v_I be the value of the
principal Jacobi compression on I. The flux identity (1d, Cesàro
§2:85–94, boxed; re-derivable in two lines from H lambda = S lambda):

    S − v_I = [ b(c_{a−1}) lambda_{a−1} lambda_a
              + b(c_b) lambda_b lambda_{b+1} ] / M_I.              (5.1)

Only the two cut edges are unpaid; b <= 1/2 gives S − v_I <=
(1/2)·B_I/M_I with B_I := |lambda_{a−1}lambda_a| +
|lambda_b lambda_{b+1}|.

5.2 FROM COMPRESSION TO THE STRATEGY: THE THREE-ROW TABLE. Let V_I be
the Bell value of the §4 strategy. Relative to the principal
compression, the endpoint completion changes exactly three things:

    row 1: the two cut-bond OFF-DIAGONAL terms  -> already and only
           accounted by the flux identity (5.1); NOT charged again.
    row 2: the two RETAINED ENDPOINT DIAGONALS  -> coefficient change
           of modulus <= 2 per affected Bell term, at sites a and b;
           charged in 5.3.
    row 3: everything else                      -> unchanged, exactly.

5.3 THE ENDPOINT-DIAGONAL PAYMENT. R_max (2.1) is finite. By the
transport law (1.1), lambda_a² <= R_max·|lambda_{a−1} lambda_a| and
lambda_b² <= R_max·|lambda_b lambda_{b+1}|, so

    lambda_a² + lambda_b² <= R_max · B_I.                          (5.2)

The operator display (§0) has marginal coefficients of absolute sum 4
and eight joint coefficients of modulus 1. All six measurement
operators are projections, hence contractions; a joint term's
diagonal is a product of two projector diagonals, so its change has
modulus at most 2, and the SAFE two-sided count is

    C_diag <= 4·1 + 8·2 = 20,
    |V_I − v_I| <= C_diag · R_max · B_I / M_I <= 20 R_max B_I/M_I. (5.3)

(The one-sided count gives 12; the proof uses only the safe 20 —
constants are existential, the change is absorbed. Verified by the
round-3 proof auditor, its F15.)

5.4 THE NAMED CONSTANT. Combining (5.1) and (5.3), with
T_I := sum_{j not in I} lambda_j² and M_I = 1 − T_I:

    0 <= S − V_I <= C_B · B_I / (1 − T_I),
    C_B := 1/2 + 20 R_max < infinity.                              (5.4)

5.5 TAIL AND BOND ESTIMATES (derived from 3.6). For every eta > 0,
eventually lambda_j² <= C_eta e^{−(kappa_+ − eta) j} on the right
tail and symmetrically on the left; geometric summation gives

    T_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)},          (5.5)
    B_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)},          (5.6)

and, absorbing C_B and (1 − T_I)^{−1} = 1 + o(1) into the o(·):

    S − V_I <= e^{−kappa_− L + o(L)} + e^{−kappa_+ R + o(R)}.      (5.7)

## 6. Every dimension, the balance, and the rate

6.1 ALLOCATION. For every sufficiently large integer d set

    L_d := floor( kappa_+ (d−1) / (kappa_− + kappa_+) ),
    R_d := d − 1 − L_d,                                            (6.1)

so |I| = L_d + R_d + 1 = d EXACTLY: the §4 strategy has local
dimension exactly d, for every such d.

6.2 BALANCE. kappa_− L_d = kappa_eff (d−1) + O(1) and kappa_+ R_d =
kappa_eff (d−1) + O(1) with kappa_eff as in (3.11). (Verified by the
round-3 proof auditor, its F23.)

6.3 THE RATE, FOR EVERY d. Substituting (6.1) into (5.7):

    S − S_d <= S − V_{I_d} <= exp( −kappa_eff d + o(d) ).          (6.3)

## 7. The theorem

For every 0 < eta < kappa_eff, (6.3) gives eventually S − S_d <=
e^{−(kappa_eff − eta) d}; choosing d(eps) = max{ d_eta,
ceil( log(1/eps) / (kappa_eff − eta) ) } and letting eta ↓ 0:

    limsup_{eps ↓ 0} D_upper(eps) / log(1/eps) <= 1/kappa_eff.     (7.1)

    THEOREM (U1G). D_upper(eps) = O( log(1/eps) ), existential
    constant 1/kappa_eff > 0; moreover the anchored uniform bound
    (3.11) gives 1/kappa_eff <= 23.9010650 — a derived inequality
    from the certified window and the band algebra alone, claiming
    no sharpness, and inheriting the disclosed residual risk of the
    [P] root (§1a).                                                (7.2)

## 8. Conditional corollary (scope-fenced)

IF AND ONLY IF this U1G gate promotes: together with the promoted
lower bound (1f), D(eps) = Theta(log(1/eps)) at local-dimension
scope, existential constants. Not an independently promoted claim of
this document.

## 9. Claim boundaries

Local Hilbert-space dimension only; no Schmidt-rank reading. All
constants existential except the explicit UPPER bound in (3.11)/(7.2),
which is a derived inequality, guard-checked two-sidedly, claiming no
sharpness. S is consumed only through: the certified window (0.1)
[for the explicit bound], and the doubly-anchored fact S > 1/4 [for
existential strictness]. The residual risk of the [P] root's §§6–9 is
inherited and disclosed at its exact point of consumption (§1a). The
distorted-return functional, the return-quotient orientation, and the
endpoint return-sector mechanism are not invoked anywhere; the
strictness algebra (3.5) is the Lean-checked scalar band ceiling. No
selection theorem, no sextic, no hyperbolicity, no retired numerical
constant appears in this document's live chain — the retirement record
lives in authority/U1E_CORRECTION_LEDGER.md and the on-disk gate
verdicts, not here.
