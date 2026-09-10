# Publication procedure

Local preparation does not authorize external publication.

1. Complete [VERIFY.md](../VERIFY.md), including public-file exclusion,
   source/PDF identity and clean-filter stability.
2. Test an isolated candidate containing only the intended public files and
   freeze `release/SOURCE-MANIFEST.json` from those Git-normalized bytes.
3. Inspect the PDF, source diff and [correction record](REVISION-NOTES.md).
4. Obtain author approval of inventory, version and release. Version 4.1.0
   was published at DOI 10.5281/zenodo.22698978. Decisions are recorded in
   `release/RELEASE-DECISIONS.json`.

The verified integration archives a **published GitHub release** and then
assigns its version DOI. A commit or pushed tag alone is not that publication.
Do not create a duplicate manual Zenodo deposit or invent a future DOI.
Before release, CITATION.cff identifies the versioned GitHub release URL;
.zenodo.json supplies the version and archive metadata and has precedence
over CITATION.cff for Zenodo ingestion. The paper's concept and historical
DOIs remain explicitly distinguished from the current revision.

Record approvals against that manifest, configure the protected
`i3322-release-review` environment and approved hash variables, and only then
commit/push/tag as authorized. Wait for the tag's hosted verification and
human release-review approval **before publishing the GitHub release**.
The webhook does not wait for CI; publishing prematurely bypasses that order.
Local checks do not certify hosted execution.

After authorized publication, obtain the actual Zenodo record. Verify the
version, concept DOI, archive filename, and every archived source byte against
the approved manifest. Record the new version DOI in GitHub release notes.
Keep the tag and archived source immutable. If adding the new DOI to the
arXiv paper, build a separate citation-only variant and record its distinct
PDF/source hashes; do not claim it is byte-identical to the archived PDF.
No mathematical edits are implicit in DOI reconciliation. A pre-reserved DOI
route is allowed only if a supported linked workflow is independently verified.

The main-branch paper now includes the minted v4.1.0 DOI. Its rebuilt
source/PDF hashes are recorded in `paper/BUILD.json`; the frozen release
retains its original files. No arXiv replacement has been submitted by this
DOI update.

Replace the existing arXiv article, not a duplicate submission. Its source ZIP
contains only `resolution.tex` and `LOWER-BOUND-REVISION.tex`. Inspect arXiv's
generated PDF before completing replacement.

Suggested factual comment:

> Replaced the quantitative lower-bound argument with a weighted-flow proof;
> corrected foundational and upper-bound estimates and spatial-proof exposition.
> Main statements unchanged; concurrent work and verification scope clarified.

Official procedures (recheck at submission):
[arXiv replacements](https://info.arxiv.org/help/replace.html) and
[Zenodo versions](https://help.zenodo.org/docs/deposit/manage-versions/).
Previous public versions remain part of the record.
