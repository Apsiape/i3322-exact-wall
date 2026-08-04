# Move the partition instead of refining it forever

Status: **exact moving-partition theorem; temporal rank accounting remains
open**

## 1. Exact partition transport

Let `Q_s={I_k(s)}` be any shifted predecessor-coordinate partition from
Sprint 1222. For a Borel bijection `g`, write

```text
g Q_s={g(I_k(s))}.                                  (1)
```

Every cell remains an interval because the contact reflections are monotone.
For either generator `r in {a,b}`,

```text
r[g Q_s]=(r g)Q_s                                   (2)
```

exactly. No common refinement, representative point, or cellwise rounding is
needed. The partition is a moving frame for the contact dynamics.

The paired local blocks at frame `g` are

```text
U cell: g(I_k),
X cell: P(g(I_k)).                                  (3)
```

They remain one-to-one and therefore retain Sprint 1221's rank-compression
property at every frame.

## 2. Explicit distortion

On the active chart,

```text
a=P^-1 o (-P),
|a'(u)|=P'(u)/P'(a(u)).                              (4)
```

Sprint 1217 certifies `1/10<P'<2`, hence

```text
1/20<|a'|<20.                                       (5)
```

Since `a` is an involution, the same upper bound applies to its inverse.
The other generator `b(u)=-u` is an isometry. Therefore, if a reduced or
unreduced word `g` contains `m` occurrences of `a`,

```text
Lip(g),Lip(g^-1)<=20^m.                             (6)
```

Cancellation can improve this bound but can never make it worse.

## 3. Rounding in a moved frame

Two coordinates `y,u` lie in different cells of `gQ_s` precisely when
`g^-1(y),g^-1(u)` lie in different cells of `Q_s`. Averaging over the shift
and using (6) gives

```text
Pr_s[g^-1(y),g^-1(u) separated]
 <=|g^-1(y)-g^-1(u)|/h
 <=20^m |y-u|/h.                                    (7)
```

The Sprint 1222 contact estimate then yields a deterministic shift with

```text
rho_g(s)<=[40 sqrt(10)/h]20^m sqrt(epsilon_0).       (8)
```

For all frames with at most `n` occurrences of `a`, the sum of the separate
average losses is bounded by

```text
[40 sqrt(10)/h] [(20^(n+1)-1)/19] sqrt(epsilon_0).  (9)
```

Because the same shift is averaged in every term, one deterministic shift
simultaneously achieves the summed bound. This is the correct alternative to
asserting that one shift is individually optimal in every frame.

### Dependency-audit correction to (9)

Equation (9) omitted the multiplicity of distinct dihedral frames with the
same number of `a` occurrences. The per-frame estimate (8) is unchanged. For
all distinct reduced frames, there are at most two frames with no `a` and at
most four frames for each positive `a` count. A safe replacement is

```text
[40 sqrt(10)/h]
 [2+4 sum_(m=1)^n 20^m] sqrt(epsilon_0).             (9a)
```

For a specified one-sided history, sum (8) only over the frames actually
visited; its smaller multiplicity may be retained. This is a finite constant-
factor correction and does not change the exponential dependence. The
verifier certifies (2), (6), and the per-frame bound; it never tested the
multi-frame count in the original (9).

## 4. What this resolves

The old obstruction was framed as:

```text
finite grid + infinite dihedral closure -> infinitely thin refinement.
```

Equation (2) removes the refinement. Each response acts exactly between two
frames, while (8) prices the distortion of reading contact in that frame.
Exponential distortion is acceptable at this stage: the desired dimension
lower bound is itself exponential, and no uncontrolled or superexponential
factor has appeared.

## 5. Remaining rank-in-time gate

Sprint 1221 retains at most `d` heavy paired blocks in any one frame. Applying
that theorem independently in `n` frames could retain `nd` different labels,
which is not yet the `d`-site chain budget required by Sprint 1215.

The next theorem must exploit that all moved partitions are functions of the
same finite local operators. It must either:

1. label chains by the at most `d` local spectral atoms and let only their
   cell addresses change with the frame; or
2. prove a simultaneous low-rank compression inequality for the family
   `{D_g}` with one common set of at most `d` ancestry channels.

No final dimension inequality is claimed before that temporal rank theorem.
