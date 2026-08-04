# The quarter margin is a quadratic packet-mass gap

Status: **exact scalar/Hilbert bridge; near-fixed pair extraction remains
separate**

## 1. Closure matrix

Use Sprint 1211's notation

```text
B=b(x)+b(u),
delta=x-u,
Q=q_*-x u+1.
```

For nonnegative packet amplitudes `z_+,z_-`, define

```text
R_+=(Q-delta/2)z_+-Bz_-,
R_-=(Q+delta/2)z_--Bz_+.
```

The closure matrix has eigenvalues

```text
lambda_+/-=Q +/- sqrt(B^2+delta^2/4).
```

Sprint 1211 proves

```text
Q-sqrt(B^2+delta^2/4)>=q_*-1/4=:m_0>0.
```

Therefore

```text
R_+^2+R_-^2>=m_0^2(z_+^2+z_-^2).                 (1)
```

This remains valid when either amplitude vanishes.

## 2. Certificate-owned decomposition

Let

```text
r_A(x)=A(x)/b(x),
r_B(u)=B(u)/b(u),
e_A=z_--r_A(x)z_+,
e_B=z_--r_B(u)z_+,
r_0(x,u)=q_*-d(x,u)-A(x)-B(u).
```

The product laws give the exact identities

```text
R_+=z_+r_0(x,u)-b(x)e_A-b(u)e_B,
R_-=z_-r_0(-x,-u)+A(-x)e_A+B(-u)e_B.             (2)
```

Thus the closure gap is paid by the contact remainder on the packet and its
reflected partner and by the two response-amplitude residuals. No fourth
certificate remainder is introduced.

## 3. Uniform energy consequence

On the certified active box, `b<=1/2` and `A,B<=13/10`. The three-term square
inequality yields

```text
R_+^2
 <=3[r_0(x,u)^2 z_+^2+(1/4)e_A^2+(1/4)e_B^2],
R_-^2
 <=3[r_0(-x,-u)^2 z_-^2
      +(169/100)e_A^2+(169/100)e_B^2].             (3)
```

Consequently, after summing an orthogonal reflected-packet family,

```text
m_0^2 W_pair
 <=3 R_0,max epsilon_0,pair
   +(291/50)(E_A,pair+E_B,pair),                  (4)
```

where `E_A,pair` and `E_B,pair` denote squared-error sums. The local contact
quantity `epsilon_0,pair` counts both source and reflected-target contact
contributions. When it is compared with the single global remainder
`epsilon_0`, those two internally orthogonal families need not be mutually
orthogonal; the safe global bound is `epsilon_0,pair<=2 epsilon_0`. This
factor of two is retained explicitly in Sprint 1229.

## Claim boundary

This theorem charges an already paired reflected packet family. Sprint 1227
constructs common pullback cells, but those cells do **not** by themselves
localize the global response defect. Sprint 1229's numerical consequence is
therefore conditional on a localized-response/commutator estimate or a
packet-completion intertwiner that controls the omitted complements.
