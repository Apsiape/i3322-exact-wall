#!/usr/bin/env python3
"""Validated graph-transform bound for the unstable-manifold tail.

The affine function space fixes P(0)=p and P'(0)=v. Differences therefore
vanish to second order. For

    T(P)(t) = F(P(t/mu)),

rescaling contributes mu^-2. If sup||DF||/mu^2 < 1, T is a contraction.
An Arb/Cauchy bound on T(P_12)-P_12 then encloses the exact analytic manifold.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

from flint import acb, arb, ctx


HERE = Path(__file__).resolve().parent


def load_engine():
    path = HERE / "validated_truncated_shooting.py"
    spec = importlib.util.spec_from_file_location("arb_tail_engine", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def upper(value: arb) -> arb:
    return value.upper()


def polynomial_value(coefficients, t):
    value = 0 * t
    for coefficient in reversed(coefficients):
        value = value * t + coefficient
    return value


def plain_step(state, q):
    x, y, u = state
    sx = (1 - x**2).sqrt()
    sy = (1 - y**2).sqrt()
    diagonal = x * y + (x - y) / 2 - 1
    v = 2 * (q - diagonal - sx / (2 * u)) / sy
    z = (((1 - 2 * x) + 2 * y * v / sy) / v**2 - 1) / 2
    return [y, z, v]


def matrix_inverse_3x3(matrix):
    """Exact interval inverse by Gauss-Jordan elimination."""
    augmented = [
        [acb(matrix[i][j]) for j in range(3)]
        + [acb(int(i == j)) for j in range(3)]
        for i in range(3)
    ]
    for column in range(3):
        pivot = augmented[column][column]
        assert not pivot.contains(0)
        augmented[column] = [entry / pivot for entry in augmented[column]]
        for row in range(3):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                a - factor * b
                for a, b in zip(augmented[row], augmented[column])
            ]
    return [row[3:] for row in augmented]


def matrix_product(left, right):
    return [
        [sum((left[i][k] * right[k][j] for k in range(3)), acb(0)) for j in range(3)]
        for i in range(3)
    ]


def matrix_vector(matrix, vector):
    return [
        sum((matrix[i][j] * vector[j] for j in range(3)), acb(0))
        for i in range(3)
    ]


def matrix_infinity_norm(matrix):
    return max(
        (upper(sum((abs(entry) for entry in row), arb(0))) for row in matrix),
        key=float,
    )


def main() -> None:
    engine = load_engine()
    ctx.prec = 400
    order = 12
    coefficient_cutoff = 50
    rho = arb("1/100")
    cauchy_radius = arb("1/20")
    safety_radius = arb("1/10000000000")

    c_center = engine.decimal_fraction(
        "0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091"
    )
    # This ball is deliberately much wider than the interval-Newton root box;
    # it provides room for the later boundary-degree argument.
    c_radius = Fraction(1, 10**18)
    c_value = engine.arb_fraction(c_center, c_radius)
    c = engine.Dual(c_value, (arb(0), arb(0)))
    q = engine.q_formula(c)
    parameterization, mu = engine.parameterization(q, c, order)

    # Fixed real eigenbasis at the centre of the certified C-ball.  This is
    # merely a coordinate choice defining an equivalent norm; it is not used
    # as an approximate eigenbasis assertion.  All subsequent matrix products
    # and the inverse are recomputed with Arb/Acb balls.
    basis_strings = [
        [
            "1",
            "1",
            "1",
        ],
        [
            "5.83798406533022158482568237501617269512858208455736275963785",
            "0.147375539213555872628282953358236113330701073427561536979537",
            "0.860376049548188400514725469785472410962351184877729869827388",
        ],
        [
            "2.559123472061512728620169469360829741294327898388433296495889",
            "2.559123472061512728620169469360829741294327898388433296495895",
            "6.783139954341418595474219959236725985824162002974276816065149",
        ],
    ]
    basis = [[acb(arb(value)) for value in row] for row in basis_strings]
    basis_inverse = matrix_inverse_3x3(basis)
    basis_norm = matrix_infinity_norm(basis)
    basis_inverse_norm = matrix_infinity_norm(basis_inverse)

    padded = []
    scaled = []
    for row in range(3):
        coefficients = [entry.value for entry in parameterization[row]]
        padded.append(
            [engine.Dual(value, (arb(0), arb(0))) for value in coefficients]
            + [engine.Dual.lift(0) for _ in range(coefficient_cutoff - order)]
        )
        scaled.append(
            [engine.Dual(coefficients[n] / mu.value**n, (arb(0), arb(0))) for n in range(order + 1)]
            + [engine.Dual.lift(0) for _ in range(coefficient_cutoff - order)]
        )

    image = engine.map_series(scaled, q)
    defect_coefficients = [
        [image[row][n].value - padded[row][n].value for n in range(coefficient_cutoff + 1)]
        for row in range(3)
    ]
    for row in range(3):
        for degree in range(order + 1):
            assert defect_coefficients[row][degree].contains(0)

    finite_tail = [arb(0), arb(0), arb(0)]
    for degree in range(order + 1, coefficient_cutoff + 1):
        transformed = matrix_vector(
            basis_inverse,
            [defect_coefficients[row][degree] for row in range(3)],
        )
        for row in range(3):
            finite_tail[row] += abs(transformed[row]) * rho**degree
    finite_tail = [upper(value) for value in finite_tail]
    """Original-coordinate diagnostic, not used in the proof.
    for row in range(3):
        total = arb(0)
        for degree in range(order + 1, coefficient_cutoff + 1):
            total += abs(defect_coefficients[row][degree]) * rho**degree
        finite_tail.append(upper(total))
    """

    # Cauchy remainder: evaluate the complete defect on a complex rectangle
    # containing |t|<=R, then bound every coefficient beyond the cutoff.
    t_disk = acb(arb(0, cauchy_radius), arb(0, cauchy_radius))
    p_coefficients = [[entry.value for entry in row] for row in parameterization]
    p_at_t = [polynomial_value(row, t_disk) for row in p_coefficients]
    p_at_scaled_t = [polynomial_value(row, t_disk / acb(mu.value)) for row in p_coefficients]
    cauchy_radicands = [1 - p_at_scaled_t[0] ** 2, 1 - p_at_scaled_t[1] ** 2]
    assert all(value.real.lower() > 0 for value in cauchy_radicands)
    assert abs(p_at_scaled_t[2]).lower() > 0
    cauchy_image = plain_step(p_at_scaled_t, acb(q.value))
    assert abs(cauchy_image[2]).lower() > 0
    complete_defect = [a - b for a, b in zip(cauchy_image, p_at_t)]
    ratio = rho / cauchy_radius
    cauchy_factor = ratio ** (coefficient_cutoff + 1) / (1 - ratio)
    transformed_complete_defect = matrix_vector(basis_inverse, complete_defect)
    cauchy_tail = [upper(abs(value) * cauchy_factor) for value in transformed_complete_defect]
    eta_coordinates = [upper(a + b) for a, b in zip(finite_tail, cauchy_tail)]
    eta = max(eta_coordinates, key=float)

    # Bound DF on a complex polydisc containing P_12(t/mu) and the future
    # correction.  The mu^-2 gain below is a Schwarz-lemma gain, so a real-only
    # enclosure would be invalid.  Tiling a slightly larger complex square
    # controls interval dependency while rigorously covering the disk.
    class TripleDual:
        def __init__(self, value, derivative=(acb(0), acb(0), acb(0))):
            self.value, self.derivative = value, derivative

        @staticmethod
        def lift(value):
            return value if isinstance(value, TripleDual) else TripleDual(acb(value))

        def __add__(self, other):
            other = self.lift(other)
            return TripleDual(self.value + other.value, tuple(a + b for a, b in zip(self.derivative, other.derivative)))

        __radd__ = __add__

        def __neg__(self):
            return TripleDual(-self.value, tuple(-x for x in self.derivative))

        def __sub__(self, other):
            return self + (-self.lift(other))

        def __rsub__(self, other):
            return self.lift(other) - self

        def __mul__(self, other):
            other = self.lift(other)
            return TripleDual(self.value * other.value, tuple(a * other.value + self.value * b for a, b in zip(self.derivative, other.derivative)))

        __rmul__ = __mul__

        def __truediv__(self, other):
            other = self.lift(other)
            return self * TripleDual(1 / other.value, tuple(-x / other.value**2 for x in other.derivative))

        def __rtruediv__(self, other):
            return self.lift(other) / self

        def __pow__(self, power):
            if power == 2:
                return self * self
            raise ValueError(power)

        def sqrt(self):
            value = self.value.sqrt()
            return TripleDual(value, tuple(x / (2 * value) for x in self.derivative))

    local_radius = rho / mu.value.lower()
    subdivision_radius = arb("1/500")
    assert local_radius < subdivision_radius
    subdivisions = 20
    half_width = Fraction(1, 500 * subdivisions)
    row_sums = [arb(0), arb(0), arb(0)]
    tiles_checked = 0
    analytic_real_margin = arb("1000")
    analytic_denominator_margin = arb("1000")
    for real_index in range(subdivisions):
        for imag_index in range(subdivisions):
            real_center = Fraction(2 * real_index + 1 - subdivisions, 500 * subdivisions)
            imag_center = Fraction(2 * imag_index + 1 - subdivisions, 500 * subdivisions)
            local_t = acb(
                engine.arb_fraction(real_center, half_width),
                engine.arb_fraction(imag_center, half_width),
            )
            local_state = [polynomial_value(row, local_t) for row in p_coefficients]
            expanded_state = [
                acb(
                    arb(value.real.mid(), value.real.rad() + safety_radius),
                    arb(value.imag.mid(), value.imag.rad() + safety_radius),
                )
                for value in local_state
            ]
            tile_radicands = [
                1 - expanded_state[0] ** 2,
                1 - expanded_state[1] ** 2,
            ]
            for radicand in tile_radicands:
                assert radicand.real.lower() > 0
                analytic_real_margin = min(
                    (analytic_real_margin, radicand.real.lower()), key=float
                )
            assert abs(expanded_state[2]).lower() > 0
            analytic_denominator_margin = min(
                (analytic_denominator_margin, abs(expanded_state[2]).lower()),
                key=float,
            )
            variables = [
                TripleDual(
                    expanded_state[axis],
                    tuple(acb(int(axis == j)) for j in range(3)),
                )
                for axis in range(3)
            ]
            dual_image = plain_step(variables, TripleDual(acb(q.value)))
            assert abs(dual_image[2].value).lower() > 0
            analytic_denominator_margin = min(
                (
                    analytic_denominator_margin,
                    abs(dual_image[2].value).lower(),
                ),
                key=float,
            )
            derivative_matrix = [list(entry.derivative) for entry in dual_image]
            adapted_derivative = matrix_product(
                matrix_product(basis_inverse, derivative_matrix), basis
            )
            tile_row_sums = [
                upper(sum((abs(value) for value in row), arb(0)))
                for row in adapted_derivative
            ]
            row_sums = [
                max((old, new), key=float)
                for old, new in zip(row_sums, tile_row_sums)
            ]
            tiles_checked += 1
    lipschitz = max(row_sums, key=float)
    mu_lower = mu.value.lower()
    contraction = upper(lipschitz / mu_lower**2)
    assert contraction < 1
    correction = upper(eta / (1 - contraction))
    original_manifold_correction = upper(basis_norm * correction)
    original_correction_after_rescaling = upper(
        basis_norm * correction / mu_lower**2
    )
    assert original_correction_after_rescaling < safety_radius

    result = {
        "status": "validated graph-transform enclosure of the exact local unstable manifold",
        "precision_bits": ctx.prec,
        "order": order,
        "coefficient_cutoff": coefficient_cutoff,
        "rho": str(rho),
        "cauchy_radius": str(cauchy_radius),
        "c_parameter_ball": str(c_value),
        "mu": str(mu.value),
        "finite_defect_tail": [str(value) for value in finite_tail],
        "cauchy_remainder": [str(value) for value in cauchy_tail],
        "eta_coordinates": [str(value) for value in eta_coordinates],
        "coordinate_norm": "infinity norm in the fixed displayed eigenbasis",
        "complex_square_radius": str(subdivision_radius),
        "complex_tiles_checked": tiles_checked,
        "analytic_radicand_real_margin": str(analytic_real_margin),
        "analytic_denominator_margin": str(analytic_denominator_margin),
        "basis_infinity_norm": str(basis_norm),
        "basis_inverse_infinity_norm": str(basis_inverse_norm),
        "lipschitz_row_sums": [str(value) for value in row_sums],
        "lipschitz_bound": str(lipschitz),
        "contraction_bound": str(contraction),
        "manifold_sup_correction": str(correction),
        "adapted_manifold_sup_correction": str(correction),
        "original_coordinate_manifold_sup_correction": str(
            original_manifold_correction
        ),
        "original_coordinate_correction_after_rescaling": str(
            original_correction_after_rescaling
        ),
        "claim_boundary": (
            "For every exact plateau parameter in the displayed C ball, an "
            "analytic unstable parameterization exists uniquely on |t|<=rho "
            "within the stated sup-norm correction of P_12. This does not by "
            "itself prove that the exact reflection residual has a zero."
        ),
    }
    (HERE / "analytic-tail-graph-transform.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
