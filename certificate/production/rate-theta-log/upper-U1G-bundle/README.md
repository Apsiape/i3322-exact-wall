# U1G — I3322 upper-bound bundle — **PROMOTED (round 7, 2026-08-07)**

GATE CLOSED: the frozen blind-before-promotion gate ran SEVEN rounds
(U1, U1E, U1F DENIED on substance; U1G rounds 4-6 DENIED on
progressively narrower instrument/custody findings; round 7 PROMOTE
on both surfaces at frozen commit bf47d0b8). The proof surface issued
PROMOTE at round 5 after full independent rederivation and it carried
through two delta audits; five consecutive auditors reported the
mathematics is not what fails; the round-7 integrity auditor ran 30
injections and found ZERO false displays in the frozen live chain.
See PROMOTION_RECORD.md for the closure statement and STATUS_U1E.json
for the complete verdict index.

PROMOTED CLAIM: D_upper(eps) = O(log(1/eps)) at local-Hilbert-space-
dimension scope, existential constant, with the derived safe bound
1/kappa_eff <= 23.9010650 (no sharpness claimed; inherits the [P]
root's disclosed residual risk). With the previously promoted lower
bound, the section-8 conditional fires:
D(eps) = Theta(log(1/eps)).

Start here, in order:

1. PROMOTION_RECORD.md — the gate-closure statement.
2. authority/00_AUTHORITY_BANNER_U1E.md — the promoted claim, gate
   rule, freeze rule, LIVE CHAIN definition, provenance model
   (SEVEN full byte-identical dependency copies, zero extracts),
   retraction-block registry, partition rule.
3. proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md — THE PROMOTED PROOF,
   fully self-contained; §1 anchors every authority by hash
   (5 certificate + 6 Lean commit-blob + 2 public-repo + 7 dependency
   digests), §3 the band-strictness route, §§4-7 truncation/
   accounting/allocation, §8 the (now fired) conditional corollary.
4. authority/U1E_CORRECTION_LEDGER.md — the complete seven-round
   repair record (entries 1-26), including every kill, every blocker
   execution, and the custody rules adopted along the way.
5. authority/U1E_DEPENDENCY_GRAPH.md — the promoted dependency graph.
6. audit_archive/ — ALL FOURTEEN gate verdicts on disk (rounds 1-7,
   both surfaces; three transcribed verdicts carry disclosed
   provenance headers and were authenticity-tested by the round-7
   integrity auditor against reconstructed git trees), plus
   superseded extracts and self-audits, each stamped in-file.
7. guards/ — three live guards plus the injection self-test, stdout
   only:
   - guard_a8_strictness.py — the strictness chain, exact + 60-digit,
     two-sided brackets, G5 chain check on every displayed surrogate
     + structural range check of displayed bounds.
   - guard_live_upper_authority_hygiene.py — H0 scope coincidence,
     RB content-digest registry, H5 parsed anchors verified against
     commit blobs (hard-fail, no SKIP), H6 pointers, H7 digest-
     registry byte-identity of all seven copies AND their external
     sealed sources, H8 manifest partition + full filename allowlist,
     H9/H9x fencing and token scans, H10 verdict-custody cmp.
   - guard_second_engine_projectors.py — PART A symbolic projector
     second engine; PART B load-bearing ONLY for the exhibited
     d=24/d=33 values > 1/4 (asserted, Rayleigh-backed; construction
     caveat disclosed in artifacts/small_d_demoted/DISCLOSURE.md).
   - guard_selftest_injection.py — 40 cases: the round-3, round-4,
     round-5 AND round-6 auditors' complete injection sets, all
     firing (run it; writes only to the system temp directory).
8. dependencies/ — EXACTLY seven FULL byte-identical faithful
   predecessor copies, each hash-pinned in proof §1, the manifest,
   and the guard's digest registry.

REPRODUCIBILITY NOTE (round-7 finding F9, disclosed): this bundle's
manifest pins WORKING-TREE digests on the machine of record, which
uses git core.autocrlf=true — a clone checked out with different
line-ending normalization will re-hash differently. To verify the
seal from a clone, either set core.autocrlf=true before checkout or
verify against `git ls-tree -r bf47d0b8 -- U1E` blob identities.
Line-ending normalization is uniform and cannot carry semantic
content. The *.pyc/__pycache__ exclusion in H8 is stricter in code
than the shorthand "sole disclosed exclusion: *.pyc bytecode" used in
three descriptions (round-7 F10; safe direction).

Historical (stamped in-file, nothing live): proof/
CONSTRUCTIVE_LOG_UPPER_BOUND_{U1,U1E,U1F}.md; audit_archive/;
audit_diff/; artifacts/.
