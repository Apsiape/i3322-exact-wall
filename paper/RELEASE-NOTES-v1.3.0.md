# Prospective v1.3.0 release notes

This prospective revision adds a quantitative convergence theorem for the
explicit finite sections of the certified spatial wall. It is not yet a
tagged archival release; DOI and citation metadata remain those of v1.2.0.

## Release blocked by Bellman normalization audit

Sprint 1285 proves an exact nonzero global-amplitude mismatch in the
load-bearing Bellman assembly. Sprint 1287 subsequently certifies a separate
exact upper bound, refined in Sprint 1293 to
`omega_c<=0.250875391558130` and independently reconstructed with exact
arithmetic. It still does not prove equality at the historical wall value.
Sprint 1292 adds the independently reconstructed finite lower bound
`omega_tensor>0.2508753845015185`. Therefore no `v1.3.0`
release may be tagged as the
historical exact-optimum/nonattainment theorem. The finite-section flux and
tail calculations may remain exact statements about the explicit wall, but
they cannot currently be promoted as deficits from the true I3322 optimum.

## New theorem

Compressing the normal spatial maximizer to the centered principal section of
local dimension `d=2L+1` gives an exact two-boundary flux formula. The
certified geometric tails imply

```text
lim -log(q_*-v_L)/d = log R,
R = 1.07809205080209208....
```

Consequently the unrestricted dimension-`d` optimum, with binary POVMs
allowed, satisfies

```text
0 < q_*-Q_d <= exp[-d log R+O(1)].
```

Equivalently, `log(1/epsilon)/log R+O(1)` local dimension is sufficient to
reach deficit `epsilon`.

A separate robust-certificate campaign proposed that every tensor-product
strategy with both local dimensions at most `d` satisfies

```text
q_*-Q_d >= kappa d^-4 Gamma^-d,
Gamma = 312^4 = 9,475,854,336,
kappa = 4.2946546143271441824...e-52.
```

The prefactor and exponential base are explicit but conditional. Independent
adversarial reconstruction found that the near-fixed packet step does not
follow from the stated hypotheses: the global response defect was restricted
without charging the resulting commutator/interface term. Consequently the
matching lower bound and `Theta(log(1/epsilon))` conclusion are **not** claims
of the prospective revision.

## Pre-release adversarial correction

Independent frontier-model review blocked the prospective packet. It found
two omitted theorem owners, an active-chart packet formula where the saturated
coordinate was required, a factor-of-two contact multiplicity, and finally a
load-bearing localization gap. The package now:

- includes the weighted-closure and pullback-pairing proofs (Sprints 1226 and
  1227) in the standalone dependency closure;
- uses `Y^-1(g_k I_i)` for the canonical saturated packet;
- charges source and target contact families separately, replacing `24` by
  `48` in the conditional near-fixed inequality and recomputing the
  conditional `kappa`;
- states the exponential tail estimate needed for the dimension-independent
  prefactor in the constructive bound; and
- explicitly records that common pullback packets do not localize the global
  response defect without an additional flux/commutator theorem.

The constructive theorem survives. `Gamma` and `kappa` are retained only as
the exact ledger of a conditional lower-bound route. No v1.3 tag or DOI exists.

## Literature placement

Pal--Vertesi numerically identified the approaching finite-dimensional family.
Navascues--Feix--Araujo--Vertesi developed convergent fixed-dimension
hierarchies and applied them to I3322.  Coladangelo proved substantially
stronger dimension growth for a purpose-built larger nonlocal game.  The new
claim here is narrower: an exact boundary-flux identity and certified
exponential convergence rate for canonical I3322 wall truncations. No matching
prior theorem was found, but the priority statement remains provisional and
the manuscript does not use "first" language.

## Verification added

- an exact-rational production guard for the principal-section flux identity;
- an independent SymPy reconstruction with missing-boundary controls;
- an independent `mpmath.iv` derivation and enclosure of `R` and `log R`;
- a same-dimension pure/projective reduction for arbitrary binary POVMs;
- a production record for the conditional response-localization and
  finite-rank lower-bound campaign, including its unresolved implication;
- a separately written lower-bound reconstruction, preserved as evidence of
  how the missing premise propagated through the ledger;
- a post-verdict exact SymPy audit of every final constant and absorption;
- release-level replay and semantic gates for both receipts.
- a hostile public-claim contract covering the POVM quantifier, asymptotic
  scope, literature placement, and prospective-release metadata.
- a canonical joint order--resolution coupling, charged common-cell descent,
  and exact coarse stability law for the pointwise quarter wall;
- hostile transport controls rejecting total variation on moving atoms and
  ordinary provenance-forgetting Wasserstein transport; and
- an exact synchronized-prefix theorem recovering the vertical fibre bill,
  while leaving its I3322 operator-receipt comparison explicitly open.
- an upper-tail contact integral and trace-normalized upper cap, eliminating
  hidden lower-spectrum and rank dependence at the two vertical interfaces;
- sign-coherence theorems on source and output cells, blocking cancellation
  by unresolved multiplicity; and
- a one-grid four-coordinate theorem supplying the same numerical prefixes
  before and after both responses. The final integrated deficit ledger is
  still open and no lower-bound claim is promoted.

## Claim boundary

The proved result is an achievability bound: explicit centered truncations
reach deficit `exp[-d log R+O(1)]`. It is not a universal dimension lower
bound, a statement about experimental noise, a commuting-operator dimension
bound, or a claim that the centered truncations are finite-dimensional
optimizers. The lower-bound route remains an open problem with a precisely
localized missing lemma.
