#!/usr/bin/env python3
"""Exact-rational guard for the order-or-resolution scalar dichotomy."""

from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def main() -> None:
    # Custody of every rounded coefficient in the written proof.
    alpha_max = Q(13, 5)
    weight_max = Q(13, 10)
    reflected_lipschitz = Q(14)
    log_alpha_lipschitz = Q(14)

    # Derivative ledger on |t|<=9/10.  The only irrational comparison is
    # |b'|<=9/(2 sqrt(19))<21/20; squaring positive rationals proves it.
    bprime_bound = Q(21, 20)
    assert Q(81, 76) < bprime_bound**2
    log_ratio_derivative = Q(7)
    b_weight_derivative = (
        bprime_bound * alpha_max + weight_max * log_ratio_derivative
    )
    assert b_weight_derivative == Q(1183, 100)
    assert b_weight_derivative < 12
    # |x+1/2|<=7/5, so the reflected remainder derivative is <67/5<14.
    assert Q(7, 5) + 12 == Q(67, 5) < reflected_lipschitz
    # 1/2 * P'_max * 2 * (|F'|_max/F_min) = 14.
    assert Q(1, 2) * 2 * 2 * (Q(7, 5) / Q(1, 5)) == log_alpha_lipschitz

    order_exact = alpha_max * reflected_lipschitz
    ratio_to_log = weight_max * alpha_max
    order_total = order_exact + ratio_to_log * log_alpha_lipschitz
    vertical_total = ratio_to_log / 2

    assert order_total == Q(2093, 25)
    assert vertical_total == Q(169, 100)
    assert order_total <= Q(84)
    assert vertical_total <= Q(17, 10)

    rng = random.Random(1253)
    fixtures = 0
    minimum_slack = None
    wrong_mean_detections = 0
    for _ in range(50000):
        bx = Q(rng.randint(1, 100), 100)
        bu = Q(rng.randint(1, 100), 100)
        alpha = Q(rng.randint(500, 3380), 1300)
        beta = Q(rng.randint(500, 3380), 1300)
        rho = (bx * alpha + bu * beta) / (bx + bu)
        ea = rho - alpha
        eb = rho - beta
        identity_slack = abs(alpha - beta) - (abs(ea) + abs(eb))
        assert identity_slack == 0
        if minimum_slack is None or identity_slack < minimum_slack:
            minimum_slack = identity_slack

        # A generic, unweighted mean does not have the cancellation needed to
        # set R_+ to zero when bx != bu.
        wrong = (alpha + beta) / 2
        if bx * (alpha - wrong) + bu * (beta - wrong) != 0:
            wrong_mean_detections += 1
        fixtures += 1

    report = {
        "status": "exact-rational order-resolution dichotomy guard",
        "fixtures": fixtures,
        "exact_order_coefficient": str(order_total),
        "exact_vertical_coefficient": str(vertical_total),
        "certified_B_derivative_upper": str(b_weight_derivative),
        "certified_log_alpha_derivative_upper": str(log_alpha_lipschitz),
        "rounded_order_coefficient": "84",
        "rounded_vertical_coefficient": "17/10",
        "minimum_weighted_mean_identity_slack": str(minimum_slack),
        "wrong_mean_detections": wrong_mean_detections,
        "gates": {
            "weighted_mean_cancellation": minimum_slack == 0,
            "rounded_constants_dominate": (
                order_total <= Q(84) and vertical_total <= Q(17, 10)
            ),
            "generic_wrong_mean_rejected": wrong_mean_detections > 30000,
        },
        "all_gates_pass": (
            minimum_slack == 0
            and order_total <= Q(84)
            and vertical_total <= Q(17, 10)
            and wrong_mean_detections > 30000
        ),
        "claim_boundary": (
            "The scalar coefficient ledger is exact. The global event-measure "
            "invariance and finite-rank boundary theorem remain open."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "order-resolution-dichotomy-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
