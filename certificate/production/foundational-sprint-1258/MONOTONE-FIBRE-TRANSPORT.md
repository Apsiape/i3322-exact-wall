# The correct output receiver is monotone-fibre transport

Status: **exact transport theorem and two metric kills; receipt comparison
remains open**

## 1. Total variation is the wrong topology

For every `delta>0`,

```text
||delta_0-delta_delta||_TV=2,                        (1)
W_1(delta_0,delta_delta)=delta.                      (2)
```

Thus the Sprint 1255 flow theorem cannot be reached from the continuously
charged contact coupling merely by making its output mesh finer.  Total
variation turns an arbitrarily small response displacement into a full atom
loss.  This is not an absent estimate; it is a topological obstruction.

## 2. Monotone horizontal transport is exact

Let an ordered finite source have positive masses `w_i`, and let `A_i` and
`B_i` be two strictly decreasing real lists.  Define

```text
nu_A=sum_i w_i delta_(A_i),
nu_B=sum_i w_i delta_(B_i).                          (3)
```

The one-dimensional quantile coupling matches the `i`th source tranche to
the `i`th source tranche because both lists have the same order and the same
successive masses.  Therefore

```text
boxed: W_1(nu_A,nu_B)=sum_i w_i |A_i-B_i|.          (4)
```

No minimum atom separation occurs in (4).  Applied to the retained common
cells, it says that the horizontal term of Sprint 1257 is not merely bounded
by a transport distance: it **is** the monotone transport bill after the
cell representative is chosen.

## 3. Ordinary joint Wasserstein still forgets provenance

Horizontal transport alone is insufficient once the response translates
log resolution.  Put equal unit masses at two ordered fibres separated by
`delta`, and use vertical outputs

```text
Alice: (delta,+1), (0,-1),
Bob:   (delta,-1), (0,+1).                           (5)
```

The sourcewise vertical mismatch costs `4`.  Ordinary Wasserstein transport
cross-matches the fibres and costs only `2 delta`.  Hence it tends to zero as
the fibres coalesce while the response-resolution debt remains fixed.

This is the transport version of the terminal-fork countermodel: optimizing
over all couplings is allowed to exchange multiplicity provenance.

## 4. Monotone-fibre transport

The complete ordered flag supplies the missing address.  For measures made
from an ordered source, define the monotone-fibre coupling in two stages:

1. couple horizontal marginals by their common quantile tranches;
2. inside the `i`th tranche, couple the two translated copies of its vertical
   measure monotonically.

If `mu_i` has mass `w_i` and the two response translations are `p_i,q_i`,
the resulting weighted cost is exactly

```text
D_MF^(K,G)
 =sum_i w_i [K|A_i-B_i|+G|p_i-q_i|].                (6)
```

Indeed translation of any finite measure on the real line by `p_i` and
`q_i` has one-dimensional Wasserstein cost `w_i|p_i-q_i|`.

Combining (6) with the half-wall of Sprint 1257 gives, for the retained core,

```text
D_MF^(182/5,169/100) >=(m_0/2) M_core.              (7)
```

up to the already explicit source-cell and vertical-boundary bills.

## 5. The sharpened final gate

The old route asked for total-variation control of rounded atoms and is now
rejected.  The remaining theorem is instead:

```text
response rectangle receipts + contact bill + cut flux
   >= controlled monotone-fibre transport.           (8)
```

This is stronger than ordinary Wasserstein and weaker than remembering a
chosen Schmidt basis: its provenance is exactly the canonical ordered flag.
It is therefore the first output metric whose information type matches both
the response receipts and the terminal-fork audit.

Equation (8) is not proved here.  Until it is, neither a universal dimension
lower bound nor `D(epsilon)=Theta(log(1/epsilon))` is claimed.

