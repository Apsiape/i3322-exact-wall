# Lane I — independence, custody, and claim boundaries

**Reviewer verdict:** `FAIL`  
**Repository state audited:** immutable commit `b3aeee7`  
**Edits by reviewer:** none

## P0 — dependency closure was false as published

The standalone tree omitted load-bearing Sprints 1226 and 1227 while Sprints
1228 and 1229 cited them.  The sealed 19-source packet omitted the same two
dependencies.  Nevertheless the release manifest unconditionally reported
`complete_dependency_closure: true`, and the release receipt reported no
private-corpus dependency.  The reviewer therefore rejected the current
standalone-closure claim and, with it, promotion of the two-sided dimension law
in that package state.

## P1 — blind chronology is not externally sealed

The preregistration, source manifest, production assembly, blind
reconstruction, and post-blind acceptance first appeared in one Git commit.
Their internal chronology is self-reported; the public record does not prove
that the source boundary was sealed before the reconstruction verdict.  This
does not show contamination, but it prevents the stronger externally-auditable
chronology claim.

## P1 — PASS receipts overstated their checks

The v1.3 claim-contract guard relied substantially on string presence and
literal booleans.  The release verifier did not traverse the analytic
dependency graph and did not itself enforce a post-replay manifest rehash.
The reviewer independently performed a subsequent custody run and found the
regenerated artifacts byte-stable, but the verifier had not guaranteed that
postcondition.

## P2 — arithmetic checks are correlated

The Decimal and SymPy constant audits encode essentially the same assembly
formulas.  They support arithmetic correctness but are not independent
derivations of the analytic packet theorem.

## Checks that passed

- Exactly 223 selected published files matched the 223-file manifest.
- Default and full replays passed under Python 3.13.12 with pinned
  dependencies.
- A subsequent custody run confirmed byte stability in the audited Windows
  environment.
- The production Arb and separately implemented `mpmath.iv` wall lanes both
  replayed.
- No private filesystem path appeared in public text or extracted PDF text.
- v1.3 metadata remained prospective; no v1.3 tag or DOI had been created.
- Priority language was appropriately qualified as negative search evidence,
  not proof.

## Epistemic limits recorded by the reviewer

The review did not establish chronology of the blind information boundary,
cross-platform replay, bibliographic priority, or line-by-line validity of the
long packet/discard proof.  These limitations must remain visible after any
repair.
