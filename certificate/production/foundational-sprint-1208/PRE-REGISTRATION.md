# Sprint 1208 pre-registration -- robust remainder localization

Date: 2026-08-03

## Target

Start the arbitrary-strategy half of the quantitative I3322 campaign at the
three positive certificate remainders. Determine exactly what a Bell deficit
`epsilon` forces before any finite-path or index interpretation is imposed.

## Registered predictions

1. Each local response remainder factors as `L(I-K)L`, where `K` is a
   self-adjoint involution and `L` is the positive Bellman weight.
2. Its expectation is exactly one half of the squared failed-reflection norm:
   `||(I-K)L psi||^2 = 2 <psi,R psi>`.
3. On every sign-symmetric spectral region where both reflected Bellman
   weights are at least `eta`, the normalized weighted transport has defect at
   most `sqrt(2 epsilon/eta)`.
4. The transport remainder `R0` gives a measure bound outside every fixed
   neighborhood of its double-contact zero set.
5. Combining 1--4 yields approximate weighted Alice and Bob reflections on
   state mass `1-O(epsilon)`, but does not by itself yield a discrete common
   orbit, a translation, or a dimension lower bound.

## Failure conditions

- a local factorization requires commutation not present in the operator
  certificate;
- the squared-norm identity fails outside scalar fibers;
- the necessary cutoff is not invariant under the sign flip;
- the double-contact zero set meets a response-weight degeneracy;
- or the result silently assumes aligned/Jacobi form.

No numerical constant will be fitted after the run. A future explicit
dimension bound must separately certify the contact modulus, orbit rounding,
and finite-rank boundary charge.
