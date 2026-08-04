# Sprint 1242 pre-registration -- regularized Schmidt flags

Date: 2026-08-04

## Target

Add the ordered spectral flag missing from the marginal-volume invariant.
Interpolate between state mass and algebraic rank with the regularized Schmidt
support

```text
W_A,t=D(tI+D^*D)^(-1)D^*,
W_B,t=D^*(tI+DD^*)^(-1)D.
```

Its nonzero eigenvalues are `s_j^2/(t+s_j^2)`.

## Registered predictions

1. `W_A,t D=D W_B,t` exactly and the two soft ranks have equal trace.
2. If left and right spectral flags `E,F` are approximately identified by the
   contact-supported Schmidt operator, then their soft ranks differ by at
   most

   ```text
   sqrt(r)/(2 sqrt(t)) ||E D-D F||_HS.
   ```

3. The soft support is stable under a matrix perturbation `M-N` with the
   explicit resolvent bound

   ```text
   ||W(M)-W(N)||_HS
   <= (||M||+||N||)/t ||M-N||_HS.
   ```

4. The Sprint 1241 doppelganger is detected by its transported cumulative
   flags even though every marginal volume agrees.

## Claim boundary

This sprint will establish the regularized flag calculus. It will not claim
that the I3322 remainders already control every flag uniformly in threshold,
nor that soft flag closure by itself yields a dimension lower bound.
