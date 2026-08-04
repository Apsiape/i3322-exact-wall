# Sprint 1214 pre-registration -- square-root cocycle bridge

Date: 2026-08-03

## Target

Close the packet-to-scalar bridge without converting Hilbert energy into a
linear mass error. Transport packet amplitudes `z_i=sqrt(m_i)` and identify
their positive cocycle as the square root of Sprint 1210's mass cocycle.

## Registered prediction

Let `a,b` be involutions of a finite packet index set, `tau=a o b`, and let
`p_i,q_i>0`. Suppose packet transports have errors `e^A_i,e^B_i` and packet
amplitudes `z_i>=0`, so that

```text
|p_(a i) z_(a i)-p_i z_i| <= e^A_i,
|q_(b i) z_(b i)-q_i z_i| <= e^B_i.                 (1)
```

Then

```text
z_(tau i)=c_i z_i+s_i,
c_i=p_(b i)q_i/[p_(tau i)q_(b i)],                  (2)
```

with

```text
sum_i s_i^2
 <= 2 p_min^-2 sum_i (e^A_i)^2
  + 2 p_max^2 p_min^-2 q_min^-2 sum_i (e^B_i)^2.    (3)
```

On the I3322 contact graph, `c_i^2=C_i` exactly.

## Failure conditions

- composition produces a different cocycle orientation;
- the energy estimate acquires a block-count or dimension factor;
- the I3322 coefficient squares to `1/C` rather than `C`;
- or cellwise Bellman-weight oscillation cannot be added in direct-sum norm.

## Claim boundary

This theorem will close the algebraic packet-to-cocycle bridge. It will not
yet supply explicit contact-tube moduli, a local-dimension packet budget, or
the final numerical lower-bound constants.
