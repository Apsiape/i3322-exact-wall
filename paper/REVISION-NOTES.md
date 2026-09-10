# September 2026 correction record

The main statements remain finite-dimensional nonattainment, spatial
attainment, and D(epsilon) = Theta(log(1/epsilon)). The current paper is
`resolution.pdf`; its sources supersede older papers in this directory.
Historical v4.0.0 remains unchanged at DOI 10.5281/zenodo.22099128.

## Substantive corrections

- Replaced an unjustified paired-component identification in the lower bound
  with weighted flow over all retained edges and arbitrary multiplicity.
  The old Lean cores did not prove the missing quantum reduction.
- Corrected the limiting-weld justification and endpoint-gap constant.
- Corrected spatial parity-specific amplitude notation; made its marginal,
  conull domain and orbit enumeration explicit.
- Corrected the mixed-state argument in binary-input minimality.
- Corrected upper-rate exponent slack and the boundary-flux prefactor.
  The eventual numerical coefficient is unchanged.

These are proof and exposition corrections, not merely formatting.
[CERTIFICATE-MAP.md](CERTIFICATE-MAP.md) states source precedence.

## Attribution and scope

Pauwels' Theorem 1 (arXiv:2608.29734v1) establishes equality of the full finite
Pal--Vertesi-family supremum and the finite quantum supremum, distinct from
the limit of a prescribed numerical sequence. His nonattainment theorem and
Coladangelo's independent nonattainment/spatial-attainment results
(arXiv:2609.06038v1) are credited. Mghirbi's prior enclosures and related
Bellman--Jacobi work are cited.

The failure of this project's withdrawn amplitude construction does not refute
the Pal--Vertesi family. The earlier August withdrawal and rebuilding remain
disclosed in the paper and preserved releases.

Lean checks 37 selected declarations, not the full analytic theorem.
See [VERIFY.md](../VERIFY.md). Historical audits have a stated scope and are
not guarantees of correctness.

## Historical documents

`manuscript.*`, `rate-companion.*`, `technical-supplement.*`, uppercase Markdown
manuscripts, old status/priority files and versioned release notes describe
earlier snapshots. They are not alternatives to `resolution.pdf`.
Historical certificate paths and hashes are preserved rather than rewritten.
