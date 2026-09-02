# VERIFY — how to check this repository's claims yourself

This page is for a skeptical reader who wants to verify what is proved here
without first absorbing the repository's history. It states exactly what each
command checks, what its expected output is, and — just as importantly — what
is **not** covered by any machine check. Every command below was executed on a
clean checkout before this page was written; expected outputs are quoted from
those runs.

The four public claims (stated precisely in `paper/resolution.pdf`):

| # | Claim | Certificate root |
|---|---|---|
| W | Unconditional window `0.2508753845015185 < S ≤ 0.250875388108398` (width `3.607e-9`) for the common I3322 quantum value | `certificate/release/`, sprints 1287–1295 |
| N | **Theorem (N):** no finite-dimensional quantum strategy (any dimensions, mixed states, POVMs) attains `S` — the Pál–Vértesi (2010) conjecture | `certificate/production/theorem-N-four-receipts-at-S/` |
| S | **Theorem (S):** `S` *is* attained by a spatial strategy on `ℓ²(Z) ⊗ ℓ²(Z)`; hence `C_qs(3,3;2,2) \ C_q(3,3;2,2)` is nonempty and `C_q` is not closed | `certificate/production/theorem-S-spatial-attainment-at-S/` |
| R | **Theorem (Rate):** `D(ε) = Θ(log(1/ε))` — reaching `S` to accuracy `ε` requires, and an explicit truncation achieves, local dimension of order `log(1/ε)` | `certificate/production/rate-theta-log/` |

---

## 1. Sixty-second start

Requires Python ≥ 3.11 with the pinned dependencies:

```
pip install -r requirements.txt        # mpmath, numpy, python-flint, sympy
python certificate/release/verify_release.py
```

**Expected:** process exit code `0`, a JSON report ending with
`"rigorous_two_sided_window_certificate_closed": true`, and the status string

```
CUSTODY_PASS_COMMON_VALUE_HISTORICAL_HEADLINE_GAP
```

Measured runtime: **~4 seconds**. This checks manifest coverage, frozen
SHA-256 custody of every certificate file, and the exact rational window —
including the full-precision rational endpoints printed in the report.

**Read the status string carefully — it is honest, not alarming.** The
"HISTORICAL_HEADLINE_GAP" clause refers to a *withdrawn early claim* (exact
identification of the optimum with a specific decimal), which this repository
itself refuted, decertified, and does not assert. The current claims W, N, S,
R are **not** gated by that clause; each has its own certificate directory and
status file. `"exact_optimum_identified": false` in the report is the same
disclosure: the exact value of `S` beyond the certified window is open and
not claimed. See §6 for the correction history.

Deterministic full replay (regenerates every production and independent
receipt in dependency order, then rechecks all semantics):

```
python certificate/release/verify_release.py --full
```

This takes substantially longer than the default mode and is byte-
deterministic; the default mode above is sufficient to check custody and the
window.

---

## 2. Verifying Theorem (N) — finite-dimensional nonattainment

Directory: `certificate/production/theorem-N-four-receipts-at-S/`.
Start with `THEOREM_N_SIGNED_PUBLIC_STATEMENT.md` (the exact statement and
its dependency list) and `FOUR_RECEIPTS_AT_S_ASSEMBLY.md` (how the four
receipts compose into the theorem). The proof survived three rounds of
refutation-first adversarial review; the review record is in `review/`.

Machine-checkable parts (`artifacts/`, each runs in seconds):

```
python artifacts/four_receipts_at_S_endpoint_exact.py
```
Expected output — the two exact endpoint margins, as rationals:
```
m_plus = 23686917837403/3008753881083980
m_minus = 274562305945801/4008753881083980
```
These are the *same fractions* proved positive, antitone, and dominating the
paper's displayed decimals in the Lean lemma `EndpointMargins.lean` (§5) — a
cross-check between two entirely different toolchains.

```
python artifacts/convex_envelope_algebraic_guards.py
python artifacts/critical_zero_set_algebraic_guards.py
```
Expected: each prints a `PASS:` line for its algebraic identities **and an
explicit `NOT VERIFIED:` line** naming the analytic steps the script does not
cover (envelope existence/maximality; gluing, limiting passage, spectral
support, operator closure). Those steps are proved in the paper and audited
in the review record; the scripts guard the algebra only. This split is
deliberate — see §7.

---

## 3. Verifying Theorem (S) — spatial attainment

Directory: `certificate/production/theorem-S-spatial-attainment-at-S/`.
Start with `THEOREM_S_SIGNED_PUBLIC_STATEMENT.md` and
`CURRENT_S_SPATIAL_ATTAINMENT_THEOREM.md`; `STATUS.json` records the
promotion history (referee verdict "PROMOTE conditional on repairs"; the
repairs V1–V9 and their execution ledger are included). `MANIFEST_SHA256.txt`
freezes the package.

Honest boundary: Sections 6–9 of the proof document (conull invariant set,
Borel transversal, uniqueness of disintegration) were originally flagged in
`STATUS.json` as carrying the residual proof risk. That risk was
**discharged on 2026-08-07**: `AMENDMENT-2026-08-07-SECTIONS-6-9.md` records
the full expanded write-up
(`sections-6-9-expansion/U2-SECTIONS-6-9-EXPANDED.md`: 25 numbered lemmas
with complete proofs, explicit quantifier labels, and an axiom inventory),
reviewed in two blind adversarial rounds — a hostile proof-surface review
plus an independent countermodel search (22 constructed attacks, no
counterexample), then a diff-scoped re-review of the repaired document that
verified every repair item by item. `STATUS.json` itself is hash-frozen and
deliberately unamended; the amendment file is the correction of record. A
reader auditing Theorem (S) should still read exactly those sections
hardest — the amendment says where.

---

## 4. Verifying Theorem (Rate) — `D(ε) = Θ(log(1/ε))`

Directory: `certificate/production/rate-theta-log/` (result now stated as
Section 5 of the paper). Two bundles:

- `lower-v28_1-bundle/` — the sealed lower-bound chain. `guards/` contains
  the exact-arithmetic guard scripts (endpoint line certificate, grid/edge
  budget, projection squeeze, replay, historical hashes); `STATUS_V28.json`
  and the dependency receipt index record the chain's audit state.
- `upper-U1G-bundle/` — the constructive upper bound with its
  self-contained proof, seven byte-identical dependency copies, four guard
  scripts with a 40-case injection self-test, and the complete
  fourteen-verdict record of its seven-round promotion gate, including every
  denial and the repair each forced.

The derived upper-half constant is `1/κ_eff ≤ 23.9010650` (no sharpness
claimed); constants are existential.

---

## 5. Machine-checked cores (Lean 4 + Mathlib)

Directory: `lean/I3322Kernel/`. Toolchain: `leanprover/lean4:v4.30.0`.

```
cd lean/I3322Kernel
lake build          # must complete with no errors, no `sorry`
```

The first build downloads Mathlib and takes a while; subsequent builds are
fast. `AxiomCheck.lean` confirms the results use standard axioms only.

**Claim boundary (stated in `lean/I3322Kernel/README.md` and repeated here):**
the formalization covers the paper's *algebraic cores* — the displayed
formulas a referee would otherwise check by hand (the amplitude-elimination
chain and quarter ceiling; the exact endpoint margins of §2; the finite-
closure lemma, which is the single point where finite dimensionality enters
Theorem (N)). The measure-theoretic chain, the operator-algebraic chain, and
the interval-arithmetic window are **not** formalized in Lean; they are
covered by the paper, the adversarial review records, and the exact-
arithmetic scripts above.

---

## 6. Correction history — read this before comparing versions

An early release of this repository claimed an exact identification of the
optimum. **That claim was refuted by this project's own audit and publicly
decertified**; the current theorems were rebuilt on independent routes that
never pose the failed step (amplitudes are read off an existing conditional
spectral measure, so the broken compatibility equation does not arise). The
decertified route is preserved — not hidden — in the frozen DOI releases and
the sprint history below the warning line in `README.md`. The custody status
string in §1 exists precisely to keep that history disclosed on every run.

Version record: concept DOI `10.5281/zenodo.21782008`; v3.0.0 (2026-08-05)
restored nonattainment and nonclosure on the independent route; v4.0.0
(version DOI `10.5281/zenodo.22099128`) is the merged paper of record.

---

## 7. What "verified" means here, and what it does not

Three layers, kept deliberately distinct:

1. **Exact-arithmetic scripts** (rationals, interval arithmetic, symbolic
   residuals) verify every load-bearing *computation*: the window endpoints,
   the algebraic identities, the endpoint margins, the witness
   reconstructions. Wherever a script covers only part of a proof, it prints
   a `NOT VERIFIED:` line naming the remainder.
2. **Independent reconstructions** re-derive key objects in separately
   written engines that do not import their production counterparts
   (`certificate/independent/`, and the independence boundary listed in the
   §1 report): the 255-dimensional strategy re-evaluated at 160-digit
   interval precision, both 25,601-knot upper witnesses rebuilt with
   different partition traversals, the Bellman–path equality theorem
   rebuilt against 24 exact carrier fixtures, and more. One caveat is
   disclosed in the report itself: the reconstructions' chronology is not
   externally time-sealed and is not represented as cryptographic evidence
   of blindness.
3. **Analytic steps** (weak-* limits, disintegration, operator closure,
   Sections 6–9 of Theorem (S)) are proved in the paper and were subjected
   to multi-round refutation-first review (records in `review/` and in each
   certificate directory), but are *not* machine-checked. For Theorem (S)
   §§6–9 specifically, the expanded 25-lemma write-up and its two-round
   blind gate live in the certificate's `sections-6-9-expansion/` directory
   (see §3 above). They are the right
   place for a referee to spend effort, and the documents say so.

No claim in this repository rests on a check that is not either runnable
above or explicitly labeled as analytic.

---

## 8. Suggested reading paths

- **15 minutes:** §1 quickstart; `paper/resolution.pdf` abstract and
  theorem statements; `paper/CERTIFICATE-MAP.md` (one table from every claim
  to its owner and verification).
- **2 hours:** the above, plus `THEOREM_N_SIGNED_PUBLIC_STATEMENT.md` with
  its assembly document and one review round; run the §2 scripts; skim the
  Lean lemmas.
- **Full audit:** add Theorem (S) Sections 6–9 (originally flagged residual
  risk, discharged by the 2026-08-07 amendment — read both),
  the rate bundles' promotion records, `verify_release.py --full`, and
  `lake build`. The sprint directories under `certificate/production/`
  contain the complete construction history, including failures.

Questions, corrections, and refutation attempts are welcome — refutation-
first review is how every theorem here was promoted, and the fastest way to
improve this record is to attack it. Contact: see `CITATION.cff`.
