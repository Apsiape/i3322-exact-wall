# Common target norms repair the near-fixed type crossing

Status: **exact abstract theorem and hostile dependency audit; coefficient
oscillation and global ancestry assembly remain open**

## 1. The missing object was weaker than a fibre isometry

Let `G_i` and `G'_i` be common source and target joint projections. For each
response label `sigma in {A,B}`, let `L_sigma>=0` commute with both packet
families and let `K_sigma` be unitary. Put

```text
v_i=G_i psi,              v'_i=G'_i psi,
z_i=||v_i||,              z'_i=||v'_i||,
p^sigma_i=||L_sigma v_i||/z_i,
p'^sigma_i=||L_sigma v'_i||/z'_i.                    (1)
```

Zero packets are discarded. If the two-frame packet theorem supplies

```text
e^sigma_i
 =||K_sigma L_sigma v_i-L_sigma v'_i||,              (2)
```

then reverse triangle gives

```text
|p^sigma_i z_i-p'^sigma_i z'_i|<=e^sigma_i,          (3)
```

and, whenever `p'^sigma_i>=m>0`,

```text
|z'_i-(p^sigma_i/p'^sigma_i)z_i|
 <=e^sigma_i/m.                                      (4)
```

Both response laws therefore act on the same two scalar amplitudes
`(z_i,z'_i)`. The theorem does **not** identify the spectral fibres carrying
`v_i` and `v'_i`; it does not need to. Norm is the common quotient used by
Sprint 1214's scalar recurrence.

In Sprint 1227's pullback cell, the same source joint projection lies below
Alice's and Bob's respective source coarse blocks. The same target joint
projection lies below both target coarse blocks. Sprint 1225 can therefore be
applied twice with the same `G_i,G'_i`, producing (3) for `A` and `B` with one
shared pair `(z_i,z'_i)`.

## 2. Exact oscillation bill

Let a positive scalar weight `ell` take values in `[m,M]`. Suppose chosen
source and target representatives have weights `ell_s,ell_t`, while packet
RMS weights obey

```text
|p-ell_s|<=omega,
|p'-ell_t|<=omega,
p',ell_t>=m.                                        (5)
```

Then

```text
|p/p'-ell_s/ell_t|
 <=|p-ell_s|/p'
   +ell_s |ell_t-p'|/(p' ell_t)
 <=omega(1/m+M/m^2).                                (6)
```

Combining (4) and (6), the point-representative response residual satisfies

```text
|z'-(ell_s/ell_t)z|
 <=e/m+omega(1/m+M/m^2)z.                           (7)
```

There is no packet-count, block-count, multiplicity, or dimension factor.
For I3322, `ell=sqrt(A)` or `sqrt(B)`, and on the certified active box one may
take

```text
m>(1/12)^(1/2),       M<(13/10)^(1/2).               (8)
```

Because these weights are continuously differentiable on every compact
active sub-box, `omega=O(h)` on width-`h` cells. Thus Sprint 1226's scalar
closure inequality can be used after paying an explicit `O(h^2)` energy
term. A partial isometry is not the missing gate.

## 3. Hostile dependency audit

| Sprint | abstract result | application verdict |
|---|---|---|
| 1218 | RMS compression is exact | displayed endpoint consequence is conditional on a chain decomposition |
| 1219 | ordinary finite-flow theorem is exact | scalar generalized-flow completion is killed by 1220 |
| 1221 | matched-block rank inequality is exact | top-`d` selection in one frame does not itself produce a transport-closed history |
| 1222 | shifted mismatch bound is exact | supplies paired blocks per frame only |
| 1223 | moving partition and distortion bounds are exact | common temporal ancestry is not automatic |
| 1224 | ordered-cell rank theorem is exact | requires an actual captured path through the moving cells |
| 1225 | two-frame packet theorem and coarse addresses are exact | “drift chain complete” was premature until the paths and endpoint leakage are assembled |
| 1226 | scalar closure matrix theorem is exact | applies after common scalar amplitudes and coefficient errors are supplied |
| 1227 | pullback address and separation bound are exact | fibre-isometry demand was too strong; zero-oscillation promotion remains retracted |

One further repair is immediate. Sprint 1215 assumed
`sum_alpha n_alpha<=d` in its many-chain statement. For the displayed common
lower bound it is enough that **each** `n_alpha<=d`, because

```text
n_alpha^2 M^(2(n_alpha-1))
 <=d^2 M^(2(d-1)).                                  (9)
```

Hence arbitrarily many orthogonal chains may be summed without a global
chain-count bill, provided every captured chain separately consumes at most
`d` ordered spectral subspaces.

## 4. Exact remaining gates

The proof is not finished by this repair. The live obligations are now:

1. bank a concrete Lipschitz/oscillation constant for `sqrt(A)` and
   `sqrt(B)` on the active sub-box;
2. write the path decomposition across moving frames and charge every path
   endpoint by the existing discard/response energy;
3. use a near-fixed coarse mesh and a drift fine mesh without assuming that
   either mesh is globally invariant;
4. discard the inactive predecessor strip by a positive `r_0` gap; and
5. collect constants into one explicit `q_*-Q_d` inequality.

This narrows the wall from “construct a fibre isometry” to a conventional,
quantitative scalarization and ancestry assembly.

