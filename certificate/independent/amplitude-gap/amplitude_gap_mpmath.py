#!/usr/bin/env python3
"""Independent mpmath.iv reconstruction of the global amplitude gap."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import sys

from mpmath import iv


HERE = Path(__file__).resolve().parent
INDEPENDENT = HERE.parent
sys.path.insert(0, str(INDEPENDENT))

from iv_core import (  # noqa: E402
    Dual,
    I,
    contains_zero,
    endpoint_text,
    evaluate,
    expand,
    hi,
    hull,
    lo,
    parameterization,
    q_formula,
    step,
    upper_abs,
)


C_CENTER = Fraction(
    "0.8782729451808124520614776394587039268823793661623032741245323669525"
)
C_RADIUS = Fraction(1, 10**20)
T1 = Fraction("0.0015293272133344497")
T2_LEFT = Fraction("0.0015874649714962908")
T2_RIGHT = Fraction("0.001588503145749181")
TILES = 256


def interval_row(value) -> dict:
    return {
        "interval": endpoint_text(value),
        "lower": lo(value),
        "upper": hi(value),
        "contains_zero": contains_zero(value),
    }


def main() -> None:
    c_box = I(C_CENTER - C_RADIUS, C_CENTER + C_RADIUS)
    c_dual = Dual(c_box, (I(0), I(0)))
    q_dual = q_formula(c_dual)
    series, _ = parameterization(q_dual, c_dual, 12)
    value_error = I("3e-25")
    derivative_error = I("1e-20")

    def state_four(t_value, differentiate: bool = False):
        t_dual = Dual(
            t_value,
            (I(1) if differentiate else I(0), I(0)),
        )
        polynomial = evaluate(series, t_dual)
        state = [
            Dual(
                expand(item.value, value_error),
                (
                    expand(item.derivative[0], derivative_error)
                    if differentiate
                    else I(0),
                    I(0),
                ),
            )
            for item in polynomial
        ]
        for _ in range(4):
            state = step(state, q_dual)
        return state

    state1 = state_four(I(T1))
    next1 = step(state1, q_dual)
    y1 = state1[1].value
    v1 = next1[2].value
    radicand1 = I(1) - y1 * y1
    source_amplitude = iv.sqrt(radicand1) / (2 * v1)

    left_residual = state_four(I(T2_LEFT))[1].value + y1
    right_residual = state_four(I(T2_RIGHT))[1].value + y1

    target_intervals: list[object] = []
    difference_intervals: list[object] = []
    monotonicity_uppers: list[float] = []
    positivity: list[bool] = []
    tile_receipts: list[dict] = []

    for index in range(TILES):
        left = T2_LEFT + (T2_RIGHT - T2_LEFT) * index / TILES
        right = T2_LEFT + (T2_RIGHT - T2_LEFT) * (index + 1) / TILES
        center = (left + right) / 2
        half_width = (right - left) / 2

        center_state = state_four(I(center))
        center_next = step(center_state, q_dual)
        center_radicand = I(1) - center_state[1].value**2
        center_amplitude = iv.sqrt(center_radicand) * center_next[2].value / 2

        derivative_state = state_four(I(left, right), differentiate=True)
        derivative_next = step(derivative_state, q_dual)
        derivative_radicand = Dual.lift(I(1)) - derivative_state[1] ** 2
        derivative_amplitude = (
            derivative_radicand.sqrt() * derivative_next[2] / 2
        )
        local_radicand = I(1) - derivative_state[1].value**2
        local_v = derivative_next[2].value
        positive = lo(local_radicand) > 0 and lo(local_v) > 0
        positivity.append(positive)

        derivative_bound = upper_abs(derivative_amplitude.derivative[0])
        target = expand(center_amplitude, I(derivative_bound) * I(half_width))
        difference = target - source_amplitude
        target_intervals.append(target)
        difference_intervals.append(difference)
        monotonicity_uppers.append(hi(derivative_state[1].derivative[0]))
        if index in (0, TILES - 1):
            tile_receipts.append(
                {
                    "tile": index,
                    "t_interval": [str(left), str(right)],
                    "y_derivative_upper": monotonicity_uppers[-1],
                    "amplitude_derivative_bound": derivative_bound,
                    "difference_interval": endpoint_text(difference),
                }
            )

    target_interval = target_intervals[0]
    for value in target_intervals[1:]:
        target_interval = hull(target_interval, value)
    difference_interval = difference_intervals[0]
    for value in difference_intervals[1:]:
        difference_interval = hull(difference_interval, value)
    lower_bound = lo(difference_interval) if lo(difference_interval) > 0 else 0.0

    imports_production_engine = any(
        name == "flint" or "foundational-sprint" in name for name in sys.modules
    )
    gates = {
        "no_production_or_flint_import": not imports_production_engine,
        "complete_cover_strictly_decreasing": max(monotonicity_uppers) < 0,
        "faces_have_strict_opposite_signs": (
            lo(left_residual) > 0 and hi(right_residual) < 0
        ),
        "all_radicands_and_denominators_positive": (
            lo(radicand1) > 0 and lo(v1) > 0 and all(positivity)
        ),
        "complete_bracket_difference_above_one_e_minus_four": (
            not contains_zero(difference_interval) and lower_bound > 1e-4
        ),
    }
    report = {
        "status": "independent mpmath.iv global-amplitude-gap reconstruction",
        "backend": "mpmath.iv plus independently implemented iv_core map and series",
        "imports_production_engine": imports_production_engine,
        "c_interval": endpoint_text(c_box),
        "t1": str(T1),
        "complete_t2_bracket": [str(T2_LEFT), str(T2_RIGHT)],
        "subdivision_tiles": TILES,
        "face_residuals": {
            "left": interval_row(left_residual),
            "right": interval_row(right_residual),
        },
        "largest_y_derivative_upper": max(monotonicity_uppers),
        "reflected_source_amplitude": interval_row(source_amplitude),
        "original_target_amplitude_over_complete_bracket": interval_row(
            target_interval
        ),
        "amplitude_difference_over_complete_bracket": interval_row(
            difference_interval
        ),
        "amplitude_difference_lower_absolute_bound": lower_bound,
        "boundary_tile_receipts": tile_receipts,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The independently reconstructed unique coordinate-matched point "
            "has a nonzero reflected-source/global-target amplitude mismatch."
        ),
        "claim_boundary": (
            "This independently reconstructs the certificate gap; it does not "
            "determine the corrected I3322 optimum."
        ),
    }
    output = HERE / "amplitude-gap-mpmath.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
