#!/usr/bin/env python3
"""Miranda-degree certificate for a zero of the exact shooting residual.

The local graph-transform certificate supplies a uniform C0 enclosure of the
exact unstable parameterization around the degree-12 polynomial.  This script
propagates that enclosure through the five finite map steps with interval
Jacobian bounds, preconditions the two reflection residuals, and verifies the
opposite-face signs required by Miranda's theorem.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx


HERE = Path(__file__).resolve().parent


def load_engine():
    path = HERE / "validated_truncated_shooting.py"
    spec = importlib.util.spec_from_file_location("exact_degree_engine", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class TripleDual:
    def __init__(self, value, derivative=(arb(0), arb(0), arb(0))):
        self.value = value
        self.derivative = derivative

    @staticmethod
    def lift(value):
        return value if isinstance(value, TripleDual) else TripleDual(arb(value))

    def __add__(self, other):
        other = self.lift(other)
        return TripleDual(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.derivative, other.derivative)),
        )

    __radd__ = __add__

    def __neg__(self):
        return TripleDual(-self.value, tuple(-x for x in self.derivative))

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        return TripleDual(
            self.value * other.value,
            tuple(
                a * other.value + self.value * b
                for a, b in zip(self.derivative, other.derivative)
            ),
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return self * TripleDual(
            1 / other.value,
            tuple(-x / other.value**2 for x in other.derivative),
        )

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __pow__(self, power):
        if power != 2:
            raise ValueError(power)
        return self * self

    def sqrt(self):
        value = self.value.sqrt()
        return TripleDual(
            value, tuple(x / (2 * value) for x in self.derivative)
        )


def step(state, q):
    x, y, u = state
    sx = (1 - x**2).sqrt()
    sy = (1 - y**2).sqrt()
    diagonal = x * y + (x - y) / 2 - 1
    v = 2 * (q - diagonal - sx / (2 * u)) / sy
    z = (((1 - 2 * x) + 2 * y * v / sy) / v**2 - 1) / 2
    return [y, z, v]


def expand(value: arb, radius: arb) -> arb:
    return arb(value.mid(), value.rad() + radius)


def propagate_once(state, errors, q):
    hull = [expand(value, error) for value, error in zip(state, errors)]
    variables = [
        TripleDual(
            hull[axis], tuple(arb(int(axis == column)) for column in range(3))
        )
        for axis in range(3)
    ]
    image = step(variables, TripleDual(q))
    jacobian = [list(entry.derivative) for entry in image]
    next_errors = [
        sum((abs(jacobian[i][j]) * errors[j] for j in range(3)), arb(0)).upper()
        for i in range(3)
    ]
    return step(state, q), next_errors, jacobian


def polynomial_state(engine, c, t, order=12):
    c_dual = engine.Dual(c, (arb(0), arb(0)))
    q_dual = engine.q_formula(c_dual)
    series, _ = engine.parameterization(q_dual, c_dual, order)
    state = engine.evaluate(series, engine.Dual(t, (arb(0), arb(0))))
    return [entry.value for entry in state], q_dual.value


def truncated_residual(engine, c, t):
    c_dual = engine.Dual(c, (arb(0), arb(0)))
    q_dual = engine.q_formula(c_dual)
    residual = engine.shooting(
        q_dual, engine.Dual(t, (arb(0), arb(0))), c_dual, 12, 3
    )
    return [entry.value for entry in residual]


def matvec(matrix, vector):
    return [
        sum((matrix[i][j] * vector[j] for j in range(2)), arb(0))
        for i in range(2)
    ]


def main() -> None:
    engine = load_engine()
    ctx.prec = 400
    c_center = engine.decimal_fraction(
        "0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091"
    )
    t_center = engine.decimal_fraction(
        "0.0037582873342893242664459189962066910676629840186553796094448138632075256300327923349823554459797969788641666991575"
    )
    # Wide compared with both interval-Newton images, narrow compared with the
    # graph-transform C-ball (radius 1e-18).
    c_radius = Fraction(1, 10**20)
    t_radius = Fraction(1, 10**20)

    # Central preconditioner for the truncated residual.
    c_point = engine.arb_fraction(c_center)
    t_point = engine.arb_fraction(t_center)
    c_dual = engine.Dual(c_point, (arb(1), arb(0)))
    t_dual = engine.Dual(t_point, (arb(0), arb(1)))
    central = engine.shooting(engine.q_formula(c_dual), t_dual, c_dual, 12, 3)
    jacobian = [[central[i].derivative[j] for j in range(2)] for i in range(2)]
    inverse = engine.interval_inverse_2x2(jacobian)

    # Uniform tail propagation over the whole rectangle.  The initial 3e-25
    # is a rational outward rounding of ||S||_inf * 2.132e-26 from the graph
    # transform certificate.
    c_box = engine.arb_fraction(c_center, c_radius)
    t_box = engine.arb_fraction(t_center, t_radius)
    state, q = polynomial_state(engine, c_box, t_box)
    errors = [arb("3e-25"), arb("3e-25"), arb("3e-25")]
    propagation = []
    states = []
    error_history = []
    for index in range(5):
        state, errors, local_jacobian = propagate_once(state, errors, q)
        states.append(state)
        error_history.append(errors)
        propagation.append(
            {
                "step": index + 1,
                "coordinate_error": [str(value) for value in errors],
                "jacobian_abs_row_sums": [
                    str(sum((abs(x) for x in row), arb(0)).upper())
                    for row in local_jacobian
                ],
            }
        )
    crossing, after = states[3], states[4]
    crossing_errors, after_errors = error_history[3], error_history[4]
    inverse_lipschitz = abs(
        1 / expand(crossing[2], crossing_errors[2]) ** 2
    ).upper()
    residual_error = [
        (crossing_errors[0] + crossing_errors[1]).upper(),
        (after_errors[2] + inverse_lipschitz * crossing_errors[2]).upper(),
    ]
    preconditioned_error = [
        sum((abs(inverse[i][j]) * residual_error[j] for j in range(2)), arb(0)).upper()
        for i in range(2)
    ]

    # One interval Jacobian over the rectangle, transformed by the fixed
    # inverse.  Face evaluation below uses a mean-value enclosure so the
    # cancellation in M*J is retained instead of lost to direct interval
    # evaluation through five iterates.
    c_rect_dual = engine.Dual(c_box, (arb(1), arb(0)))
    t_rect_dual = engine.Dual(t_box, (arb(0), arb(1)))
    rect_residual = engine.shooting(
        engine.q_formula(c_rect_dual), t_rect_dual, c_rect_dual, 12, 3
    )
    rect_jacobian = [
        [rect_residual[i].derivative[j] for j in range(2)] for i in range(2)
    ]
    transformed_jacobian = [
        [
            sum((inverse[i][k] * rect_jacobian[k][j] for k in range(2)), arb(0))
            for j in range(2)
        ]
        for i in range(2)
    ]

    face_checks = []
    all_pass = True
    centers = [c_center, t_center]
    radii = [c_radius, t_radius]
    for axis in range(2):
        for sign in (-1, 1):
            coordinates = [engine.arb_fraction(value) for value in centers]
            coordinates[axis] = engine.arb_fraction(
                centers[axis] + sign * radii[axis]
            )
            residual = truncated_residual(engine, coordinates[0], coordinates[1])
            transformed_point = matvec(inverse, residual)
            other = 1 - axis
            mean_value_radius = (
                abs(transformed_jacobian[axis][other])
                * engine.arb_fraction(radii[other])
            ).upper()
            transformed = list(transformed_point)
            transformed[axis] = arb(
                transformed_point[axis].mid(),
                transformed_point[axis].rad() + mean_value_radius,
            )
            if sign < 0:
                passed = transformed[axis].upper() < -preconditioned_error[axis]
            else:
                passed = transformed[axis].lower() > preconditioned_error[axis]
            all_pass = all_pass and bool(passed)
            face_checks.append(
                {
                    "axis": "C" if axis == 0 else "t",
                    "face": "lower" if sign < 0 else "upper",
                    "preconditioned_truncated_residual": str(transformed[axis]),
                    "mean_value_cross_radius": str(mean_value_radius),
                    "tail_error_allowance": str(preconditioned_error[axis]),
                    "opposite_sign_certified": bool(passed),
                }
            )
    if not all_pass:
        print("residual_error", [str(value) for value in residual_error])
        print("preconditioned_error", [str(value) for value in preconditioned_error])
        print(json.dumps(face_checks, indent=2))
    assert all_pass

    q_box = engine.q_formula(engine.Dual(c_box, (arb(0), arb(0)))).value
    result = {
        "status": "Miranda-degree existence certificate for an exact shooting zero",
        "precision_bits": ctx.prec,
        "rectangle": {"C": str(c_box), "t": str(t_box), "Q": str(q_box)},
        "initial_manifold_error_coordinate_bound": "3e-25",
        "propagation": propagation,
        "exact_residual_error_bound": [str(value) for value in residual_error],
        "preconditioned_error_bound": [str(value) for value in preconditioned_error],
        "face_checks": face_checks,
        "miranda_conditions": all_pass,
        "claim_boundary": (
            "This proves existence, not uniqueness, of a zero of the exact "
            "reflection shooting residual in the displayed rectangle, conditional "
            "only on the separately emitted graph-transform enclosure. It does not "
            "prove global optimality of the resulting I3322 realization."
        ),
    }
    (HERE / "validated-exact-shooting-degree.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
