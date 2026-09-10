# Verify the I3322 paper

The current [paper](paper/resolution.pdf) uses [resolution.tex](paper/resolution.tex)
and [LOWER-BOUND-REVISION.tex](paper/LOWER-BOUND-REVISION.tex). Read the
[correction record](paper/REVISION-NOTES.md) before historical proofs.

## Public checks

Install the pinned Python requirements. On Windows, from the root:

```powershell
python -m pip install -r requirements.txt
python tools/run_capped.py --limit-mib 512 --timeout-seconds 60 -- python tools/check_revision.py
python tools/run_capped.py --limit-mib 512 --timeout-seconds 60 -- python tools/release-preflight-selftest.py
python tools/run_capped.py --limit-mib 512 --timeout-seconds 60 -- python tools/verify_candidate_selftest.py
python tools/run_capped.py --limit-mib 512 --timeout-seconds 60 -- python tools/verify_candidate.py static
python tools/run_capped.py --limit-mib 512 --timeout-seconds 60 -- python tools/check_publication.py
```

On Linux use bounded inner commands, for example
`(ulimit -v 524288; timeout 60s python tools/check_revision.py)`.
Run numerical work sequentially; keep local aggregate allocation below 2 GiB.
Default checks need no private audit folder. Optional `--provenance` checks
the author's local imports and is not required for public reproduction.

## Selected Lean declarations

The toolchain fixes Lean 4.30.0; the manifest fixes nine dependency revisions.
From `lean/I3322Kernel/`, with the pinned toolchain installed:

```text
lake exe cache get Mathlib.Tactic Mathlib.Analysis.SpecialFunctions.Sqrt
lake --no-cache build I3322Kernel.QuarterCeiling
lake --no-cache build I3322Kernel.EndpointMargins
lake --no-cache build I3322Kernel.FiniteClosure
lake --no-cache build I3322Kernel.RateCores
lake --no-cache build I3322Kernel.WeightedFlow
lake --no-cache build
lake env lean AxiomCheck.lean
```

Set `LEAN_NUM_THREADS=1`. On Windows prefix each command with
`python ../../tools/run_capped.py --limit-mib 1536 --timeout-seconds 600 --`.
Save the axiom output outside the source set; from the root run
`python tools/verify_candidate.py axioms --log PATH` and
`python tools/verify_lean_pins.py`. The axiom parser requires all 37 requested
names and allows only `propext`, `Classical.choice`, and `Quot.sound`.

A separate fresh local rebuild on 10 September 2026 used new dependency
checkouts and freshly downloaded official Mathlib artifacts, then compiled all
project modules and checked these declarations. It reused the installed
compiler; it was not a full upstream source build. Hosted GitHub execution is
a separate, not-yet-executed check.

## Mathematical coverage

| Component | Evidence and limitation |
|---|---|
| Value/path and critical storage | Analytic sources in the certificate map; not inferred from finite tests |
| Exact value window | Rational/interval certificates; local replay checked all 46,458 upper cells and reconstructed the 255-dimensional lower quotient |
| Nonattainment | Current corrected N1--N5; also implied by the new lower proof conditional on its storage inputs |
| Spatial attainment | Analytic orbit/disintegration proof and expanded certificate; not Lean-formalized |
| Lower rate | Complete current lower include; finite controls and selected conditional Lean accounting lemmas |
| Upper rate | Current exponent slack, weighted boundary payment and strict coefficient margin |

Lean does not prove convex-envelope regularity, potential existence or the
quantum reduction. Historical staircase cores are not dependencies of the new
lower proof. Scoped analytic reviews are evidence, not guarantees. See the
[certificate map](paper/CERTIFICATE-MAP.md) for correction precedence.

## PDF and source integrity

Copy the two current TeX sources into a clean build directory. Run
`pdflatex -interaction=nonstopmode -halt-on-error -no-shell-escape resolution.tex`
twice. Check the log and visually inspect every rendered page. The bibliography
is embedded; no external figures or bibliography files are needed.
arXiv's generated PDF must still be inspected during submission.

[paper/BUILD.json](paper/BUILD.json) binds the PDF to its two sources.
`tools/check_publication.py` checks public links, private-file exclusion,
manuscript hygiene, build identity and actual Git clean-filter stability.
A frozen candidate's `release/SOURCE-MANIFEST.json` is checked with
`python tools/verify_candidate.py integrity --root PATH_TO_CANDIDATE`.
Custody is not mathematical approval. Freeze Git-normalized publication bytes;
historical certificate bytes are protected by attributes.

The old `certificate/release/release-manifest.json` belongs to its historical
snapshot. Its `--full` verifier can rewrite receipts: use it only in an isolated
copy of that matching snapshot. No tool here pushes or publishes; follow the
[release procedure](paper/ARXIV-SUBMISSION.md).
