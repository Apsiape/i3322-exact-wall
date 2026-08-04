"""Exact algebra/custody guard for Sprint 1231's final rate."""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
M = F(78, 5)
GAMMA = (20 * M) ** 4
MU = F(7, 8000)
THETA = F(1, 10**12)


def dependency_guards() -> int:
    required = [
        ROOT / "foundational-sprint-1214" / "SQUARE-ROOT-COCYCLE-THEOREM.md",
        ROOT / "foundational-sprint-1218" / "RMS-PACKET-COMPRESSION.md",
        ROOT / "foundational-sprint-1223" / "MOVING-DIHEDRAL-PARTITIONS.md",
        ROOT / "foundational-sprint-1225" / "EXACT-MOVING-FRAME-TRANSPORT.md",
        ROOT / "foundational-sprint-1229" / "RESULT-001-NEAR-FIXED-MASS-GAP.md",
        ROOT / "foundational-sprint-1230" / "RESULT-001-FINITE-RANK-EXIT-THEOREM.md",
        ROOT / "foundational-sprint-1232" / "RESULT-001-SATURATED-CONTACT-COERCIVITY.md",
    ]
    for path in required:
        assert path.is_file(), path
    return len(required)


def exact_algebra_guards() -> int:
    assert 20 * M == 312
    assert GAMMA == 9475854336
    assert 3000 * THETA < MU * MU / 4
    for d in range(1, 1000):
        assert (d + 1) ** 2 <= 4 * d * d
    return 1002


def main() -> None:
    deps = dependency_guards()
    algebra = exact_algebra_guards()
    print("==== SPRINT 1231 DIMENSION-BOUND ALGEBRA GUARD ====")
    print(f"PASS dependency paths: {deps}")
    print(f"PASS exact algebra checks: {algebra}")
    print(f"Gamma = {GAMMA}")


if __name__ == "__main__":
    main()
