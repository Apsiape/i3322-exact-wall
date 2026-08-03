#!/usr/bin/env python3
"""Exact normalization concordance for the I3322 release package."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def main() -> None:
    # Repository / Pal--Vertesi projector convention.
    a_marg = (0, -1, 0)
    b_marg = (-1, -2, 0)
    joint = sp.Matrix(
        [
            [1, 1, -1],
            [1, 1, 1],
            [-1, 1, 0],
        ]
    )

    # Collins--Gisin convention: A=(A2,A1,A3), B=(B2,B1,B3).
    a_perm = (1, 0, 2)
    b_perm = (1, 0, 2)
    cg_a = tuple(a_marg[i] for i in a_perm)
    cg_b = tuple(b_marg[j] for j in b_perm)
    cg_joint = joint.extract(a_perm, b_perm)
    expected_cg_joint = sp.Matrix([[1, 1, 1], [1, 1, -1], [1, -1, 0]])

    assert cg_a == (-1, 0, 0)
    assert cg_b == (-2, -1, 0)
    assert cg_joint == expected_cg_joint

    # Pal--Vertesi best-response rows, Eqs. (9)--(14) of arXiv:1006.3032.
    pal_alice = (
        (1, 1, -1, 0),
        (1, 1, 1, -1),
        (-1, 1, 0, 0),
    )
    pal_bob = (
        (1, 1, -1, -1),
        (1, 1, 1, -2),
        (-1, 1, 0, 0),
    )
    our_alice = tuple(tuple(int(joint[i, j]) for j in range(3)) + (a_marg[i],) for i in range(3))
    our_bob = tuple(tuple(int(joint[i, j]) for i in range(3)) + (b_marg[j],) for j in range(3))
    assert our_alice == pal_alice
    assert our_bob == pal_bob

    # Dichotomic conversion in CG order:
    # P_i=(I-A_i)/2, Q_j=(I+B_j)/2.
    # Then B_projector = -I + H_dichotomic/4.
    dich_a = tuple(-2 * cg_a[i] - sum(int(cg_joint[i, j]) for j in range(3)) for i in range(3))
    dich_b = tuple(2 * cg_b[j] + sum(int(cg_joint[i, j]) for i in range(3)) for j in range(3))
    dich_joint = -cg_joint
    constant_times_four = 2 * sum(cg_a) + 2 * sum(cg_b) + sum(int(x) for x in cg_joint)

    expected_dich_joint = sp.Matrix([[-1, -1, -1], [-1, -1, 1], [-1, 1, 0]])
    assert dich_a == (-1, -1, 0)
    assert dich_b == (-1, -1, 0)
    assert dich_joint == expected_dich_joint
    assert constant_times_four == -4

    output = {
        "status": "exact I3322 normalization concordance",
        "repository_projector": {
            "alice_marginals": a_marg,
            "bob_marginals": b_marg,
            "joint": [list(map(int, joint.row(i))) for i in range(3)],
        },
        "collins_gisin": {
            "alice_setting_permutation_zero_based": a_perm,
            "bob_setting_permutation_zero_based": b_perm,
            "alice_marginals": cg_a,
            "bob_marginals": cg_b,
            "joint": [list(map(int, cg_joint.row(i))) for i in range(3)],
        },
        "pal_vertesi_rows_match_exactly": True,
        "dichotomic": {
            "substitution": "P_i=(I-A_i)/2, Q_j=(I+B_j)/2",
            "alice_marginals_times_four": dich_a,
            "bob_marginals_times_four": dich_b,
            "joint_times_four": [list(map(int, dich_joint.row(i))) for i in range(3)],
            "affine_relation": "B_projector=-I+H_dichotomic/4",
        },
        "all_gates_pass": True,
    }
    (HERE / "normalization-concordance.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
