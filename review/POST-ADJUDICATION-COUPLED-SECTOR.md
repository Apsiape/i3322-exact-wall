# Post-adjudication result: coupled sectors and the terminal fork

**Date:** 2026-08-04  
**Release decision:** unchanged -- do not tag or mint v1.3

## What was repaired

The full coarse omissions cannot be replaced by near-fixed capture loss, but
they can be split without localizing the response vector:

```text
Delta_coarse <= delta_cap+4(m_D+m_out).
```

This gives a valid coupled theorem

```text
m_N<=C_D(m_D+m_out)+C_N sqrt(epsilon),
```

and hence an exact alternative: either the deficit is already bounded below
by a fixed constant or a dimension-independent drift mass `m_D>=w_0>0`
exists. Sprint 1238 contains the proof and an exact hostile measure guard.

This is genuine progress, but it is not the former claim
`m_N=O(sqrt(epsilon))`.

## What failed next

The natural shortcut was to run the finite drift chains on the forced drift
mass and charge every terminal entry into the near-fixed sector by Sprint
1229's valid already-captured packet theorem.

Sprint 1239 gives an exact countermodel. Two self-adjoint response
involutions can fix the global state and transport one localized source
packet with zero error into orthogonal multiplicity fibres carrying the same
coarse target label. The countermodel also has the shared-factor forms

```text
K_A=J_A tensor S_B,       K_B=S_A tensor J_B
```

and the exact coarse sign relations. Thus a terminal source does not
canonically produce the common target amplitude required by the scalar
closure theorem.

## Adjudication

The scalar norm-packet route cannot close the universal dimension lower bound
from the present hypotheses. It forgets branch provenance at exactly the
place where the response-specific targets must be compared.

The remaining serious route is operator-valued: a PSD/Gram transport or a
robust self-testing theorem that retains multiplicity fibres and uses the
contact remainder before scalarization. This is a new campaign, not a repair
to equation (16).

The proved public consequence remains the one-sided constructive estimate

```text
q_*-Q_d<=exp[-d log(R)+O(1)].
```

No universal lower rate or `Theta(log(1/epsilon))` dimension law is restored.
