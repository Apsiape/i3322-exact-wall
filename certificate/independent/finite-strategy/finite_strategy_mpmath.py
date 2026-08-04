#!/usr/bin/env python3
"""Independent mpmath.iv evaluation of the finite I3322 witness."""

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
    / "certificate/production/foundational-sprint-1288/finite-strategy-candidate.json"
)
PRODUCTION = (
    ROOT
    / "certificate/production/foundational-sprint-1288/exact-finite-strategy-lower-bound.json"
)
iv.dps = 160


def point(text: str):
    return iv.mpf(text)


def endpoints(value) -> list[str]:
    return [to_str(value._mpi_[0], 170), to_str(value._mpi_[1], 170)]


def main() -> None:
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    profile_strings = candidate["profile_decimal"]
    vector_strings = candidate["vector_decimal"]
    payload = "\n".join(profile_strings + ["--"] + vector_strings)
    digest = hashlib.sha256(payload.encode("ascii")).hexdigest()

    profile = [point(value) for value in profile_strings]
    vector = [point(value) for value in vector_strings]
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
            * vector[index]
            * vector[index]
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
    value = (diagonal + neighbors) / norm
    local_endpoints = endpoints(value)
    width = float(value.b - value.a)

    # Only after the local interval has been assembled, compare it with the
    # separately produced rational floor certificate.
    production = json.loads(PRODUCTION.read_text(encoding="utf-8"))
    production_lower = Fraction(production["certified_value_lower"])
    production_box = (
        iv.mpf(production_lower.numerator) / iv.mpf(production_lower.denominator)
    )

    gates = {
        "dimensions_match": (
            dimension == 127
            and len(profile) == 128
            and len(vector) == 127
        ),
        "candidate_payload_hash_matches": (
            digest == candidate["sha256_profile_separator_vector"]
        ),
        "all_radicands_strictly_positive": all(value.a > 0 for value in radicands),
        "interval_lower_above_point_25087519": bool(
            value.a > iv.mpf("0.25087519").b
        ),
        "interval_width_below_one_e_minus_eighty": width < 1e-80,
        "actual_interval_above_production_floor": bool(
            value.a >= production_box.b
        ),
    }
    report = {
        "status": "independent mpmath.iv finite-strategy reconstruction",
        "precision_decimal_digits": 160,
        "imports_production_engine": False,
        "dimension": dimension,
        "candidate_payload_sha256": digest,
        "direct_value_interval": local_endpoints,
        "interval_width_upper_float": width,
        "production_floor_interval": endpoints(production_box),
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "Independent arithmetic reconstruction of the committed finite "
            "witness; not an independent witness search or exact-optimum claim."
        ),
    }
    output = HERE / "finite-strategy-mpmath.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
