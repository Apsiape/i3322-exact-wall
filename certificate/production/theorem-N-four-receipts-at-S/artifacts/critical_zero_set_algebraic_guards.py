#!/usr/bin/env python3
"""Critical-zero-set algebra guards only; not a theorem verifier."""
import sympy as sp
x,y=sp.symbols('x y', real=True)
def d(a,b): return a*b+(a-b)/2-1
def b2(a): return (1-a*a)/4
assert sp.expand(d(-y,-x)-d(x,y))==0
assert sp.expand(b2(-x)-b2(x))==0
p,r,delta,z=sp.symbols('p r delta z', positive=True)
M=sp.Matrix([[p,-z],[-z,r]])
assert sp.expand((p-delta)*(r-delta)-z**2)==sp.expand((M-delta*sp.eye(2)).det())
gx,gmx,gu,gmu,bx2,bu2=sp.symbols('gx gmx gu gmu bx2 bu2', positive=True)
px=bx2/gx; pmu=bu2/gmu; Kx=gx*gmx/bx2; Ku=gu*gmu/bu2
assert sp.simplify((px/gmx)/(gu/pmu)-1/(Kx*Ku))==0
x1,x2,u1,u2=sp.symbols('x1 x2 u1 u2', real=True)
cross=sp.expand(d(x1,u1)+d(x2,u2)-d(x1,u2)-d(x2,u1))
assert cross==sp.expand((x1-x2)*(u1-u2))
g,gminus,gplus,bb=sp.symbols('g gminus gplus bb', positive=True)
assert sp.simplify(-bb*(gplus-gminus)/g**2-bb*(gminus-gplus)/g**2)==0
print('PASS: zero-set algebraic identities only')
print('NOT VERIFIED: gluing construction, limiting passage, spectral support, operator closure')
