#!/usr/bin/env python3
"""Non-load-bearing algebraic smoke tests for Theorem (S)."""
import sympy as sp

x,u,rho,bx,bu,S = sp.symbols("x u rho bx bu S", positive=True, real=True)

# Two-reflection product consistency.
ra, ram, rb, rbm = sp.symbols("ra ram rb rbm", positive=True)
assert sp.simplify((ra*ram).subs(ram,1/ra)-1) == 0
assert sp.simplify((rb*rbm).subs(rbm,1/rb)-1) == 0
assert sp.simplify((ra*rb).subs(rb,1/ra)-1) == 0

# Jacobi recurrence from one-step ratio and Bellman equality.
bp,gp,b0,g0,d0 = sp.symbols("bp gp b0 g0 d0", positive=True)
lam_prev_over = bp/gp
lam_next_over = g0/b0
jac = d0 + bp*lam_prev_over + b0*lam_next_over
assert sp.simplify(jac - (d0 + bp**2/gp + g0)) == 0

# Fixed-sector reciprocal Bellman sums used by the quarter elimination.
forward = rho*(bx+bu)
reverse = (bx+bu)/rho
assert sp.simplify(forward*reverse - (bx+bu)**2) == 0

# Positive transport block polynomial relation t(t-d)=0 has roots 0,d.
t,d = sp.symbols("t d", real=True)
poly = sp.factor(t*(t-d))
assert poly == t*(t-d)

print("PASS: strengthened algebraic smoke tests")
print("SCOPE: no measure-theoretic or infinite-dimensional step is certified")
