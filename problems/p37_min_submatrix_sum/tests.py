import pytest

cases = [
    ("1x1 pos",       [[5]],                         5),
    ("1x1 neg",       [[-3]],                       -3),
    ("all pos",       [[1, 2], [3, 4]],              1),
    ("mixed 2x2",     [[1, -2], [3, 4]],            -2),
    ("all neg",       [[-1, -2], [-3, -4]],        -10),
    ("wide row",      [[2, -3, -4, 1, 5]],          -7),
    ("tall col",      [[2], [-3], [-4], [1], [5]], -7),
    ("col wins",      [[1, -5], [2, -5], [3, -5]],-15),
    ("2x3 mix",       [[-1, -2, 3], [4, -5, -6]], -11),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_min_submatrix_sum(solution, name, matrix, expected):
    assert solution(matrix) == expected
