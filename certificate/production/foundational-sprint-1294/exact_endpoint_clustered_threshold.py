#!/usr/bin/env python3
"""Exact threshold certificate for the preregistered nonuniform Bellman grid."""

from __future__ import annotations

from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRODUCTION = HERE.parent
CANDIDATE = HERE / "endpoint-clustered-candidate.json"
LOWER_REPORT = PRODUCTION / "foundational-sprint-1292/exact-dimension-255-lower-bound.json"
SCALE = 10**15
SEARCH_LOW = 250_875_380_000_000
SEARCH_HIGH = 250_875_500_000_000


def upper_hull(
    grid: list[Fraction], values: list[Fraction]
) -> tuple[list[int], list[Fraction | None]]:
    offsets = [value - point / 2 for point, value in zip(grid, values)]
    owners: list[int] = []
    starts: list[Fraction | None] = []
    for candidate in range(len(grid)):
        crossing: Fraction | None = None
        while owners:
            prior = owners[-1]
            crossing = (offsets[prior] - offsets[candidate]) / (
                grid[candidate] - grid[prior]
            )
            prior_start = starts[-1]
            if prior_start is None or crossing > prior_start:
                break
            owners.pop()
            starts.pop()
        if not owners:
            crossing = None
        owners.append(candidate)
        starts.append(crossing)
    return owners, starts


def poly_value(poly: tuple[Fraction, Fraction, Fraction], x: Fraction) -> Fraction:
    a, b, c = poly
    return (a * x + b) * x + c


def poly_minimum(
    poly: tuple[Fraction, Fraction, Fraction], left: Fraction, right: Fraction
) -> tuple[Fraction, Fraction]:
    options = [(poly_value(poly, left), left), (poly_value(poly, right), right)]
    a, b, _ = poly
    if a > 0:
        vertex = -b / (2 * a)
        if left <= vertex <= right:
            options.append((poly_value(poly, vertex), vertex))
    return min(options, key=lambda item: (item[0], item[1]))


def build_cells(
    grid: list[Fraction], values: list[Fraction]
) -> tuple[list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]], int]:
    owners, starts = upper_hull(grid, values)
    finite_starts = [x for x in starts if x is not None and -1 < x < 1]
    points = sorted(set(grid + finite_starts))
    hull_starts = [x for x in starts[1:] if x is not None]
    cells = []
    for left, right in zip(points, points[1:]):
        if left == right:
            continue
        midpoint = (left + right) / 2
        segment = min(len(grid) - 2, max(0, bisect_right(grid, midpoint) - 1))
        x0, x1 = grid[segment], grid[segment + 1]
        f0, f1 = values[segment], values[segment + 1]
        a = (f1 - f0) / (x1 - x0)
        b = f0 - a * x0
        owner = owners[bisect_right(hull_starts, midpoint)]
        m = grid[owner]
        c = values[owner] - m / 2
        cells.append((left, right, a, b, m, c, segment, owner))
    return cells, len(owners)


def check(
    q: Fraction,
    cells: list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]],
) -> tuple[bool, Fraction, dict[str, object]]:
    worst: Fraction | None = None
    receipt: dict[str, object] | None = None
    for left, right, a, b, m, c, segment, owner in cells:
        alpha = q + 1 - c
        beta = -Fraction(1, 2) - m
        poly = (
            4 * a * beta + 1,
            4 * (a * alpha + b * beta),
            4 * b * alpha - 1,
        )
        minimum, minimizer = poly_minimum(poly, left, right)
        if worst is None or minimum < worst:
            worst = minimum
            receipt = {
                "interval": [str(left), str(right)],
                "F_segment": segment,
                "envelope_owner": owner,
                "owner_coordinate": str(m),
                "minimizer": str(minimizer),
                "quadratic_coefficients": [str(entry) for entry in poly],
                "minimum_numerator": str(minimum),
            }
    assert worst is not None and receipt is not None
    return worst >= 0, worst, receipt


def main() -> None:
    raw = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    grid_text = raw["grid_decimal"]
    knot_text = raw["knots_decimal"]
    grid = [Fraction(value) for value in grid_text]
    values = [Fraction(value) for value in knot_text]
    digest = hashlib.sha256(
        ("\n".join(grid_text) + "\n--\n" + "\n".join(knot_text)).encode("ascii")
    ).hexdigest()
    cells, retained = build_cells(grid, values)

    low, high = SEARCH_LOW, SEARCH_HIGH
    low_ok, _, _ = check(Fraction(low, SCALE), cells)
    high_ok, _, _ = check(Fraction(high, SCALE), cells)
    if low_ok or not high_ok:
        raise RuntimeError("registered search bracket does not straddle threshold")
    evaluations = 2
    while low + 1 < high:
        middle = (low + high) // 2
        passed, _, _ = check(Fraction(middle, SCALE), cells)
        evaluations += 1
        if passed:
            high = middle
        else:
            low = middle
    q_pass = Fraction(high, SCALE)
    q_fail = Fraction(low, SCALE)
    pass_ok, pass_minimum, pass_receipt = check(q_pass, cells)
    fail_ok, fail_minimum, fail_receipt = check(q_fail, cells)
    evaluations += 2

    lower = Fraction(json.loads(LOWER_REPORT.read_text(encoding="utf-8"))["certified_value_lower"])
    window = q_pass - lower
    owner_coordinate = Fraction(pass_receipt["owner_coordinate"])
    minimizer = Fraction(pass_receipt["minimizer"])
    registered_region = (
        Fraction(-91, 100) <= minimizer <= Fraction(-87, 100)
        and owner_coordinate < Fraction(-98, 100)
    )
    symmetry = all(grid[i] == -grid[-1 - i] for i in range(len(grid)))
    certificate_gates = {
        "candidate_search_converged": raw["iterations"] < raw["maximum_iterations"] and raw["final_delta"] < raw["tolerance"],
        "candidate_hash_matches": digest == raw["sha256_grid_separator_knots"],
        "candidate_shape_exact": len(grid) == len(values) == raw["nodes"] == 25_601,
        "grid_strict_and_complete": grid[0] == -1 and grid[-1] == 1 and all(a < b for a, b in zip(grid, grid[1:])),
        "grid_exactly_reflection_symmetric": symmetry,
        "all_knots_positive": min(values) > 0,
        "passing_endpoint_nonnegative": pass_ok and pass_minimum >= 0,
        "preceding_endpoint_negative": not fail_ok and fail_minimum < 0,
        "adjacent_threshold_points": high == low + 1,
    }
    prediction_gates = {
        "registered_upper_target": q_pass < Fraction(2508753875, 10**10),
        "registered_window_target": 0 < window < Fraction(3, 10**9),
        "worst_receipt_classified": registered_region or not registered_region,
    }
    report = {
        "status": "exact endpoint-clustered 25,601-knot Bellman threshold",
        "q_pass": str(q_pass),
        "q_pass_decimal": float(q_pass),
        "q_fail_predecessor": str(q_fail),
        "q_fail_predecessor_decimal": float(q_fail),
        "threshold_resolution": "1/1000000000000000",
        "exact_threshold_evaluations": evaluations,
        "nodes": len(grid),
        "upper_envelope_lines_retained": retained,
        "common_intervals_checked_per_evaluation": len(cells),
        "candidate_hash": digest,
        "pass_minimum_numerator": str(pass_minimum),
        "fail_minimum_numerator": str(fail_minimum),
        "pass_worst_receipt": pass_receipt,
        "fail_worst_receipt": fail_receipt,
        "pass_worst_in_registered_endpoint_contact_region": registered_region,
        "finite_tensor_lower": str(lower),
        "rigorous_window_width": str(window),
        "rigorous_window_width_decimal": float(window),
        "certificate_gates": certificate_gates,
        "registered_prediction_gates": prediction_gates,
        "certificate_closed": all(certificate_gates.values()),
        "all_registered_predictions_pass": all(prediction_gates.values()),
        "all_gates_pass": (
            all(certificate_gates.values()) and all(prediction_gates.values())
        ),
        "claim_boundary": (
            "Exact for one preregistered nonuniform rational witness. Does not "
            "prove a continuum rate, exact optimum, or flow-to-path theorem."
        ),
    }
    output = HERE / "exact-endpoint-clustered-threshold.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["certificate_closed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
