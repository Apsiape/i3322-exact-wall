"""Exact development controls, not a proof of the analytic interfaces.

No source files or receipts are written. No asymptotic inference from tests.
"""
from fractions import Fraction as F
import sympy as s

# Physical response and its orientation, with nontrivial multiplicity mixing.
for m in range(1, 9):
    U = s.zeros(m)
    for j in range(m):
        U[(j + 1) % m, j] = (-1) ** j
    v = s.Matrix([s.Rational(j + 1, m + 1) for j in range(m)])
    r, b = s.Rational(2, 3), s.Rational(3, 10)
    z = s.zeros(m)
    W = b * z.row_join(U.T).col_join(U.row_join(z))
    A = s.diag(*([b*r]*m + [b/r]*m))
    Ap = s.diag(*([b/r]*m + [b*r]*m))
    X = s.diag(*([s.Rational(4, 5)]*m + [-s.Rational(4, 5)]*m))
    Q, T = A-W, Ap+W
    psi = v.col_join(r * U * v)
    assert W.T == W and W*X == -X*W
    assert W*W == b*b*s.eye(2*m)
    assert Q*T == s.zeros(2*m) and T*Q == s.zeros(2*m)
    assert Q*psi == s.zeros(2*m, 1)
    plus = (v.T*v)[0]
    minus = ((r*U*v).T*(r*U*v))[0]
    assert minus == r*r*plus
    assert minus != plus/(r*r)  # reciprocal orientation must fail
print('PASS response product, residual kernel, and ratio orientation at multiplicities 1..8')

# Symmetrizing measures does not require symmetrizing physical realizations.
pX, pU, fpX, fpU, R = s.symbols('pX pU fpX fpU R', nonzero=True)
q, p = (pU+fpX)/2, (pX+fpU)/2
rhs = (fpX-R*pX)/2 - R*(fpU-pU/R)/2
assert s.simplify(q-R*p-rhs) == 0
print('PASS reflection-swap marginal identity')

# Exact weighted boundary flux. A finite fixture is built from a positive
# sequence and couplings; the diagonal is chosen to satisfy the recurrence.
lam = [F(2), F(3), F(5), F(4), F(7), F(3), F(2)]
bonds = [F(1,5), F(3,10), F(1,4), F(2,5), F(1,3), F(1,5)]
S = F(5,4)
for lo in range(1, 6):
    for hi in range(lo, 6):
        mass = sum(lam[j]**2 for j in range(lo, hi+1))
        diag = {j:S-bonds[j-1]*lam[j-1]/lam[j]-bonds[j]*lam[j+1]/lam[j]
                for j in range(lo, hi+1)}
        energy = sum(diag[j]*lam[j]**2 for j in range(lo, hi+1))
        energy += 2*sum(bonds[j]*lam[j]*lam[j+1] for j in range(lo, hi))
        flux = bonds[lo-1]*lam[lo-1]*lam[lo] + bonds[hi]*lam[hi]*lam[hi+1]
        assert S*mass-energy == flux
        ratios = [lam[j+1]/lam[j] for j in range(len(lam)-1)]
        rmax = max(ratios + [1/r for r in ratios])
        b0 = min(bonds)
        assert lam[lo]**2+lam[hi]**2 <= rmax/b0*flux
print('PASS weighted flux and endpoint bound for all 15 retained intervals')

K0, coeff = F(8367827985, 100000000000), F(239010650,10000000)
assert coeff-2/K0 == F(23132161,334713119400000) > 0
print('PASS exact positive slack for eventual upper coefficient')
print('NOT VERIFIED: convex-envelope regularity, support trimming, orbit extraction, or the full dimension theorem')
