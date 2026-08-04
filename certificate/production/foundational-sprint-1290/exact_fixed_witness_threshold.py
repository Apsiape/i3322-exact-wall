#!/usr/bin/env python3
"""Find the sharp 10^-15 Bellman threshold for the fixed Sprint 1287 witness."""

from __future__ import annotations

from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRODUCTION = HERE.parent
CANDIDATE = PRODUCTION / "foundational-sprint-1287/bellman-subsolution-candidate.json"
LOWER_REPORT = PRODUCTION / "foundational-sprint-1288/exact-finite-strategy-lower-bound.json"
SCALE = 10**15
SEARCH_LOW = 250_875_300_000_000
SEARCH_HIGH = 250_876_384_514_000


def upper_envelope(
    grid: list[Fraction], values: list[Fraction]
) -> tuple[list[int], list[Fraction | None]]:
    slopes = grid
    intercepts = [value - coordinate / 2 for coordinate, value in zip(grid, values)]
    owners: list[int] = []
    starts: list[Fraction | None] = []
    for index in range(len(grid)):
        start: Fraction | None = None
        while owners:
            previous = owners[-1]
            start = (intercepts[previous] - intercepts[index]) / (
                slopes[index] - slopes[previous]
            )
            previous_start = starts[-1]
            if previous_start is None or start > previous_start:
                break
            owners.pop()
            starts.pop()
        if not owners:
            start = None
        owners.append(index)
        starts.append(start)
    return owners, starts


def quadratic_value(
    coefficients: tuple[Fraction, Fraction, Fraction], x: Fraction
) -> Fraction:
    aa, bb, cc = coefficients
    return (aa * x + bb) * x + cc


def quadratic_minimum(
    coefficients: tuple[Fraction, Fraction, Fraction],
    left: Fraction,
    right: Fraction,
) -> tuple[Fraction, Fraction]:
    aa, bb, _ = coefficients
    candidates = [
        (quadratic_value(coefficients, left), left),
        (quadratic_value(coefficients, right), right),
    ]
    if aa > 0:
        vertex = -bb / (2 * aa)
        if left <= vertex <= right:
            candidates.append((quadratic_value(coefficients, vertex), vertex))
    return min(candidates)


def build_pieces(
    grid: list[Fraction], values: list[Fraction]
) -> tuple[list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]], int]:
    owners, starts = upper_envelope(grid, values)
    finite_starts = [start for start in starts if start is not None and -1 < start < 1]
    breakpoints = sorted(set(grid + finite_starts))
    envelope_starts = [start for start in starts[1:] if start is not None]
    pieces = []
    denominator = len(grid) - 1
    for left, right in zip(breakpoints, breakpoints[1:]):
        if left == right:
            continue
        midpoint = (left + right) / 2
        position = (midpoint + 1) * denominator / 2
        f_index = min(
            len(grid) - 2,
            max(0, position.numerator // position.denominator),
        )
        x0, x1 = grid[f_index], grid[f_index + 1]
        f0, f1 = values[f_index], values[f_index + 1]
        a = (f1 - f0) / (x1 - x0)
        b = f0 - a * x0
        owner_position = bisect_right(envelope_starts, midpoint)
        owner = owners[owner_position]
        m = grid[owner]
        c = values[owner] - m / 2
        pieces.append((left, right, a, b, m, c, f_index, owner))
    return pieces, len(owners)


def check_threshold(
    q: Fraction,
    pieces: list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]],
) -> tuple[bool, Fraction, dict[str, object]]:
    global_minimum: Fraction | None = None
    receipt: dict[str, object] | None = None
    for left, right, a, b, m, c, f_index, owner in pieces:
        alpha = q + 1 - c
        beta = -Fraction(1, 2) - m
        coefficients = (
            4 * a * beta + 1,
            4 * (a * alpha + b * beta),
            4 * b * alpha - 1,
        )
        minimum, minimizer = quadratic_minimum(coefficients, left, right)
        if global_minimum is None or minimum < global_minimum:
            global_minimum = minimum
            receipt = {
                "interval": [str(left), str(right)],
                "F_segment": f_index,
                "envelope_owner": owner,
                "minimizer": str(minimizer),
                "quadratic_coefficients": [str(entry) for entry in coefficients],
                "minimum_numerator": str(minimum),
            }
    assert global_minimum is not None and receipt is not None
    return global_minimum >= 0, global_minimum, receipt


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    values = [Fraction(value) for value in candidate["knots_decimal"]]
    digest = hashlib.sha256(
        "\n".join(candidate["knots_decimal"]).encode("ascii")
    ).hexdigest()
    nodes = candidate["nodes"]
    grid = [Fraction(-1) + Fraction(2 * index, nodes - 1) for index in range(nodes)]
    pieces, retained_lines = build_pieces(grid, values)

    low = SEARCH_LOW
    high = SEARCH_HIGH
    low_pass, _, _ = check_threshold(Fraction(low, SCALE), pieces)
    high_pass, _, _ = check_threshold(Fraction(high, SCALE), pieces)
    if low_pass or not high_pass:
        raise RuntimeError("registered threshold bracket is invalid")
    evaluations = 2
    while low + 1 < high:
        middle = (low + high) // 2
        passed, _, _ = check_threshold(Fraction(middle, SCALE), pieces)
        evaluations += 1
        if passed:
            high = middle
        else:
            low = middle

    q_pass = Fraction(high, SCALE)
    q_fail = Fraction(low, SCALE)
    pass_gate, pass_minimum, pass_receipt = check_threshold(q_pass, pieces)
    fail_gate, fail_minimum, fail_receipt = check_threshold(q_fail, pieces)
    evaluations += 2

    lower_data = json.loads(LOWER_REPORT.read_text(encoding="utf-8"))
    tensor_lower = Fraction(lower_data["certified_value_lower"])
    window = q_pass - tensor_lower
    gates = {
        "fixed_candidate_hash_matches": (
            digest == candidate["sha256_newline_joined_knots"]
        ),
        "all_fixed_witness_knots_positive": min(values) > 0,
        "registered_lower_grid_point_fails": not fail_gate,
        "returned_grid_point_passes": pass_gate,
        "adjacent_grid_points": high == low + 1,
        "upper_endpoint_below_point_2508756": q_pass < Fraction(2508756, 10_000_000),
        "historical_source_region_not_certified": q_pass > Fraction(250875384514, 10**12),
        "rigorous_window_below_four_e_minus_seven": window < Fraction(4, 10_000_000),
        "pass_minimum_nonnegative": pass_minimum >= 0,
        "fail_minimum_negative": fail_minimum < 0,
    }
    report = {
        "status": "exact fixed-witness Bellman threshold on the 10^-15 grid",
        "q_pass": str(q_pass),
        "q_pass_decimal": float(q_pass),
        "q_fail_predecessor": str(q_fail),
        "q_fail_predecessor_decimal": float(q_fail),
        "threshold_resolution": "1/1000000000000000",
        "exact_threshold_evaluations": evaluations,
        "piecewise_linear_knots": nodes,
        "upper_envelope_lines_retained": retained_lines,
        "common_intervals_checked_per_evaluation": len(pieces),
        "pass_minimum_numerator": str(pass_minimum),
        "fail_minimum_numerator": str(fail_minimum),
        "pass_worst_receipt": pass_receipt,
        "fail_worst_receipt": fail_receipt,
        "finite_tensor_lower": str(tensor_lower),
        "rigorous_window_width": str(window),
        "rigorous_window_width_decimal": float(window),
        "improvement_over_sprint_1287_upper": str(
            Fraction(125438192257, 500000000000) - q_pass
        ),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The fixed rational Sprint 1287 witness certifies the displayed "
            "commuting-projective I3322 upper bound."
        ),
        "proof_runtime": (
            "Python standard library only; all threshold decisions, envelope "
            "breakpoints, and quadratic minima use exact Fraction arithmetic."
        ),
        "claim_boundary": (
            "This is sharp only on the registered 10^-15 grid for this fixed "
            "piecewise-linear witness; it does not identify the exact optimum."
        ),
    }
    output = HERE / "exact-fixed-witness-threshold.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
