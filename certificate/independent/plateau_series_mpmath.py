#!/usr/bin/env python3
"""Independent exact/interval plateau and degree-12 invariance audit."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from iv_core import Dual, I, contains_zero, endpoint_text, hi, lo, map_series, parameterization, q_formula


HERE = Path(__file__).resolve().parent


def main() -> None:
    # Exact symbolic fixed-point identities, derived directly from the map.
    c = sp.symbols("c", real=True)
    s = sp.sqrt(1-c**2)
    r = s*(2*c-1)/((1-c)*(2*c+1))
    q = (4*c**4-5*c**2+2)/(4*c**2-1)
    diagonal = c**2-1
    v = sp.factor(2*(q-diagonal-s/(2*r))/s)
    z = sp.factor(((1-2*c)+2*c*v/s)/v**2/2-sp.Rational(1, 2))
    exact_fixed_residuals = [sp.simplify(v-r), sp.simplify(z-c)]
    exact_fixed = all(value == 0 for value in exact_fixed_residuals)

    center = Fraction("0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091")
    box = I(center-Fraction(1, 10**18), center+Fraction(1, 10**18))
    C = Dual(box, (I(0), I(0)))
    Q = q_formula(C)
    series, mu = parameterization(Q, C, 12)
    image = map_series(series, Q)
    invariance = []
    for row in range(3):
        for degree in range(13):
            target = series[row][degree]*mu**degree
            invariance.append(contains_zero(image[row][degree].value-target.value))

    aa = 4*C**3-3*C+1
    bb = 4*C**2*(1-4*C**2)
    dd = -4*C**3+3*C+1
    discriminant = (bb**2-4*aa*dd).sqrt()
    root_large = (-bb+discriminant)/(2*aa)
    root_middle = (-bb-discriminant)/(2*aa)
    root_small = dd/aa
    multipliers = [root_large.value, root_middle.value, root_small.value]
    hyperbolic = lo(multipliers[0]) > 1 and all(lo(value) > 0 and hi(value) < 1 for value in multipliers[1:])

    result = {
        "status": "independent exact plateau and degree-12 invariance audit",
        "backend": "SymPy exact algebra plus mpmath.iv",
        "imports_production_engine": False,
        "exact_fixed_point_residuals": [str(value) for value in exact_fixed_residuals],
        "exact_fixed_point": exact_fixed,
        "c_interval": endpoint_text(box),
        "q_interval": endpoint_text(Q.value),
        "multiplier_intervals": [[lo(value), hi(value)] for value in multipliers],
        "one_unstable_two_stable": hyperbolic,
        "degree_12_coefficient_checks": len(invariance),
        "degree_12_invariance": all(invariance),
        "all_gates_pass": exact_fixed and hyperbolic and all(invariance) and lo(Q.value) > 0.25,
    }
    (HERE/"plateau-series-mpmath.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert result["all_gates_pass"]


if __name__ == "__main__":
    main()
