#!/usr/bin/env python3
"""Finite guard for v28 raw-cell parity decomposition and corrected sparse bound."""
from fractions import Fraction
import random

def far_inversion(e1,e2):
    p,q=e1; p2,q2=e2
    return (p-p2)*(q-q2)<0 and abs(p-p2)>=2 and abs(q-q2)>=2

def no_far(E):
    E=list(E)
    return all(not far_inversion(E[i],E[j]) for i in range(len(E)) for j in range(i+1,len(E)))

def monotone(E):
    E=list(E)
    for i,(p,q) in enumerate(E):
        for p2,q2 in E[i+1:]:
            if p<p2 and q>q2: return False
            if p2<p and q2>q: return False
    return True

def check_support(m,n,E):
    assert no_far(E)
    nonempty=0
    for rp in (0,1):
        for cp in (0,1):
            sub={(p,q) for p,q in E if p%2==rp and q%2==cp}
            assert monotone(sub)
            rows={p for p,q in sub}; cols={q for p,q in sub}
            if sub:
                nonempty+=1
                assert len(sub) <= len(rows)+len(cols)-1
    if E:
        assert nonempty>=1
        assert len(E) <= 2*m+2*n-nonempty
    else:
        assert len(E)==0

# Explicit negative control for the dropped v27 display 2m+2n-4.
E={(0,0)}
assert len(E) > 2*1+2*1-4
check_support(1,1,E)

exhaustive=0
sharp={}
for m in range(1,5):
    for n in range(1,5):
        edges=[(i,j) for i in range(m) for j in range(n)]
        maxe=0
        for mask in range(1<<len(edges)):
            E={edges[k] for k in range(len(edges)) if (mask>>k)&1}
            if not no_far(E): continue
            check_support(m,n,E)
            maxe=max(maxe,len(E)); exhaustive+=1
        sharp[f'{m}x{n}']=maxe

rng=random.Random(280806)
random_checks=0
for _ in range(50000):
    m=rng.randint(2,10); n=rng.randint(2,10)
    cand=[(i,j) for i in range(m) for j in range(n)]
    rng.shuffle(cand); E=set()
    for e in cand:
        if rng.random()<0.45 and all(not far_inversion(e,f) for f in E): E.add(e)
    check_support(m,n,E); random_checks+=1

# scale only: conservative 128*r bound, now with I<=2 epsilon (even stronger).
scale=0
for k in range(1,1001):
    r=Fraction(k,1000)
    target=Fraction(2,1)/r
    N=(target.numerator+target.denominator-1)//target.denominator
    if N%2==0: N+=1
    eta=Fraction(2,N)
    assert Fraction(1,2)*r < eta <= r
    # 8*sqrt(2)*r^4/eta^3 < 128*r; square the rational inequality.
    lhs_sq=128*r**8/eta**6  # (8 sqrt2)^2 =128
    rhs_sq=(128*r)**2
    assert lhs_sq < rhs_sq
    scale+=1
print(f'PASS v28 raw-cell/grid guard: exhaustive_supports={exhaustive}, random={random_checks}, scale={scale}')
print('  sparse 1x1 negative control exercised')
print('  sharp maxima:',sharp)
