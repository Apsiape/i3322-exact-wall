#!/usr/bin/env python3
"""Exact closure-logic guard for |index gap|>=2 => strict scalar gap > eta."""
from fractions import Fraction as F

checks=0
nearest=0
for N in range(3,402,2):
    M=(N-1)//2
    eta=F(2,N)
    a=[F(-1)+j*eta for j in range(N+1)]
    def incl(j):
        if j<M: return True,False   # [a_j,a_{j+1})
        if j==M: return True,True   # central closed
        return False,True           # (a_j,a_{j+1}]
    for p in range(N):
        for q in range(p+2,N):
            # geometric infimum between I_p and I_q
            gap=a[q]-a[p+1]
            assert gap>=eta
            if gap==eta:
                nearest+=1
                left_R=incl(p)[1]
                right_L=incl(q)[0]
                # equality would require both facing endpoints to be owned
                assert not (left_R and right_L), (N,p,q)
            else:
                assert gap>eta
            checks+=1
print('PASS v28 strict mixed-closure grid-transfer guard')
print('  cell pairs checked =',checks)
print('  nearest gap-2 closure cases =',nearest)
