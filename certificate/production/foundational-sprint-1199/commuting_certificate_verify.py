"""Symbolic and hidden-direct-sum guards for the commuting I3322 certificate."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
HULL = HERE.parent / "foundational-sprint-1179" / "minplus-hull-32001.npz"
Q_CERT = 250875394515 / 1_000_000_000_000


def projector(rng: np.random.Generator, n: int, rank: int) -> np.ndarray:
    raw = rng.normal(size=(n, rank)) + 1j * rng.normal(size=(n, rank))
    q, _ = np.linalg.qr(raw)
    return q @ q.conj().T


def direct_sum(blocks: list[np.ndarray]) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    out = np.zeros((size, size), dtype=complex)
    start = 0
    for block in blocks:
        stop = start + block.shape[0]
        out[start:stop, start:stop] = block
        start = stop
    return out


def functional(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.conj().T


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def main() -> None:
    # Exact 2x2 multiplicity-fiber factorization.
    ap, am, bb, z = sp.symbols("A_plus A_minus b z", positive=True)
    root_ap, root_am = sp.sqrt(ap), sp.sqrt(am)
    local = sp.Matrix([[ap, -2 * bb * z], [-2 * bb * z, am]])
    middle = sp.Matrix([[1, -2 * z], [-2 * z, 1]])
    roots = sp.diag(root_ap, root_am)
    factor = roots * middle * roots
    factor_residual = factor.applyfunc(lambda value: sp.simplify(value.subs(sp.sqrt(ap * am), bb))) - local
    factor_residual = factor_residual.applyfunc(
        lambda value: sp.simplify(value.subs(sp.sqrt(ap) * sp.sqrt(am), bb))
    )
    middle_characteristic = sp.factor(middle.det())

    data = np.load(HULL)
    hull = data["slopes"], data["intercepts"], data["starts"]

    def f_scalar(values: np.ndarray) -> np.ndarray:
        slopes, intercepts, starts = hull
        owners = np.searchsorted(starts, values, side="right") - 1
        return slopes[owners] * values + intercepts[owners]

    def a_fun(t: np.ndarray) -> np.ndarray:
        bt = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - t * t))
        return bt * np.sqrt(f_scalar(-t) / f_scalar(t))

    def b_fun(t: np.ndarray) -> np.ndarray:
        bt = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - t * t))
        return bt * np.sqrt(f_scalar(t) / f_scalar(-t))

    rng = np.random.default_rng(119901)
    checks = []
    sector_families = [
        [(2, 2), (2, 3)],
        [(2, 3), (3, 2)],
        [(3, 2), (2, 2), (2, 3)],
        [(3, 3), (2, 2)],
    ]
    for family_index, sectors in enumerate(sector_families):
        for fixture in range(5):
            a_blocks = [[], [], []]
            b_blocks = [[], [], []]
            for da, db in sectors:
                ia, ib = np.eye(da), np.eye(db)
                local_a = [projector(rng, da, int(rng.integers(1, da + 1))) for _ in range(3)]
                local_b = [projector(rng, db, int(rng.integers(1, db + 1))) for _ in range(3)]
                for k in range(3):
                    a_blocks[k].append(np.kron(local_a[k], ib))
                    b_blocks[k].append(np.kron(ia, local_b[k]))
            a = [direct_sum(blocks) for blocks in a_blocks]
            b = [direct_sum(blocks) for blocks in b_blocks]

            # Hide the spatial/direct-sum coordinates with one global unitary.
            n = a[0].shape[0]
            raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            unitary, _ = np.linalg.qr(raw)
            a = [unitary @ item @ unitary.conj().T for item in a]
            b = [unitary @ item @ unitary.conj().T for item in b]
            identity = np.eye(n)

            x, y = a[0] + a[1] - identity, a[1] - a[0]
            u, v = b[0] + b[1] - identity, b[1] - b[0]
            alpha_x = functional(x, lambda t: 0.5 - a_fun(t))
            beta_u = functional(u, lambda t: Q_CERT - 0.5 - b_fun(t))
            g = x @ u + x / 2 - u / 2 - identity
            r0 = alpha_x + beta_u - g
            ra = 0.5 * identity - alpha_x - y @ (b[2] - identity / 2)
            rb = (Q_CERT - 0.5) * identity - beta_u - (a[2] - identity / 2) @ v

            bell = -a[1] - b[0] - 2 * b[1]
            for coefficient, ai, bj in [
                (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1),
                (-1, 0, 2), (1, 1, 2), (-1, 2, 0), (1, 2, 1),
            ]:
                bell += coefficient * (a[ai] @ b[bj])
            assembly = r0 + ra + rb - (Q_CERT * identity - bell)
            max_cross_commutator = max(
                float(np.linalg.norm(commutator(ai, bj), ord=2))
                for ai in a for bj in b
            )
            checks.append({
                "family": family_index,
                "fixture": fixture,
                "dimension": n,
                "max_cross_commutator": max_cross_commutator,
                "minimum_R0": float(np.linalg.eigvalsh(r0).min()),
                "minimum_RA": float(np.linalg.eigvalsh(ra).min()),
                "minimum_RB": float(np.linalg.eigvalsh(rb).min()),
                "assembly_residual": float(np.linalg.norm(assembly, ord=2)),
            })

    exact_factor_zero = all(value == 0 for value in factor_residual)
    report = {
        "status": "commutant factorization plus hidden direct-sum commuting guards",
        "exact_local_factor_residual": [[str(value) for value in row] for row in factor_residual.tolist()],
        "middle_determinant": str(middle_characteristic),
        "middle_spectrum": "1+/-2z, nonnegative for |z|<=1/2",
        "fixtures": len(checks),
        "maximum_cross_commutator": max(row["max_cross_commutator"] for row in checks),
        "minimum_R0": min(row["minimum_R0"] for row in checks),
        "minimum_RA": min(row["minimum_RA"] for row in checks),
        "minimum_RB": min(row["minimum_RB"] for row in checks),
        "maximum_assembly_residual": max(row["assembly_residual"] for row in checks),
        "all_gates_pass": (
            exact_factor_zero
            and sp.factor(middle_characteristic - (1 - 4 * z**2)) == 0
            and max(row["max_cross_commutator"] for row in checks) < 1e-11
            and min(
                min(row["minimum_R0"], row["minimum_RA"], row["minimum_RB"])
                for row in checks
            ) > -1e-10
            and max(row["assembly_residual"] for row in checks) < 1e-11
        ),
        "checks": checks,
        "claim_boundary": (
            "The exact factorization is representation-free. The numerical fixtures "
            "are hidden finite direct sums and guard implementation only."
        ),
    }
    output = HERE / "commuting-certificate-audit.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "checks"}, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
