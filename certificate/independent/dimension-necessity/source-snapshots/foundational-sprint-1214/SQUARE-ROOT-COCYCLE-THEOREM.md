# Response packets carry the square root of the Bellman cocycle

Status: **exact packet-to-scalar energy theorem; quantitative global assembly
still open**

## 1. Abstract composition theorem

Let `a,b` be involutions of a finite index set and put `tau=a o b`. Let
`z_i>=0` and let `p_i,q_i>0`. Define the one-reflection amplitude residuals

```text
r^A_i=p_(a i)z_(a i)-p_i z_i,
r^B_i=q_(b i)z_(b i)-q_i z_i.                       (1)
```

Then the two equations in (1) compose exactly to

```text
z_(tau i)=c_i z_i+s_i,                               (2)

c_i=p_(b i)q_i/[p_(tau i)q_(b i)],                  (3)

s_i=r^A_(b i)/p_(tau i)
   +p_(b i)r^B_i/[p_(tau i)q_(b i)].                (4)
```

If

```text
p_min<=p_i<=p_max,
q_min<=q_i,                                          (5)
```

then

```text
sum_i s_i^2
 <=2 p_min^-2 sum_i (r^A_i)^2
  +2 p_max^2 p_min^-2 q_min^-2 sum_i (r^B_i)^2.     (6)
```

The estimate has no index-count, dimension, atom, or multiplicity factor.

## 2. From Hilbert packets to scalar residuals

Let `v_i` be mutually orthogonal packet vectors with `z_i=||v_i||`. If
unitaries `K_A,K_B` satisfy

```text
e^A_i=||K_A(p_i v_i)-p_(a i)v_(a i)||,
e^B_i=||K_B(q_i v_i)-q_(b i)v_(b i)||,              (7)
```

then the reverse triangle inequality gives

```text
|r^A_i|<=e^A_i,
|r^B_i|<=e^B_i.                                     (8)
```

Consequently (6) holds with the packet-error energies on its right-hand
side. Sprint 1212 controls precisely their direct-sum norms.

If the functional-calculus weights are not constant on a contact cell,
choose representatives `p_i,q_i`. If their uniform cell oscillations are at
most `omega_p,omega_q`, direct-sum orthogonality gives

```text
E_A,scalar <= E_A,packet+2 omega_p ||psi||,
E_B,scalar <= E_B,packet+2 omega_q ||psi||.          (9)
```

There is again no number-of-cells factor. Uniform continuity makes the two
oscillation terms vanish with contact-cell diameter.

## 3. Identification with the I3322 cocycle

On the exact contact graph, take

```text
p_i=sqrt(A(x_i)),
q_i=sqrt(B(u_i)),                                      (10)

A(x)=sqrt([b(x)^2/F(x)]F(-x)),
B(u)=sqrt(F(u)[b(u)^2/F(-u)]).
```

These are the balanced response weights of Sprint 1197; they are not equal
to `F(-x)` and `F(u)`. Their exact ratio laws are

```text
A(x)/A(-x)=F(-x)/F(x),
B(u)/B(-u)=F(u)/F(-u).                               (11)
```

For a source coordinate `u`, the first reflection is `b(u)=-u`, the second is
`a`, and

```text
x_(b i)=P(-u),
x_(tau i)=-P(-u).                                    (12)
```

Squaring (3) and using (11) therefore gives

```text
c(u)^2
 =F(-P(-u))F(u)/[F(P(-u))F(-u)]
 =C(u),                                                (13)
```

exactly Sprint 1210's positive mass cocycle. The apparent square-root loss in
passing from Hilbert norm to mass was an artifact of transporting the wrong
variable. The certificate controls the `l2` energy of the amplitude
recurrence residual directly.

## 4. Consequence for the dimension campaign

Combining Sprints 1212--1214 gives

```text
positive certificate energy
 -> packetwise weighted reflection errors
 -> square-root cocycle recurrence on dihedral chains
 -> recurrence-residual energy plus endpoints.       (13)
```

This is the algebraic operator-to-cocycle bridge requested after Sprint 1211.
The remaining work is quantitative assembly:

1. choose explicit contact tubes and cell diameters and bank all moduli;
2. prove how many orthogonal chain packets a local dimension or Schmidt-rank
   budget permits;
3. combine the amplitude telescope with the weighted endpoint lemma; and
4. compute whether the resulting exponent is the sharp `log R` or only an
   explicit weaker constant.

No device-independent dimension bound is claimed before those steps land.

## Proof

The `b` equation in (1) gives

```text
z_(b i)=[q_i z_i+r^B_i]/q_(b i).                    (14)
```

Insert (14) into the `a` equation at `b i`; since `a b=tau`, equations
(2)--(4) follow. Applying `(x+y)^2<=2x^2+2y^2`, using that `b` is a
permutation, and then (5), proves (6). Equations (8)--(9) follow from the
reverse triangle inequality and Minkowski's inequality in the orthogonal
direct sum. Equation (13) follows from the balanced-weight ratio laws (11).
