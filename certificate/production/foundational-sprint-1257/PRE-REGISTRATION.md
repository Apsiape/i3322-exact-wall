# Pre-registration: common-cell quarter wall

Start from a retained event `(y,u,zeta)` of Sprint 1256, so `y` and `u`
belong to one interval cell of width `h`.  Choose any representative `r` in
that cell.  Before rounding either response output, register the target:

```text
m_0 <= (182/5)|a(y)+u|
       +(169/100)|p(y)-q(u)|
       +(41769/50)h,

p=2 log(alpha),  q=2 log(beta).
```

Thus `h<=25m_0/41769` must leave a pointwise gap of at least `m_0/2`
between the actual Alice and Bob response events.

Falsifiers:

1. the unrounded quarter wall does not hold at every cell representative;
2. one of `a`, `log(alpha)`, or `log(beta)` lacks the claimed Lipschitz box;
3. replacing the representative by the actual coupled coordinates costs
   more than the displayed diameter tax; or
4. the result silently replaces the actual response outputs by rounded ones.

