#!/usr/bin/env python3
"""Certify the second branch of the exact wall manifold to the boundary."""

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
    spec = importlib.util.spec_from_file_location("s1193_engine", SOURCE)
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
    series, _ = engine.parameterization(q_dual, c_dual, 12)
    value_error = arb("3e-25")
    derivative_error = arb("1e-20")

    def state_at(t_value: arb, differentiate: bool):
        derivative = arb(1) if differentiate else arb(0)
        polynomial = engine.evaluate(series, engine.Dual(t_value, (derivative, arb(0))))
        return [engine.Dual(
            expand(item.value, value_error),
            (expand(item.derivative[0], derivative_error) if differentiate else arb(0), item.derivative[1]),
        ) for item in polynomial]

    center = arb("-0.003719358976358651")
    radius = arb("1e-14")
    left, right = center-radius, center+radius
    endpoint_residuals = []
    for label, point in (("more_negative", left), ("less_negative", right)):
        state = state_at(point, False)
        state = engine.step(engine.step(state, q_dual), q_dual)
        endpoint_residuals.append({"face": label, "residual": state[1].value-1})
    root_box = arb(center.mid(), radius)
    derivative_state = state_at(root_box, True)
    derivative_state = engine.step(engine.step(derivative_state, q_dual), q_dual)
    root_derivative = derivative_state[1].derivative[0]
    signs_opposite = (
        endpoint_residuals[0]["residual"].lower() > 0
        and endpoint_residuals[1]["residual"].upper() < 0
    )
    unique = signs_opposite and root_derivative.upper() < 0

    tiles = 32768
    records = []
    failures = []
    failure_count = 0
    # Certify a slight superset of the true segment, using the more-negative
    # bracket face. This avoids assuming the root's location inside its box.
    t_min = left
    for tile in range(tiles):
        a = t_min + (arb(0)-t_min)*tile/tiles
        b = t_min + (arb(0)-t_min)*(tile+1)/tiles
        t_box = arb(((a+b)/2).mid(), (b-a).upper()/2+a.rad()+b.rad())
        state = state_at(t_box, True)
        for iterate in range(2):
            nxt = engine.step(state, q_dual)
            dx, dy = state[1].derivative[0], nxt[1].derivative[0]
            pivot = (1-state[0].value**2).sqrt()*state[2].value/2
            passed = dx.upper() < 0 and dy.upper() < 0 and pivot.lower() > 0
            if not passed:
                failure_count += 1
                if len(failures) < 20:
                    failures.append({"tile": tile, "iterate": iterate, "dx": str(dx), "dy": str(dy), "pivot": str(pivot)})
            records.append((iterate, float(dx.upper()), float(dy.upper()), float(pivot.lower())))
            state = nxt
    pieces = []
    for iterate in range(2):
        rows = [row for row in records if row[0] == iterate]
        pieces.append({
            "iterate": iterate,
            "largest_dx_upper": max(row[1] for row in rows),
            "largest_dy_upper": max(row[2] for row in rows),
            "minimum_pivot_lower": min(row[3] for row in rows),
            "tiles_certified": sum(row[1] < 0 and row[2] < 0 and row[3] > 0 for row in rows),
        })

    terminal = state_at(center, False)
    terminal = engine.step(terminal, q_dual)
    terminal_x = terminal[1].value
    output = {
        "status": "exact boundary-wing certificate",
        "precision_bits": ctx.prec,
        "root_bracket": str(root_box),
        "endpoint_residuals": [{"face": row["face"], "residual": str(row["residual"])} for row in endpoint_residuals],
        "root_derivative": str(root_derivative),
        "existence_by_IVT": signs_opposite,
        "uniqueness_in_bracket": unique,
        "terminal_predecessor_interval": str(terminal_x),
        "tiles": tiles,
        "pieces": pieces,
        "failure_count": failure_count,
        "first_failures": failures,
        "complete_right_wing_graph": unique and failure_count == 0,
        "claim_boundary": (
            "The negative branch of the exact positive-plateau unstable manifold "
            "is a positive monotone graph ending at contact +1. Reflection gives "
            "the left wing. Bellman support-line closure is a separate theorem."
        ),
    }
    (HERE / "exact-boundary-wing.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
