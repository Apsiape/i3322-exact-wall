#!/usr/bin/env python3
"""Exactly verify a committed rational piecewise-linear Bellman subsolution.

The floating-point builder is only a witness search.  This verifier imports
only the Python standard library and treats every knot, breakpoint, envelope
intersection, quadratic coefficient, and minimum as a ``Fraction``.
"""

from __future__ import annotations

from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Q_HAT = Fraction(125438192257, 500000000000)  # 0.250876384514 exactly
CANDIDATE = HERE / "bellman-subsolution-candidate.json"


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
    candidates = [(quadratic_value(coefficients, left), left)]
    candidates.append((quadratic_value(coefficients, right), right))
    if aa > 0:
        vertex = -bb / (2 * aa)
        if left <= vertex <= right:
            candidates.append((quadratic_value(coefficients, vertex), vertex))
    return min(candidates)


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    values = [Fraction(value) for value in candidate["knots_decimal"]]
    nodes = candidate["nodes"]
    iterations = candidate["iterations"]
    final_delta = candidate["final_delta"]
    denominator = nodes - 1
    grid = [Fraction(-1) + Fraction(2 * index, denominator) for index in range(nodes)]
    owners, starts = upper_envelope(grid, values)

    finite_starts = [
        start for start in starts if start is not None and -1 < start < 1
    ]
    breakpoints = sorted(set(grid + finite_starts))
    envelope_starts = [start for start in starts[1:] if start is not None]

    all_denominators_positive = True
    minimum_numerator: Fraction | None = None
    minimum_residual_bound: Fraction | None = None
    worst_receipt: dict | None = None
    intervals_checked = 0

    for left, right in zip(breakpoints, breakpoints[1:]):
        if left == right:
            continue
        midpoint = (left + right) / 2
        grid_position = (midpoint + 1) * denominator / 2
        f_index = min(
            nodes - 2,
            max(0, grid_position.numerator // grid_position.denominator),
        )
        # Exact floor arithmetic.  Because midpoint lies in an open common
        # interval, it selects a unique piecewise-linear segment.
        x0, x1 = grid[f_index], grid[f_index + 1]
        f0, f1 = values[f_index], values[f_index + 1]
        a = (f1 - f0) / (x1 - x0)
        b = f0 - a * x0

        owner_position = bisect_right(envelope_starts, midpoint)
        owner = owners[owner_position]
        m = grid[owner]
        c = values[owner] - m / 2

        d_left = a * left + b
        d_right = a * right + b
        positive = d_left > 0 and d_right > 0
        all_denominators_positive = all_denominators_positive and positive
        if not positive:
            continue

        alpha = Q_HAT + 1 - c
        beta = -Fraction(1, 2) - m
        coefficients = (
            4 * a * beta + 1,
            4 * (a * alpha + b * beta),
            4 * b * alpha - 1,
        )
        local_minimum, minimizer = quadratic_minimum(
            coefficients, left, right
        )
        max_denominator = 4 * max(d_left, d_right)
        residual_bound = local_minimum / max_denominator
        intervals_checked += 1
        if minimum_numerator is None or local_minimum < minimum_numerator:
            minimum_numerator = local_minimum
        if (
            minimum_residual_bound is None
            or residual_bound < minimum_residual_bound
        ):
            minimum_residual_bound = residual_bound
            worst_receipt = {
                "interval": [str(left), str(right)],
                "F_segment": f_index,
                "envelope_owner": owner,
                "quadratic_coefficients": [str(value) for value in coefficients],
                "minimizer": str(minimizer),
                "minimum_numerator": str(local_minimum),
                "maximum_four_F": str(max_denominator),
                "residual_lower_bound": str(residual_bound),
            }

    assert minimum_numerator is not None
    assert minimum_residual_bound is not None
    digest = hashlib.sha256(
        "\n".join(candidate["knots_decimal"]).encode("ascii")
    ).hexdigest()
    candidate_shape_valid = (
        nodes == 6401
        and len(values) == nodes
        and candidate["digits_after_decimal"] == 18
        and grid[0] == -1
        and grid[-1] == 1
    )
    envelope_partition_valid = (
        len(owners) == len(starts)
        and starts[0] is None
        and all(start is not None for start in starts[1:])
        and all(
            left < right
            for left, right in zip(breakpoints, breakpoints[1:])
        )
        and breakpoints[0] == -1
        and breakpoints[-1] == 1
    )
    gates = {
        "candidate_iteration_converged": (
            iterations < candidate["maximum_iterations"]
            and final_delta < candidate["tolerance"]
        ),
        "candidate_witness_hash_matches": (
            digest == candidate["sha256_newline_joined_knots"]
        ),
        "candidate_shape_and_domain_exact": candidate_shape_valid,
        "all_rational_knots_positive": min(values) > 0,
        "upper_envelope_covers_domain": envelope_partition_valid,
        "all_piece_denominators_positive": all_denominators_positive,
        "all_exact_quadratic_minima_positive": minimum_numerator > 0,
        "global_residual_bound_above_five_e_minus_seven": (
            minimum_residual_bound > Fraction(5, 10_000_000)
        ),
    }
    report = {
        "status": "exact rational piecewise-linear Bellman subsolution",
        "q_hat": str(Q_HAT),
        "q_hat_decimal": float(Q_HAT),
        "nodes": nodes,
        "candidate_iterations": iterations,
        "candidate_final_delta": final_delta,
        "rational_digits_after_decimal": 18,
        "candidate_profile_sha256": digest,
        "minimum_rational_knot": str(min(values)),
        "upper_envelope_lines_retained": len(owners),
        "common_intervals_checked": intervals_checked,
        "minimum_quadratic_numerator": str(minimum_numerator),
        "global_residual_lower_bound": str(minimum_residual_bound),
        "global_residual_lower_bound_float": float(minimum_residual_bound),
        "worst_interval_receipt": worst_receipt,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The exact rational piecewise-linear G satisfies the global "
            "Bellman inequality at q_hat on [-1,1]^2."
        ),
        "claim_boundary": (
            "This certifies a near-exact commuting/tensor-product upper bound. "
            "It does not restore equality at q_*, nonattainment, or nonclosure."
        ),
        "proof_runtime": (
            "Python standard library only; all theorem-stage arithmetic is exact Fraction arithmetic."
        ),
    }
    output = HERE / "exact-rational-bellman-subsolution.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
