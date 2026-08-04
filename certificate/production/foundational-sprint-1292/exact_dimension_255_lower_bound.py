#!/usr/bin/env python3
"""Exactly certify the committed dimension-255 I3322 strategy."""

from __future__ import annotations

from fractions import Fraction
import hashlib
from math import isqrt
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CANDIDATE = HERE / "dimension-255-candidate.json"
UPPER = Fraction(50175098917669, 200000000000000)
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

    sines = [Fraction(0)]
    receipts = []
    for index, coordinate in enumerate(profile[1:-1], start=1):
        radicand = 1 - coordinate * coordinate
        lower = rational_sqrt_floor(radicand)
        sines.append(lower)
        receipts.append({
            "index": index,
            "lower_square_slack": str(radicand - lower * lower),
        })
    sines.append(Fraction(0))

    norm = sum((entry * entry for entry in vector), Fraction(0))
    diagonal = sum(
        (
            (
                profile[index] * profile[index + 1]
                + (profile[index] - profile[index + 1]) / 2
                - 1
            )
            * vector[index] ** 2
            for index in range(dimension)
        ),
        Fraction(0),
    )
    neighbors = sum(
        (
            sines[index] * vector[index - 1] * vector[index]
            for index in range(1, dimension)
        ),
        Fraction(0),
    )
    certified = (diagonal + neighbors) / norm
    window = UPPER - certified
    gates = {
        "candidate_search_completed_at_registered_cap": (
            candidate["iterations"] <= candidate["maximum_iterations"]
        ),
        "candidate_payload_hash_matches": (
            digest == candidate["sha256_profile_separator_vector"]
        ),
        "dimensions_and_endpoints_exact": (
            dimension == 255
            and len(profile) == 256
            and len(vector) == 255
            and profile[0] == 1
            and profile[-1] == -1
            and all(-1 < entry < 1 for entry in profile[1:-1])
        ),
        "committed_vector_strictly_positive": all(entry > 0 for entry in vector),
        "all_square_root_floors_certified": all(
            Fraction(receipt["lower_square_slack"]) >= 0 for receipt in receipts
        ),
        "normalization_denominator_positive": norm > 0,
        "certified_value_above_point_2508753844": (
            certified > Fraction(2508753844, 10_000_000_000)
        ),
        "rigorous_window_below_one_point_two_e_minus_seven": (
            0 < window < Fraction(12, 100_000_000)
        ),
    }
    report = {
        "status": "exact dimension-255 finite tensor I3322 lower strategy",
        "dimension": dimension,
        "candidate_payload_sha256": digest,
        "sqrt_floor_decimal_places": 60,
        "normalization": str(norm),
        "diagonal_numerator": str(diagonal),
        "neighbor_numerator_lower": str(neighbors),
        "certified_value_lower": str(certified),
        "certified_value_lower_decimal": float(certified),
        "rigorous_upper": str(UPPER),
        "rigorous_upper_decimal": float(UPPER),
        "rigorous_window_width": str(window),
        "rigorous_window_width_decimal": float(window),
        "minimum_sqrt_floor_slack": str(
            min(Fraction(receipt["lower_square_slack"]) for receipt in receipts)
        ),
        "minimum_vector_entry": str(min(vector)),
        "search_diagnostic": {
            "hit_iteration_cap": (
                candidate["iterations"] == candidate["maximum_iterations"]
            ),
            "final_profile_delta": candidate["final_profile_delta"],
            "registered_tolerance_not_reached": (
                candidate["final_profile_delta"] >= candidate["tolerance"]
            ),
            "load_bearing_for_lower_bound": False,
        },
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "theorem": (
            "The committed 255-dimensional tensor-product strategy gives the "
            "displayed rigorous I3322 lower bound."
        ),
        "claim_boundary": (
            "This does not identify the exact optimum or prove nonattainment, "
            "tensor/commuting separation, or nonclosure."
        ),
    }
    output = HERE / "exact-dimension-255-lower-bound.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
