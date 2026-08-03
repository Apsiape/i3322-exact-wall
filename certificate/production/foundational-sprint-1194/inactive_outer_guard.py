#!/usr/bin/env python3
"""Certify that contacts beyond the active predecessor range cannot undercut."""

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
    spec = importlib.util.spec_from_file_location("s1194_engine", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expand(value: arb, radius: arb) -> arb:
    return arb(value.mid(), value.rad()+radius)


def main() -> None:
    engine = load_engine()
    ctx.prec = 300
    c_center = engine.decimal_fraction(
        "0.8782729451808124520614776394587039268823793661623032741245323669525"
    )
    c_box = engine.arb_fraction(c_center, Fraction(1, 10**20))
    c_dual = engine.Dual(c_box, (arb(0), arb(0)))
    q = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q, c_dual, 12)
    value_error, derivative_error = arb("3e-25"), arb("1e-20")

    root_center = arb("-0.003719358976358651")
    root_radius = arb("1e-14")
    root_box = arb(root_center.mid(), root_radius)
    inner_box = root_box/mu.value
    # A fixed superset of every [t_*,t_*/mu] interval allowed by the boxes.
    t_left = (root_center-root_radius).lower()
    t_right = inner_box.upper()

    def initial(t_box: arb):
        polynomial = engine.evaluate(series, engine.Dual(t_box, (arb(1), arb(0))))
        return [engine.Dual(
            expand(item.value, value_error),
            (expand(item.derivative[0], derivative_error), item.derivative[1]),
        ) for item in polynomial]

    tiles = 32768
    rows = []
    failures = []
    for tile in range(tiles):
        left = t_left+(t_right-t_left)*tile/tiles
        right = t_left+(t_right-t_left)*(tile+1)/tiles
        t_box = arb(((left+right)/2).mid(), (right-left).upper()/2)
        state = engine.step(initial(t_box), q)
        nxt = engine.step(state, q)
        predecessor = state[1]
        target = nxt[1]
        ratio = nxt[2]
        f_predecessor = (1-predecessor**2).sqrt()*ratio/2
        f_target = (
            q + 1 - predecessor/2 - (predecessor-engine.Dual.lift(arb(1)/2))*target
            - (1-predecessor**2)/(4*f_predecessor)
        )
        line_at_one = (
            q + engine.Dual.lift(arb(3)/2) - engine.Dual.lift(arb(3)/2)*target
            - (1-target**2)/(4*f_target)
        )
        fprime = engine.Dual.lift(arb(1)/2)-predecessor
        stationarity_target = (
            -engine.Dual.lift(arb(1)/2) + target/(2*f_target)
            + (1-target**2)*fprime/(4*f_target**2)
        )
        dx = target.derivative[0]
        dline = line_at_one.derivative[0]
        d_stationarity_target = stationarity_target.derivative[0]
        passed = (
            dx.upper() < 0 and d_stationarity_target.upper() < 0
            and f_target.value.lower() > 0
        )
        if not passed and len(failures) < 20:
            failures.append({
                "tile": tile,
                "target": str(target.value),
                "dx": str(dx),
                "d_line_at_one": str(dline),
                "d_stationarity_target": str(d_stationarity_target),
                "F_target": str(f_target.value),
            })
        rows.append((float(dx.upper()), float(dline.upper()), float(d_stationarity_target.upper()), float(f_target.value.lower()), passed))
    failure_count = sum(not row[4] for row in rows)
    output = {
        "status": "inactive outer-contact guard",
        "precision_bits": ctx.prec,
        "tiles": tiles,
        "largest_dx_upper": max(row[0] for row in rows),
        "largest_d_line_at_one_upper": max(row[1] for row in rows),
        "largest_d_stationarity_target_upper": max(row[2] for row in rows),
        "minimum_F_target_lower": min(row[3] for row in rows),
        "failure_count": failure_count,
        "first_failures": failures,
        "literal_strict_line_derivative_test": False,
        "successor_monotonicity_repair": failure_count == 0,
        "right_outer_contacts_excluded": failure_count == 0,
        "left_outer_contacts_excluded_by_reflection": failure_count == 0,
        "claim_boundary": (
            "On the complete inactive right tail, L_x(1) increases from its "
            "calibrated value at x_*. Slope ordering then gives L_x(y)>=F(y) "
            "for every y. Reflection supplies the left tail."
        ),
    }
    (HERE / "inactive-outer-guard.json").write_text(
        json.dumps(output, indent=2)+"\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
