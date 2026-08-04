#!/usr/bin/env python3
"""Certify a quadratic lower gap on the inactive predecessor tails."""

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
    spec = importlib.util.spec_from_file_location("s1232_engine", SOURCE)
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
    q = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q, c_dual, 12)
    value_error, derivative_error = arb("3e-25"), arb("1e-20")

    root_center = arb("-0.003719358976358651")
    root_radius = arb("1e-14")
    root_box = arb(root_center.mid(), root_radius)
    inner_box = root_box / mu.value
    t_left = (root_center - root_radius).lower()
    t_right = inner_box.upper()

    def initial(t_box: arb):
        polynomial = engine.evaluate(series, engine.Dual(t_box, (arb(1), arb(0))))
        return [
            engine.Dual(
                expand(item.value, value_error),
                (expand(item.derivative[0], derivative_error), item.derivative[1]),
            )
            for item in polynomial
        ]

    tiles = 32768
    target = arb(1) / 100
    smallest_lower = None
    largest_upper = None
    failures = []
    for tile in range(tiles):
        left = t_left + (t_right - t_left) * tile / tiles
        right = t_left + (t_right - t_left) * (tile + 1) / tiles
        t_box = arb(((left + right) / 2).mid(), (right - left).upper() / 2)
        state = engine.step(initial(t_box), q)
        nxt = engine.step(state, q)
        predecessor = state[1]
        x = nxt[1]
        ratio = nxt[2]
        f_predecessor = (1 - predecessor**2).sqrt() * ratio / 2
        f_x = (
            q
            + 1
            - predecessor / 2
            - (predecessor - engine.Dual.lift(arb(1) / 2)) * x
            - (1 - predecessor**2) / (4 * f_predecessor)
        )
        fprime = engine.Dual.lift(arb(1) / 2) - predecessor
        stationarity = (
            -engine.Dual.lift(arb(1) / 2)
            + x / (2 * f_x)
            + (1 - x**2) * fprime / (4 * f_x**2)
        )
        dx = x.derivative[0]
        ds = stationarity.derivative[0]
        passed_sign = dx.upper() < 0 and ds.upper() < 0
        quotient = ds / dx if passed_sign else arb(0)
        passed = passed_sign and quotient.lower() > target
        if passed_sign:
            lo = float(quotient.lower())
            hi = float(quotient.upper())
            smallest_lower = lo if smallest_lower is None else min(smallest_lower, lo)
            largest_upper = hi if largest_upper is None else max(largest_upper, hi)
        if not passed and len(failures) < 20:
            failures.append(
                {
                    "tile": tile,
                    "dx_dt": str(dx),
                    "dS_dt": str(ds),
                    "dS_dx": str(quotient),
                }
            )

    report = {
        "status": "300-bit Arb inactive-tail quadratic coercivity certificate",
        "precision_bits": ctx.prec,
        "tiles": tiles,
        "registered_dS_dx_lower": "1/100",
        "smallest_dS_dx_lower": smallest_lower,
        "largest_dS_dx_upper": largest_upper,
        "failure_count": len(failures),
        "first_failures": failures,
        "right_tail_pass": not failures and smallest_lower is not None,
        "left_tail_by_reflection": not failures and smallest_lower is not None,
        "all_gates_pass": not failures and smallest_lower is not None,
        "claim_boundary": (
            "This certifies dS/dx>1/100 on the complete inactive outer tail. "
            "Together with S(x_*)=1 it yields an endpoint support gap at least "
            "(x-x_*)^2/200. The Bellman-to-r_0 assembly is analytic and separate."
        ),
    }
    (HERE / "inactive-quadratic-interval.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    assert report["all_gates_pass"]


if __name__ == "__main__":
    main()

