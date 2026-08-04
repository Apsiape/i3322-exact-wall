# Sprint 1225 pre-registration -- exact moving-frame packet addresses

Date: 2026-08-03

## Target

Remove the coordinate-step error left open in Sprint 1224. Generalize matched
packet transport from one permuted PVM to two exactly related partition
frames.

## Registered theorem

Let `{E_i}` and `{E'_i}` be complete orthogonal projection decompositions,
with

```text
K E_i K*=E'_i.                                      (1)
```

Let `G_i<=E_i`, `G'_i<=E'_i`, `G=sum G_i`, and `G'=sum G'_i`. For every `w`,
the prediction is

```text
D=[sum_i ||K G_i w-G'_i w||^2]^(1/2)
 <=||Kw-w||+||(I-G)w||+||(I-G')w||.                 (2)
```

Consequently

```text
D^2<=3[delta^2+gamma_s^2+gamma_t^2].                (3)
```

## I3322 prediction

For a moved contact partition `gQ`, the next reflection sends each coarse
local block exactly to the same-index block of `rgQ`. Thus packet debt is
amplitude leakage, not coordinate error, and Sprint 1224 may take `eta=0`.

## Failure conditions

- the direct-sum orthogonality is lost between different frames;
- target discard cannot be controlled independently of source discard;
- cell indices require approximate geometric matching;
- or exact rational fixtures violate (3).

## Claim boundary

This theorem does not charge the near-fixed region or assemble the full
certificate constants.
