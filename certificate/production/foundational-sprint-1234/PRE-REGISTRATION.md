# Pre-registration -- outer affine dominance

Write `m(x)=1/2-x` for the slope of `L_x`.

The sprint passes only if exact symbolic subtraction proves both identities

```text
[L_x(y)-L_x*(y)]-[L_x(1)-L_x*(1)]
  =(x-x_*)(1-y),                    x>=x_*, -1<=y<=1,

[L_x(y)-L_-x*(y)]-[L_x(-1)-L_-x*(-1)]
  =(-x_*-x)(y+1),                   x<=-x_*, -1<=y<=1.
```

It must also pass at least 100,000 exact-rational hostile fixtures spanning
both tails.  Any negative remainder kills the additive outer-tail step and
reopens the quantitative theorem.

Passing certifies only the affine subtraction.  It does not recertify the Arb
endpoint gap, strong concavity, response coercivity, or packet ownership.
