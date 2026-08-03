#!/usr/bin/env python3
"""Independent Miranda certificate for the exact I3322 shooting zero."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from iv_core import Dual, I, contains_zero, endpoint_text, evaluate, expand, hi, lo, parameterization, q_formula, shooting, step


HERE = Path(__file__).resolve().parent


def inverse2(matrix):
    determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    assert not contains_zero(determinant)
    return [[matrix[1][1]/determinant, -matrix[0][1]/determinant], [-matrix[1][0]/determinant, matrix[0][0]/determinant]]


def matvec(matrix, vector):
    return [sum((matrix[i][j]*vector[j] for j in range(2)), I(0)) for i in range(2)]


def polynomial_state(c, t):
    c_dual = Dual(c, (I(0), I(0)))
    q_dual = q_formula(c_dual)
    series, _ = parameterization(q_dual, c_dual, 12)
    state = evaluate(series, Dual(t, (I(0), I(0))))
    return [entry.value for entry in state], q_dual.value


def truncated_residual(c, t):
    c_dual = Dual(c, (I(0), I(0)))
    residual = shooting(q_formula(c_dual), Dual(t, (I(0), I(0))), c_dual, 12, 3)
    return [entry.value for entry in residual]


def propagate_once(state, errors, q):
    hull = [expand(value, error) for value, error in zip(state, errors)]
    variables = [Dual(hull[axis], tuple(I(int(axis == column)) for column in range(3))) for axis in range(3)]
    image = step(variables, Dual(q, (I(0), I(0), I(0))))
    jacobian = [list(entry.derivative) for entry in image]
    next_errors = [sum((abs(jacobian[i][j])*errors[j] for j in range(3)), I(0)) for i in range(3)]
    point_state = [Dual(value, (I(0), I(0))) for value in state]
    point_image = step(point_state, Dual(q, (I(0), I(0))))
    return [entry.value for entry in point_image], next_errors, jacobian


def main() -> None:
    c_center = Fraction("0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091")
    t_center = Fraction("0.0037582873342893242664459189962066910676629840186553796094448138632075256300327923349823554459797969788641666991575")
    c_radius = t_radius = Fraction(1, 10**20)

    c_point, t_point = I(c_center), I(t_center)
    c_dual = Dual(c_point, (I(1), I(0)))
    t_dual = Dual(t_point, (I(0), I(1)))
    central = shooting(q_formula(c_dual), t_dual, c_dual, 12, 3)
    jacobian = [[central[i].derivative[j] for j in range(2)] for i in range(2)]
    inverse = inverse2(jacobian)

    c_box = I(c_center-c_radius, c_center+c_radius)
    t_box = I(t_center-t_radius, t_center+t_radius)
    state, q = polynomial_state(c_box, t_box)
    errors = [I("3e-25") for _ in range(3)]
    propagation = []
    states, histories = [], []
    for index in range(5):
        state, errors, local_jacobian = propagate_once(state, errors, q)
        states.append(state)
        histories.append(errors)
        propagation.append({
            "step": index+1,
            "coordinate_error_uppers": [hi(value) for value in errors],
            "jacobian_abs_row_sum_uppers": [sum(hi(abs(x)) for x in row) for row in local_jacobian],
        })
    crossing, after = states[3], states[4]
    crossing_errors, after_errors = histories[3], histories[4]
    inverse_lipschitz = hi(abs(1/expand(crossing[2], crossing_errors[2])**2))
    residual_error = [
        I(hi(crossing_errors[0])+hi(crossing_errors[1])),
        I(hi(after_errors[2])+inverse_lipschitz*hi(crossing_errors[2])),
    ]
    preconditioned_error = [sum((abs(inverse[i][j])*residual_error[j] for j in range(2)), I(0)) for i in range(2)]

    c_rect = Dual(c_box, (I(1), I(0)))
    t_rect = Dual(t_box, (I(0), I(1)))
    rect = shooting(q_formula(c_rect), t_rect, c_rect, 12, 3)
    rect_jacobian = [[rect[i].derivative[j] for j in range(2)] for i in range(2)]
    transformed_jacobian = [[sum((inverse[i][k]*rect_jacobian[k][j] for k in range(2)), I(0)) for j in range(2)] for i in range(2)]

    centers, radii = [c_center, t_center], [c_radius, t_radius]
    faces, all_pass = [], True
    for axis in range(2):
        for sign in (-1, 1):
            coordinates = [I(value) for value in centers]
            coordinates[axis] = I(centers[axis]+sign*radii[axis])
            residual = truncated_residual(coordinates[0], coordinates[1])
            transformed_point = matvec(inverse, residual)
            other = 1-axis
            mean_radius = hi(abs(transformed_jacobian[axis][other])*I(radii[other]))
            transformed = expand(transformed_point[axis], I(mean_radius))
            passed = hi(transformed) < -hi(preconditioned_error[axis]) if sign < 0 else lo(transformed) > hi(preconditioned_error[axis])
            all_pass = all_pass and passed
            faces.append({
                "axis": "C" if axis == 0 else "t",
                "face": "lower" if sign < 0 else "upper",
                "transformed_interval": [lo(transformed), hi(transformed)],
                "mean_value_cross_radius": mean_radius,
                "tail_error_allowance_upper": hi(preconditioned_error[axis]),
                "opposite_sign_certified": passed,
            })

    q_box = q_formula(Dual(c_box, (I(0), I(0)))).value
    result = {
        "status": "independent mpmath Miranda shooting certificate",
        "backend": "mpmath.iv; no production imports",
        "rectangle": {
            "C": endpoint_text(c_box),
            "t": endpoint_text(t_box),
            "Q": endpoint_text(q_box),
        },
        "initial_manifold_error": 3e-25,
        "propagation": propagation,
        "residual_error_uppers": [hi(value) for value in residual_error],
        "preconditioned_error_uppers": [hi(value) for value in preconditioned_error],
        "face_checks": faces,
        "miranda_conditions": all_pass,
        "all_gates_pass": all_pass and lo(q_box) > 0.25,
        "claim_boundary": "Existence of an exact shooting zero conditional only on the independently reconstructed analytic-tail allowance.",
    }
    (HERE/"shooting-miranda-mpmath.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert result["all_gates_pass"]


if __name__ == "__main__":
    main()
