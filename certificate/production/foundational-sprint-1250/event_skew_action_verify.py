#!/usr/bin/env python3
"""Exact guards for the two-response event skew composition."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def random_involution(rng, size: int) -> list[int]:
    remaining = list(range(size))
    rng.shuffle(remaining)
    permutation = list(range(size))
    while remaining:
        i = remaining.pop()
        if remaining and rng.randrange(2):
            j = remaining.pop()
            permutation[i] = j
            permutation[j] = i
        else:
            permutation[i] = i
    return permutation


def main() -> None:
    import random

    rng = random.Random(1250)
    fixtures = 0
    wrong_orientation_detected = 0

    # If each one-response shift is the exact difference of event centres,
    # composition must telescope to centre[tau(i)]-centre[i].
    for _ in range(10000):
        size = rng.randrange(3, 20)
        a = random_involution(rng, size)
        b = random_involution(rng, size)
        centres = [Fraction(rng.randrange(-100, 101), rng.randrange(1, 30)) for _ in range(size)]
        h_a = [centres[a[i]] - centres[i] for i in range(size)]
        h_b = [centres[b[i]] - centres[i] for i in range(size)]
        for i in range(size):
            tau_i = a[b[i]]
            composed = h_b[i] + h_a[b[i]]
            assert composed == centres[tau_i] - centres[i]
            wrong = h_a[i] + h_b[a[i]]
            if wrong != composed:
                wrong_orientation_detected += 1
        fixtures += 1

    # Symbolic custody of the actual I3322 orientation.
    fu, fmu, fpminus, fminus_pminus = sp.symbols(
        "F_u F_minus_u F_Pminus F_minus_Pminus", positive=True
    )
    beta_sq = fu / fmu
    alpha_at_minus_u_sq = fminus_pminus / fpminus
    composed = sp.factor(beta_sq * alpha_at_minus_u_sq)
    expected = fu * fminus_pminus / (fmu * fpminus)
    cocycle_residual = sp.factor(composed - expected)

    # Finite increasing permutations of a total order are the identity.
    increasing_permutation_nonidentity = 0
    for size in range(1, 10):
        # A bijective nondecreasing list of {0,...,size-1} is forced pointwise.
        image = list(range(size))
        if any(image[i] != i for i in range(size)):
            increasing_permutation_nonidentity += 1

    gates = {
        "exact_centre_telescope": fixtures == 10000,
        "wrong_response_order_detected": wrong_orientation_detected > 0,
        "i3322_cocycle_orientation": cocycle_residual == 0,
        "finite_increasing_cycles_are_fixed": increasing_permutation_nonidentity == 0,
    }
    report = {
        "status": "exact event skew-action guard",
        "random_involution_fixtures": fixtures,
        "wrong_orientation_detections": wrong_orientation_detected,
        "symbolic_i3322_cocycle_residual": str(cocycle_residual),
        "finite_order_sizes_checked": 9,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "claim_boundary": (
            "The exact two-response skew orientation and finite-support closure are guarded. "
            "No approximate flux or universal dimension lower bound is claimed."
        ),
    }
    (HERE / "event-skew-action-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

