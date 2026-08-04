# Normalization tariff and cocycle drift are distinct

Status: **exact tariff identities; three of five numerical predictions fail**

Define the even normalization defect

```text
K(x)=F(x)F(-x)/b(x)^2.                              (1)
```

For a Bellman contact `z=P(x)`, put

```text
a=p(z)=b(z)/u,
c=F(x)=b(x)v.                                       (2)
```

Direct algebra gives the exact balanced weights

```text
A(z)=a sqrt(K(z)),
B(x)=c/sqrt(K(x)),                                  (3)
```

and therefore the exact symmetrization tariff

```text
r_sym=a[1-sqrt(K(z))]+c[1-1/sqrt(K(x))].            (4)
```

The reflected Bellman comparison is likewise

```text
r_ref=a[1-K(z)]+c[1-1/K(x)].                        (5)
```

The independent symbolic residuals for (4)--(5) are zero.

## Registered numerical test

Separate 1601- and 3201-node min-plus Bellman reconstructions were run.  Two
of five predictions pass:

- `K>=1` survives within the cross-resolution allowance;
- the exact tariff formulas agree with direct evaluation below `4e-16`.

Three predictions fail:

1. `K` does not have its maximum at the origin.  On `[-0.9,0.9]` the largest
   sampled value occurs at the two boundary points and is about `1.00733`.
2. Consequently `max(K)-1` is not below half of `q_*-1/4`.
3. The symmetrization tariff does not vanish at the two outer cocycle-drift
   roots.  Its fine-grid values there are approximately `9.1e-6` and
   `6.9e-6`; only the symmetry-fixed middle root is numerically compatible
   with zero at this resolution.

Thus normalization geometry and cocycle drift are not two readings of one
scalar obstruction.  `K` prices the gluing of Bellman normalization across
reflection, while `chi` measures the response cocycle.  Both enter the same
architecture, but neither determines the other.

## Instrument correction to Sprint 1271

Sprint 1270's atlas is assembled from local characteristic charts and their
exact reversible images.  Its reciprocal diagnostic therefore measures the
failure of those local chart normalizations to glue; it is not a quantitative
reconstruction of the globally normalized Bellman `K` profile.  The global
min-plus reconstruction in this sprint gives the larger `1.00733` boundary
value.  The Sprint-1271 conclusion—reciprocity is not available for free—
survives, but its reported local range must not be quoted as the global range.

## Consequence

The hoped-for shortcut from three drift zeros to zeros of one
symmetrization-tariff function is dead.  A rigorous chamber theorem must carry
the globally normalized `F`, `P`, and `K`, or certify `chi` directly.  The
exact tariff formulas remain useful for charging normalization error once
those global profiles are interval enclosed.  No new public I3322 or dimension
lower-bound claim follows from this scout.
