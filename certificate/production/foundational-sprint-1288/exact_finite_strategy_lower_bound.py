#!/usr/bin/env python3
"""Exactly certify a finite-dimensional I3322 strategy lower bound."""

from __future__ import annotations

from fractions import Fraction
import hashlib
from math import isqrt
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "finite-strategy-candidate.json"
UPPER = Fraction(125438192257, 500000000000)
SQRT_SCALE = 10**60


def rational_sqrt_floor(value: Fraction) -> Fraction:
    if value < 0:
        raise ValueError("square-root input must be nonnegative")
    scaled_square = value.numerator * SQRT_SCALE * SQRT_SCALE // value.denominator
    return Fraction(isqrt(scaled_square), SQRT_SCALE)


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    profile_strings = candidate["profile_decimal"]
    vector_strings = candidate["vector_decimal"]
    profile = [Fraction(value) for value in profile_strings]
    vector = [Fraction(value) for value in vector_strings]
    dimension = candidate["dimension"]

    payload = "\n".join(profile_strings + ["--"] + vector_strings)
    digest = hashlib.sha256(payload.encode("ascii")).hexdigest()

    square_root_floors = [Fraction(0)]
    square_root_receipts = []
    for index, coordinate in enumerate(profile[1:-1], start=1):
        radicand = 1 - coordinate * coordinate
        lower = rational_sqrt_floor(radicand)
        square_root_floors.append(lower)
        square_root_receipts.append({
            "index": index,
            "radicand": str(radicand),
            "lower": str(lower),
            "lower_square_slack": str(radicand - lower * lower),
        })
    square_root_floors.append(Fraction(0))

    norm = sum((entry * entry for entry in vector), Fraction(0))
    diagonal_numerator = sum(
        (
            (
                profile[index] * profile[index + 1]
                + (profile[index] - profile[index + 1]) / 2
                - 1
            )
            * vector[index]
            * vector[index]
            for index in range(dimension)
        ),
        Fraction(0),
    )
    neighbor_numerator_lower = sum(
        (
            square_root_floors[index]
            * vector[index - 1]
            * vector[index]
            for index in range(1, dimension)
        ),
        Fraction(0),
    )
    certified_value = (diagonal_numerator + neighbor_numerator_lower) / norm
    rigorous_window_width = UPPER - certified_value

    gates = {
        "candidate_iteration_converged": (
            candidate["iterations"] < candidate["maximum_iterations"]
            and candidate["final_profile_delta"] < candidate["tolerance"]
        ),
        "candidate_witness_hash_matches": (
            digest == candidate["sha256_profile_separator_vector"]
        ),
        "dimensions_and_endpoints_exact": (
            dimension == 127
            and len(profile) == dimension + 1
            and len(vector) == dimension
            and profile[0] == 1
            and profile[-1] == -1
            and all(-1 < entry < 1 for entry in profile[1:-1])
        ),
        "committed_vector_strictly_positive": all(entry > 0 for entry in vector),
        "all_square_root_floors_certified": all(
            receipt["lower"] != "0"
            and Fraction(receipt["lower_square_slack"]) >= 0
            for receipt in square_root_receipts
        ),
        "normalization_denominator_positive": norm > 0,
        "certified_value_above_point_250875": (
            certified_value > Fraction(250875, 1_000_000)
        ),
        "rigorous_window_width_below_one_point_four_e_minus_six": (
            0 < rigorous_window_width < Fraction(14, 10_000_000)
        ),
    }
    report = {
        "status": "exact finite-dimensional I3322 lower strategy",
        "dimension": dimension,
        "candidate_profile_sha256": digest,
        "sqrt_floor_decimal_places": 60,
        "normalization": str(norm),
        "diagonal_numerator": str(diagonal_numerator),
        "neighbor_numerator_lower": str(neighbor_numerator_lower),
        "certified_value_lower": str(certified_value),
        "certified_value_lower_decimal": float(certified_value),
        "rigorous_upper": str(UPPER),
        "rigorous_upper_decimal": float(UPPER),
        "rigorous_window_width": str(rigorous_window_width),
        "rigorous_window_width_decimal": float(rigorous_window_width),
        "minimum_sqrt_floor_slack": str(
            min(Fraction(row["lower_square_slack"]) for row in square_root_receipts)
        ),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The displayed finite 127-dimensional tensor-product strategy gives "
            "a rigorous lower bound on the true I3322 value. Together with Sprint "
            "1287 it yields the displayed unconditional two-sided window."
        ),
        "proof_runtime": (
            "Python standard library only; every theorem-stage operation uses integers or Fraction."
        ),
        "claim_boundary": (
            "This does not identify the exact optimum or prove nonattainment, "
            "tensor/commuting separation, or nonclosure."
        ),
    }
    output = HERE / "exact-finite-strategy-lower-bound.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        key: value
        for key, value in report.items()
        if key not in {"diagonal_numerator", "neighbor_numerator_lower", "normalization"}
    }, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
