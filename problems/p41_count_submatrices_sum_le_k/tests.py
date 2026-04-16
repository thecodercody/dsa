import pytest

cases = [
    ("single fits",    [[5]],                              5,    1),
    ("single exceeds", [[5]],                              4,    0),
    ("all fit",        [[1, 2], [3, 4]],                 100,    9),
    ("tight k=3",      [[1, 2], [3, 4]],                   3,    4),
    ("all neg",        [[-1, -2], [-3, -4]],               0,    9),
    ("all zeros",      [[0, 0], [0, 0]],                   0,    9),
    ("mixed",          [[1, -1], [1, -1]],                 0,    6),
    ("2x3 mix",        [[1, 0, 1], [0, -2, 3]],            2,   15),
    ("1 row",          [[1, -2, 3, -1, 2]],                1,    8),
]


@pytest.mark.parametrize("name,matrix,k,expected", cases, ids=[c[0] for c in cases])
def test_count_submatrices_sum_le_k(solution, name, matrix, k, expected):
    assert solution(matrix, k) == expected
