# Adversarial audit of the exact I3322 wall

Status: **passed with one scope-wording repair and no theorem retraction**

This audit reconstructs Sprints 1195--1199 from their equations and reruns the
load-bearing interval and symbolic engines. It does not treat the previous
theorem documents as authorities.

## Verdict

The following statements survive.

1. The validated domain-wall parameter `q_*` supports a positive Bellman fixed
   point with a unique strictly increasing predecessor map.
2. The geometrically symmetrized three-remainder certificate proves the
   commuting-operator upper bound `B_I3322<=q_*`.
3. Tensor-product strategies approach `q_*`, so both the tensor and commuting
   suprema equal `q_*`.
4. Equality on a finite joint spectral support forces two decreasing support
   bijections to coincide. The resulting amplitude equations imply a value at
   most `1/4`; since `q_*>1/4`, finite-dimensional attainment is impossible.

## Load-bearing checks

### A. Strict and unique Bellman contact

This was the most exposed step in Sprint 1198. Merely having an active
predecessor would not be enough.

The exact interval rerun gives:

- central/local chart: `dx<0`, `dy<0` on all 8,192 tiles;
- four central iterates: `dx<0`, `dy<0` on all `4*32,768` tiles;
- two right-wing iterates: `dx<0`, `dy<0` on all `2*32,768` tiles;
- reflected charts supply the opposite halves;
- every inactive outer predecessor is excluded.

Thus the active contact relation is a single-valued strictly monotone graph,
not merely a set-valued hull. This justifies the inverse used in the finite
support maps.

### B. Upper certificate

The Bell operator reparameterization has zero symbolic residual. The forward
and reflected Bellman inequalities combine by an exact Cauchy identity. The
two local product laws are exact.

The cleaner representation-free local proof is

```text
R_A=sqrt(A(X))[I-J_A(2B3-I)]sqrt(A(X))>=0,
```

and its Bob analog. It requires only cross-party commutation. The transport
remainder requires only joint functional calculus for commuting `X,U`.
Their sum reconstructs `q_*I-B` exactly.

### C. Finite-support nonattainment

Let the occupied zero-support pairs be `(P(u),u)`. The two local kernel
equations induce

```text
a(u)=P^{-1}(-P(u)),   b(u)=-u.
```

Each is a decreasing bijection of the same finite ordered set. Such a set has
only one decreasing bijection, so `a=b`. This pairs every occupied component
with `(-x,-u)`.

The two unitary kernel equations then assign the same norm ratio `rho`.
Bellman and Cauchy equality force

```text
q_*=xu-1+sqrt((b(x)+b(u))^2+(x-u)^2/4).
```

Writing `t=1-xu` and using

```text
(1-xu)^2-(1-x^2)(1-u^2)=(x-u)^2
```

gives `q_*<=-t+sqrt(t)<=1/4`, contradiction.

### D. Finite commuting representations

Two proofs are available.

1. The support proof above uses only a finite joint spectrum and cross-party
   commutation.
2. Independently, finite-dimensional commuting C*-algebras decompose into a
   finite direct sum of spatial matrix blocks. The Bell value is a convex
   combination of tensor-block values. Equality would force one finite tensor
   block to attain `q_*`, already impossible by C.

The second proof removes correlated dependence on the support argument.

## Correction made by this audit

The Sprint-1199 theorem included an unnecessary sentence asserting a general
binary-POVM extension through commuting Naimark dilation. The standard
commuting correlation model is already presented by PVMs, and no POVM claim is
needed for the theorem. The sentence is removed from the load-bearing
statement rather than defended incidentally.

## Exactness language

`q_*` is exact in the validated-numerics sense: it is defined by the certified
domain-wall zero and enclosed in

```text
[0.250875384513976536 +/- 4.86e-19].
```

It is not claimed to have a known algebraic or elementary closed form. The
standalone manuscript uses **rigorously characterized** where that distinction
could otherwise be ambiguous.

## What remains outside the theorem

- Whether the supremum is attained by a completed infinite-dimensional
  strategy is not needed for the supremum or finite-nonattainment statements
  and is not promoted here.
- Priority and novelty relative to unpublished work are separate from
  correctness.
- No experimental, physical-foundational, or corpus-metaphysical consequence
  follows from this Bell theorem alone.
