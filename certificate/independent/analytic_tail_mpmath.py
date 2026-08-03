#!/usr/bin/env python3
"""Independent complex graph-transform certificate using mpmath intervals."""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from iv_core import (
    CRect,
    Dual,
    I,
    complex_step,
    contains_zero,
    expand,
    hi,
    iv,
    lo,
    map_series,
    parameterization,
    polynomial_value,
    q_formula,
)


HERE = Path(__file__).resolve().parent


def cabs(value: CRect):
    return value.abs()


def cinverse3(matrix):
    augmented = [
        [CRect.lift(matrix[i][j]) for j in range(3)]
        + [CRect.lift(int(i == j)) for j in range(3)]
        for i in range(3)
    ]
    for column in range(3):
        pivot = augmented[column][column]
        assert not (contains_zero(pivot.re) and contains_zero(pivot.im))
        augmented[column] = [entry/pivot for entry in augmented[column]]
        for row in range(3):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [a-factor*b for a, b in zip(augmented[row], augmented[column])]
    return [row[3:] for row in augmented]


def cmatmul(left, right):
    return [[sum((left[i][k]*right[k][j] for k in range(3)), CRect.lift(0)) for j in range(3)] for i in range(3)]


def cmatvec(matrix, vector):
    return [sum((matrix[i][j]*vector[j] for j in range(3)), CRect.lift(0)) for i in range(3)]


def matrix_inf_upper(matrix):
    return max(sum(hi(cabs(entry)) for entry in row) for row in matrix)


@dataclass
class CDual:
    value: CRect
    derivative: tuple

    @staticmethod
    def lift(value):
        if isinstance(value, CDual):
            return value
        return CDual(CRect.lift(value), tuple(CRect.lift(0) for _ in range(3)))

    def __add__(self, other):
        other = CDual.lift(other)
        return CDual(self.value+other.value, tuple(a+b for a, b in zip(self.derivative, other.derivative)))

    __radd__ = __add__

    def __neg__(self):
        return CDual(-self.value, tuple(-x for x in self.derivative))

    def __sub__(self, other):
        return self+(-CDual.lift(other))

    def __rsub__(self, other):
        return CDual.lift(other)-self

    def __mul__(self, other):
        other = CDual.lift(other)
        return CDual(self.value*other.value, tuple(a*other.value+self.value*b for a, b in zip(self.derivative, other.derivative)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = CDual.lift(other)
        inverse = other.value.reciprocal()
        return self*CDual(inverse, tuple(-x/(other.value**2) for x in other.derivative))

    def __rtruediv__(self, other):
        return CDual.lift(other)/self

    def __pow__(self, power: int):
        if power != 2:
            raise ValueError(power)
        return self*self

    def sqrt(self):
        value = self.value.sqrt()
        return CDual(value, tuple(x/(2*value) for x in self.derivative))


def main() -> None:
    order, cutoff = 12, 50
    rho, cauchy_radius, safety = I(Fraction(1, 100)), I(Fraction(1, 20)), I(Fraction(1, 10_000_000_000))
    c_center = Fraction("0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091")
    c_value = I(c_center-Fraction(1, 10**18), c_center+Fraction(1, 10**18))
    c = Dual(c_value, (I(0), I(0)))
    q = q_formula(c)
    series, mu = parameterization(q, c, order)

    basis_text = [
        ["1", "1", "1"],
        ["5.83798406533022158482568237501617269512858208455736275963785", "0.147375539213555872628282953358236113330701073427561536979537", "0.860376049548188400514725469785472410962351184877729869827388"],
        ["2.559123472061512728620169469360829741294327898388433296495889", "2.559123472061512728620169469360829741294327898388433296495895", "6.783139954341418595474219959236725985824162002974276816065149"],
    ]
    basis = [[CRect(I(value), I(0)) for value in row] for row in basis_text]
    basis_inverse = cinverse3(basis)
    basis_norm = matrix_inf_upper(basis)
    basis_inverse_norm = matrix_inf_upper(basis_inverse)

    padded, scaled = [], []
    for row in range(3):
        coefficients = [entry.value for entry in series[row]]
        padded.append([Dual(value, (I(0), I(0))) for value in coefficients]+[Dual.lift(0) for _ in range(cutoff-order)])
        scaled.append([Dual(coefficients[n]/mu.value**n, (I(0), I(0))) for n in range(order+1)]+[Dual.lift(0) for _ in range(cutoff-order)])
    image = map_series(scaled, q)
    defects = [[image[row][n].value-padded[row][n].value for n in range(cutoff+1)] for row in range(3)]
    low_degree_zero = all(contains_zero(defects[row][degree]) for row in range(3) for degree in range(order+1))
    assert low_degree_zero

    finite_tail = [I(0), I(0), I(0)]
    for degree in range(order+1, cutoff+1):
        transformed = cmatvec(basis_inverse, [CRect(defects[row][degree], I(0)) for row in range(3)])
        for row in range(3):
            finite_tail[row] += cabs(transformed[row])*rho**degree

    # Complete defect on the complex square containing |t| <= 1/20.
    t_disk = CRect(I(-Fraction(1, 20), Fraction(1, 20)), I(-Fraction(1, 20), Fraction(1, 20)))
    coeffs = [[CRect(entry.value, I(0)) for entry in row] for row in series]
    p_t = [polynomial_value(row, t_disk) for row in coeffs]
    p_scaled = [polynomial_value(row, t_disk/CRect(mu.value, I(0))) for row in coeffs]
    cauchy_radicands = [1-p_scaled[0]**2, 1-p_scaled[1]**2]
    assert all(value.re.a > 0 for value in cauchy_radicands)
    assert p_scaled[2].abs().a > 0
    complete_image = complex_step(p_scaled, CRect(q.value, I(0)))
    assert complete_image[2].abs().a > 0
    complete_defect = [a-b for a, b in zip(complete_image, p_t)]
    ratio = rho/cauchy_radius
    cauchy_factor = ratio**(cutoff+1)/(1-ratio)
    transformed_complete = cmatvec(basis_inverse, complete_defect)
    cauchy_tail = [cabs(value)*cauchy_factor for value in transformed_complete]
    eta_coordinates = [a+b for a, b in zip(finite_tail, cauchy_tail)]
    eta_upper = max(hi(value) for value in eta_coordinates)

    subdivisions = 20
    half_width = Fraction(1, 500*subdivisions)
    row_upper = [0.0, 0.0, 0.0]
    analytic_real_margin = float("inf")
    analytic_denominator_margin = float("inf")
    tiles = 0
    for ri in range(subdivisions):
        for ii in range(subdivisions):
            rc = Fraction(2*ri+1-subdivisions, 500*subdivisions)
            ic = Fraction(2*ii+1-subdivisions, 500*subdivisions)
            t = CRect(I(rc-half_width, rc+half_width), I(ic-half_width, ic+half_width))
            local = [polynomial_value(row, t) for row in coeffs]
            local = [CRect(expand(value.re, safety), expand(value.im, safety)) for value in local]
            radicands = [1-local[0]**2, 1-local[1]**2]
            for radicand in radicands:
                assert radicand.re.a > 0
                analytic_real_margin = min(analytic_real_margin, lo(radicand.re))
            analytic_denominator_margin = min(analytic_denominator_margin, lo(local[2].abs()))
            variables = [CDual(local[axis], tuple(CRect.lift(int(axis == j)) for j in range(3))) for axis in range(3)]
            dual_image = complex_step(variables, CDual.lift(CRect(q.value, I(0))))
            analytic_denominator_margin = min(analytic_denominator_margin, lo(dual_image[2].value.abs()))
            derivative = [list(entry.derivative) for entry in dual_image]
            adapted = cmatmul(cmatmul(basis_inverse, derivative), basis)
            for row in range(3):
                row_upper[row] = max(row_upper[row], sum(hi(cabs(value)) for value in adapted[row]))
            tiles += 1

    lipschitz = max(row_upper)
    mu_lower = lo(mu.value)
    contraction = lipschitz/mu_lower**2
    correction = eta_upper/(1-contraction)
    original_correction = basis_norm*correction
    rescaled_correction = original_correction/mu_lower**2
    passed = (
        low_degree_zero and tiles == 400 and analytic_real_margin > 0
        and analytic_denominator_margin > 0 and contraction < 1
        and original_correction < 3e-25 and rescaled_correction < 1e-10
    )
    result = {
        "status": "independent mpmath complex graph-transform reconstruction",
        "backend": "mpmath.iv plus local rectangular-complex arithmetic",
        "imports_production_engine": False,
        "order": order,
        "coefficient_cutoff": cutoff,
        "low_degree_invariance_contains_zero": low_degree_zero,
        "complex_tiles_checked": tiles,
        "analytic_radicand_real_margin": analytic_real_margin,
        "analytic_denominator_margin": analytic_denominator_margin,
        "basis_infinity_norm_upper": basis_norm,
        "basis_inverse_infinity_norm_upper": basis_inverse_norm,
        "lipschitz_row_sums_upper": row_upper,
        "contraction_upper": contraction,
        "eta_coordinate_uppers": [hi(value) for value in eta_coordinates],
        "adapted_correction_upper": correction,
        "original_coordinate_correction_upper": original_correction,
        "rescaled_original_correction_upper": rescaled_correction,
        "all_gates_pass": passed,
        "claim_boundary": "Independent analytic-tail reconstruction only; shooting and global graph are separate gates.",
    }
    (HERE/"analytic-tail-mpmath.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert passed


if __name__ == "__main__":
    main()
