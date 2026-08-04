"""Exact integer-arithmetic terminal-fork countermodel."""

from __future__ import annotations

import json
from pathlib import Path


def mat_vec(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def mat_mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    columns = list(zip(*right))
    return [[sum(a * b for a, b in zip(row, col)) for col in columns] for row in left]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def norm_squared(vector: list[int]) -> int:
    return sum(x * x for x in vector)


def kron(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [a * b for a in left_row for b in right_row]
        for left_row in left
        for right_row in right
    ]


def diagonal(values: list[int]) -> list[list[int]]:
    return [[value if i == j else 0 for j in range(len(values))] for i, value in enumerate(values)]


def permutation(size: int, swaps: tuple[tuple[int, int], ...]) -> list[list[int]]:
    image = list(range(size))
    for left, right in swaps:
        image[left], image[right] = image[right], image[left]
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for source, target in enumerate(image):
        matrix[target][source] = 1
    return matrix


def basis_projection(size: int, index: int) -> list[list[int]]:
    result = [[0 for _ in range(size)] for _ in range(size)]
    result[index][index] = 1
    return result


def main() -> None:
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    K_A = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
    K_B = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    G = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    G_A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    G_B = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    G_common = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
    w = [1, 1, 1]

    for K in (K_A, K_B):
        assert transpose(K) == K
        assert mat_mul(K, K) == I
        assert mat_vec(K, w) == w

    source = mat_vec(G, w)
    assert mat_vec(K_A, source) == mat_vec(G_A, w)
    assert mat_vec(K_B, source) == mat_vec(G_B, w)
    assert mat_mul(G_A, G_B) == [[0, 0, 0]] * 3

    common_A_error = sub(mat_vec(K_A, source), mat_vec(G_common, w))
    common_B_error = sub(mat_vec(K_B, source), mat_vec(G_common, w))
    assert norm_squared(common_A_error) == 1
    assert norm_squared(common_B_error) == 1

    I_minus_G = [[I[i][j] - G[i][j] for j in range(3)] for i in range(3)]
    I_minus_GA = [[I[i][j] - G_A[i][j] for j in range(3)] for i in range(3)]
    I_minus_GB = [[I[i][j] - G_B[i][j] for j in range(3)] for i in range(3)]
    assert mat_vec(K_A, mat_vec(I_minus_G, w)) == mat_vec(I_minus_GA, w)
    assert mat_vec(K_B, mat_vec(I_minus_G, w)) == mat_vec(I_minus_GB, w)

    # Tensor-factorized realization with exact coarse sign relations.
    X = diagonal([1, -1, -1, 1])
    U = diagonal([1, -1, -1, 1])
    J_A = permutation(4, ((0, 1), (2, 3)))
    S_A = permutation(4, ((0, 2), (1, 3)))
    S_B = permutation(4, ((0, 1), (2, 3)))
    J_B = permutation(4, ((0, 2), (1, 3)))
    minus_X = [[-entry for entry in row] for row in X]
    minus_U = [[-entry for entry in row] for row in U]
    assert mat_mul(mat_mul(J_A, X), J_A) == minus_X
    assert mat_mul(mat_mul(J_B, U), J_B) == minus_U

    K_A_tensor = kron(J_A, S_B)
    K_B_tensor = kron(S_A, J_B)
    identity_16 = diagonal([1] * 16)
    uniform_16 = [1] * 16
    for K_tensor in (K_A_tensor, K_B_tensor):
        assert transpose(K_tensor) == K_tensor
        assert mat_mul(K_tensor, K_tensor) == identity_16
        assert mat_vec(K_tensor, uniform_16) == uniform_16

    source_index = 0 * 4 + 0
    target_A_index = 1 * 4 + 1
    target_B_index = 2 * 4 + 2
    source_tensor = mat_vec(basis_projection(16, source_index), uniform_16)
    target_A_tensor = mat_vec(basis_projection(16, target_A_index), uniform_16)
    target_B_tensor = mat_vec(basis_projection(16, target_B_index), uniform_16)
    assert mat_vec(K_A_tensor, source_tensor) == target_A_tensor
    assert mat_vec(K_B_tensor, source_tensor) == target_B_tensor
    assert norm_squared(target_A_tensor) == norm_squared(target_B_tensor) == 1
    assert sum(a * b for a, b in zip(target_A_tensor, target_B_tensor)) == 0
    labels = [1, -1, -1, 1]
    assert (labels[1], labels[1]) == (labels[2], labels[2]) == (-1, -1)

    result = {
        "status": "exact terminal common-fork countermodel",
        "dimension": 3,
        "both_response_involutions_self_adjoint": True,
        "both_global_response_defects_zero": True,
        "both_response_specific_packet_errors_zero": True,
        "fine_targets_orthogonal_inside_one_coarse_block": True,
        "common_coarse_target_error_squared": [1, 1],
        "complement_cancellation_exact": True,
        "shared_factor_tensor_realization_dimension": [4, 4],
        "shared_factor_forms_exact": True,
        "coarse_sign_relations_exact": True,
        "tensor_targets_share_joint_coarse_label": "(-1,-1)",
        "tensor_targets_orthogonal": True,
        "scalar_terminal_commonization_proved": False,
        "all_gates_pass": True,
        "claim_boundary": (
            "This kills terminal commonization from the abstract packet "
            "hypotheses, including shared-factor and coarse sign typing. A "
            "stronger contact identity or PSD/Gram-valued transport remains "
            "possible."
        ),
    }
    target = Path(__file__).with_name("terminal-fork-guard.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
