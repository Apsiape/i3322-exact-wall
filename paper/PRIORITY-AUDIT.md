# Priority audit for the exact I3322 wall

**Search date:** 2026-08-03

**Status:** archived theorem with a corrected literature record. The original
v1.0.0 sweep missed a prior Zenodo-only exact-enclosure release; the omission
does not overlap the exact-value or nonattainment theorem, but it narrows the
novelty claim and is recorded explicitly here.

## Exact claim being searched

The claim is not the general fact that finite-dimensional quantum correlation
sets can fail to be closed. It is the conjunction, for the canonical
three-setting/two-outcome I3322 functional, that

1. its tensor-product and commuting-operator suprema equal the same rigorously
   characterized number `0.250875384513976536...`;
2. the number is certified by an explicit Bellman/domain-wall boundary-value
   problem and a representation-free positive-operator decomposition; and
3. neither model has a finite-dimensional maximizer.

## Primary literature checked

- Collins and Gisin (2004) introduce I3322 as the simplest relevant bipartite
  binary Bell inequality beyond CHSH.
- Pal and Vertesi (2010), [arXiv:1006.3032](https://arxiv.org/abs/1006.3032),
  construct the domain-wall sequence, report the numerical value, and state
  optimality and finite-dimensional insufficiency as conjectures.
- Gigena and Kaniewski (2022),
  [arXiv:2203.01837](https://arxiv.org/abs/2203.01837), treat the branch
  containing I3322 numerically; their analytic characterization applies to a
  different branch.
- Coladangelo and Stark (2018),
  [arXiv:1804.05116](https://arxiv.org/abs/1804.05116), prove an unconditional
  finite/infinite-dimensional separation by another construction and still
  describe the corresponding I3322 property as conjectural. Their notation
  places finite-dimensional correlations in `C_q` and arbitrary spatial
  tensor-product correlations in `C_qs`.
- Slofstra (2017), [arXiv:1703.08618](https://arxiv.org/abs/1703.08618), proves
  general non-closure using a linear-system game. This establishes the general
  phenomenon, not the I3322 value or its finite-dimensional nonattainment.
- Araujo, Klep, Garner, Vertesi, and Navascues (version of record 2026-07-07),
  [DOI 10.1007/s10208-026-09761-x](https://doi.org/10.1007/s10208-026-09761-x),
  develop noncommutative first-order optimality conditions and study Bell
  inequalities computationally. The work does not supply the theorem proved
  here and treats the I3322 infinite-dimensional optimum as unresolved.
- Mortimer (2024),
  [arXiv:2412.08532](https://arxiv.org/abs/2412.08532), uses I3322 as a
  large-scale upper-bounding benchmark and explicitly does not claim the
  tightest upper bound.
- Flora, Matos, Krivachy, Garriga, and Acin (2026),
  [arXiv:2607.14755](https://arxiv.org/abs/2607.14755), use I3322 as a hard
  benchmark for budgeted NPA moment selection. They improve numerical moment
  selection; they do not give the exact value or prove nonattainment.
- Mghirbi (July 20--21, 2026),
  [DOI 10.5281/zenodo.21477901](https://doi.org/10.5281/zenodo.21477901),
  gives exact rational upper and lower I3322 certificates with enclosure width
  below `10^-9`, backed by proof objects at
  [DOI 10.5281/zenodo.21462892](https://doi.org/10.5281/zenodo.21462892).
  This predates this repository's archival release and must be credited as
  prior proof-carrying exact certification. It explicitly does not determine
  the exact supremum, finite-dimensional attainment, or equality of the tensor
  and commuting values.
- Dykema, Paulsen, and Prakash (2018),
  [DOI 10.26421/QIC18.7-8-5](https://doi.org/10.26421/QIC18.7-8-5),
  state that conjectured I3322 nonattainment would imply nonclosure of
  `C_q(3,2)`. The nonclosure implication is therefore prior recognized; the
  present corollary closes its previously conjectural premise.

## Search receipt and limitations

Searches included the exact decimal, `I3322 finite dimensional nonattainment`,
`I3322 exact quantum value`, `I3322 commuting operator maximum`, and citations
forward and backward from the papers above. The sweep used arXiv, INSPIRE,
Crossref, OpenAlex, zbMATH-facing web search, publisher pages, and general web
search. The arXiv literal-title query returned six I3322 records through 2024;
INSPIRE returned ten records and also exposed the July 2026 moment-optimization
preprint. Crossref's literal query produced an unrelated article identifier,
and OpenAlex's literal query initially returned no usable records. A repeat
after archival publication exposed the Mghirbi Zenodo records above. This is a
concrete demonstration of indexing lag and corrects the earlier negative
search. The original queries and blind spots remain frozen in
`PRIORITY-SEARCH-RECEIPT.json`; they are not rewritten after the fact.

No prior matching theorem was found. Mghirbi's independently replayable exact
certificate is an important antecedent but proves a strict enclosure rather
than the supremum or nonattainment. The July 2026 journal treatment by Araujo
et al., which includes Vertesi as a coauthor, still calls the I3322
infinite-dimensional optimum conjectural. This is particularly strong current
evidence, but it does not turn a negative search into a priority theorem.

## Adjudication

The package closes the Pal--Vertesi I3322 conjecture in a particularly small,
canonical Bell scenario. Version 1.2 makes explicit a consequence latent in
their construction and in this package's wall certificate: the geometrically
decaying bi-infinite Schmidt vector and alternating projectors form a normal
spatial maximizer. Together with nonattainment this gives an I3322 witness in
`C_qs(3,3;2,2) \ C_q(3,3;2,2)`. The alternating construction is due to Pal and
Vertesi, and the general separation `C_q != C_qs` is due to Coladangelo and
Stark; neither is claimed as new here.

The package is not the first exact proof-carrying I3322 enclosure; Mghirbi has
that priority. Its distinct content is the matching true supremum,
tensor--commuting equality for this functional, finite-dimensional
nonattainment, and the resulting canonical minimal-input spatial separation.
The likely value is therefore
**canonicality and exact resolution**, not priority for exact bounding or for
the general nonclosure phenomenon.

This audit is not a proof of priority. The theorem has an archival timestamp,
and the first missed antecedent has been corrected openly rather than hidden.
Further corrections remain welcome if another antecedent is identified.

The independently implemented interval reconstruction is complete and passes
all eight gates. Direct author notification may be useful after archival
posting, but it is not a validity gate and is not required for the theorem.

Manuscripts should say "we prove," credit the earlier exact enclosure, and
avoid "first proof" language.
