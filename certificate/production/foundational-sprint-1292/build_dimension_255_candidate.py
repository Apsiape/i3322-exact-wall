#!/usr/bin/env python3
"""Search for a dimension-255 aligned I3322 strategy; no proof authority."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_EVEN, getcontext
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
DIMENSION = 255
MAX_ITERATIONS = 1000
TOLERANCE = 2e-14
DAMPING = 0.65
QUANTUM = Decimal("0.000000000000000000000000000001")
getcontext().prec = 50


def jacobi(profile: np.ndarray) -> np.ndarray:
    diagonal = (
        profile[:-1] * profile[1:]
        + (profile[:-1] - profile[1:]) / 2.0
        - 1.0
    )
    matrix = np.diag(diagonal)
    off_diagonal = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - profile[1:-1] ** 2))
    matrix += np.diag(off_diagonal, 1) + np.diag(off_diagonal, -1)
    return matrix


def optimize_profile() -> tuple[np.ndarray, np.ndarray, float, int, float]:
    plateau = 0.8782729451808125
    coordinate = np.arange(DIMENSION + 1, dtype=float) - DIMENSION / 2.0
    profile = -plateau * np.tanh(coordinate / 3.0)
    profile[0], profile[-1] = 1.0, -1.0
    delta = float("inf")
    for iteration in range(1, MAX_ITERATIONS + 1):
        eigenvalues, eigenvectors = np.linalg.eigh(jacobi(profile))
        vector = np.abs(eigenvectors[:, -1])
        if np.min(vector) == 0:
            raise RuntimeError("Perron vector acquired an exact zero")
        proposal = profile.copy()
        left = vector[:-1]
        right = vector[1:]
        linear = (
            (profile[:-2] - 0.5) * left * left
            + (profile[2:] + 0.5) * right * right
        )
        curved = left * right
        proposal[1:-1] = linear / np.sqrt(linear * linear + curved * curved)
        updated = DAMPING * proposal + (1.0 - DAMPING) * profile
        updated[0], updated[-1] = 1.0, -1.0
        delta = float(np.max(np.abs(updated - profile)))
        profile = updated
        if delta < TOLERANCE:
            break
    eigenvalues, eigenvectors = np.linalg.eigh(jacobi(profile))
    vector = np.abs(eigenvectors[:, -1])
    vector /= np.linalg.norm(vector)
    return profile, vector, float(eigenvalues[-1]), iteration, delta


def decimal_string(value: float) -> str:
    return format(
        Decimal(str(float(value))).quantize(QUANTUM, rounding=ROUND_HALF_EVEN),
        "f",
    )


def main() -> None:
    profile, vector, eigenvalue, iterations, delta = optimize_profile()
    profile_decimals = [decimal_string(value) for value in profile]
    vector_decimals = [decimal_string(value) for value in vector]
    payload = "\n".join(profile_decimals + ["--"] + vector_decimals)
    digest = hashlib.sha256(payload.encode("ascii")).hexdigest()
    report = {
        "status": "floating dimension-255 candidate only",
        "dimension": DIMENSION,
        "iterations": iterations,
        "maximum_iterations": MAX_ITERATIONS,
        "final_profile_delta": delta,
        "tolerance": TOLERANCE,
        "damping": DAMPING,
        "floating_top_eigenvalue": eigenvalue,
        "digits_after_decimal": 30,
        "sha256_profile_separator_vector": digest,
        "profile_decimal": profile_decimals,
        "vector_decimal": vector_decimals,
        "claim_boundary": (
            "Floating search only. The exact rational verifier owns every theorem claim."
        ),
    }
    output = HERE / "dimension-255-candidate.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "dimension": DIMENSION,
        "iterations": iterations,
        "final_profile_delta": delta,
        "floating_top_eigenvalue": eigenvalue,
        "minimum_vector_entry": float(np.min(vector)),
        "sha256": digest,
    }, indent=2))


if __name__ == "__main__":
    main()
