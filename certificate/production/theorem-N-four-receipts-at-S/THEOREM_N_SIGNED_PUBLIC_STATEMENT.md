# Theorem (N) — signed public statement

**Promotion:** signed after three rounds of independent adversarial review (record: `review/ROUND3-VERDICT.md`).

## Theorem (N)

Let `I` denote the I3322 Bell functional in the Collins–Gisin normalization
used throughout the repository (classical bound `0`; qubit and qutrit maximum
exactly `1/4`), and let

\[
S:=\omega_{\rm tensor}(I3322)=\omega_{\rm commuting}(I3322)
\]

be its quantum supremum, certified to lie in

\[
(0.2508753845015185,0.250875388108398].
\]

Then **no finite-dimensional quantum strategy attains `S`**: for every finite
dimension `d`, every state `rho` on `C^d tensor C^d` (pure or mixed), and every
triple of binary measurements per party (projective or POVM),

\[
\langle I\rangle_\rho<S.
\]

Equivalently, the supremum over finite-dimensional strategies is approached
but never reached, and the finite-dimensional quantum correlation set

\[
\boxed{C_q(3,3;2,2)\text{ is not closed}.}
\]

This is the operative content of the Pál–Vértesi conjecture (2010).

## Binding public wording

1. Identify `S` only by the certified interval above. Do not equate it with the
   historical Pál–Vértesi decimal or assert that the historical construction is
   optimal.
2. State the normalization: classical bound `0`; qubit/qutrit maximum `1/4`.
3. Distinguish the asymmetric active envelope (numerically about
   `[-0.8936,+0.8981]`) from the `u -> -u` symmetry forced on a hypothetical
   occupied finite equality orbit. They are different objects; the left wing
   is not obtained by reflection.
4. Describe package scripts as algebraic/exact-arithmetic guards, not theorem
   verifiers.
5. The nonclosure corollary uses `sup C_q = S` from Sprints 1287/1295. Do not
   conflate nonclosure with the stronger spatial separation
   `C_qs \\ C_q`, which requires current spatial attainment and is not promoted
   here.

## Exact operative dependencies

### Round-3 analytic package

1. Limiting-weld substitute: subsequential limit of `g_q`, uniform bound,
   `3/2`-Lipschitz modulus, Arzelà–Ascoli, interior positivity, and passage of
   the weld on the finite occupied spectrum using the explicit symmetric
   spectral cutoff.
2. Exact endpoint margins `m_+`, `m_-` and endpoint `R_0` gaps.
3. Storage concavity; reflection-gluing `K >= 1`; zero-set localization; strict
   Monge.
4. Open-interval convex-minorant reduction, no-kink theorem, horizontal
   plateau exclusion, dual-tie involution, vertical exclusion on `R_0^{-1}(0)`,
   and the strict full-zero graph.

### Repository

5. Sprint 1197: Bell reparameterization and CS fibres.
6. Sprint 1287: generic positive operator weld.
7. Sprint 1295: Bellman/path value equality, `g_q` for every `q>S`, and
   Pál–Vértesi principal-block padding.
8. Sprint 1206: **finite** Pál–Vértesi block-to-Jacobi identity only.
9. Sprint 1294: exact upper bound `S <= 0.250875388108398`.
10. Sprint 1292: exact dimension-255 strategy giving
    `S > 0.2508753845015185 > 1/4`.
11. Sprint 1198: unitary transports, totality, finite ordered-set closure,
    multiplicity-uniform amplitude elimination, and quarter ceiling.

### Standard mathematics

Naimark dilation/extreme-effect replacement; Arzelà–Ascoli; Schur complements;
joint spectral theory for a commuting pair; elementary convex analysis on an
open interval.

## Explicitly not used

The decertified Sprint-1195 fixed point or amplitude normalization; a reflected
left wing; a `C^1` storage; global uniqueness of raw first contact; interiority
of `range(P)`; attainment of the Sprint-1295 storage infimum at `S`; spatial
attainment; DOC-C shooting/heteroclinic artifacts; or the retracted conditional
dimension-necessity campaign.
