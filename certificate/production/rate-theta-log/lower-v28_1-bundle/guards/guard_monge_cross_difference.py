#!/usr/bin/env python3
"""Exact-rational guard for the v28 bilinear+separable Monge cross-difference."""
from fractions import Fraction as F


def phi(x,u):
    # Concrete separable representatives; C is large enough to keep phi >=0.
    C=F(100)
    FX=x*x + F(2)*x + F(1,7)
    FU=F(3)*u*u - u + F(2,9)
    return C-x*u-FX-FU

checks=0
vals=[F(k,7) for k in range(-6,7)]
for x in vals:
  for xp in vals:
    for u in vals:
      for up in vals:
        p=phi(x,u); pp=phi(xp,up); pc1=phi(x,up); pc2=phi(xp,u)
        assert p>=0 and pp>=0 and pc1>=0 and pc2>=0
        cross=p+pp-pc1-pc2
        prod=(x-xp)*(u-up)
        assert cross == -prod
        neg=max(F(0),-prod)
        assert neg <= p+pp
        checks+=1
print('PASS v28 bilinear+separable Monge guard')
print('  exact quadruples =',checks)
