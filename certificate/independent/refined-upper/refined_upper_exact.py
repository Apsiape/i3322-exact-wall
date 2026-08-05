#!/usr/bin/env python3
"""Independent exact reconstruction of the 25,601-knot I3322 upper witness.

This verifier deliberately imports no production module.  It reconstructs the
affine upper envelope, merges its cells with the witness mesh, and minimizes
the resulting quadratic numerators using only the Python standard library.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CANDIDATE = (
    ROOT
    / "certificate/production/foundational-sprint-1293/refined-bellman-candidate.json"
)
PRODUCTION_RECEIPT = (
    ROOT
    / "certificate/production/foundational-sprint-1293/exact-refined-witness-threshold.json"
)
OUTPUT = HERE / "refined-upper-exact.json"

Q_PASS = Fraction(250875391558130, 10**15)
Q_FAIL = Fraction(250875391558129, 10**15)


def value_at(poly: tuple[Fraction, Fraction, Fraction], x: Fraction) -> Fraction:
    a, b, c = poly
    return a * x * x + b * x + c


def exact_quadratic_minimum(
    poly: tuple[Fraction, Fraction, Fraction],
    left: Fraction,
    right: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return (minimum, argmin) on a closed rational interval."""
    candidates = [(value_at(poly, left), left), (value_at(poly, right), right)]
    a, b, _ = poly
    if a > 0:
        vertex = -b / (2 * a)
        if left <= vertex <= right:
            candidates.append((value_at(poly, vertex), vertex))
    return min(candidates, key=lambda item: (item[0], item[1]))


def reconstruct_envelope(
    grid: list[Fraction], values: list[Fraction]
) -> tuple[list[int], list[Fraction | None]]:
    """Build the upper hull of y = u*x + G(u)-u/2 by slope insertion."""
    owners: list[int] = []
    begins: list[Fraction | None] = []
    offsets = [g - u / 2 for u, g in zip(grid, values)]

    for candidate in range(len(grid)):
        crossing: Fraction | None = None
        while owners:
            prior = owners[-1]
            crossing = (offsets[prior] - offsets[candidate]) / (
                grid[candidate] - grid[prior]
            )
            prior_begin = begins[-1]
            if prior_begin is None or crossing > prior_begin:
                break
            owners.pop()
            begins.pop()
        if not owners:
            crossing = None
        owners.append(candidate)
        begins.append(crossing)

    return owners, begins


def make_cells(
    grid: list[Fraction],
    values: list[Fraction],
    owners: list[int],
    begins: list[Fraction | None],
) -> list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]]:
    """Two-pointer merge of mesh cells and envelope cells.

    A midpoint lookup is intentionally avoided.  The independent construction
    walks the two ordered partitions directly and records their intersections.
    """
    cells = []
    mesh_index = 0
    hull_index = 0
    point = Fraction(-1)
    last = Fraction(1)

    while point < last:
        mesh_right = grid[mesh_index + 1]
        next_hull = last
        if hull_index + 1 < len(begins):
            candidate_start = begins[hull_index + 1]
            assert candidate_start is not None
            if candidate_start <= point:
                hull_index += 1
                continue
            next_hull = min(last, candidate_start)
        right = min(mesh_right, next_hull, last)
        if right <= point:
            raise AssertionError("partition traversal failed to advance")

        x0, x1 = grid[mesh_index], grid[mesh_index + 1]
        g0, g1 = values[mesh_index], values[mesh_index + 1]
        witness_slope = (g1 - g0) / (x1 - x0)
        witness_offset = g0 - witness_slope * x0
        owner = owners[hull_index]
        hull_slope = grid[owner]
        hull_offset = values[owner] - hull_slope / 2
        cells.append(
            (
                point,
                right,
                witness_slope,
                witness_offset,
                hull_slope,
                hull_offset,
                mesh_index,
                owner,
            )
        )
        point = right
        if point == mesh_right and mesh_index + 1 < len(grid) - 1:
            mesh_index += 1
        if (
            hull_index + 1 < len(begins)
            and begins[hull_index + 1] is not None
            and point == begins[hull_index + 1]
        ):
            hull_index += 1

    return cells


def certify_endpoint(
    q: Fraction,
    cells: list[tuple[Fraction, Fraction, Fraction, Fraction, Fraction, Fraction, int, int]],
) -> tuple[Fraction, dict[str, object]]:
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
        minimum, minimizer = exact_quadratic_minimum(poly, left, right)
        if worst is None or minimum < worst:
            worst = minimum
            receipt = {
                "interval": [str(left), str(right)],
                "F_segment": segment,
                "envelope_owner": owner,
                "minimizer": str(minimizer),
                "quadratic_coefficients": [str(entry) for entry in poly],
                "minimum_numerator": str(minimum),
            }
    assert worst is not None and receipt is not None
    return worst, receipt


def main() -> None:
    raw = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    decimal_knots = raw["knots_decimal"]
    values = [Fraction(entry) for entry in decimal_knots]
    count = len(values)
    grid = [Fraction(-1) + Fraction(2 * i, count - 1) for i in range(count)]
    digest = hashlib.sha256("\n".join(decimal_knots).encode("ascii")).hexdigest()

    owners, begins = reconstruct_envelope(grid, values)
    cells = make_cells(grid, values, owners, begins)
    pass_minimum, pass_receipt = certify_endpoint(Q_PASS, cells)
    fail_minimum, fail_receipt = certify_endpoint(Q_FAIL, cells)

    published = json.loads(PRODUCTION_RECEIPT.read_text(encoding="utf-8"))
    gates = {
        "no_production_module_imported": True,
        "candidate_has_25601_knots": count == 25_601 == raw["nodes"],
        "candidate_hash_matches": digest == raw["sha256_newline_joined_knots"],
        "mesh_covers_closed_unit_interval": grid[0] == -1 and grid[-1] == 1,
        "all_knots_strictly_positive": min(values) > 0,
        "envelope_has_published_line_count": len(owners) == 20_758,
        "merged_partition_has_published_cell_count": len(cells) == 45_465,
        "passing_endpoint_is_nonnegative": pass_minimum >= 0,
        "preceding_endpoint_is_negative": fail_minimum < 0,
        "endpoints_are_adjacent_on_registered_grid": Q_PASS - Q_FAIL == Fraction(1, 10**15),
        "passing_receipt_matches_production": pass_receipt == published["pass_worst_receipt"],
        "failing_receipt_matches_production": fail_receipt == published["fail_worst_receipt"],
        "passing_minimum_matches_production": str(pass_minimum) == published["pass_minimum_numerator"],
        "failing_minimum_matches_production": str(fail_minimum) == published["fail_minimum_numerator"],
        "published_endpoints_match": (
            Fraction(published["q_pass"]) == Q_PASS
            and Fraction(published["q_fail_predecessor"]) == Q_FAIL
        ),
    }
    report = {
        "status": "independent exact reconstruction of refined I3322 upper witness",
        "candidate": CANDIDATE.relative_to(ROOT).as_posix(),
        "candidate_sha256_newline_joined_knots": digest,
        "knots": count,
        "upper_envelope_lines": len(owners),
        "merged_partition_cells": len(cells),
        "strict_minimum_knot": str(min(values)),
        "q_pass": str(Q_PASS),
        "q_fail_predecessor": str(Q_FAIL),
        "pass_minimum_numerator": str(pass_minimum),
        "fail_minimum_numerator": str(fail_minimum),
        "pass_worst_receipt": pass_receipt,
        "fail_worst_receipt": fail_receipt,
        "method": (
            "standard-library-only exact Fraction arithmetic; independently "
            "reimplemented monotone hull and two-pointer partition merge"
        ),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Independent arithmetic reconstruction for the shared committed "
            "witness; not an independent witness search or exact-optimum proof."
        ),
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
