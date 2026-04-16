import pytest

cases = [
    ("single match",   [[0]],                                0,  1),
    ("single exact",   [[5]],                                5,  1),
    ("single miss",    [[5]],                                0,  0),
    ("target 3",       [[1, 2], [3, 4]],                     3,  2),
    ("zero with negs", [[1, -1], [1, -1]],                   0,  3),
    ("all zeros",      [[0, 0], [0, 0]],                     0,  9),
    ("target 1",       [[1, 0], [0, 1]],                     1,  6),
    ("LC 1074",        [[0, 1, 0], [1, 1, 1], [0, 1, 0]],    0,  4),
    ("neg target",     [[1, -2, 1], [-1, 1, -1]],           -1,  9),
]


@pytest.mark.parametrize("name,matrix,target,expected", cases, ids=[c[0] for c in cases])
def test_count_submatrices_target(solution, name, matrix, target, expected):
    assert solution(matrix, target) == expected
