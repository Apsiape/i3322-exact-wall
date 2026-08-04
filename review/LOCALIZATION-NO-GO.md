# Near-fixed localization no-go and maximal surviving lemma

**Status:** independently reconstructed; blocks the prospective universal
dimension lower bound

## Maximal valid transport lemma

Let `K` be unitary. Let `{E_j}` and `{E'_j}` be finite orthogonal projection
families, not necessarily complete, with `K E_j K*=E'_j`. For `G_j<=E_j` and
`G'_j<=E'_j`, put

```text
E=sum_j E_j,   E'=sum_j E'_j,
G=sum_j G_j,   G'=sum_j G'_j,
D^2=sum_j ||K G_j w-G'_j w||^2.
```

Then

```text
D <= ||E'(K w-w)||+||(E-G)w||+||(E'-G')w||,
D^2 <= 3[||E'(K w-w)||^2
          +||(E-G)w||^2+||(E'-G')w||^2].
```

The proof is the exact direct-sum decomposition

```text
K G_j w-G'_j w
 =K(G_j-E_j)w+E'_j(Kw-w)+(E'_j-G'_j)w.
```

This removes `E^perp`, but it does not remove the mass in `E-G`. That is the
distinction crossed in the former blind reconstruction.

For the two I3322 response estimates, let `Delta_coarse` be the sum of the four
actual source/target coarse omissions. The weight bound
`L_sigma^2<=13/10` gives

```text
D_A^2+D_B^2
 <=6(epsilon_A+epsilon_B)+(39/10)Delta_coarse.
```

Combining this with the valid conditional Sprint 1229 inequality gives only

```text
(mu^2/2)m_N
 <=48 epsilon_0
   +(27936/25)(epsilon_A+epsilon_B)
   +(90792/125)Delta_coarse
   +(mu^2/2)delta_cap.
```

The shifted-grid theorem controls the genuinely localized capture loss
`delta_cap`; it does not control `Delta_coarse`, which may contain order-one
drift mass.

## Minimal countermodel

Take `H=C^2`, let `K` swap `e0,e1`, and put

```text
w=(e0+e1)/sqrt(2),   P_N=|e0><e0|.
```

Then `K w=w`, but

```text
||(I-K)P_N w||=1.
```

Thus a zero global response defect gives no localized response defect without
a commutator or boundary-flux term.

An equivalent packet example takes `K=I`, `E=E'=I`,

```text
G=|e0><e0|,   G'=|e1><e1|,
w=(e0+e1)/sqrt(2).
```

The occurrence-internal omissions can both be zero while
`||G w-G' w||=1`. Completing the packets with orthogonal fillers does not
repair the inference: the local and filler errors may cancel. A filler theorem
would need cross conditions equivalent to no inbound/outbound flux.

## Exact repair criterion

A future proof must establish an I3322-specific estimate of the form

```text
Delta_coarse <= 4 theta m_N+C_0 sqrt(epsilon_0),
```

or an equivalent commutator/quasi-invariance/no-flux theorem. No such result
is present in the current public hypotheses. The countermodels attack the
abstract inference, not the existence of a stronger I3322-specific theorem.
