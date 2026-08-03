#!/usr/bin/env python3
"""Interval certificate for the exact wall manifold's graph projection."""

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
    spec = importlib.util.spec_from_file_location("s1192_engine", SOURCE)
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
    t_center = engine.decimal_fraction(
        "0.0037582873342893242664459189962066910676629840186553796094448138632"
    )
    c_box = engine.arb_fraction(c_center, Fraction(1, 10**20))
    c_dual = engine.Dual(c_box, (arb(0), arb(0)))
    q_dual = engine.q_formula(c_dual)
    series, mu = engine.parameterization(q_dual, c_dual, 12)

    # This interval safely covers the certified t rectangle and the mu range.
    t_hi = arb("0.0037582873342893243", "2e-19")
    t_lo = t_hi / mu.value
    tiles = 32768
    value_error = arb("3e-25")
    # Cauchy from the graph-transform disk |t|<=0.01 gives <4e-23 in
    # original coordinates.  1e-20 is a deliberately loose rational cover.
    derivative_error = arb("1e-20")
    records = []
    failures = []
    failure_count = 0
    local_tiles = 8192

    # The local segment from the plateau t=0 to the first fundamental-domain
    # endpoint.  Invariance maps it into the first propagated piece.
    local_records = []
    for tile in range(local_tiles):
        left = t_lo * tile / local_tiles
        right = t_lo * (tile+1) / local_tiles
        t_box = arb(((left+right)/2).mid(), (right-left).upper()/2 + left.rad() + right.rad())
        polynomial = engine.evaluate(series, engine.Dual(t_box, (arb(1), arb(0))))
        state = [engine.Dual(
            expand(item.value, value_error),
            (expand(item.derivative[0], derivative_error), item.derivative[1]),
        ) for item in polynomial]
        nxt = engine.step(state, q_dual)
        dx, dy = state[1].derivative[0], nxt[1].derivative[0]
        pivot = (1-state[0].value**2).sqrt() * state[2].value / 2
        passed = dx.upper() < 0 and dy.upper() < 0 and pivot.lower() > 0
        if not passed:
            failure_count += 1
            if len(failures) < 20:
                failures.append({"tile": tile, "iterate": "local", "dx": str(dx), "dy": str(dy), "pivot": str(pivot)})
        local_records.append((float(dx.upper()), float(dy.upper()), float(pivot.lower())))
    for tile in range(tiles):
        left = t_lo + (t_hi-t_lo) * tile / tiles
        right = t_lo + (t_hi-t_lo) * (tile+1) / tiles
        t_box = arb(((left+right)/2).mid(), (right-left).upper()/2 + left.rad() + right.rad())
        t_dual = engine.Dual(t_box, (arb(1), arb(0)))
        polynomial = engine.evaluate(series, t_dual)
        state = []
        for item in polynomial:
            state.append(engine.Dual(
                expand(item.value, value_error),
                (expand(item.derivative[0], derivative_error), item.derivative[1]),
            ))
        # Four forward pieces reach the certified reflection section.  The
        # remaining half of the heteroclinic graph is its exact reversible
        # image; propagating forward beyond the section is the wrong chart.
        for iterate in range(4):
            nxt = engine.step(state, q_dual)
            dx = state[1].derivative[0]
            dy = nxt[1].derivative[0]
            sx = (1-state[0].value**2).sqrt()
            pivot = sx * state[2].value / 2
            passed = (
                dx.upper() < 0 and dy.upper() < 0 and pivot.lower() > 0
            )
            if not passed:
                failure_count += 1
                if len(failures) < 20:
                    failures.append({
                        "tile": tile,
                        "iterate": iterate,
                        "dx": str(dx),
                        "dy": str(dy),
                        "pivot": str(pivot),
                    })
            records.append((iterate, float(dx.upper()), float(dy.upper()), float(pivot.lower())))
            state = nxt
    pieces = []
    for iterate in range(4):
        rows = [row for row in records if row[0] == iterate]
        pieces.append({
            "iterate": iterate,
            "largest_dx_upper": max(row[1] for row in rows),
            "largest_dy_upper": max(row[2] for row in rows),
            "minimum_pivot_lower": min(row[3] for row in rows),
            "tiles_certified": sum(row[1] < 0 and row[2] < 0 and row[3] > 0 for row in rows),
        })
    output = {
        "status": "exact invariant-graph projection certificate",
        "precision_bits": ctx.prec,
        "tiles": tiles,
        "local_plateau_tiles": local_tiles,
        "local_plateau_piece": {
            "largest_dx_upper": max(row[0] for row in local_records),
            "largest_dy_upper": max(row[1] for row in local_records),
            "minimum_pivot_lower": min(row[2] for row in local_records),
            "tiles_certified": sum(row[0] < 0 and row[1] < 0 and row[2] > 0 for row in local_records),
        },
        "pieces": pieces,
        "failure_count": failure_count,
        "first_failures": failures,
        "all_tiles_certified": failure_count == 0,
        "literal_six_forward_piece_prediction": False,
        "corrected_plateau_to_section_plus_reflection": failure_count == 0,
        "claim_boundary": (
            "If all_tiles_certified is true, the exact unstable-manifold branch "
            "selected by the certified shooting rectangle projects as a positive "
            "single-valued monotone twist graph from the plateau through the "
            "reflection section; reversibility supplies the other half. The "
            "literal preregistered six-forward-piece formulation failed because "
            "it used the wrong chart beyond reflection. Global Bellman minimality "
            "is separate."
        ),
    }
    (HERE / "exact-invariant-graph-projection.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
