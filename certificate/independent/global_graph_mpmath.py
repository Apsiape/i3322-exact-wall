#!/usr/bin/env python3
"""Independent central, wing, and exterior interval covers."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from iv_core import Dual, I, evaluate, expand, hi, hull, iv, lo, parameterization, q_formula, step


HERE = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-tiles", type=int, default=8192)
    parser.add_argument("--central-tiles", type=int, default=32768)
    parser.add_argument("--other-tiles", type=int, default=4096)
    args = parser.parse_args()
    local_tiles, central_tiles, other_tiles = args.local_tiles, args.central_tiles, args.other_tiles

    c_center = Fraction("0.87827294518081245206147763945870392688237936616230327412453236695251283590175466345779517416027083617482033185091")
    c_radius = Fraction(1, 10**20)
    c_box = I(c_center-c_radius, c_center+c_radius)
    c_dual = Dual(c_box, (I(0), I(0)))
    q = q_formula(c_dual)
    series, mu = parameterization(q, c_dual, 12)
    value_error, derivative_error = I("3e-25"), I("1e-20")

    def state_at(t_box, differentiate=True):
        derivative = I(1) if differentiate else I(0)
        polynomial = evaluate(series, Dual(t_box, (derivative, I(0))))
        return [Dual(
            expand(item.value, value_error),
            (expand(item.derivative[0], derivative_error) if differentiate else I(0), item.derivative[1]),
        ) for item in polynomial]

    def graph_predicate(state):
        nxt = step(state, q)
        dx, dy = state[1].derivative[0], nxt[1].derivative[0]
        pivot = iv.sqrt(1-state[0].value**2)*state[2].value/2
        passed = hi(dx) < 0 and hi(dy) < 0 and lo(pivot) > 0
        return nxt, passed, (hi(dx), hi(dy), lo(pivot))

    # Central positive branch. Superset endpoints avoid dependence on a
    # particular interval midpoint/radius representation.
    t_hi_box = I(Fraction("0.0037582873342893243")-Fraction(2, 10**19), Fraction("0.0037582873342893243")+Fraction(2, 10**19))
    t_lo_box = t_hi_box/mu.value
    local_extrema = [float("-inf"), float("-inf"), float("inf")]
    central_extrema = [[float("-inf"), float("-inf"), float("inf")] for _ in range(4)]
    failures = []
    for tile in range(local_tiles):
        a, b = t_lo_box*tile/local_tiles, t_lo_box*(tile+1)/local_tiles
        _, passed, values = graph_predicate(state_at(hull(a, b)))
        local_extrema = [max(local_extrema[0], values[0]), max(local_extrema[1], values[1]), min(local_extrema[2], values[2])]
        if not passed and len(failures) < 20:
            failures.append({"region": "local", "tile": tile, "values": values})
    for tile in range(central_tiles):
        a = t_lo_box+(t_hi_box-t_lo_box)*tile/central_tiles
        b = t_lo_box+(t_hi_box-t_lo_box)*(tile+1)/central_tiles
        state = state_at(hull(a, b))
        for iterate in range(4):
            state, passed, values = graph_predicate(state)
            record = central_extrema[iterate]
            central_extrema[iterate] = [max(record[0], values[0]), max(record[1], values[1]), min(record[2], values[2])]
            if not passed and len(failures) < 20:
                failures.append({"region": "central", "tile": tile, "iterate": iterate, "values": values})
    central_pass = not failures

    # Negative branch and endpoint root.
    root_center, root_radius = Fraction("-0.003719358976358651"), Fraction(1, 10**14)
    root_left, root_right = root_center-root_radius, root_center+root_radius
    endpoints = []
    for point in (root_left, root_right):
        state = state_at(I(point), False)
        state = step(step(state, q), q)
        endpoints.append(state[1].value-1)
    derivative_state = state_at(I(root_left, root_right), True)
    derivative_state = step(step(derivative_state, q), q)
    root_derivative = derivative_state[1].derivative[0]
    root_pass = lo(endpoints[0]) > 0 and hi(endpoints[1]) < 0 and hi(root_derivative) < 0

    wing_extrema = [[float("-inf"), float("-inf"), float("inf")] for _ in range(2)]
    wing_failures = []
    for tile in range(other_tiles):
        a = root_left*Fraction(other_tiles-tile, other_tiles)
        b = root_left*Fraction(other_tiles-tile-1, other_tiles)
        state = state_at(I(a, b))
        for iterate in range(2):
            state, passed, values = graph_predicate(state)
            record = wing_extrema[iterate]
            wing_extrema[iterate] = [max(record[0], values[0]), max(record[1], values[1]), min(record[2], values[2])]
            if not passed and len(wing_failures) < 20:
                wing_failures.append({"tile": tile, "iterate": iterate, "values": values})
    terminal = step(state_at(I(root_center), False), q)[1].value
    wing_pass = root_pass and not wing_failures

    # Inactive outer predecessor guard.
    inner_box = I(root_left, root_right)/mu.value
    outer_left, outer_right = I(root_left), inner_box
    outer_extrema = [float("-inf"), float("-inf"), float("-inf"), float("inf")]
    outer_failures = []
    for tile in range(other_tiles):
        a = outer_left+(outer_right-outer_left)*tile/other_tiles
        b = outer_left+(outer_right-outer_left)*(tile+1)/other_tiles
        state = step(state_at(hull(a, b)), q)
        nxt = step(state, q)
        predecessor, target, ratio = state[1], nxt[1], nxt[2]
        f_predecessor = (1-predecessor**2).sqrt()*ratio/2
        f_target = q+1-predecessor/2-(predecessor-Dual.lift(I(1)/2))*target-(1-predecessor**2)/(4*f_predecessor)
        line_at_one = q+Dual.lift(I(3)/2)-Dual.lift(I(3)/2)*target-(1-target**2)/(4*f_target)
        fprime = Dual.lift(I(1)/2)-predecessor
        stationarity = -Dual.lift(I(1)/2)+target/(2*f_target)+(1-target**2)*fprime/(4*f_target**2)
        values = (hi(target.derivative[0]), hi(line_at_one.derivative[0]), hi(stationarity.derivative[0]), lo(f_target.value))
        passed = values[0] < 0 and values[2] < 0 and values[3] > 0
        outer_extrema = [max(outer_extrema[0], values[0]), max(outer_extrema[1], values[1]), max(outer_extrema[2], values[2]), min(outer_extrema[3], values[3])]
        if not passed and len(outer_failures) < 20:
            outer_failures.append({"tile": tile, "values": values})
    outer_pass = not outer_failures

    result = {
        "status": "independent mpmath global Bellman graph reconstruction",
        "backend": "mpmath.iv; no production imports",
        "tiles": {"local": local_tiles, "central_per_piece": central_tiles, "wing_per_piece": other_tiles, "exterior": other_tiles},
        "central": {
            "local_extrema_dx_dy_pivot": local_extrema,
            "four_piece_extrema_dx_dy_pivot": central_extrema,
            "failure_count": len(failures),
            "all_gates_pass": central_pass,
        },
        "boundary_wing": {
            "endpoint_residual_intervals": [[lo(value), hi(value)] for value in endpoints],
            "root_derivative_interval": [lo(root_derivative), hi(root_derivative)],
            "two_piece_extrema_dx_dy_pivot": wing_extrema,
            "terminal_predecessor_interval": [lo(terminal), hi(terminal)],
            "failure_count": len(wing_failures),
            "all_gates_pass": wing_pass,
        },
        "inactive_exterior": {
            "extrema_dx_dline_dstationarity_minF": outer_extrema,
            "failure_count": len(outer_failures),
            "all_gates_pass": outer_pass,
        },
        "all_gates_pass": central_pass and wing_pass and outer_pass,
        "first_failures": failures+wing_failures+outer_failures,
        "claim_boundary": "Independent full-domain real interval covers; reflection supplies the opposite central/wing/exterior halves.",
    }
    (HERE/"global-graph-mpmath.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    assert result["all_gates_pass"]


if __name__ == "__main__":
    main()
