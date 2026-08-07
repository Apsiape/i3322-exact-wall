#!/usr/bin/env python3
from fractions import Fraction


def cells(N):
    assert N % 2 == 1 and N >= 3
    M=(N-1)//2
    eta=Fraction(2,N)
    a=[Fraction(-1)+j*eta for j in range(N+1)]
    # membership encoded directly to avoid floating endpoint ambiguity
    def idx(x):
        assert Fraction(-1) <= x <= Fraction(1)
        # central owns both its endpoints
        if a[M] <= x <= a[M+1]:
            return M
        if x < a[M]:
            for j in range(M):
                if a[j] <= x < a[j+1]:
                    return j
        else:
            for j in range(M+1,N):
                if a[j] < x <= a[j+1]:
                    return j
        raise AssertionError((N,x))
    return a,idx

checks=0
boundary_checks=0
for N in range(3,102,2):
    a,idx=cells(N)
    # every boundary and midpoint, plus quarter points in every cell
    pts=set(a)
    for j in range(N):
        lo,hi=a[j],a[j+1]
        pts.add((lo+hi)/2)
        pts.add((3*lo+hi)/4)
        pts.add((lo+3*hi)/4)
    for x in pts:
        j=idx(x)
        k=idx(-x)
        assert k == N-1-j, (N,x,j,k)
        checks += 1
        if x in a:
            boundary_checks += 1
    # exact coverage on a fine rational mesh and reflection projector-index law
    for q in range(0,20*N+1):
        x=Fraction(-1)+Fraction(q,10*N)
        j=idx(x)
        assert 0 <= j < N
        assert idx(-x)==N-1-j
        checks += 1

print('PASS reflection-equivariant boundary-atom partition')
print('checks =',checks)
print('exact boundary atoms checked =',boundary_checks)
