# Sprint 1239 pre-registration -- terminal common-fork attack

## Question

Does an explicit canonical drift endpoint entering the near-fixed sector
automatically supply the common source/target packet required by Sprint 1229,
using only:

- two self-adjoint response involutions;
- small global response defects;
- exact coarse spectral addresses; and
- response-specific fine packet transports?

## Registered prediction

The statement is expected to fail because coarse spectral labels do not
record multiplicity fibres. A finite countermodel should have:

```text
K_A w=w,                  K_B w=w,
K_A G w=G'_A w,           K_B G w=G'_B w,
G'_A G'_B=0,
```

while `G'_A` and `G'_B` lie under the same coarse target block. Then each
response-specific fine error is zero, but there is no zero-cost common target
packet.

## Failure conditions

The attack fails if the claimed involutions are not self-adjoint unitaries,
if the global state is not fixed, if the response-specific packet equations
do not hold exactly, or if the two fine targets do not share one coarse
spectral label.

Even if the attack lands, it kills only derivation from the abstract packet
hypotheses. It does not kill a stronger I3322-specific theorem using the
shared tensor factors in `K_A=J_A S_B` and `K_B=S_A J_B`, or a PSD/Gram-valued
transport retaining branch provenance.
