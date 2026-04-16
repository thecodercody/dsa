import pytest

cases = [
    ("1x1 pos",       [[5]],                         5),
    ("1x1 neg",       [[-3]],                       -3),
    ("all pos 2x2",   [[1, 2], [3, 4]],             10),
    ("mixed 2x2",     [[1, -2], [3, 4]],             7),
    ("wide row",      [[-2, 1, 3, -1, 4]],           7),
    ("tall col",      [[-2], [1], [3], [-1], [4]],   7),
    ("all neg",       [[-1, -2], [-3, -4]],         -1),
    ("small mix",     [[1, -1, 1], [1, 1, -1]],      2),
    ("row wins",      [[1, 2, 3], [-5, -5, -5]],     6),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_max_submatrix_sum(solution, name, matrix, expected):
    assert solution(matrix) == expected
