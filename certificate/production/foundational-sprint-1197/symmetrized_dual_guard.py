"""Numerical guard for the geometrically symmetrized Bellman dual."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
HULL = HERE.parent / "foundational-sprint-1179" / "minplus-hull-32001.npz"
Q_STAR = 0.250875384513976536


def main() -> None:
    data = np.load(HULL)
    slopes = data["slopes"]
    intercepts = data["intercepts"]
    starts = data["starts"]
    grid = np.linspace(-1.0, 1.0, 32001)
    owners = np.searchsorted(starts, grid, side="right") - 1
    f = slopes[owners] * grid + intercepts[owners]
    b = 0.5 * np.sqrt(np.maximum(0.0, 1.0 - grid**2))

    a_potential = np.zeros_like(grid)
    b_potential = np.zeros_like(grid)
    interior = b > 0
    a_potential[interior] = b[interior] * np.sqrt(f[::-1][interior] / f[interior])
    b_potential[interior] = b[interior] * np.sqrt(f[interior] / f[::-1][interior])

    maximum = -np.inf
    argmax = (0, 0)
    for j, u in enumerate(grid):
        values = grid * (u + 0.5) + a_potential
        i = int(np.argmax(values))
        candidate = values[i] + b_potential[j] - u / 2 - 1
        if candidate > maximum:
            maximum = float(candidate)
            argmax = (i, j)

    report = {
        "status": "numerical guard for corrected geometric dual",
        "grid_size": len(grid),
        "dual_ceiling": maximum,
        "exact_wall_reference": Q_STAR,
        "dual_excess": maximum - Q_STAR,
        "argmax": [float(grid[argmax[0]]), float(grid[argmax[1]])],
        "max_A_product_residual": float(np.max(np.abs(a_potential * a_potential[::-1] - b**2))),
        "max_B_product_residual": float(np.max(np.abs(b_potential * b_potential[::-1] - b**2))),
        "passes_registered_guard": maximum - Q_STAR < 1e-10,
        "claim_boundary": "The continuum proof is symbolic; this hull calculation is a hostile numerical normalization and endpoint guard only.",
    }
    output = HERE / "symmetrized-dual-guard.json"
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["passes_registered_guard"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
