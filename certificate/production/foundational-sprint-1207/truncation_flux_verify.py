#!/usr/bin/env python3
"""Exact rational guards for the Jacobi truncation boundary-flux identity."""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def fixture(size: int, left: int, right: int, offset: int) -> dict[str, object]:
    if not (1 <= left <= right < size - 1):
        raise ValueError("interval must have two exterior neighbors")
    q = F(7 + offset, 11 + offset)
    lam = [
        F((index + 2) * (size + 1 - index) + offset, size * size + 13)
        for index in range(size)
    ]
    edge = [F(0)] + [
        F((3 * index + 2 + offset) % 11 + 1, 17 + index)
        for index in range(1, size)
    ]

    diagonal = []
    for index in range(size):
        incoming = edge[index] * lam[index - 1] if index > 0 else F(0)
        outgoing = edge[index + 1] * lam[index + 1] if index + 1 < size else F(0)
        diagonal.append(q - (incoming + outgoing) / lam[index])

    norm = sum((lam[index] ** 2 for index in range(left, right + 1)), F(0))
    numerator = sum(
        (diagonal[index] * lam[index] ** 2 for index in range(left, right + 1)),
        F(0),
    )
    numerator += 2 * sum(
        (edge[index] * lam[index - 1] * lam[index] for index in range(left + 1, right + 1)),
        F(0),
    )
    left_flux = edge[left] * lam[left - 1] * lam[left]
    right_flux = edge[right + 1] * lam[right] * lam[right + 1]
    residual = q * norm - numerator - left_flux - right_flux
    omit_left = q * norm - numerator - right_flux
    omit_right = q * norm - numerator - left_flux
    assert residual == 0
    assert omit_left != 0 and omit_right != 0
    return {
        "size": size,
        "interval": [left, right],
        "offset": offset,
        "exact_flux_residual": str(residual),
        "omit_left_detected": str(omit_left),
        "omit_right_detected": str(omit_right),
        "positive_flux": left_flux + right_flux > 0,
    }


def main() -> None:
    rows = [
        fixture(size, left, right, offset)
        for size, left, right in ((7, 1, 5), (9, 2, 6), (11, 2, 8), (13, 3, 9))
        for offset in (0, 2, 5)
    ]
    report = {
        "status": "exact rational Jacobi truncation-flux guard",
        "arithmetic": "fractions.Fraction only",
        "fixtures": rows,
        "all_gates_pass": all(
            row["exact_flux_residual"] == "0"
            and row["omit_left_detected"] != "0"
            and row["omit_right_detected"] != "0"
            and row["positive_flux"]
            for row in rows
        ),
        "claim_boundary": (
            "This proves the algebraic boundary-flux identity. The I3322 "
            "application additionally uses the certified spatial wall and "
            "its analytic plateau asymptotics."
        ),
    }
    (HERE / "truncation-flux-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
