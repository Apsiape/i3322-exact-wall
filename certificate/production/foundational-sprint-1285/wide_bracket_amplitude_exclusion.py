#!/usr/bin/env python3
"""Wide-bracket Arb exclusion of the global amplitude compatibility equation."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys

from flint import arb, ctx


HERE = Path(__file__).resolve().parent
FRONTIER = HERE.parent
ENGINE_PATH = (
    FRONTIER / "foundational-sprint-1116" / "validated_truncated_shooting.py"
)
T1 = "0.0015293272133344497"
T2_LEFT = "0.0015874649714962908"
T2_RIGHT = "0.001588503145749181"


def load_engine():
    spec = importlib.util.spec_from_file_location("s1285_engine", ENGINE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expand(value: arb, radius: arb) -> arb:
    return arb(value.mid(), value.rad() + radius)


def contains_zero(value: arb) -> bool:
    return bool(value.lower() <= 0 and value.upper() >= 0)


def row(value: arb) -> dict:
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
    derivative_error = arb("1e-20")

    def state_four(t_value: arb, differentiate: bool = False):
        polynomial = engine.evaluate(
            series,
            engine.Dual(
                t_value,
                (arb(1) if differentiate else arb(0), arb(0)),
            ),
        )
        state = [
            engine.Dual(
                expand(item.value, value_error),
                (
                    expand(item.derivative[0], derivative_error)
                    if differentiate
                    else arb(0),
                    arb(0),
                ),
            )
            for item in polynomial
        ]
        for _ in range(4):
            state = engine.step(state, q_dual)
        return state

    state1 = state_four(arb(T1))
    next1 = engine.step(state1, q_dual)
    y1 = state1[1].value
    v1 = next1[2].value

    left = arb(T2_LEFT)
    right = arb(T2_RIGHT)
    left_residual = state_four(left)[1].value + y1
    right_residual = state_four(right)[1].value + y1
    opposite_signs = bool(
        left_residual.lower() > 0 and right_residual.upper() < 0
    )

    radicand1 = 1 - y1 * y1
    reflected_source_amplitude = radicand1.sqrt() / (2 * v1)
    tiles = 256
    target_amplitudes = []
    differences = []
    tile_positivity = []
    tile_rows = []
    for index in range(tiles):
        tile_left = left + (right - left) * index / tiles
        tile_right = left + (right - left) * (index + 1) / tiles
        tile_box = arb(
            ((tile_left + tile_right) / 2).mid(),
            (tile_right - tile_left).upper() / 2,
        )
        center = arb(tile_box.mid())
        center_state = state_four(center)
        center_next = engine.step(center_state, q_dual)
        center_amplitude = (
            (1 - center_state[1].value * center_state[1].value).sqrt()
            * center_next[2].value
            / 2
        )
        derivative_state = state_four(tile_box, differentiate=True)
        derivative_next = engine.step(derivative_state, q_dual)
        derivative_amplitude = (
            (1 - derivative_state[1] * derivative_state[1]).sqrt()
            * derivative_next[2]
            / 2
        )
        radicand2 = 1 - derivative_state[1].value * derivative_state[1].value
        v2 = derivative_next[2].value
        positive = bool(radicand2.lower() > 0 and v2.lower() > 0)
        tile_positivity.append(positive)
        if not positive:
            continue
        mean_value_radius = (
            abs(derivative_amplitude.derivative[0]).upper()
            * (tile_right - tile_left).upper()
            / 2
        )
        target = arb(
            center_amplitude.mid(),
            center_amplitude.rad() + mean_value_radius,
        )
        difference = target - reflected_source_amplitude
        target_amplitudes.append(target)
        differences.append(difference)
        tile_rows.append({
            "tile": index,
            "t_box": str(tile_box),
            "derivative_bound": str(abs(derivative_amplitude.derivative[0]).upper()),
            "difference": str(difference),
        })

    target_lower = min(value.lower() for value in target_amplitudes)
    target_upper = max(value.upper() for value in target_amplitudes)
    difference_lower = min(value.lower() for value in differences)
    difference_upper = max(value.upper() for value in differences)
    original_target_amplitude = arb(
        ((target_lower + target_upper) / 2).mid(),
        (target_upper - target_lower) / 2,
    )
    difference = arb(
        ((difference_lower + difference_upper) / 2).mid(),
        (difference_upper - difference_lower) / 2,
    )
    lower_absolute_bound = (
        float(difference.lower())
        if difference.lower() > 0
        else -float(difference.upper())
        if difference.upper() < 0
        else 0.0
    )

    graph = json.loads(
        (
            FRONTIER
            / "foundational-sprint-1192"
            / "exact-invariant-graph-projection.json"
        ).read_text(encoding="utf-8")
    )
    monotonicity = bool(
        graph["all_tiles_certified"]
        and graph["pieces"][3]["largest_dy_upper"] < 0
    )
    positivity = bool(
        radicand1.lower() > 0
        and v1.lower() > 0
        and all(tile_positivity)
    )
    gates = {
        "exact_graph_monotonicity_loaded": monotonicity,
        "bracket_faces_have_strict_opposite_signs": opposite_signs,
        "all_radicands_and_denominators_positive": positivity,
        "wide_bracket_difference_excludes_zero_by_five_e_minus_five": (
            not contains_zero(difference) and lower_absolute_bound > 5e-5
        ),
    }
    report = {
        "status": "wide-bracket Arb amplitude exclusion",
        "precision_bits": ctx.prec,
        "c_box": str(c_box),
        "t1": T1,
        "complete_t2_bracket": [T2_LEFT, T2_RIGHT],
        "face_residuals": {
            "left": row(left_residual),
            "right": row(right_residual),
        },
        "subdivision_tiles": tiles,
        "first_tile": tile_rows[0],
        "last_tile": tile_rows[-1],
        "reflected_source_amplitude": row(reflected_source_amplitude),
        "original_target_amplitude_over_complete_bracket": row(
            original_target_amplitude
        ),
        "amplitude_difference_over_complete_bracket": row(difference),
        "amplitude_difference_lower_absolute_bound": lower_absolute_bound,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The unique matched-coordinate root in the certified monotone "
            "four-step chart has a nonzero reflected-source/global-target "
            "amplitude mismatch."
        ),
        "claim_boundary": (
            "This proves a normalization gap in the current aligned-wall "
            "certificate assembly. It does not determine whether the stated "
            "I3322 value can be recovered by a corrected normalization."
        ),
    }
    (HERE / "wide-bracket-amplitude-exclusion.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
