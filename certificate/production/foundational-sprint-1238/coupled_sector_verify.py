"""Exact guards for Sprint 1238's coupled near/drift closure.

The finite fixtures guard only the measure split.  The theorem's operator
inputs are owned by Sprints 1225--1229 and the localization no-go review.
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path


def main() -> None:
    mu = Fraction(7, 8000)
    h0 = Fraction(1, 10**7)
    K = Fraction(4656, 25)
    H = Fraction(39, 10) * K + mu * mu / 2
    theta = mu * mu / (16 * H)
    J = 4 * Fraction(39, 10) * K
    C0_bar = Fraction(700, 1) / h0
    C_N = 4 * (48 + 6 * K + H * C0_bar) / (mu * mu)
    C_D = 4 * J / (mu * mu)
    C_out = Fraction(400 * 10**12, 1883**2)
    C_T = C_N + (1 + C_D) * C_out
    w0 = Fraction(1, 2 * (1 + C_D))

    assert 4 * H * theta == mu * mu / 4
    assert J == Fraction(78, 5) * K
    assert w0 > 0

    # Hostile finite-measure check of the only new structural inequality.
    # Four arbitrary omission events are split into near and complement.
    rng = random.Random(1238)
    fixtures = 100_000
    for _ in range(fixtures):
        atom_count = rng.randint(1, 24)
        weights = [Fraction(rng.randint(0, 30), rng.randint(1, 31)) for _ in range(atom_count)]
        total = sum(weights, Fraction(0))
        if total == 0:
            continue
        weights = [w / total for w in weights]
        sectors = [rng.choice(("N", "D", "O")) for _ in range(atom_count)]
        omissions = [
            [bool(rng.getrandbits(1)) for _ in range(atom_count)]
            for _ in range(4)
        ]
        delta_coarse = sum(
            weights[i]
            for event in omissions
            for i, present in enumerate(event)
            if present
        )
        delta_cap = sum(
            weights[i]
            for event in omissions
            for i, present in enumerate(event)
            if present and sectors[i] == "N"
        )
        m_D = sum(weights[i] for i in range(atom_count) if sectors[i] == "D")
        m_out = sum(weights[i] for i in range(atom_count) if sectors[i] == "O")
        assert delta_coarse <= delta_cap + 4 * (m_D + m_out)

    result = {
        "status": "exact coupled near/drift sector guard",
        "hostile_measure_fixtures": fixtures,
        "absorption_identity": "4*H*theta=mu^2/4",
        "coarse_complement_coefficient": "4 occurrences",
        "C_N_numerator_digits": len(str(C_N.numerator)),
        "C_D": str(C_D),
        "C_T_numerator_digits": len(str(C_T.numerator)),
        "w0": str(w0),
        "forced_alternative": "epsilon>=1/(4*C_T^2) or m_D>=w0",
        "terminal_near_entry_closed": False,
        "universal_dimension_lower_bound_proved": False,
        "all_gates_pass": True,
        "claim_boundary": (
            "This proves the global omission split and coupled-sector algebra. "
            "It does not charge terminal near-entry packets and therefore does "
            "not prove the dimension lower bound."
        ),
    }
    target = Path(__file__).with_name("coupled-sector-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
