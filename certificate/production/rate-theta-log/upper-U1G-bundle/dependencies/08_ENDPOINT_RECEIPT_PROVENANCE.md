# Endpoint Receipt Provenance — Do Not Conflate the Two Rational Families

**Status:** binding provenance note for the promotion audit.

Two different endpoint receipt families exist. Previous working notes occasionally called both of them “endpoint margins.” They have different statements and different proofs.

## A. Coarse finite-history endpoint-line inactivity reserves

**Source:** `dependencies/REFLECTION_DUAL_UPPER_ENVELOPE_AND_ADAPTIVE_TAILS.md`, Theorem 4.1 and its exact rational verifier.

The source constructs a finite-history upper envelope `H` at

\[
q_0=S_++10^{-7},
\]

using 2001 depth-100 rational histories and exact rational Schur pivots. It defines the lower-certified endpoint predecessor lines

\[
E_+(u)=S_-+\frac12-\frac u2,
\]

\[
E_-(u)=S_-+\frac32+\frac{3u}{2}.
\]

The exact rational segment minimization proves, for **every** `u in [-1,1]`,

\[
\boxed{E_+(u)-H(u)>\frac{4039}{100000}},
\]

\[
\boxed{E_-(u)-H(u)>\frac{9893}{50000}}.
\]

Since `g_S<=H` and the true endpoint predecessor lines at `S` lie above the lines at `S_-`, the lawful conclusions are

\[
\boxed{
 g_S(u)<S+\frac12-\frac u2-\frac{4039}{100000}
}
\]

and

\[
\boxed{
 g_S(u)<S+\frac32+\frac{3u}{2}-\frac{9893}{50000}
}
\]

for every `u`.

In particular,

\[
 g_S(1)<S-\frac{4039}{100000},
\qquad
 g_S(-1)<S-\frac{9893}{50000}.
\]

### What these rationals are

They are **coarse lower bounds on endpoint predecessor-line minus the finite-history upper envelope**, propagated to endpoint-contact inactivity inequalities for `g_S`.

### What these rationals are not

They are **not** the exact Theorem-(N) quantities `m_+`,`m_-`, and they are **not** themselves the exact boundary `R_0` gaps.

---

## B. Theorem-(N) exact endpoint margins and boundary `R_0` gaps

**Source:** `dependencies/THEOREM_N_ROUND3_BLIND_AUDIT_SOURCE.md`, assembly table steps 2–3; provenance there is Assembly V1 Receipt (iii), `four_receipts_at_S_endpoint_and_scout.py`, independently re-derived in `r3_exact.py`.

The exact quantities are

\[
\boxed{
m_+=\frac{23686917837403}{3008753881083980}
}
\]

and

\[
\boxed{
m_-=\frac{274562305945801}{4008753881083980}.
}
\]

They arise from explicit one-edge endpoint history comparisons, uniformly over the certified near-critical `q` window. The receipt gives one Bellman sum at least `m_±` below the endpoint line while the other remains feasible. The geometric-mean step then proves the **boundary-set scalar remainder** estimate

\[
\boxed{R_0\ge m_\pm/2}
\]

on the corresponding endpoint source sets, with target cases obtained by the exact I3322 reflection identities.

These are the endpoint-atom exclusion / boundary-`R_0` receipts used in promoted Theorem (N).

---

## C. Binding use in this promotion bundle

The new G1 endpoint-positivity contradiction uses family **A** only to obtain the coarse upper bounds on `g_S(1)` and `g_S(-1)`.

The package retains family **B** as the promoted endpoint boundary receipt and provenance dependency, but does not relabel `4039/100000` or `9893/50000` as `m_+` or `m_-`.
