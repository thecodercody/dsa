import pytest

cases = [
    ("square",    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],   [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
    ("1xN",       [[1, 2, 3]],                          [[1], [2], [3]]),
    ("Nx1",       [[1], [2], [3]],                      [[1, 2, 3]]),
    ("3x2",       [[1, 2], [3, 4], [5, 6]],             [[1, 3, 5], [2, 4, 6]]),
    ("single",    [[1]],                                [[1]]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_transpose_matrix(solution, name, matrix, expected):
    assert solution(matrix) == expected
