# Pre-registration: quantitative coalescence of the two order reversals

At a selected resolution cut, let `nu_A,nu_B` be the horizontal marginals of
the Alice and Bob event measures.  They have equal total mass.  The target is
to bound the disagreement of the two decreasing response maps without
constructing common Hilbert-space target fibres.

Registered identity:

```text
W1(a_*nu,b_*nu)=integral |a(u)-b(u)| dnu(u)
```

for any finite measure `nu` and decreasing maps `a,b` on an interval.

Registered I3322 bound at `t=exp(-L)`:

```text
integral |a(u)+u| dnu_B(u)
 <=21 sqrt[d/(2t)] (40 epsilon_0)^(1/4)
   +9 sqrt(d/t)(sqrt(epsilon_A)+sqrt(epsilon_B))
   +2(Flux_A+Flux_B).
```

The proof must retain unequal vertical-cut masses during each individual
response comparison and charge them by the flux terms.  It may not identify
orthogonal multiplicity fibres.

