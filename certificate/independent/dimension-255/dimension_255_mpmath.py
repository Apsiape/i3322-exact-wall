#!/usr/bin/env python3
"""Independent interval evaluation of the committed dimension-255 witness."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from mpmath import iv
from mpmath.libmp import to_str


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CANDIDATE = (
    ROOT
    / "certificate/production/foundational-sprint-1292/dimension-255-candidate.json"
)
PRODUCTION = (
    ROOT
    / "certificate/production/foundational-sprint-1292/exact-dimension-255-lower-bound.json"
)
UPPER = Fraction(50175098917669, 200000000000000)
iv.dps = 160


def endpoints(value) -> list[str]:
    return [to_str(value._mpi_[0], 170), to_str(value._mpi_[1], 170)]


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    profile_strings = candidate["profile_decimal"]
    vector_strings = candidate["vector_decimal"]
    payload = "\n".join(profile_strings + ["--"] + vector_strings)
    digest = hashlib.sha256(payload.encode("ascii")).hexdigest()

    profile = [iv.mpf(value) for value in profile_strings]
    vector = [iv.mpf(value) for value in vector_strings]
    dimension = candidate["dimension"]
    radicands = [iv.mpf(1) - coordinate * coordinate for coordinate in profile[1:-1]]
    sines = [iv.mpf(0)] + [iv.sqrt(value) for value in radicands] + [iv.mpf(0)]
    norm = sum((entry * entry for entry in vector), iv.mpf(0))
    diagonal = sum(
        (
            (
                profile[index] * profile[index + 1]
                + (profile[index] - profile[index + 1]) / 2
                - 1
            )
            * vector[index] * vector[index]
            for index in range(dimension)
        ),
        iv.mpf(0),
    )
    neighbors = sum(
        (
            sines[index] * vector[index - 1] * vector[index]
            for index in range(1, dimension)
        ),
        iv.mpf(0),
    )
    direct = (diagonal + neighbors) / norm
    direct_endpoints = endpoints(direct)
    width = float(direct.b - direct.a)

    # Production data enters only after the direct interval is complete.
    production = json.loads(PRODUCTION.read_text(encoding="utf-8"))
    floor = Fraction(production["certified_value_lower"])
    floor_box = iv.mpf(floor.numerator) / iv.mpf(floor.denominator)
    upper_box = iv.mpf(UPPER.numerator) / iv.mpf(UPPER.denominator)
    gates = {
        "dimensions_match": (
            dimension == 255
            and len(profile) == 256
            and len(vector) == 255
        ),
        "candidate_payload_hash_matches": (
            digest == candidate["sha256_profile_separator_vector"]
        ),
        "all_interior_radicands_strictly_positive": all(
            value.a > 0 for value in radicands
        ),
        "direct_interval_width_below_one_e_minus_one_hundred": width < 1e-100,
        "direct_interval_above_production_floor": bool(direct.a >= floor_box.b),
        "direct_interval_below_rigorous_upper": bool(direct.b < upper_box.a),
    }
    report = {
        "status": "independent mpmath.iv dimension-255 strategy reconstruction",
        "precision_decimal_digits": 160,
        "imports_production_engine": False,
        "dimension": dimension,
        "candidate_payload_sha256": digest,
        "direct_value_interval": direct_endpoints,
        "interval_width_upper_float": width,
        "production_floor_interval": endpoints(floor_box),
        "rigorous_upper_interval": endpoints(upper_box),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Independent arithmetic reconstruction of the committed witness; "
            "not an independent search or an exact-optimum theorem."
        ),
    }
    output = HERE / "dimension-255-mpmath.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
