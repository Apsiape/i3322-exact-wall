# v4.1.0 — proof correction and verification release

The main theorem statements are unchanged: finite-dimensional nonattainment
of the I3322 quantum value, spatial attainment, and logarithmic dimension
complexity. This revision corrects the supporting arguments; it is not merely
an editorial update.

- Replaces the quantitative lower-bound chain, including an unjustified
  component-identification step, with a finite weighted-flow proof.
- Corrects foundational and upper-bound estimates and clarifies the spatial
  construction and its amplitude assignments.
- Updates attribution to concurrent work and narrows priority language.
- Adds exact arithmetic and interface controls, selected Lean checks, and
  source/PDF identity and public-package verification. Lean coverage is
  explicitly limited to 37 selected declarations, not the full analytic proof.
- Preserves historical certificates with clear correction and precedence
  notices; private operational audit files are excluded from the release.

See [revision notes](REVISION-NOTES.md), [verification instructions](../VERIFY.md),
and the [current paper](resolution.pdf) for the statements and scope.

The version DOI is assigned by Zenodo after this GitHub release is published.
The concept DOI 10.5281/zenodo.21782008 identifies the version family;
10.5281/zenodo.22099128 is historical v4.0.0, not this revision. The new record
and archive must be verified before adding its DOI to the release notes.
