#!/usr/bin/env python3
"""Exact rational exercise of the v27 L6 local-error horn."""
from fractions import Fraction as F
checks=0
for sigma in [F(1,10),F(1,3),F(4,5),F(3,2)]:
    for Gamma in [F(1,100),F(1,10),F(1,2)]:
        for z0 in [F(1,7),F(1,2),F(5,4)]:
            for hmin in [F(1,10),F(1,4),F(1,2)]:
                z=Gamma*z0/F(2)
                threshold=sigma*hmin*Gamma*z0/F(4)
                for h in [hmin, hmin+F(1,10), hmin+F(1,2)]:
                    for frac in [F(0),F(1,4),F(3,4),F(1),F(5,4),F(2)]:
                        e=frac*threshold
                        if e >= threshold:
                            # direct-payment horn: e^2 is at least threshold^2
                            assert e*e >= threshold*threshold
                        else:
                            m=sigma*h*z-e
                            assert m >= threshold, (sigma,Gamma,z0,hmin,h,e,m,threshold)
                        checks+=1
print('PASS L6 local-error horn')
print('exact rational cases =',checks)
