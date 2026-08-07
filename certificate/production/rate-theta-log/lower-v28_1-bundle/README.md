# I3322 v28.1 Lower-Bound Final-Fixes Bundle

This tree is the **v28.1 final-fixes layer** for the quantitative lower bound only:
\[
S-S_d\ge c(1+d)^{-K}e^{-Cd},
\qquad
D_{\rm lower}(\varepsilon)=\Omega(\log(1/\varepsilon)).
\]

**Route change:** none. **New receipt lemmas:** none. v28.1 is restricted to Commission v28.1 blockers B1--B3 and minors M1--M8.

The authoritative comparison is `V28_TO_V28.1_DIFF.patch`, generated over the **entire tree**, not only `new_docs`. It must contain every changed file and nothing outside the commission scope. Expected changed files are:

- `new_docs/01_RAW_CELL_PARITY_EDGE_BUDGET_V28.md`
- `new_docs/02_CELL_RESPONSE_AND_BRIDGE_RECURRENCE_V28.md`
- `new_docs/03_REPEATED_CELL_CYCLE_EXACTIFICATION_V28.md`
- `new_docs/04_STATE_CARRYING_COMMON_RETURN_AND_NEUTRAL_GAIN_V28.md`
- `new_docs/05_EXPONENTIAL_LOWER_ASSEMBLY_V28.md`
- `new_docs/06_P4_RECEIPTS_AND_SYMBOL_HYGIENE_V28.md`
- `new_docs/07_CORRECTION_AND_SUPERSESSION_LEDGER_V28.md`
- `new_docs/09_TERMINAL_EVENT_TABLE_V28.md`
- `guards/guard_live_authority_hygiene.py`
- `guards/guard_return_hygiene.py`
- `guards/GUARD_RESULTS.txt` (final v28.1 replay output)
- `README.md`
- `STATUS_V28.json`

Doc 03 §2 is restored verbatim from the v27 historical authority. Hashing the complete section including its trailing newline before the next `##` heading gives SHA-256 `95b51d04aeaa15560e9b8b3fd8d8ded236ecedd8884ce65a3dd0105ff9ef7e91`. From v28.1 onward, any claim that inherited content is “unchanged” requires an explicit source hash or an explicit diff hunk.

The diff artifact itself is necessarily not self-included; it covers every content/guard/status file changed relative to the sealed v28 archive.

Constructive upper-bound artifacts remain supplementary and outside this lower-bound promotion rule.
