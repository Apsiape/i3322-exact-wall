#!/usr/bin/env python3
"""High-precision guards for RMS packet compression and effective constants."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random

import mpmath as mp


HERE = Path(__file__).resolve().parent
Q = Fraction


def main() -> None:
    mp.mp.dps = 100
    rng = random.Random(1218)
    fixtures = 0
    maximum_violation = mp.mpf("0")

    for _ in range(3000):
        size = rng.randint(1, 20)
        v = [mp.mpf(rng.randint(-20, 20)) / rng.randint(1, 17) for _ in range(size)]
        w = [mp.mpf(rng.randint(-20, 20)) / rng.randint(1, 17) for _ in range(size)]
        if not any(v):
            v[0] = 1
        if not any(w):
            w[0] = 1
        weights = [
            mp.sqrt(mp.mpf(1) / 12 + mp.mpf(rng.randint(0, 1000)) / 1000 * (mp.mpf(13) / 10 - mp.mpf(1) / 12))
            for _ in range(size)
        ]
        lv = [weights[j] * v[j] for j in range(size)]
        lw = [weights[j] * w[j] for j in range(size)]
        zv = mp.sqrt(mp.fsum(x * x for x in v))
        zw = mp.sqrt(mp.fsum(x * x for x in w))
        pv = mp.sqrt(mp.fsum(x * x for x in lv)) / zv
        pw = mp.sqrt(mp.fsum(x * x for x in lw)) / zw

        # Identity K is sufficient to guard the norm inequality; arbitrary
        # unitary K preserves ||Lv|| exactly.
        error = mp.sqrt(mp.fsum((lv[j] - lw[j]) ** 2 for j in range(size)))
        lhs = abs(pv * zv - pw * zw)
        violation = max(mp.mpf("0"), lhs - error)
        maximum_violation = max(maximum_violation, violation)
        assert pv * pv >= mp.mpf(1) / 12
        assert pv * pv <= mp.mpf(13) / 10
        assert pw * pw >= mp.mpf(1) / 12
        assert pw * pw <= mp.mpf(13) / 10
        fixtures += 1

    p_ratio_squared = Q(13, 10) / Q(1, 12)
    effective_cocycle = p_ratio_squared
    assert effective_cocycle == Q(78, 5)
    assert effective_cocycle > Q(13, 2)

    report = {
        "status": "100-digit RMS packet-compression guard",
        "high_precision_fixtures": fixtures,
        "maximum_detected_reverse_triangle_violation": mp.nstr(maximum_violation, 20),
        "safe_grouped_amplitude_cocycle": str(effective_cocycle),
        "pointwise_contact_cocycle_bound": str(Q(13, 2)),
        "all_gates_pass": fixtures == 3000 and maximum_violation == 0,
        "claim_boundary": (
            "This verifies RMS compression and the safe grouped constant. It "
            "does not construct the common matched packet family or prove the "
            "final dimension inequality."
        ),
    }
    assert report["all_gates_pass"]
    (HERE / "rms-packet-guard.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
