# Registration -- equality-kernel classification

Status: **registered after the initial zero-locus scan and before the formal
kernel proof and verification engines**

Sprint 1197 proves the exact tensor-product supremum but leaves finite
attainment open.  An exploratory 32,001-point hull scan found that the
transport remainder is not pointwise strict: its near-zero set follows the
central reversible Bellman characteristic.  The easy strict-gap argument is
therefore dead.

The next claim is narrower and structural.

## Registered target

Assume a finite-dimensional projective strategy attains `q_*`.  Equality in
the three positive remainders must:

1. confine the state to the unique reversible Bellman contact graph;
2. make the two local response kernels act as decreasing involutions of the
   finite spectral support;
3. force those involutions to coincide, because a finite ordered set has only
   one decreasing bijection;
4. reduce every occupied spectral pair to a two-point reflected component;
5. make the Alice and Bob amplitude ratios incompatible with `q_*>1/4`.

The target is a proof that no finite-dimensional tensor-product strategy
attains `q_*`.

## Falsifiers

- The scalar zero set is not a one-to-one increasing contact graph.
- A local equality kernel can map a nonzero spectral component to more than
  one scalar partner despite the graph property.
- The two response equations do not impose the same component-norm ratio.
- The resulting scalar expression can exceed `1/4`.
- The argument needs a finite-dimensional alignment assumption not already
  forced by the equality kernels.

## Boundary

The exploratory scan is not evidence for the theorem.  The promoted result
must use the exact Sprint-1195 Bellman fixed point, elementary finite spectral
calculus, and an independently checked scalar inequality.  Commuting-operator
attainment, physical realization, and foundational interpretation are outside
this registration.
