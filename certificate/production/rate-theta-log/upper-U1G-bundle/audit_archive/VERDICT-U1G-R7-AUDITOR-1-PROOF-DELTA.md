# VERDICT — U1G round-7 gate, PROOF surface (MINIMAL DELTA AUDIT) — **PROMOTE CARRIES**

PROVENANCE: delivered in-session by the round-7 proof-surface delta
auditor on 2026-08-07 against frozen commit bf47d0b8 and written to
disk the same day by the adjudicating track, verbatim (task output
file empty; delivery record is the session transcript — the same
disclosed channel as the round-2/round-6 transcriptions, which the
round-7 integrity auditor authenticity-tested by reconstructing the
prior tree from git and reproducing every falsifiable claim).

---

# GATE VERDICT — U1G ROUND 7, PROOF SURFACE (MINIMAL DELTA AUDIT)

**VERDICT: PROMOTE CARRIES to bf47d0b8**

Auditor: hostile external, refutation-first, default FAIL. Subject frozen at `bf47d0b8`. Delta base `a52d24aa`. Zero blocking findings.

## 1. Diff summary — proof surface

`git diff a52d24aa bf47d0b8 -- U1E/proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md`: one hunk at §3.7, `-4/+6` lines, file 532 → 534 lines. I did not trust the visual diff: I extracted both blobs, collapsed all whitespace, and ran a word-level SequenceMatcher. Result — exactly TWO non-equal opcode blocks in the entire 26.4 KB document: `K` → `K_0` and `K/2,` → `K_0/2,`, both in the single §3.7 safety sentence named by round-6 F-02. Every other byte of difference is line rewrap. This is exactly the sanctioned rename and nothing else. No mathematical content, no display value, no fence, no scope word touched. Custody clean.

## 2. Internal consistency of the renamed sentence

`" K/2"` absent; `"2/K "` absent; `"K :="` absent (required); `"K_0 :="` present, line 380, sole definition site. Full bare-K census (regex boundary-guarded): 7 hits, all denoting §2's compact set — line 382 is the disambiguating prose itself. No bare-K reference to the decimal surrogate survives anywhere in the proof.

## 3. §3.7 chain, exact rationals + guard

K_0 = 1673565597/20000000000 exact: 2/K_0 = 23.90106493088959... <= 23.9010650 TRUE; K_0/2 = 0.041839139925 >= 0.0418391 TRUE; premise carried by (3.10). The F-02 counterexample reproduces (2/0.0836782 = 23.90108773... > bound) and the short surrogate is confirmed absent from §3.7's chain. All four guards run by me: EXIT=0 each. Because I lean on G5 and G5 changed in this commit, I audited its diff for weakening: it is a strengthening on every axis (identifier widened so the rename cannot narrow the tripwire; all six comparison syntaxes; mu_min branch). Nothing removed, no assert relaxed.

## 4. Freeze

Manifest 50/50 at open and close; zero mismatched/missing/unlisted; 0 .pyc anywhere; git clean throughout; independent recursive digest over all 51 files byte-identical at open and close (4a245387e8616b3ef1bd286ea2c48f005494fbd10b60b79ca8342ea17331305d). Zero drift of my own; guards wrote nothing.

## 5. Theta(log) fencing

Unchanged at all live sites; §8 fence verbatim intact; "unconditional" nowhere in the proof; "sharp" only as denials.

## Observations (non-blocking)

O-1 (LOW): the rewrap shifts the proof +2 lines; hunted for stale citations — no live document cites U1G proof line numbers; archived verdicts' cites are frozen records of their own commits, correctly historical. O-2 (LOW, pre-existing): §3.7's "G5 parses EVERY displayed K_0" is slightly generous — G5 parses every definition site (today exactly one) with other decimals covered by the structural range check; substance not overstated. O-3 (COSMETIC): orphan short wrap line.

**The round-6 F-02 recommendation is implemented exactly, completely, and in isolation. The round-5 PROMOTE, carried by round 6, carries again. PROMOTE CARRIES to bf47d0b8.**
