import pytest

# Note: LC 363 guarantees a valid submatrix exists for all test cases.
cases = [
    ("lc example",   [[1, 0, 1], [0, -2, 3]],              2,    2),
    ("row exact",    [[2, 2, -1]],                         3,    3),
    ("row le zero",  [[2, 2, -1]],                         0,   -1),
    ("square tight", [[1, 1], [1, 1]],                     3,    2),
    ("square loose", [[1, 1], [1, 1]],                   100,    4),
    ("all negative", [[-1, -2], [-3, -4]],                -3,   -3),
    ("3x3 loose",    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 100,   45),
    ("3x3 tight",    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  10,    9),
    ("single cell",  [[5]],                               10,    5),
]


@pytest.mark.parametrize("name,matrix,k,expected", cases, ids=[c[0] for c in cases])
def test_max_submatrix_sum_le_k(solution, name, matrix, k, expected):
    assert solution(matrix, k) == expected
