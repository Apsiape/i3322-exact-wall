# arXiv submission sheet — `paper/resolution.tex`

Working notes for submitting *The $I_{3322}$ quantum value is attained spatially
but not in finite dimension* (Seth Douglas) to arXiv. Nothing here changes any
mathematical content; it records the metadata to paste into the submission form
and the items still awaiting an author decision.

---

## 1. Comments field

Paste verbatim:

```
Results first announced 5 August 2026 (Zenodo, DOI 10.5281/zenodo.21782008). Independent and concurrent with arXiv:2608.29734 (Pauwels) and A. Coladangelo, "The I3322 Bell inequality requires infinite dimensions" (to appear on arXiv, September 3, 2026). Verification guide and machine-checked certificates at the linked repository.
```

**No open placeholders.** Once the Coladangelo arXiv identifier is issued
(3 September 2026), the parenthetical may optionally be replaced by the bare
`arXiv:NNNN.NNNNN` number for symmetry with the Pauwels citation.

Optional additions if the author wants them (arXiv allows a longer comments
field): page count ("21 pages"), and the repository URL
`https://github.com/Apsiape/i3322-exact-wall`.

---

## 2. Categories

| Slot | Choice | Rationale |
|---|---|---|
| **Primary** | `quant-ph` | Bell inequalities, quantum correlation sets, $C_q$ vs $C_{qs}$ — the whole readership for $I_{3322}$, Pál–Vértesi, Dykema–Paulsen–Prakash, Coladangelo–Stark lives here. Pauwels' concurrent paper (arXiv:2608.29734) is also quant-ph. |
| **Secondary (recommended)** | `math-ph` | Cross-listing math-ph automatically cross-lists `math.MP`, which is the standard pairing for operator-theoretic Bell work and reaches the mathematical-physics audience. |
| **Secondary (alternative)** | `math.OA` | Defensible instead of, or in addition to, math-ph: the paper works with the universal $C^*$-algebra of two commuting triples, commuting-operator suprema, spectral disintegration, and the $C_q$/$C_{qs}$/$C_{qa}$ taxonomy — squarely operator algebras, and the natural home for the Dykema–Paulsen–Prakash / Musat–Rørdam line the corollary settles. |

Recommendation: `quant-ph` primary, cross-list `math-ph`; add `math.OA` as well if
the author wants the operator-algebras community reached directly (arXiv permits
multiple cross-lists, and moderators routinely accept this triple for this
subject matter).

MSC / ACM codes: optional, leave blank.

---

## 3. License

**Recommended: CC BY 4.0** (`http://creativecommons.org/licenses/by/4.0/`).

Reason: `LICENSE.md` already licenses everything under `paper/` as CC BY 4.0,
`CITATION.cff` declares `license: CC-BY-4.0`, and `.zenodo.json` declares
`"license": "cc-by-4.0"`. Selecting CC BY 4.0 on arXiv keeps the arXiv posting,
the Zenodo record of record, and the repository under one consistent, verifiable
licence — which matters here because the paper's credibility argument rests on
the reader being able to redistribute and re-run the certificate bundle.

The arXiv default (`arXiv.org perpetual, non-exclusive license`) would also be
accepted, but it is *more restrictive* than the licence the same text already
carries on Zenodo, so it would create an inconsistency between the two archived
copies. Do not select it unless there is a specific reason.

---

## 4. Files to upload

The source is fully self-contained. Upload **one file**:

- `resolution.tex`

Verified properties (checked by compiling from a clean directory containing only
this file):

- Packages used: `geometry`, `amsmath`/`amssymb`/`amsthm`, `hyperref` — all in
  arXiv's TeX Live. No `mdframed`, `framed`, `tcolorbox`, or other add-ons; the
  verification box is a package-free `\fbox{\begin{minipage}...}`.
- No `\input`, `\include`, or `\includegraphics`. No figures, no external files,
  no repo-relative paths.
- Bibliography is an inline `thebibliography` environment — **no `.bib` upload and
  no BibTeX run needed**. (`references.bib` in this directory belongs to
  `manuscript.tex`, not to `resolution.tex`.)
- Three `pdflatex` passes from scratch: exit 0, **21 pages** (was 18 before the
  2026-09-02 readability pass), no undefined references, no undefined
  citations, no overfull boxes. Underfull `\hbox` warnings remain in the
  abstract, the long `\texttt` repository paths, and the bibliography; they are
  pre-existing and harmless.

Do **not** upload `.aux`, `.log`, `.out`, `.fls`, `.fdb_latexmk`, `.bbl`, or the
prebuilt `resolution.pdf`; arXiv builds the PDF itself and stray auxiliary files
can break the build.

---

## 5. Title and authors (for the form)

- **Title:** `The I3322 quantum value is attained spatially but not in finite dimension`
  (arXiv's title field is plain text; the `$I_{3322}$` subscript in the PDF title
  is fine to render as `I3322`, or as `$I_{3322}$` — arXiv accepts inline TeX in
  titles.)
- **Author:** `Seth Douglas`
- **ORCID:** `0009-0007-4708-3252` — present in the PDF author block and worth
  linking in the arXiv account so the paper attaches to the ORCID record.
- **Contact e-mail:** `apsiape@gmail.com` — present in the PDF author block.

---

## 6. Abstract — ⚠ AUTHOR DECISION REQUIRED

**The PDF abstract is over arXiv's 1920-character form limit.** Measured as
plain text it is ~2686 characters (~2885 with the LaTeX markup as written), so
the form will reject it as-is.

The `.tex` abstract has been **left untouched** — the PDF has no length limit,
and shortening it would have meant editing the paper's own claims, which was out
of scope. Instead, a condensed version for the *submission form only* is given
below. arXiv does not require the form abstract to be byte-identical to the PDF's,
and a condensation is routine, but **the author should read and approve this text
before pasting it**, since abstract wording is an authorial choice.

Condensed form abstract — **must be re-counted after any edit** (limit 1920
characters). *Updated 2026-09-03 to track the reviewer-pass changes in the
`.tex` abstract: the Mghirbi parenthetical now states independence rather than
derivation ("independently and more tightly enclosed by Mghirbi's prior
certificates"); "shipped with it" became "in the accompanying repository"
(nothing ships with an arXiv submission); and the decertification sentence was
dropped here as in the PDF abstract (the paper's Correction history subsection
carries it).*

```
Let $S$ be the quantum supremum of the $I_{3322}$ Bell functional in the Collins-Gisin normalization (classical bound 0; two-qubit maximum exactly 1/4). From a certified window $S\in(0.2508753845015185,0.250875388108398]$ (independently and more tightly enclosed by Mghirbi's prior certificates) and a certified equality of the tensor-product and commuting-operator suprema, we prove: (i) no finite-dimensional quantum strategy attains $S$ -- any finite local dimensions, pure or mixed states, projective or POVM measurements -- proving the conjecture of Pal and Vertesi (2010); (ii) $S$ is attained by a spatial strategy on $\ell^2(\mathbb{Z})\otimes\ell^2(\mathbb{Z})$, the infinite-dimensional attainment those authors asserted, on an independent route. So $C_q(3,3;2,2)$ is not closed -- the smallest two-outcome bipartite scenario by input count where nonclosure is known -- and $C_{qs}(3,3;2,2)\setminus C_q(3,3;2,2)$ is nonempty, settling the attainment question raised by Dykema, Paulsen and Prakash. Nonattainment is proved via a concave critical Bellman storage, exact rational endpoint-exclusion certificates, reflection-gluing and a convex-envelope theorem: finiteness forces an exact maximizer's two equality transports to coincide, capping its value at $1/4<S$. Attainment is proved by disintegrating a commuting maximizer's spectral measure over the orbits of its two response transports, yielding an $\ell^2$ Jacobi eigenvector with inherited normalizability. We also determine the dimension complexity: with $S_d$ the optimum at local dimension $\le d$ and $D(\epsilon)=\min\{d:S-S_d\le\epsilon\}$, $D(\epsilon)=\Theta(\log(1/\epsilon))$ -- the upper half constructively, with $D(\epsilon)\le 23.9010650\log(1/\epsilon)$; the lower half in a certificate chain in the accompanying repository. Cores of both halves are machine-checked in Lean 4.
```

Changes made in the 2026-09-02 update, all wording-only, no claim added or
dropped: added the Mghirbi attribution as a parenthetical; "sealed certificate
chain" → "a certificate chain shipped with it"; "by this program" → "of ours";
"Hence" → "So"; "in which" → "where"; "the two equality transports of an exact
maximizer" → "an exact maximizer's two equality transports"; "the spectral
measure of a maximizing commuting state" → "a commuting maximizer's spectral
measure"; "We further determine" → "We also determine"; "at local dimension at
most $d$" → "at local dimension $\le d$"; dropped the redundant `$I_{3322}$`
qualifier before "attainment question" (the subject is named twice already).
These freed the 60 characters the two tracked additions cost.

What was compressed, and what was preserved:

- **Preserved in full:** the normalization and both anchors (classical bound 0,
  two-qubit maximum $1/4$); the certified window digits; the certified
  tensor/commuting equality as an *input*; claim (i) with its full quantifier
  list and the Pál–Vértesi attribution; claim (ii) with the exact carrier
  $\ell^2(\mathbb{Z})\otimes\ell^2(\mathbb{Z})$ and the "independent route"
  qualifier; the nonclosure corollary with its minimality qualifier and the
  Dykema–Paulsen–Prakash attribution; the $C_{qs}\setminus C_q\neq\emptyset$
  statement; both proof architectures; the decertification disclosure; the rate
  $\Theta(\log(1/\varepsilon))$ with the explicit constant `23.9010650` and the
  constructive/sealed split; the Lean 4 machine-checking.
- **Compressed (wording only, no claim dropped):** "smallest scenario by input
  count, among two-outcome bipartite scenarios" → "smallest two-outcome
  bipartite scenario by input count"; "whose normalizability is inherited from
  the probability measure rather than imposed" → "with inherited
  normalizability"; a few connectives.
- **Dropped:** only the closing structural *observation* — "in every case known
  to us, finite-dimensional attainment is accompanied by closed (finitely
  recurrent) optimal carriers, while the known transport-class nonattainment
  phenomena are carried by infinite open chains." This is flagged in the paper
  itself as an observation suggested by the results, not a theorem, and it is
  the only way to fit 1920 characters. **If the author wants it kept in the form
  abstract, roughly 250 further characters must come out elsewhere — this is the
  main abstract decision to make.**

---

## 6b. Optional tightened abstract (author's call)

**Not applied to `resolution.tex`.** This is a drafted replacement for the PDF
abstract, produced by the 2026-09-02 consumability review and checked here
against the current `.tex` abstract claim by claim. It is offered as an option,
not a correction: the shipped abstract is complete and correct as it stands.

**One-line diff:** it keeps every claim, quantifier and hedge, adds the Pauwels
concurrency sentence, and drops only the closing structural observation, the
names of three proof ingredients (endpoint-exclusion certificates,
reflection-gluing, the convex-envelope/contact-plateau theorem), and the
"requires and suffices" gloss on the rate.

```latex
\begin{abstract}
Let $S=\omega_{\mathrm{tensor}}(I_{3322})=\omega_{\mathrm{commuting}}(I_{3322})$
denote the quantum supremum of the $I_{3322}$ Bell functional in the
Collins--Gisin normalization (classical bound $0$; two-qubit maximum exactly
$1/4$). Working from an exactly certified window
$S\in(0.2508753845015185,\,0.250875388108398]$ --- a certified input built on
Mghirbi's proof-carrying enclosure --- and a certified equality of the
tensor-product and commuting-operator suprema, we prove:
(i)~\textbf{no finite-dimensional quantum strategy attains $S$} --- any finite
local dimensions, pure or mixed states, projective or POVM measurements ---
proving the conjecture of P\'al and V\'ertesi (2010); (ii)~$S$ \textbf{is}
attained by a spatial strategy on
$\ell^2(\mathbb{Z})\otimes\ell^2(\mathbb{Z})$ --- infinite-dimensional
attainment, which those authors asserted for their own construction, here
established on an independent route. Consequently $\Cq(3,3;2,2)$ is not closed
--- the smallest scenario by input count, among two-outcome bipartite
scenarios, in which nonclosure is known --- and
$\Cqs(3,3;2,2)\setminus\Cq(3,3;2,2)\neq\emptyset$, settling the $I_{3322}$
attainment question raised by Dykema, Paulsen, and Prakash. Result~(i) was
obtained independently and concurrently by Pauwels, on a different route.

Both proofs turn on one mechanism. Optimal strategies reduce to paths in a
one-dimensional space of block labels carrying a Jacobi matrix, and a strategy
of value exactly $S$ must occupy the zero set of the critical scalar weld
remainder; that zero set is the graph of a single strictly increasing map. In
finite dimension the two order-reversing transports it carries have no room to
differ, so they coincide, every occupied label is paired with its own
reflection, and the value is capped at $1/4<S$. In the commuting model the same
transports generate an infinite dihedral action whose orbits are copies of
$\mathbb{Z}$; disintegrating a maximizer's scalar spectral measure over one
orbit produces an $\ell^2$ Jacobi eigenvector at eigenvalue $S$, whose
normalizability is inherited from the probability measure rather than imposed.

We then determine the dimension complexity: with $S_d$ the optimum at local
dimension at most $d$ and $D(\eps)=\min\{d:S-S_d\le\eps\}$, we establish
$D(\eps)=\Theta(\log(1/\eps))$. The upper half is proved here, constructively,
with the explicit bound $D(\eps)\le 23.9010650\,\log(1/\eps)$ ($\log$ natural)
for all sufficiently small $\eps$; the matching lower half, with existential
constants, is established in a companion certificate chain that ships with the
paper. Combinatorial and scalar cores of both halves are machine-checked in
Lean~4 --- cores, not reductions. An earlier claimed proof of ours was
withdrawn after our own exact audit refuted one of its inputs; nothing from it
re-enters the present argument, and the correction record ships with the paper.
\end{abstract}
```

### Verification of the draft against the shipped abstract

**Preserved, verbatim in substance:** the normalization and both anchors; the
certified window digits; the tensor/commuting equality as a certified *input*;
claim (i) with its full quantifier list and the Pál–Vértesi attribution; claim
(ii) with the carrier `\ell^2(Z) ⊗ \ell^2(Z)`, the "which those authors
asserted for their own construction" qualifier and the "independent route"
qualifier; the nonclosure corollary with its "smallest scenario by input count,
among two-outcome bipartite scenarios" minimality qualifier; the
`C_qs \ C_q ≠ ∅` statement with the Dykema–Paulsen–Prakash attribution; the
rate `Θ(log(1/ε))` with the explicit `23.9010650`, "log natural", "for all
sufficiently small ε", "with existential constants", and the
proved-here / companion-chain split; "cores, not reductions"; the withdrawal
disclosure with "nothing from it re-enters".

**Added (not in the shipped abstract):** "Result (i) was obtained independently
and concurrently by Pauwels, on a different route." This matches the
"Relation to independent concurrent work" subsection, which is the authority
for it; if that subsection changes, this sentence must change with it.
*2026-09-02: that subsection now also records the concurrent work of
A. Coladangelo, "The $I_{3322}$ Bell inequality requires infinite dimensions".
The sentence above remains accurate as written; if this optional abstract is
adopted, consider naming both concurrent works. The §6 condensed form abstract
— the one actually pasted into the submission form — makes no concurrency
statement and is unaffected.*

**Dropped:**
1. The closing structural observation ("in every case known to us,
   finite-dimensional attainment is accompanied by closed (finitely recurrent)
   optimal carriers, while the known transport-class nonattainment phenomena
   are carried by infinite open chains"). Flagged in the paper itself as an
   observation, not a theorem; §6 makes the point in full.
2. The names of three proof ingredients: "exact rational endpoint-exclusion
   certificates", "a reflection-gluing inequality", and "a convex-envelope
   theorem excluding contact plateaus". Replaced by a mechanism description;
   all three are still stated and used in §3.
3. The gloss "reaching $S$ to accuracy $\eps$ requires and suffices local
   dimension of order $\log(1/\eps)$" — restated by the `Θ` itself.

**Two editorial notes on the draft as received:**
- The review's draft omitted the Mghirbi input parenthetical (it was written
  against a copy predating that edit). It has been **restored** in the text
  above; do not adopt the draft without it.
- The review's draft wrote "the zero set of the critical Bellman slack". The
  paper's `Z` is the zero set of the *scalar weld remainder*, not of the
  one-site Bellman slack display; the wording above has been corrected
  accordingly.
- The draft uses the `\Cq`, `\Cqs` and `\eps` macros already in the preamble,
  so it drops in without preamble changes.

---

## 7. Submission checklist

- [x] Fill the Coladangelo reference in the comments text (§1). *(Done
      2026-09-02.)*
- [x] Fill the concurrency clause in `resolution.tex`,
      §"Relation to independent concurrent work" (Introduction), and add the
      `\bibitem{Coladangelo2026}` entry, then recompile. *(Done 2026-09-02;
      no placeholders remain in the source.)*
- [ ] Confirm the Pauwels bibliography entry against the posted arXiv abstract
      page — author spelling (**Jef Pauwels**), exact title, and that the
      **Section VI** cross-reference in the concurrency paragraph matches the
      version being cited. *(These were supplied to this pass and not
      independently verified against arXiv.)*
- [x] Rebuild the tracked artifact `paper/resolution.pdf` **after** the
      placeholders are filled. *(Done 2026-09-02: rebuilt from the
      placeholder-free source; the release manifest was rebuilt afterwards.)*
- [ ] Approve or revise the condensed form abstract (§6).
- [x] Decide whether the `\date{}` on line 21 of `resolution.tex` should be
      updated to the actual submission month. *(Done 2026-09-02: set to
      `\date{September 2026}`.)*
- [ ] Decide `math.OA` in addition to / instead of `math-ph` (§2).
- [ ] Select **CC BY 4.0** on the license screen (§3).
- [ ] Upload `resolution.tex` only; confirm arXiv's build is 21 pages and the
      verification box on the Methods page renders inside its frame.
- [ ] Check the AutoTeX log for the missing-`.bbl` warning — expected and
      harmless here, since the bibliography is inline.
- [ ] After the identifier is issued: add the arXiv ID to `README.md`,
      `CITATION.cff`, `.zenodo.json`, and the Zenodo record; cut a repository
      release noting the arXiv posting.
- [ ] Confirm the repository is public and `VERIFY.md` is reachable at the root
      before the announcement goes out — the comments field points readers there.

---

## 8. Open placeholders currently in the source

**None.** All placeholders were filled on 2026-09-02:

| File | Former placeholder | Resolved to |
|---|---|---|
| `paper/resolution.tex` | `[ANDREA-TITLE-AND-ARXIV-ID]` | `\cite{Coladangelo2026}` in the concurrency paragraph |
| `paper/resolution.tex` | `[ANDREA-RESULT-CLAUSE]` | "independently establishes that the $I_{3322}$ Bell inequality requires infinite dimensions" |
| `paper/ARXIV-SUBMISSION.md` | `[ANDREA-ARXIV-ID]` | A. Coladangelo, title + "to appear on arXiv, September 3, 2026" (§1) |

The new bibliography key is `Coladangelo2026`, deliberately distinct from the
pre-existing `ColadangeloStark` (2018/2020 Nat. Commun.) and `Coladangelo`
(2020 Quantum 4, 282) entries. The result clause is phrased strictly from the
concurrent paper's title; no claim is made about its methods or scope.
