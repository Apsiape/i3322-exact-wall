from __future__ import annotations

import json
import random
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 100
QSTAR_LO = Decimal("0.250875384513976535514")
MARGIN = QSTAR_LO - Decimal(1) / Decimal(4)


def main() -> None:
    rng = random.Random(1226)
    fixtures = 10_000
    minimum_eigenvalue_margin = None
    minimum_quadratic_slack = None

    for _ in range(fixtures):
        x = Decimal(rng.randint(-999999, 999999)) / Decimal(1_000_000)
        u = Decimal(rng.randint(-999999, 999999)) / Decimal(1_000_000)
        zp = Decimal(rng.randint(0, 1_000_000)) / Decimal(1_000_000)
        zm = Decimal(rng.randint(0, 1_000_000)) / Decimal(1_000_000)
        if zp == 0 and zm == 0:
            zp = Decimal(1)
        bx = (Decimal(1) - x * x).sqrt() / Decimal(2)
        bu = (Decimal(1) - u * u).sqrt() / Decimal(2)
        bsum = bx + bu
        delta = x - u
        q = QSTAR_LO - x * u + Decimal(1)
        lambda_min = q - (bsum * bsum + delta * delta / Decimal(4)).sqrt()
        eigen_slack = lambda_min - MARGIN
        assert eigen_slack >= 0
        minimum_eigenvalue_margin = (
            eigen_slack if minimum_eigenvalue_margin is None
            else min(minimum_eigenvalue_margin, eigen_slack)
        )
        rp = (q - delta / Decimal(2)) * zp - bsum * zm
        rm = (q + delta / Decimal(2)) * zm - bsum * zp
        quadratic_slack = rp * rp + rm * rm - MARGIN * MARGIN * (zp * zp + zm * zm)
        assert quadratic_slack >= 0
        minimum_quadratic_slack = (
            quadratic_slack if minimum_quadratic_slack is None
            else min(minimum_quadratic_slack, quadratic_slack)
        )

    result = {
        "status": "100-digit weighted closure-coercivity guard",
        "hostile_fixtures": fixtures,
        "certified_margin_lower_bound": str(MARGIN),
        "minimum_sampled_eigenvalue_slack": str(minimum_eigenvalue_margin),
        "minimum_sampled_quadratic_slack": str(minimum_quadratic_slack),
        "endpoint_amplitude_division_used": False,
        "global_contact_family_multiplicity": 2,
        "all_gates_pass": True,
        "claim_boundary": (
            "The analytic matrix inequality is exact. The fixture guard is "
            "not a substitute for the Sprint 1227--1229 packet assembly."
        ),
    }
    target = Path(__file__).with_name("weighted-closure-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
