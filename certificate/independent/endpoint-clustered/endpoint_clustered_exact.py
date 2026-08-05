#!/usr/bin/env python3
"""Independent exact reconstruction of the nonuniform Sprint 1294 witness."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CANDIDATE = (
    ROOT
    / "certificate/production/foundational-sprint-1294/endpoint-clustered-candidate.json"
)
PRODUCTION = (
    ROOT
    / "certificate/production/foundational-sprint-1294/exact-endpoint-clustered-threshold.json"
)
OUTPUT = HERE / "endpoint-clustered-exact.json"
Q_PASS = Fraction(125437694054199, 500000000000000)
Q_FAIL = Fraction(250875388108397, 10**15)


def envelope(
    coordinates: list[Fraction], heights: list[Fraction]
) -> tuple[list[int], list[Fraction | None]]:
    intercept = [height - coordinate / 2 for coordinate, height in zip(coordinates, heights)]
    active: list[int] = []
    entry: list[Fraction | None] = []
    for new in range(len(coordinates)):
        start: Fraction | None = None
        while active:
            old = active[-1]
            start = (intercept[old] - intercept[new]) / (
                coordinates[new] - coordinates[old]
            )
            if entry[-1] is None or start > entry[-1]:
                break
            active.pop()
            entry.pop()
        if not active:
            start = None
        active.append(new)
        entry.append(start)
    return active, entry


def merge_partitions(
    x: list[Fraction],
    f: list[Fraction],
    active: list[int],
    entry: list[Fraction | None],
) -> list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]]:
    """Walk nonuniform mesh and hull cells without constructing a breakpoint set."""
    result = []
    mesh = 0
    hull = 0
    left = Fraction(-1)
    while left < 1:
        mesh_end = x[mesh + 1]
        hull_end = Fraction(1)
        if hull + 1 < len(entry):
            next_entry = entry[hull + 1]
            assert next_entry is not None
            if next_entry <= left:
                hull += 1
                continue
            hull_end = min(hull_end, next_entry)
        right = min(mesh_end, hull_end, Fraction(1))
        if not left < right:
            raise AssertionError("two-pointer merge did not advance")

        slope = (f[mesh + 1] - f[mesh]) / (x[mesh + 1] - x[mesh])
        offset = f[mesh] - slope * x[mesh]
        owner = active[hull]
        support_slope = x[owner]
        support_offset = f[owner] - support_slope / 2
        result.append(
            (
                left,
                right,
                slope,
                offset,
                support_slope,
                support_offset,
                mesh,
                owner,
            )
        )
        left = right
        if left == mesh_end and mesh + 1 < len(x) - 1:
            mesh += 1
        if (
            hull + 1 < len(entry)
            and entry[hull + 1] is not None
            and left == entry[hull + 1]
        ):
            hull += 1
    return result


def evaluate(poly: tuple[Fraction, Fraction, Fraction], z: Fraction) -> Fraction:
    a, b, c = poly
    return (a * z + b) * z + c


def interval_minimum(
    poly: tuple[Fraction, Fraction, Fraction], left: Fraction, right: Fraction
) -> tuple[Fraction, Fraction]:
    candidates = [(evaluate(poly, left), left), (evaluate(poly, right), right)]
    a, b, _ = poly
    if a > 0:
        critical = -b / (2 * a)
        if left <= critical <= right:
            candidates.append((evaluate(poly, critical), critical))
    return min(candidates, key=lambda pair: (pair[0], pair[1]))


def endpoint(
    q: Fraction,
    cells: list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]],
) -> tuple[Fraction, dict[str, object]]:
    global_minimum: Fraction | None = None
    receipt: dict[str, object] | None = None
    for left, right, a, b, m, c, segment, owner in cells:
        alpha = q + 1 - c
        beta = -Fraction(1, 2) - m
        poly = (
            4 * a * beta + 1,
            4 * (a * alpha + b * beta),
            4 * b * alpha - 1,
        )
        minimum, minimizer = interval_minimum(poly, left, right)
        if global_minimum is None or minimum < global_minimum:
            global_minimum = minimum
            receipt = {
                "interval": [str(left), str(right)],
                "F_segment": segment,
                "envelope_owner": owner,
                "owner_coordinate": str(m),
                "minimizer": str(minimizer),
                "quadratic_coefficients": [str(value) for value in poly],
                "minimum_numerator": str(minimum),
            }
    assert global_minimum is not None and receipt is not None
    return global_minimum, receipt


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    grid_text = candidate["grid_decimal"]
    knot_text = candidate["knots_decimal"]
    x = [Fraction(value) for value in grid_text]
    f = [Fraction(value) for value in knot_text]
    digest = hashlib.sha256(
        ("\n".join(grid_text) + "\n--\n" + "\n".join(knot_text)).encode("ascii")
    ).hexdigest()
    active, entry = envelope(x, f)
    cells = merge_partitions(x, f, active, entry)
    pass_minimum, pass_receipt = endpoint(Q_PASS, cells)
    fail_minimum, fail_receipt = endpoint(Q_FAIL, cells)
    production = json.loads(PRODUCTION.read_text(encoding="utf-8"))

    gates = {
        "imports_no_production_module": True,
        "candidate_hash_matches": digest == candidate["sha256_grid_separator_knots"],
        "shape_and_domain_exact": len(x) == len(f) == 25_601 and x[0] == -1 and x[-1] == 1,
        "strict_grid": all(left < right for left, right in zip(x, x[1:])),
        "exact_reflection_symmetry": all(x[i] == -x[-1 - i] for i in range(len(x))),
        "strictly_positive_knots": min(f) > 0,
        "passing_minimum_nonnegative": pass_minimum >= 0,
        "failing_minimum_negative": fail_minimum < 0,
        "adjacent_registered_endpoints": Q_PASS - Q_FAIL == Fraction(1, 10**15),
        "hull_count_matches": len(active) == production["upper_envelope_lines_retained"],
        "cell_count_matches": len(cells) == production["common_intervals_checked_per_evaluation"],
        "pass_receipt_matches": pass_receipt == production["pass_worst_receipt"],
        "fail_receipt_matches": fail_receipt == production["fail_worst_receipt"],
        "production_certificate_closed": production["certificate_closed"] is True,
        "production_prediction_failure_preserved": production["all_registered_predictions_pass"] is False,
    }
    report = {
        "status": "independent exact nonuniform-grid Bellman reconstruction",
        "candidate": CANDIDATE.relative_to(ROOT).as_posix(),
        "candidate_hash": digest,
        "nodes": len(x),
        "upper_envelope_lines": len(active),
        "merged_partition_cells": len(cells),
        "q_pass": str(Q_PASS),
        "q_fail_predecessor": str(Q_FAIL),
        "pass_minimum_numerator": str(pass_minimum),
        "fail_minimum_numerator": str(fail_minimum),
        "pass_worst_receipt": pass_receipt,
        "fail_worst_receipt": fail_receipt,
        "method": (
            "standard-library Fraction arithmetic; independent hull and direct "
            "two-pointer nonuniform partition merge"
        ),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Independent arithmetic reconstruction of one shared searched "
            "witness; not an independent search or exact-value theorem."
        ),
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
