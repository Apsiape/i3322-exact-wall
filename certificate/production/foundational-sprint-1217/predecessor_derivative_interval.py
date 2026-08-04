#!/usr/bin/env python3
"""Arb certificate for the global active predecessor derivative box."""

from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

from flint import arb, ctx


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "foundational-sprint-1116" / "validated_truncated_shooting.py"


def load_engine():
    spec = importlib.util.spec_from_file_location("s1217_engine", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expand(value: arb, radius: arb) -> arb:
    return arb(value.mid(), value.rad() + radius)


def main() -> None:
    engine = load_engine()
    ctx.prec = 300
    c_center = engine.decimal_fraction(
        "0.8782729451808124520614776394587039268823793661623032741245323669525"
    )
    c_box = engine.arb_fraction(c_center, Fraction(1, 10**20))
    c_dual = engine.Dual(c_box, (arb(0), arb(0)))
    q_dual = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q_dual, c_dual, 12)
    value_error = arb("3e-25")
    derivative_error = arb("1e-20")
    lower_target = arb(1) / 10
    upper_target = arb(2)
    tiles = 32768

    smallest_lower = None
    largest_upper = None
    checks = 0
    failures = []
    upper_failure_count = 0

    def state_at(t_box: arb):
        polynomial = engine.evaluate(series, engine.Dual(t_box, (arb(1), arb(0))))
        return [
            engine.Dual(
                expand(item.value, value_error),
                (expand(item.derivative[0], derivative_error), item.derivative[1]),
            )
            for item in polynomial
        ]

    def check_ratio(dx: arb, dy: arb, chart: str, tile: int, iterate: int) -> None:
        nonlocal smallest_lower, largest_upper, checks, upper_failure_count
        passed_sign = dx.upper() < 0 and dy.upper() < 0
        if passed_sign:
            ratio = dx / dy
            passed = ratio.lower() > lower_target
            if ratio.upper() >= upper_target:
                upper_failure_count += 1
            lower = float(ratio.lower())
            upper = float(ratio.upper())
            smallest_lower = lower if smallest_lower is None else min(smallest_lower, lower)
            largest_upper = upper if largest_upper is None else max(largest_upper, upper)
        else:
            ratio = arb(0)
            passed = False
        if not passed and len(failures) < 20:
            failures.append(
                {
                    "chart": chart,
                    "tile": tile,
                    "iterate": iterate,
                    "dx": str(dx),
                    "dy": str(dy),
                    "ratio": str(ratio),
                }
            )
        checks += 1

    # Central local fundamental segment.
    t_hi = arb("0.0037582873342893243", "2e-19")
    t_lo = t_hi / mu.value
    for tile in range(tiles // 4):
        left = t_lo * tile / (tiles // 4)
        right = t_lo * (tile + 1) / (tiles // 4)
        t_box = arb(
            ((left + right) / 2).mid(),
            (right - left).upper() / 2 + left.rad() + right.rad(),
        )
        state = state_at(t_box)
        nxt = engine.step(state, q_dual)
        check_ratio(
            state[1].derivative[0], nxt[1].derivative[0], "central-local", tile, 0
        )

    # Four propagated central pieces up to the reflection section.
    for tile in range(tiles):
        left = t_lo + (t_hi - t_lo) * tile / tiles
        right = t_lo + (t_hi - t_lo) * (tile + 1) / tiles
        t_box = arb(
            ((left + right) / 2).mid(),
            (right - left).upper() / 2 + left.rad() + right.rad(),
        )
        state = state_at(t_box)
        for iterate in range(4):
            nxt = engine.step(state, q_dual)
            check_ratio(
                state[1].derivative[0],
                nxt[1].derivative[0],
                "central",
                tile,
                iterate,
            )
            state = nxt

    # Boundary wing from the validated more-negative root face to the plateau.
    wing_left = arb("-0.003719358976358651") - arb("1e-14")
    for tile in range(tiles):
        left = wing_left + (arb(0) - wing_left) * tile / tiles
        right = wing_left + (arb(0) - wing_left) * (tile + 1) / tiles
        t_box = arb(
            ((left + right) / 2).mid(),
            (right - left).upper() / 2 + left.rad() + right.rad(),
        )
        state = state_at(t_box)
        for iterate in range(2):
            nxt = engine.step(state, q_dual)
            check_ratio(
                state[1].derivative[0],
                nxt[1].derivative[0],
                "wing",
                tile,
                iterate,
            )
            state = nxt

    expected_checks = tiles // 4 + 4 * tiles + 2 * tiles
    report = {
        "status": "300-bit Arb predecessor-derivative interval certificate",
        "precision_bits": ctx.prec,
        "tiles_per_main_chart": tiles,
        "ratio_checks": checks,
        "registered_ratio_box": ["1/10", "2"],
        "smallest_ratio_lower": smallest_lower,
        "largest_ratio_upper": largest_upper,
        "registered_lower_bound_pass": (
            smallest_lower is not None and smallest_lower > 0.1
        ),
        "registered_upper_bound_pass": (
            upper_failure_count == 0
        ),
        "registered_predictions_passed": int(
            smallest_lower is not None and smallest_lower > 0.1
        ) + int(largest_upper is not None and largest_upper < 2.0),
        "registered_predictions_total": 2,
        "failure_count": len(failures),
        "upper_failure_count": upper_failure_count,
        "first_failures": failures,
        "all_gates_pass": (
            checks == expected_checks and not failures and upper_failure_count == 0
        ),
        "claim_boundary": (
            "This certifies the registered derivative box on the complete active "
            "predecessor chart with inherited analytic-tail enlargements. "
            "Reflection supplies the symmetric pieces. It does not price the "
            "inactive outer sliver."
        ),
    }
    (HERE / "predecessor-derivative-interval.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    assert report["all_gates_pass"]


if __name__ == "__main__":
    main()
