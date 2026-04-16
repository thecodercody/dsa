import pytest

cases = [
    ("center zero",  [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                     [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ("two zeros",    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                     [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ("1x2 zero",     [[1, 0]], [[0, 0]]),
    ("2x1 zero",     [[1], [0]], [[0], [0]]),
    ("corner zero",  [[0, 1], [1, 1]], [[0, 0], [0, 1]]),
    ("col has zero", [[1], [0], [3]], [[0], [0], [0]]),
    ("diag zeros",   [[1, 0], [0, 1]], [[0, 0], [0, 0]]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_set_matrix_zeros(solution, name, matrix, expected):
    m = [row[:] for row in matrix]
    result = solution(m)
    actual = result if result is not None else m
    assert actual == expected
