#!/usr/bin/env python3
"""Exact finite guard for the actual-Z minimum squeeze.

The guard deliberately uses partial domains that are not reflection closed.
It never evaluates P(-t).  It checks the abstract inequality consumed by v27:
  |s_k+t_k| <= delta,
  |P(t_{k+1})+P(s_k)| <= delta
=> at a minimum t_j,
  |P(t_j)+P(s_j)| <= delta + omega_P(2 delta).
"""
from fractions import Fraction as F
from itertools import product

# Several increasing partial graphs; domains deliberately not reflection closed.
cases = [
    ([F(-4,5),F(-1,2),F(-1,10),F(1,5),F(3,5),F(9,10)],
     lambda x: x + x*x*x/F(5)),
    ([F(-9,10),F(-3,5),F(-1,5),F(1,10),F(1,2),F(4,5)],
     lambda x: F(2,3)*x + x*x*x/F(7)),
]

def omega(D,P,h):
    out=F(0)
    for a in D:
        for b in D:
            if abs(a-b) <= h:
                out=max(out,abs(P[a]-P[b]))
    return out

checked=0
non_reflection_closed_witnesses=0
for D,fun in cases:
    P={x:fun(x) for x in D}
    assert all(P[D[i]] < P[D[i+1]] for i in range(len(D)-1))
    Dset=set(D)
    for delta in [F(1,20),F(1,10),F(1,5),F(2,5)]:
        om=omega(D,P,2*delta)
        # length 3 is enough to exercise incoming/outgoing cyclic indexing.
        for t in product(D, repeat=3):
            j=min(range(3), key=lambda k:t[k])
            for s in product(D, repeat=3):
                if any(abs(s[k]+t[k]) > delta for k in range(3)):
                    continue
                if any(abs(P[t[(k+1)%3]]+P[s[k]]) > delta for k in range(3)):
                    continue
                lhs=abs(P[t[j]]+P[s[j]])
                assert lhs <= delta+om, (D,delta,t,s,j,lhs,delta+om)
                checked += 1
                if -t[j] not in Dset:
                    non_reflection_closed_witnesses += 1

assert checked > 0
assert non_reflection_closed_witnesses > 0
print('PASS actual-Z projection minimum squeeze')
print('admissible cyclic configurations checked =',checked)
print('minimum nodes with -t_min outside dom(P) =',non_reflection_closed_witnesses)
