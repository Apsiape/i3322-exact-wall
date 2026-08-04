# Sprint 1245 pre-registration -- resolution-scale lift

Date: 2026-08-04

## Target

Determine what the response amplitude cocycle does to the regularized Schmidt
support. The registered wager is that it translates the regularization scale,
turning the former packet skew product into a canonical operator filtration.

## Registered prediction

If `rho=DD^*` commutes with a positive response multiplier `C`, then

```text
W_t(CD)=C^2 rho (tI+C^2 rho)^(-1)
       =rho (t C^(-2)+rho)^(-1).                    (1)
```

On a `C=c` spectral block this is exactly `W_(t/c^2)(D)`. Thus in
`zeta=log t` the response translates scale by `-2 log c`.

If `UDV=CD` exactly, then

```text
U W_t(D) U^*=W_t(CD),                               (2)
```

so the response correspondence is an order-and-scale skew product. Composing
Alice and Bob should multiply the two squared response multipliers, reproducing
Sprint 1214's mass cocycle with no packet choice.

## Failure conditions

- (1) has the reciprocal scale orientation;
- exact contact does not imply the required commutation;
- (2) fails because a right unitary survives in the left soft support;
- or the composed scale multiplier disagrees with Sprint 1214.

## Claim boundary

This is an exact equality/contact theorem. Quantitative control of the
commutator away from exact contact and a finite-rank scale-boundary inequality
remain open.
