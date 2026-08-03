"""Direct complex-matrix guard for the three-remainder I3322 certificate."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
Q_CERT = 250875394515 / 1_000_000_000_000


def load_algebra():
    path = HERE / "bellman_quantum_dual_verify.py"
    spec = importlib.util.spec_from_file_location("dual_algebra", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def hull_data():
    path = HERE.parent / "foundational-sprint-1179" / "minplus-hull-32001.npz"
    data = np.load(path)
    return data["slopes"], data["intercepts"], data["starts"]


def f_scalar(values: np.ndarray, hull) -> np.ndarray:
    slopes, intercepts, starts = hull
    owners = np.searchsorted(starts, values, side="right") - 1
    return slopes[owners] * values + intercepts[owners]


def functional(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.conj().T


def main() -> None:
    algebra = load_algebra()
    hull = hull_data()
    rng = np.random.default_rng(119719)
    checks = []
    for da, db in [(2, 3), (3, 5), (4, 4), (6, 3)]:
        for fixture in range(8):
            a = [algebra.random_projector(rng, da, int(rng.integers(1, da + 1))) for _ in range(3)]
            b = [algebra.random_projector(rng, db, int(rng.integers(1, db + 1))) for _ in range(3)]
            ia, ib = np.eye(da), np.eye(db)
            x, y = a[0] + a[1] - ia, a[1] - a[0]
            u, v = b[0] + b[1] - ib, b[1] - b[0]

            def a_fun(t):
                bt = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - t*t))
                ft = f_scalar(t, hull)
                fmt = f_scalar(-t, hull)
                return bt * np.sqrt(fmt / ft)

            def b_fun(t):
                bt = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - t*t))
                ft = f_scalar(t, hull)
                fmt = f_scalar(-t, hull)
                return bt * np.sqrt(ft / fmt)

            alpha_x = functional(x, lambda t: 0.5 - a_fun(t))
            beta_u = functional(u, lambda t: Q_CERT - 0.5 - b_fun(t))
            g = np.kron(x, u) + np.kron(x / 2, ib) - np.kron(ia, u / 2) - np.kron(ia, ib)
            r0 = np.kron(alpha_x, ib) + np.kron(ia, beta_u) - g
            ra = 0.5 * np.eye(da*db) - np.kron(alpha_x, ib) - np.kron(y, b[2] - ib/2)
            rb = (Q_CERT - 0.5) * np.eye(da*db) - np.kron(ia, beta_u) - np.kron(a[2] - ia/2, v)
            bell = algebra.original_bell(a, b)
            residual = r0 + ra + rb - (Q_CERT * np.eye(da*db) - bell)
            checks.append({
                "dimensions": [da, db],
                "fixture": fixture,
                "min_eigen_R0": float(np.linalg.eigvalsh(r0).min()),
                "min_eigen_RA": float(np.linalg.eigvalsh(ra).min()),
                "min_eigen_RB": float(np.linalg.eigvalsh(rb).min()),
                "assembly_residual": float(np.linalg.norm(residual, ord=2)),
            })

    report = {
        "status": "direct held-out complex-matrix remainder guard",
        "q_cert": Q_CERT,
        "fixtures": len(checks),
        "minimum_R0": min(row["min_eigen_R0"] for row in checks),
        "minimum_RA": min(row["min_eigen_RA"] for row in checks),
        "minimum_RB": min(row["min_eigen_RB"] for row in checks),
        "maximum_assembly_residual": max(row["assembly_residual"] for row in checks),
        "all_gates_pass": (
            min(min(row["min_eigen_R0"], row["min_eigen_RA"], row["min_eigen_RB"]) for row in checks) > -1e-10
            and max(row["assembly_residual"] for row in checks) < 1e-11
        ),
        "checks": checks,
        "claim_boundary": "This is a direct numerical guard using the separately certified rational hull; the exact continuum theorem is algebraic.",
    }
    output = HERE / "operator-remainder-random-guard.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "checks"}, indent=2))
    if not report["all_gates_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
