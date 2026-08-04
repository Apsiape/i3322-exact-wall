#!/usr/bin/env python3
"""Arb adjudication of one matched-coordinate amplitude mismatch."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys

from flint import arb, ctx


HERE = Path(__file__).resolve().parent
ENGINE_PATH = (
    HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"
)
T1 = "0.0015293272133344497"
T2_LEFT = "0.0015874649714962908"
T2_RIGHT = "0.001588503145749181"


def load_engine():
    spec = importlib.util.spec_from_file_location("s1284_engine", ENGINE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expand(value: arb, radius: arb) -> arb:
    return arb(value.mid(), value.rad() + radius)


def contains_zero(value: arb) -> bool:
    return bool(value.lower() <= 0 and value.upper() >= 0)


def interval_row(value: arb) -> dict:
    return {
        "interval": str(value),
        "lower": float(value.lower()),
        "upper": float(value.upper()),
        "width_upper_bound": float(2 * value.rad()),
        "contains_zero": contains_zero(value),
    }


def main() -> None:
    engine = load_engine()
    ctx.prec = 400
    c_center = engine.decimal_fraction(
        "0.8782729451808124520614776394587039268823793661623032741245323669525"
    )
    c_box = engine.arb_fraction(c_center, Fraction(1, 10**20))
    c_dual = engine.Dual(c_box, (arb(0), arb(0)))
    q_dual = engine.q_formula(c_dual)
    series, _ = engine.parameterization(q_dual, c_dual, 12)
    value_error = arb("3e-25")

    def state_four(t_value: arb):
        polynomial = engine.evaluate(
            series, engine.Dual(t_value, (arb(0), arb(0)))
        )
        state = [
            engine.Dual(
                expand(item.value, value_error),
                (arb(0), arb(0)),
            )
            for item in polynomial
        ]
        for _ in range(4):
            state = engine.step(state, q_dual)
        return state

    state1 = state_four(arb(T1))
    next1 = engine.step(state1, q_dual)
    x1, y1, u1 = (item.value for item in state1)
    v1 = next1[2].value

    def matching_residual(t_value: arb) -> arb:
        return state_four(t_value)[1].value + y1

    left = arb(T2_LEFT)
    right = arb(T2_RIGHT)
    left_residual = matching_residual(left)
    right_residual = matching_residual(right)
    initial_opposite_signs = bool(
        left_residual.lower() > 0 and right_residual.upper() < 0
    )

    bisection_steps = 0
    for _ in range(100):
        if float((right - left).upper()) < 5e-16:
            break
        midpoint = arb(((left + right) / 2).mid())
        residual = matching_residual(midpoint)
        if residual.lower() > 0:
            left = midpoint
        elif residual.upper() < 0:
            right = midpoint
        else:
            # The exact C-box uncertainty has reached the point residual.
            radius = (right - left).upper() / 4
            left = midpoint - radius
            right = midpoint + radius
            break
        bisection_steps += 1

    t2_box = arb(((left + right) / 2).mid(), (right - left).upper() / 2)
    state2 = state_four(t2_box)
    next2 = engine.step(state2, q_dual)
    y2 = state2[1].value
    v2 = next2[2].value
    coordinate_residual = y2 + y1

    sx1 = (1 - x1 * x1).sqrt()
    sy1 = (1 - y1 * y1).sqrt()
    source_value1 = sx1 * u1 / 2
    target_value1 = sy1 * v1 / 2
    raw_candidate1 = (
        q_dual.value
        + 1
        - x1 / 2
        - (x1 - arb("0.5")) * y1
        - (1 - x1 * x1) / (4 * source_value1)
    )
    raw_bellman_residual = raw_candidate1 - target_value1

    reflected_source_amplitude = sy1 / (2 * v1)
    original_target_amplitude = (1 - y2 * y2).sqrt() * v2 / 2
    amplitude_difference = original_target_amplitude - reflected_source_amplitude
    amplitude_lower_abs = (
        float(amplitude_difference.lower())
        if amplitude_difference.lower() > 0
        else -float(amplitude_difference.upper())
        if amplitude_difference.upper() < 0
        else 0.0
    )

    gates = {
        "initial_t2_faces_have_opposite_signs": initial_opposite_signs,
        "t2_bracket_width_below_one_e_minus_fifteen": (
            float(2 * t2_box.rad()) < 1e-15
        ),
        "final_coordinate_residual_contains_zero": contains_zero(
            coordinate_residual
        ),
        "raw_local_Bellman_equality_certified": (
            contains_zero(raw_bellman_residual)
            and float(2 * raw_bellman_residual.rad()) < 1e-15
        ),
        "amplitude_difference_excludes_zero_by_one_e_minus_four": (
            not contains_zero(amplitude_difference)
            and amplitude_lower_abs > 1e-4
        ),
    }
    report = {
        "status": "Arb matched-coordinate amplitude adjudication",
        "precision_bits": ctx.prec,
        "c_box": str(c_box),
        "t1": T1,
        "initial_t2_bracket": [T2_LEFT, T2_RIGHT],
        "initial_face_residuals": {
            "left": interval_row(left_residual),
            "right": interval_row(right_residual),
        },
        "bisection_steps": bisection_steps,
        "final_t2_box": interval_row(t2_box),
        "coordinate_residual": interval_row(coordinate_residual),
        "raw_local_Bellman_residual": interval_row(raw_bellman_residual),
        "reflected_source_amplitude": interval_row(reflected_source_amplitude),
        "original_target_amplitude": interval_row(original_target_amplitude),
        "amplitude_difference": interval_row(amplitude_difference),
        "amplitude_difference_lower_absolute_bound": amplitude_lower_abs,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "This certifies a normalization incompatibility in the current "
            "shooting-chart assembly. It identifies a proof-certificate gap; "
            "it does not by itself disprove the stated I3322 value."
        ),
    }
    (HERE / "arb-matched-amplitude-adjudication.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
