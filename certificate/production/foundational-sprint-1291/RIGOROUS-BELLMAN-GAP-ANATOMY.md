# Rigorous Bellman-gap anatomy

Status: **certified identity and certificate-specific quantitative diagnosis**

## The identity

Let `G_i>0` be any Bellman-feasible primal witness at value `q`, and let
`pi_ij` be any probability flow with row and column marginals `r_i,s_i`.
Then

```text
q - [sum_ij pi_ij d_ij + 2 sum_i b_i sqrt(r_i s_i)]

= sum_ij pi_ij [q-d_ij-b_i^2/G_i-G_j]

  + sum_i [r_i b_i^2/G_i+s_i G_i-2b_i sqrt(r_i s_i)].             (1)
```

The first sum is the average **contact slack**. Every summand in the second is
the square

```text
(b_i sqrt(r_i/G_i)-sqrt(s_i G_i))^2,                              (2)
```

with the continuous zero-marginal convention. Thus every term is
nonnegative. Equation (1) is the primal-dual gap identity behind the finite
duality theorem of Sprint 1289.

## Certified anatomy of the current rigorous window

Apply (1) to the exact Sprint 1290 Bellman witness and the path flow induced by
the exact Sprint 1288 profile and amplitudes. The complete window

```text
2.9879822277405625e-7
```

splits as follows:

| Bill | Certified size | Share of window |
|---|---:|---:|
| Contact slack | `1.9088629361600619e-7` | `63.8846817%` |
| Interior marginal-balance slack | `8.210898602661784e-8` | `27.4797438%` |
| Terminal sink slack | `2.5802943131432201e-8` | `8.6355745%` |
| Rational square-root floor | `4.9246e-61` | negligible |

The first and third entries are exact rational numbers. The interior and
square-root entries are enclosed with 160-decimal-digit interval arithmetic.
Their four-way closure residual encloses zero within `5.7e-160`.

## Endpoint correction

The earlier statement that endpoint terms vanish needs a type distinction.
Because `b(+/-1)=0`, unmatched endpoint marginals vanish from the **dual
objective**. Relative to a fixed positive primal witness, however, the sink
still contributes

```text
s(-1) G(-1).
```

For the committed pair this is exactly the third row above. The source charge
is zero because its column marginal is zero. An optimal limiting primal may
drive `G(-1)` to zero; this particular strictly positive piecewise-linear
witness does not.

## Consequence for the next construction

Increasing square-root precision cannot materially improve the theorem. The
next upper campaign should instead test two changes:

1. an endpoint-adaptive positive boundary layer with `G(-1)` tending toward
   zero;
2. contact-adaptive knot placement near the exact worst interval and along
   the lower path's high-mass edges.

The lower campaign, independently, should update amplitudes against the
primal KKT balance rather than reuse the failed historical amplitude rule.

## Claim boundary

The percentages diagnose one committed upper/lower certificate pair. They are
not asserted to persist for optimized witnesses, in a continuum limit, or at
the true I3322 optimum. The identity is general; the numerical allocation is
not.
