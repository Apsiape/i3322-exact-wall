#!/usr/bin/env python3
"""Exact endpoint receipts only.

Scope: verifies the rational identities and positive margins used for endpoint
atom exclusion. It does not verify Theorem (N), the limiting weld, or the
convex-envelope proof.
"""
from fractions import Fraction
import sympy as sp

Q = Fraction(250875388108398, 10**15)
r = Fraction(1, 10)
m_plus = r*((2-r)/(4*Q+2*r)-Fraction(3,2))
m_minus = r*(-Fraction(1,2)+(2-r)/(4*Q+6*r))
assert m_plus == Fraction(23686917837403,3008753881083980)
assert m_minus == Fraction(274562305945801,4008753881083980)
assert m_plus > 0 and m_minus > 0

q, rr, u = sp.symbols('q rr u', positive=True, real=True)
def d(x,y): return x*y+(x-y)/2-1
def b2(x): return (1-x*x)/4

Lp=q-d(1,u)
p0p=q-d(1,1-rr)
p1p=q-d(1-rr,u)-b2(1-rr)/p0p
assert sp.simplify(Lp-p1p-rr*((2-rr)/(4*q+2*rr)-(u+sp.Rational(1,2))))==0
Lm=q-d(-1,u)
p0m=q-d(-1,-1+rr)
p1m=q-d(-1+rr,u)-b2(-1+rr)/p0m
assert sp.simplify(Lm-p1m-rr*((u+sp.Rational(1,2))+(2-rr)/(4*q+6*rr)))==0
print('PASS: exact endpoint identities and margins only')
print('m_plus =',m_plus)
print('m_minus =',m_minus)
