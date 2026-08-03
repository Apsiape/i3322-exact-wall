# Exact I3322 quantum wall

This repository contains a computer-assisted proof that the tensor-product and
commuting-operator suprema of the canonical three-setting, two-outcome
`I3322` Bell functional equal the rigorously characterized constant

```text
q* = 0.250875384513976536...
q* in [0.250875384513976535514, 0.250875384513976536486].
```

Neither model has a finite-dimensional maximizer.

The result resolves the conjectural value and finite-dimensional
nonattainment reported by Pal and Vertesi in 2010. It is not a claim of
priority for general non-closure or finite/infinite-dimensional separation,
which are known in other Bell scenarios.

## Paper

- [Main manuscript](paper/manuscript.pdf)
- [Technical supplement](paper/technical-supplement.pdf)
- [Readable manuscript source](paper/MANUSCRIPT.md)
- [Claim-to-certificate map](paper/CERTIFICATE-MAP.md)
- [Priority audit](paper/PRIORITY-AUDIT.md)

## Reproduce the certificate

The release was tested with CPython 3.13.12. Install the four pinned numerical
dependencies in a clean environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Quick custody and semantic verification:

```powershell
python certificate/release/verify_release.py
```

Complete production and independently implemented interval replay:

```powershell
python certificate/release/verify_release.py --full
```

The full replay regenerates every load-bearing receipt, including intermediate
cyclic, symmetrization, and operator-remainder guards. On the reference
workstation it takes several minutes. The independent path uses `mpmath.iv`
and a locally implemented rectangular complex-interval layer; it imports no
production Arb/FLINT module.

## Repository structure

- `paper/`: manuscript, supplement, normalization, scope, and priority record;
- `certificate/production/`: complete Arb/SymPy/NumPy proof dependency closure;
- `certificate/independent/`: separate interval reconstruction;
- `certificate/release/`: manifest, replay entry point, and release audits.

The repository is deliberately standalone. It contains no dependency on the
broader private or public foundational-theory corpus from which the problem was
originally investigated.

## Computational disclosure

Frontier language models were used extensively for proof discovery,
implementation, adversarial auditing, and editorial assistance. Seth Douglas
assumes responsibility for this release. Every load-bearing computer-assisted
claim is mapped to replayable source and a frozen receipt.

## Author

**Seth Douglas**

[ORCID 0009-0007-4708-3252](https://orcid.org/0009-0007-4708-3252)

[apsiape@gmail.com](mailto:apsiape@gmail.com)

## License

Paper prose, figures, and PDFs are licensed under
[CC BY 4.0](LICENSES/CC-BY-4.0.txt). Executable source code is licensed under
the [BSD 3-Clause License](LICENSES/BSD-3-Clause.txt). See [LICENSE.md](LICENSE.md)
for the file-level boundary.
