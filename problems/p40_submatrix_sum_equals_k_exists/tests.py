import pytest

cases = [
    ("top-left 3",    [[1, 2], [3, 4]],                   3,   True),
    ("impossible",    [[1, 2], [3, 4]],                   100, False),
    ("whole sum",     [[1, 2], [3, 4]],                   10,  True),
    ("zero cell",     [[0]],                               0,   True),
    ("no zero",       [[5]],                               0,   False),
    ("zero cancel",   [[1, -1], [1, -1]],                  0,   True),
    ("two adjacent",  [[1, 1], [1, 1]],                    2,   True),
    ("no five",       [[1, 1], [1, 1]],                    5,   False),
    ("whole cross",   [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 5,   True),
]


@pytest.mark.parametrize("name,matrix,target,expected", cases, ids=[c[0] for c in cases])
def test_submatrix_sum_equals_k_exists(solution, name, matrix, target, expected):
    assert solution(matrix, target) == expected
