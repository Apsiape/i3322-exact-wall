# Sprint 1224 pre-registration -- ordered temporal rank

Date: 2026-08-03

## Target

Prove that changing partition frames do not consume fresh local rank on a
nonfixed drift component.

## Registered theorem

Let `tau` be increasing and suppose on one drift component either

```text
tau(u)-u>=Delta>0                                   (1)
```

throughout, or the reversed inequality holds. Let successive moving cells
have diameter at most `H`, and let their representative coordinates satisfy

```text
|c_(k+1)-tau(c_k)|<=eta.                            (2)
```

If

```text
Delta>eta+2H,                                       (3)
```

the cells should be strictly ordered and pairwise disjoint. Their nonzero
spectral projections for one local operator should therefore number at most
the local dimension `d`.

## I3322 specialization

For frames of depth at most `n`, Sprint 1223 gives `H<=20^n h`. Choosing

```text
h<=(Delta-eta)/(4*20^n)                             (4)
```

should make the moving-cell chain consume at most `d` sites.

## Failure conditions

- nonconsecutive cells can overlap despite the one-step gap;
- changing partitions invalidates spectral orthogonality;
- the bound counts grid labels rather than local spectral subspaces;
- or the negative-drift orientation needs a different constant.

## Claim boundary

This theorem is conditional on a drift threshold `Delta` and coordinate-step
error `eta`. The certificate must still charge visits to the complementary
near-fixed region and bound `eta` from its response debts.
