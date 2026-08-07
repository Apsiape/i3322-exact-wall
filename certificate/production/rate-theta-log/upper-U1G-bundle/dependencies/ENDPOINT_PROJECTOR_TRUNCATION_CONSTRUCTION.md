# Endpoint-Projector Truncation Construction

The infinite scalar carrier uses two alternating nearest-neighbour matchings
\[
\mathcal M_0=\{\{2k,2k+1\}:k\in\mathbb Z\},
\qquad
\mathcal M_1=\{\{2k-1,2k\}:k\in\mathbb Z\},
\]
with rank-one \(2\times2\) projector blocks on the relevant matching for each binary measurement.

For \(I=[-L,R]\cap\mathbb Z\):

1. keep every full \(2\times2\) block whose paired indices both lie in \(I\);
2. at the left endpoint, if its matching pairs \(-L\) with the discarded \(-L-1\), replace that severed block by the one-dimensional projector \(|-L\rangle\langle-L|\); at the right endpoint, if its matching pairs \(R\) with discarded \(R+1\), replace that severed block by \(|R\rangle\langle R|\);
3. use the complementary one-dimensional outcome for the complementary binary result, and make no change to the other matching when its endpoint block is already complete.

Thus every finite local measurement is again a direct sum of orthogonal rank-one \(2\times2\) blocks and possible one-dimensional projectors, hence is exactly a projection. This is the explicit construction consumed by the existing truncation-error theorem; it does not alter the theorem's already-stated tail/boundary error accounting.
