# Response debts control full event rectangles

Status: **proved quantitative bridge; response-composition flux remains open**

Let `D` be a coefficient operator and suppose one response correspondence has
defect

```text
delta=||C D-J D S^T||_HS,                            (1)
```

where `C>0` and `J,S` are unitary.  Put `M=CD` and `N=JDS^T`.

## Square-root stability

For any rectangular matrix `M`, introduce its self-adjoint dilation

```text
H_M=[[0,M],[M^*,0]].                                  (2)
```

For `f_t(x)=x^2/(t+x^2)`, the two diagonal blocks of `f_t(H_M)` are the left
and right soft supports of `M`.  For self-adjoint matrices, scalar Lipschitz
functional calculus in Hilbert--Schmidt norm gives

```text
||f_t(H_M)-f_t(H_N)||_HS
 <=Lip(f_t)||H_M-H_N||_HS.                           (3)
```

This follows directly by expanding in eigenbases: every matrix entry is
multiplied by a divided difference bounded by `Lip(f_t)`.  Now

```text
Lip(f_t)=9/[8 sqrt(3t)],
||H_M-H_N||_HS=sqrt(2)||M-N||_HS.                    (4)
```

Keeping only the left block proves the dimension-free estimate

```text
||W_t(M)-W_t(N)||_HS
 <=[3 sqrt(6)/(8 sqrt(t))]||M-N||_HS.                (5)
```

Unitary covariance identifies `W_t(N)=J W_t(D)J^*`.  For any rank-`k`
projection `E`, Hilbert--Schmidt duality therefore proves

```text
|Tr[E W_t(CD)]-Tr[J^*EJ W_t(D)]|
 <=[3 sqrt(6k)/(8 sqrt(t))]delta.                    (6)
```

By Sprint 1248, both traces are complete rectangle masses of the
order-resolution event measure.  Thus (3) is a quantitative pushforward law
for a full vertical tail.  It does not discard the mass below the resolution
cut; any crossing of the cut appears through the response-transformed left
rectangle.

No commutation between `C` and `DD^*` is required.  When the ordered flag `E`
commutes with `C`, Sprint 1246 rewrites its first trace exactly as

```text
Tr[E rho(t C^(-2)+rho)^(-1)],                        (7)
```

so the noncommutative operator-valued resolution is included rather than
treated as an error.

## I3322 constants

On the sign-symmetric response region of Sprint 1240,

```text
delta_A<=sqrt(2 epsilon_A/eta),
delta_B<=sqrt(2 epsilon_B/eta).                      (8)
```

The certified response box permits the safe choices

```text
eta=1/12.                                            (9)
```

Consequently, for every rank-`k` ordered rectangle,

```text
Alice response error <=[9 sqrt(k epsilon_A)/(2 sqrt(t))],
Bob response error   <=[9 sqrt(k epsilon_B)/(2 sqrt(t))]. (10)
```

Indeed `(3 sqrt(6)/8)*sqrt(24)=9/2`.  This removes the response-multiplier
operator norm from the rectangle error entirely.

## What is now closed and what is not

The following arrows are representation-free and quantitative:

```text
Bellman contact -> common ordered flag,                         Sprint 1243
response debt   -> response pushforward of every soft rectangle, this sprint
rank d          -> total event mass d,                          Sprint 1247
resolution cut  -> explicit boundary flux.                     Sprint 1248
```

The remaining arrow is not local response transport.  It is composition:
compare the two response pushforwards on the common contact measure and prove
that their nonclosing order--resolution skew action must send a controlled
amount of mass through a boundary.  Equation (10) shows why a cut at depth
`L=-log(t)` costs `exp(L/2) sqrt(epsilon)`; rank must now bound how far that cut
has to be placed.
