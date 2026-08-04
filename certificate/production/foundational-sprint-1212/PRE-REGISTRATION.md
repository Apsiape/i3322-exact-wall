# Sprint 1212 pre-registration -- matched-block transport

Date: 2026-08-03

## Target

Close the noncommutative-interference part of the operator-to-cycle arrow.
Do not infer a joint transport plan from marginal total variation. Instead,
use the exact permutation of symmetric spectral bins by each response
involution and retain Hilbert-space packets.

## Registered theorem

Let `{E_i}` be a finite orthogonal decomposition of a Hilbert space, let
`G_i<=E_i`, put `G=sum_i G_i`, and let a unitary `K` permute the coarse blocks
by `K E_i K*=E_{alpha(i)}`. For every vector `w`, put

```text
delta=||Kw-w||,
gamma=||(I-G)w||.
```

Then

```text
[sum_i ||K G_i w-G_{alpha(i)}w||^2]^(1/2)
 <= delta+2 gamma,                                      (1)
```

and hence the exact-rational quadratic relaxation

```text
sum_i ||K G_i w-G_{alpha(i)}w||^2
 <= 3 delta^2+6 gamma^2.                               (2)
```

The induced block masses `m_i=||G_iw||^2` obey

```text
sum_i |m_i-m_{alpha(i)}|
 <= 2 ||Gw|| (delta+2 gamma).                          (3)
```

## I3322 reading

For symmetric spectral bins, `K_A` and `K_B` permute the corresponding
coarse projections exactly. A thin one-cell cover of the double-contact graph
supplies the `G_i`. Sprint 1208 controls `delta`; its `R_0` localization
controls `gamma`. Thus (1) produces packetwise approximate response
transports without atoms, eigenvector selection, or a multiplicity basis.

## Failure conditions

- interference between different source blocks invalidates (1);
- the quadratic relaxation fails over exact rational fixtures;
- block-mass variation needs a dimension factor;
- or the I3322 response involutions do not exactly permute the required
  symmetric coarse spectral projections.

## Claim boundary

This theorem will not identify Alice's weighted packets with Bob's, construct
the common adaptive contact partition, or prove the dimension lower bound.
Those are the next gate if the theorem lands.
