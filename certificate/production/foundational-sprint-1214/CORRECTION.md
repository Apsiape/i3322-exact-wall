# Correction -- balanced response weights are geometric means

Date: 2026-08-03

The first committed version of `SQUARE-ROOT-COCYCLE-THEOREM.md` incorrectly
wrote

```text
A(x)=F(-x),       B(u)=F(u).
```

The certified Sprint 1197 definitions are

```text
A(x)=sqrt([b(x)^2/F(x)]F(-x)),
B(u)=sqrt(F(u)[b(u)^2/F(-u)]).
```

The square-root cocycle result does not require the false identifications. It
requires only

```text
A(x)/A(-x)=F(-x)/F(x),
B(u)/B(-u)=F(u)/F(-u),
```

which follow exactly from the balanced definitions and positivity. The
verifier now guards both squared ratio identities symbolically before checking
`c^2=C`. The packet-composition theorem, energy estimate, cocycle orientation,
and claim boundary are unchanged.
