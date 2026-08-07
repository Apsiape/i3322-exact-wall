SUPERSEDED STAMP (2026-08-07): extract superseded by the FULL
byte-identical source now in dependencies/
RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md
(round-3 findings 2/B5). Retained as history only.

# Alternating-block truncation — upper-only receipt extract

**Source theorem SHA-256:** `908874eed6fe673c80a4c4ac1481809f62b8f6d716556de34228b8fb4b07c8f9` (`RANK_COSTED_PACKET_IDENTITY_AND_ALTERNATING_TRUNCATION.md`, sealed v28.1).  
**Explicit construction SHA-256:** `d486e3e33f83afcea41a68b1930f2548e399eaa584e371c7ea03dc619df054bb` (`ENDPOINT_PROJECTOR_TRUNCATION_CONSTRUCTION.md`, sealed v28.1).

For the rank-one scalar carrier
\[
|\psi\rangle=\sum_{j\in\mathbb Z}\lambda_j|j,j\rangle
\]
with alternating nearest-neighbour rank-one projector blocks, retain a finite interval `I=[a,b]` and normalize
\[
|\psi_I\rangle=
\frac{\sum_{j=a}^b\lambda_j|j,j\rangle}
{(\sum_{j=a}^b\lambda_j^2)^{1/2}}.
\]
Every alternating `2x2` measurement block wholly inside `I` is assigned the same matrix entries as its source block by construction. Each block cut by the left or right boundary is replaced, on the retained endpoint, by the one-dimensional projector onto that endpoint basis vector; the complementary binary result is its one-dimensional complement on that severed block. Thus all six finite local measurement operators are projections and the local Hilbert-space dimension is exactly
\[
\boxed{d=|I|.}
\]

With
\[
T_I=\sum_{j\notin I}\lambda_j^2,
\qquad
B_I=|\lambda_{a-1}\lambda_a|+|\lambda_b\lambda_{b+1}|,
\]
there is a Bell-functional constant `C_B<infinity` such that
\[
\boxed{
0\le S-\mathcal B(\psi_I)
\le C_B\frac{T_I+B_I}{1-T_I}.
}
\]
Only omitted diagonal mass, omitted nearest-neighbour tail terms, the two severed bonds, and normalization are charged.
