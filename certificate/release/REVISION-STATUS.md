# Working revision, not a new release

The 2026-09-10 lower-proof revision is undergoing development. The existing
release manifest and historical verifier remain unchanged. Their old hashes
are not hashes of the new working manuscript. See `../../VERIFY.md`.

`tools/release-preflight.py` at repository root provides a separate UNRELEASED
snapshot workflow. Its hash comparison is custody only. It does not execute
the historical verifier, replay receipts, create an archive, or assign public
metadata. Historical `--full` may rewrite frozen receipts and must only run
in an isolated disposable copy of its matching snapshot.

Scoped analytic reviews and a fresh selected-Lean rebuild have been completed.
The public current record and correction precedence are in `../../VERIFY.md`
and `../../paper/REVISION-NOTES.md`. This historical manifest is not promoted
to cover the corrected manuscript. No version, DOI or approval is created here.
