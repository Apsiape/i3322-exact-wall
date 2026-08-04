# Exact global-amplitude gap

## Verdict

The current aligned-wall Bellman assembly does **not** close its global
amplitude compatibility equation.

This is an exact interval result, not a floating-point discrepancy.  On the
complete registered `t2` bracket

```text
[0.0015874649714962908, 0.001588503145749181],
```

the four-step target coordinate is strictly monotone and its two face
residuals have opposite signs.  Hence there is exactly one coordinate-matched
point in the bracket.  Arb interval arithmetic at 400-bit precision proves,
without first narrowing to that point, that the corresponding target/source
amplitude difference lies in

```text
[0.00014027592551842303, 0.00017894047518170395].
```

In particular, zero is excluded by more than `1.40e-4`.

## What is proved

The local characteristic charts used by the current certificate can satisfy
their coordinate matching equation while failing the global Bellman
normalization equation.  The mismatch is therefore not a resolution artifact
and cannot be repaired by choosing another point inside the certified matched
coordinate bracket.

All four preregistered gates passed:

1. exact central-graph monotonicity was loaded from the prior certificate;
2. the bracket faces retained strict opposite signs;
3. all radicands and amplitude denominators remained strictly positive; and
4. the wide-bracket amplitude difference excluded zero by more than `5e-5`.

## Consequence for the public theorem

The published numerical candidate `q_*` is **not disproved** by this result.
The local shooting solution and the explicit wall may remain mathematically
valid.  What fails is the presently documented inference that the assembled
local charts already supply one globally normalized Bellman fixed point.

Because that Bellman datum is the computer-assisted upper-bound input for the
claimed exact optimum, finite-dimensional nonattainment, spatial separation,
and nonclosure corollaries, those headline claims are not presently certified
by the repository.  They require either:

- a corrected globally normalized Bellman construction, or
- a different independent upper-bound proof.

The prospective finite-section rate also cannot be stated as a deficit from
the true optimum until that upper bound is repaired, although its exact
boundary-flux calculation and decay rate for the explicit wall can survive as
conditional statements about that construction.

## Reproduction

```text
python certificate/production/foundational-sprint-1285/wide_bracket_amplitude_exclusion.py
```

Machine-readable receipt:
`wide-bracket-amplitude-exclusion.json`.

## Claim boundary

This result diagnoses the current certificate assembly.  It does not prove a
different I3322 optimum, disprove the Pal--Vertesi numerical limit, or rule out
a repaired proof of the same value.
