# The Bellman derivative contracts globally after a Lyapunov change of gauge

Status: **weighted contraction passes; registered cycle count fails at fine
resolution; continuous interval lift open**

At the global numerical Bellman fixed point, linearization gives

```text
(L delta)(u)=c(u) delta(P(u)),
c(u)=[1-P(u)^2]/[4F(P(u))^2].                       (1)
```

The local coefficient is not contractive:

```text
max c(u) = 1.264... > 1.                            (2)
```

This explains why constant-width Bellman barriers and a uniform sup norm are
the wrong instruments.

The response is nevertheless deterministic: each target has one predecessor.
The coarse induced graph has one fixed vertex near `0.8785`.  The fine graph
has two adjacent fixed vertices, at `0.8780` and `0.8785`, so the registered
one-cycle prediction fails.  This is the nearest-grid projection resolving
one continuous plateau basin into two discrete self-loops; it may not be
silently merged.  All measured cycle multipliers nevertheless lie below

```text
0.861 < 0.9.                                        (3)
```

The max-plus cycle criterion therefore constructs a positive weight `w` with

```text
c(u)w(P(u))/w(u)<=0.9                              (4)
```

at every sampled vertex in both graphs.  The required dynamic range is below
`5.5`, despite the local amplification in (2).  Thus four of five registered
predictions pass: only the exact discrete cycle count fails.

This supplies a viable candidate for the missing global datum behind Sprints
1274--1275.  The
Bellman branch is not selected by local value or local Morse sign; it is
stabilized by a Lyapunov gauge accumulated along predecessor history.  Local
expansion is lawful because every closed predecessor history contracts.

## Next proof gate

Replace the sampled weight by a piecewise interval weight and prove (4) on
every carrier cell using Arb enclosures of `P`, `F`, and the cell image.  A
continuous weighted contraction would yield:

1. uniqueness of the globally normalized Bellman fixed point in the certified
   order interval;
2. rigorous weighted sub/supersolution barriers;
3. interval enclosures for `F` and `P`; and
4. the full-domain sign certificate for Sprint 1273's discriminant `D`.

The discrete cycle split means the finite graph cannot establish continuous
orbit topology.  No continuous contraction or dimension lower bound is
claimed by the present computation.
