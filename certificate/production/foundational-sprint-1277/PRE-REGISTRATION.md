# Pre-registration: continuous predecessor-debt Lyapunov potential

Fix `kappa=0.9`.  For the global numerical Bellman profiles define

```text
c(u)=[1-P(u)^2]/[4F(P(u))^2],

h(u)=sup_(n>=0) sum_(j=0)^(n-1)
     [log c(P^j(u))-log kappa],
w(u)=exp h(u).                                       (1)
```

The dynamic-programming inequality is formally

```text
h(u)>=log c(u)-log kappa+h(P(u)),
c(u)w(P(u))/w(u)<=kappa.                             (2)
```

Run the 1601- and 3201-node global Bellman reconstructions, but evaluate
`P` continuously rather than rounding it to a sampled successor.  On a
7201-point carrier use a fixed 200-step horizon in (1).  Register:

1. the maximum weighted multiplier is at most `0.900001`;
2. `max(w)/min(w)<10`;
3. every maximizing partial sum occurs before step 100;
4. all increments in steps 181--200 are negative;
5. the coarse/fine values of `h` differ by less than `5e-3` uniformly.

Passing proves only the displayed finite-horizon floating-point facts.  The
continuous theorem still requires interval orbit trapping near the plateau,
a certified negative tail increment, and Arb evaluation of (2) on every cell.
