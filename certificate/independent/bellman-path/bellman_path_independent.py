#!/usr/bin/env python3
"""Independent exact attacks on the universal Bellman--path theorem."""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WELD_SOURCE = (
    ROOT
    / "certificate/production/foundational-sprint-1287/bellman_operator_weld_verify.py"
)
WELD_RECEIPT = (
    ROOT / "certificate/production/foundational-sprint-1287/bellman-operator-weld.json"
)


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def ldl_pivots(matrix: list[list[F]]) -> list[F]:
    n = len(matrix)
    lower = [[F(0) for _ in range(n)] for _ in range(n)]
    pivots = [F(0) for _ in range(n)]
    for i in range(n):
        lower[i][i] = F(1)
        pivots[i] = matrix[i][i] - sum(
            (lower[i][k] ** 2 * pivots[k] for k in range(i)), F(0)
        )
        if pivots[i] == 0:
            raise ZeroDivisionError("zero LDL pivot")
        for j in range(i + 1, n):
            lower[j][i] = (
                matrix[j][i]
                - sum(
                    (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                    F(0),
                )
            ) / pivots[i]
    return pivots


def index_orientation_attack() -> dict[str, object]:
    rng = random.Random(1295)
    fixtures = 500
    exact_residuals = 0
    wrong_orientation_detections = 0
    minimum_remainder: F | None = None
    for _ in range(fixtures):
        n = rng.randrange(2, 9)
        labels = [rng.randrange(3) for _ in range(n + 1)]
        d = [[F(rng.randint(-9, 9), rng.randint(2, 13)) for _ in range(3)] for _ in range(3)]
        b = [F(rng.randint(0, 8), rng.randint(2, 11)) for _ in range(3)]
        g = [F(rng.randint(1, 9), rng.randint(2, 11)) for _ in range(3)]
        vector = [F(rng.randint(-8, 8), rng.randint(2, 13)) for _ in range(n)]

        actual = sum(
            d[labels[k]][labels[k + 1]] * vector[k] ** 2 for k in range(n)
        ) + 2 * sum(
            b[labels[k]] * vector[k - 1] * vector[k] for k in range(1, n)
        )
        envelope = sum(
            (
                d[labels[k]][labels[k + 1]]
                + b[labels[k]] ** 2 / g[labels[k]]
                + g[labels[k + 1]]
            )
            * vector[k] ** 2
            for k in range(n)
        )
        squares = (
            b[labels[0]] ** 2 / g[labels[0]] * vector[0] ** 2
            + g[labels[-1]] * vector[-1] ** 2
            + sum(
                (
                    g[labels[k]] * vector[k - 1]
                    - b[labels[k]] * vector[k]
                )
                ** 2
                / g[labels[k]]
                for k in range(1, n)
            )
        )
        residual = envelope - actual - squares
        exact_residuals += int(residual == 0)
        remainder = envelope - actual
        minimum_remainder = remainder if minimum_remainder is None else min(minimum_remainder, remainder)

        wrong = sum(
            (
                d[labels[k]][labels[k + 1]]
                + b[labels[k + 1]] ** 2 / g[labels[k + 1]]
                + g[labels[k]]
            )
            * vector[k] ** 2
            for k in range(n)
        )
        wrong_orientation_detections += int(wrong - actual != squares)
    return {
        "fixtures": fixtures,
        "exact_square_residuals": exact_residuals,
        "wrong_orientation_detections": wrong_orientation_detections,
        "minimum_correct_remainder": str(minimum_remainder),
    }


def pivot_floor_attack() -> dict[str, object]:
    rng = random.Random(2915)
    fixtures = 2000
    minimum_slack: F | None = None
    failures = []
    for fixture in range(fixtures):
        n = rng.randrange(1, 10)
        diagonal = [F(rng.randint(-20, 20), rng.randint(2, 17)) for _ in range(n)]
        offdiag = [F(rng.randint(-12, 12), rng.randint(2, 17)) for _ in range(n - 1)]
        row_upper = []
        for i in range(n):
            radius = (abs(offdiag[i - 1]) if i else F(0)) + (
                abs(offdiag[i]) if i + 1 < n else F(0)
            )
            row_upper.append(diagonal[i] + radius)
        spectral_upper = max(row_upper)
        delta = F(rng.randint(1, 9), rng.randint(2, 11))
        q = spectral_upper + delta
        matrix = [[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[i][i] = q - diagonal[i]
            if i + 1 < n:
                matrix[i][i + 1] = matrix[i + 1][i] = -offdiag[i]
        pivots = ldl_pivots(matrix)
        local_slack = min(pivots) - delta
        minimum_slack = local_slack if minimum_slack is None else min(minimum_slack, local_slack)
        if local_slack < 0:
            failures.append({"fixture": fixture, "slack": str(local_slack)})
            break
    return {
        "exact_rational_fixtures": fixtures,
        "minimum_pivot_minus_gershgorin_floor": str(minimum_slack),
        "failures": failures,
    }


def unit_point(k: int) -> tuple[F, F]:
    # Positive rational point on the unit circle.
    m, n = k + 2, k + 1
    den = m * m + n * n
    return F(m * m - n * n, den), F(2 * m * n, den)


def zeros(n: int) -> list[list[F]]:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def put_edge(
    matrix: list[list[F]], i: int, j: int, block: tuple[tuple[F, F], tuple[F, F]]
) -> None:
    matrix[i][i], matrix[i][j] = block[0]
    matrix[j][i], matrix[j][j] = block[1]


def put_block(
    matrix: list[list[F]], i: int, block: tuple[tuple[F, F], tuple[F, F]]
) -> None:
    put_edge(matrix, i, i + 1, block)


def open_blocks(c: list[F], s: list[F]) -> tuple[list[list[list[F]]], list[list[list[F]]]]:
    dimension = len(c) - 1
    if dimension % 2 == 0:
        raise ValueError("open carrier must be odd")
    a1, a2, a3 = zeros(dimension), zeros(dimension), zeros(dimension)
    b1, b2, b3 = zeros(dimension), zeros(dimension), zeros(dimension)
    half = F(1, 2)
    a1[0][0] = a2[0][0] = b3[0][0] = F(1)
    for edge in range(2, dimension, 2):
        i, x, y = edge - 1, c[edge], s[edge]
        put_block(a1, i, ((half * (1 - x), -half * y), (-half * y, half * (1 + x))))
        put_block(a2, i, ((half * (1 - x), half * y), (half * y, half * (1 + x))))
        put_block(b3, i, ((half, half), (half, half)))
    for edge in range(1, dimension - 1, 2):
        i, x, y = edge - 1, c[edge], s[edge]
        put_block(b1, i, ((half * (1 + x), -half * y), (-half * y, half * (1 - x))))
        put_block(b2, i, ((half * (1 + x), half * y), (half * y, half * (1 - x))))
        put_block(a3, i, ((half, half), (half, half)))
    a3[-1][-1] = F(1)
    b1[-1][-1] = b2[-1][-1] = 1 + c[-1]
    return [a1, a2, a3], [b1, b2, b3]


def marginal(lam: list[F], matrix: list[list[F]]) -> F:
    return sum((lam[i] ** 2 * matrix[i][i] for i in range(len(lam))), F(0))


def correlation(lam: list[F], a: list[list[F]], b: list[list[F]]) -> F:
    return sum(
        (
            lam[i] * lam[j] * a[i][j] * b[i][j]
            for i in range(len(lam))
            for j in range(len(lam))
        ),
        F(0),
    )


def bell(lam: list[F], a: list[list[list[F]]], b: list[list[list[F]]]) -> F:
    value = -marginal(lam, a[1]) - marginal(lam, b[0]) - 2 * marginal(lam, b[1])
    for coefficient, left, right in (
        (1, a[0], b[0]), (1, a[0], b[1]), (1, a[1], b[0]), (1, a[1], b[1]),
        (-1, a[0], b[2]), (1, a[1], b[2]), (-1, a[2], b[0]), (1, a[2], b[1]),
    ):
        value += coefficient * correlation(lam, left, right)
    return value


def jacobi_value(c: list[F], s: list[F], lam: list[F]) -> F:
    return sum(
        (
            (c[k] * c[k + 1] + (c[k] - c[k + 1]) / 2 - 1) * lam[k] ** 2
            for k in range(len(lam))
        ),
        F(0),
    ) + sum(
        (s[k] * lam[k - 1] * lam[k] for k in range(1, len(lam))), F(0)
    )


def carrier_attack() -> dict[str, object]:
    # Exercise both parity branches of the general embedding.  A word with n
    # Jacobi coordinates uses n+1 labels.  Prepending +1 and appending -1
    # gives open carrier dimension n+2; when that is even, insert one dummy
    # label and give its coordinate zero weight.
    records = []
    all_direct = True
    all_principal = True
    for word_dimension in range(1, 9):
        for offset in range(3):
            points = [
                unit_point(2 + offset + 2 * k) for k in range(word_dimension + 1)
            ]
            word_c = [point[0] for point in points]
            word_s = [point[1] for point in points]
            lam_inner = [
                F((k + 2) * (word_dimension + 1 - k) + offset, 19 + 3 * k)
                for k in range(word_dimension)
            ]
            needs_dummy = word_dimension % 2 == 0
            dummy = unit_point(31 + offset + word_dimension)
            c = [F(1)] + word_c + ([dummy[0]] if needs_dummy else []) + [F(-1)]
            s = [F(0)] + word_s + ([dummy[1]] if needs_dummy else []) + [F(0)]
            lam = [F(0)] + lam_inner + [F(0)] * (1 + int(needs_dummy))
            a, b = open_blocks(c, s)
            direct = bell(lam, a, b)
            padded = jacobi_value(c, s, lam)
            inner = jacobi_value(word_c, word_s, lam_inner)
            direct_ok = direct == padded
            principal_ok = padded == inner
            all_direct &= direct_ok
            all_principal &= principal_ok
            records.append(
                {
                    "word_dimension": word_dimension,
                    "carrier_dimension": len(lam),
                    "dummy_inserted": needs_dummy,
                    "direct_equals_padded": direct_ok,
                    "padded_equals_inner": principal_ok,
                }
            )
    return {
        "exact_rational_fixtures": len(records),
        "word_dimension_range": [1, 8],
        "both_parity_branches_exercised": {
            "without_dummy": any(not row["dummy_inserted"] for row in records),
            "with_dummy": any(row["dummy_inserted"] for row in records),
        },
        "all_direct_bell_values_equal_padded_jacobi_values": all_direct,
        "all_padded_values_equal_inner_word_values": all_principal,
        "fixtures": records,
    }


def weld_typing_audit() -> dict[str, object]:
    text = WELD_SOURCE.read_text(encoding="utf-8")
    receipt = json.loads(WELD_RECEIPT.read_text(encoding="utf-8"))
    excluded = set(receipt["excluded_dependencies"])
    expected = {
        "Bellman fixed-point equality",
        "concavity",
        "unique contact or predecessor map",
        "shooting-chart amplitude normalization",
        "domain-wall lower-bound construction",
    }
    return {
        "source_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "receipt_all_gates_pass": receipt["all_gates_pass"],
        "input_contract_is_any_positive_G": "Any positive G on [-1,1]" in receipt["input_contract"],
        "all_hidden_dependencies_excluded": expected <= excluded,
        "source_does_not_import_wall_candidate": "bellman-subsolution-candidate" not in text,
    }


def main() -> None:
    orientation = index_orientation_attack()
    pivots = pivot_floor_attack()
    carrier = carrier_attack()
    weld = weld_typing_audit()
    gates = {
        "all_index_fixtures_exact": orientation["exact_square_residuals"] == orientation["fixtures"],
        "wrong_index_orientation_detected": orientation["wrong_orientation_detections"] > 0,
        "young_remainder_nonnegative": F(orientation["minimum_correct_remainder"]) >= 0,
        "no_pivot_floor_counterexample": not pivots["failures"],
        "carrier_direct_block_identity": carrier[
            "all_direct_bell_values_equal_padded_jacobi_values"
        ],
        "carrier_principal_embedding_exact": carrier[
            "all_padded_values_equal_inner_word_values"
        ],
        "weld_receipt_valid": weld["receipt_all_gates_pass"],
        "weld_accepts_arbitrary_positive_storage": weld["input_contract_is_any_positive_G"],
        "weld_excludes_failed_wall_dependencies": weld["all_hidden_dependencies_excluded"],
        "weld_source_has_no_candidate_import": weld["source_does_not_import_wall_candidate"],
    }
    report = {
        "status": "independent exact audit of Bellman--path equivalence",
        "imports_sprint_1295_verifier": False,
        "index_orientation_attack": orientation,
        "pivot_floor_attack": pivots,
        "carrier_attack": carrier,
        "weld_typing_audit": weld,
        "gates": gates,
        "all_gates_pass": all(gates.values()),
        "abstract_proof_verdict": "accept" if all(gates.values()) else "reject",
        "i3322_consequence_verdict": "accept" if all(gates.values()) else "reject",
        "claim_boundary": (
            "Accepts equality of tensor and commuting values as the common "
            "Bellman/path variational constant only; historical decimal and "
            "attainment/nonclosure claims remain open."
        ),
    }
    output = HERE / "bellman-path-independent.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
