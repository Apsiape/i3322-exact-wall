# Pre-registration: response transport on event rectangles

The event measure is useful only if the actual Hilbert--Schmidt response debts
control its rectangle masses without selecting Schmidt vectors.

Registered theorem:

If `M=CD`, `N=JDS^T`, `J,S` are unitary, and `delta=||M-N||_HS`, then for
every rank-`k` projection `E`,

```text
|Tr(E W_t(CD))-Tr(J^*EJ W_t(D))|
 <=sqrt(k)(||CD||_op+||D||_op) delta/t.
```

The proof may use only resolvent stability and unitary covariance.  No
commutation, Schmidt basis, packet partition, or deleted complement is
allowed.  A hostile numerical guard must include noncommuting `C` and `rho`.

## Outcome of the hostile control

The registered `1/t` estimate is valid but underpowered.  The intended
negative control predicted that replacing `1/t` by `1/sqrt(t)` would fail. It
did not fail in 10,000 hostile fixtures.  A block-dilation proof then showed
why: the dimension-free bound

```text
||W_t(M)-W_t(N)||_HS<=(3 sqrt(6)/(8 sqrt(t)))||M-N||_HS
```

holds without operator-norm factors.  The theorem file records this stronger
post-control result and the verifier rejects a genuinely too-small constant.
