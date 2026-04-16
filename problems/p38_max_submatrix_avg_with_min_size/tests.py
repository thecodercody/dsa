import pytest

cases = [
    ("1x1 ok",      [[1, 2], [3, 4]],                           1, 1, 4.0),
    ("2x2 only",    [[1, 2], [3, 4]],                           2, 2, 2.5),
    ("2x1",         [[1, 2], [3, 4]],                           2, 1, 3.0),
    ("all neg",     [[-1, -2], [-3, -4]],                       1, 1, -1.0),
    ("single cell", [[5]],                                      1, 1, 5.0),
    ("3x3 2x2",     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],          2, 2, 7.0),
    ("3x3 1x1",     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],          1, 1, 9.0),
    ("mixed 2x2",   [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5]], 2, 2, 3.5),
]


@pytest.mark.parametrize("name,matrix,min_rows,min_cols,expected", cases, ids=[c[0] for c in cases])
def test_max_submatrix_avg_with_min_size(solution, name, matrix, min_rows, min_cols, expected):
    assert solution(matrix, min_rows, min_cols) == pytest.approx(expected)
