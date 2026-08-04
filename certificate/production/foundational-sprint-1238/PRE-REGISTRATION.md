# Sprint 1238 pre-registration -- coupled near/drift closure

## Target

Replace the false standalone estimate `m_N=O(sqrt(epsilon))` by a theorem
that keeps the two-frame response estimate global and charges every omitted
coarse packet outside the near-fixed sector to the complementary sector.

## Registered statements

Let `m_N`, `m_D`, and `m_out` be the near-fixed, retained-drift, and far-tail
masses, so that

```text
m_N+m_D+m_out=1.
```

Let `delta_cap` be the four-occurrence shifted capture loss inside the
near-fixed sector, and let `Delta_coarse` be the four actual unweighted coarse
omissions in the maximal valid two-frame lemma.

1. **Global split.** The target inequality is

   ```text
   Delta_coarse <= delta_cap+4(m_D+m_out).
   ```

   This is only a measure decomposition. It must not use a commutator,
   localized response defect, or invariance of the near-fixed projection.

2. **Coupled closure.** Combining the global split with the valid weighted
   closure theorem should give exact constants `C_N,C_D` such that

   ```text
   m_N <= C_D(m_D+m_out)+C_N sqrt(epsilon).
   ```

3. **Forced drift alternative.** After the certified tail estimate, either
   the Bell deficit already exceeds an explicit dimension-independent
   constant or

   ```text
   m_D >= w_0>0.
   ```

## Failure conditions

The sprint fails if:

- any occurrence outside the near-fixed set is silently deleted rather than
  charged to `m_D+m_out`;
- `Delta_coarse` is weighted twice or the factor four is reduced without an
  orthogonality proof;
- the result is advertised as `m_N=O(sqrt(epsilon))`;
- the forced drift alternative is used to prove the dimension lower bound
  before terminal near-entry packets are independently charged; or
- the terminal charge restricts a global response defect and thereby repeats
  the localization error this sprint is designed to avoid.

## Post-sprint gate

The next gate is carrier-typed: prove or refute that the explicit terminal
packet of a canonical drift chain can be inserted into Sprint 1229's
already-captured common-packet inequality with all response and contact reuse
charged. The coupled-sector theorem alone does not close v1.3.
