# Independent audit: Bellman storage equals finite-path value

Status: **accepted within the registered scope**

This audit reconstructs the argument without importing the Sprint 1295
verifier.  It accepts both the abstract theorem and its I3322 typing.

## Abstract reconstruction

For a finite word, weighted Young inequality leaves the exact remainder

```text
b(x_0)^2/g(x_0) a_0^2 + g(x_n) a_(n-1)^2
+ sum_(k=1)^(n-1) (g(x_k)a_(k-1)-b(x_k)a_k)^2/g(x_k).
```

This fixes the source/target orientation and proves the Bellman upper bound on
every path.

Conversely, for `q>S`, each `qI-J_word` is bounded below by
`delta=q-S`.  Its terminal Schur complement is the minimum of the quadratic
form with final coordinate fixed to one, so it is at least `delta`.  The
infimum over terminal pivots ending at a label is therefore positive.
Extending histories produces the Bellman inequality in the required
direction.

For continuity, every terminal-pivot function of the final endpoint is
`C-d(i,j)`.  Uniform continuity of `d` on the compact metric square gives the
same modulus to the whole family.  If all `h_alpha` obey

```text
|h_alpha(j)-h_alpha(j')| <= omega(dist(j,j')),
```

then their pointwise infimum obeys the same inequality by taking the two
one-sided infimum comparisons.  Thus the constructed storage is continuous.

## Hostile results

- 500 exact rational source/target fixtures reproduce the complete square
  remainder; the reversed indexing is detected.
- 2,000 exact rational tridiagonal fixtures produce no Schur pivot below the
  registered Gershgorin spectral floor.
- The fully branching two-label graph with all four edges in contact has
  Bellman value three, while constant finite paths approach three by the exact
  values `3-2/n`.  Branching creates no value premium.
- A separately reconstructed five-dimensional endpoint-constrained
  Pal--Vertesi carrier contains an arbitrary three-dimensional word as a
  principal block.  Direct Bell value, padded Jacobi value, and inner word
  value agree exactly.

## I3322 verdict

The older operator receipt explicitly accepts any positive Bellman storage
and excludes fixed-point equality, concavity, unique contact, shooting
normalization, and the domain-wall lower construction.  The carrier attack
supplies the reverse inequality with genuine tensor strategies.  Therefore

```text
omega_tensor(I3322) = omega_commuting(I3322)
```

and both equal the common Bellman/path variational value.

This does not certify the historical decimal, finite-dimensional
nonattainment, spatial attainment at the true value, or nonclosure.
