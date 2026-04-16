import pytest

cases = [
    ("lc example",   [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]],  6),
    ("single one",   [[1]],                                                 1),
    ("single zero",  [[0]],                                                 0),
    ("full 2x2",     [[1,1],[1,1]],                                         4),
    ("empty 2x2",    [[0,0],[0,0]],                                         0),
    ("checkerboard", [[1,0,1],[0,1,0],[1,0,1]],                             1),
    ("full 2x3",     [[1,1,1],[1,1,1]],                                     6),
    ("L shape",      [[1,0],[1,1]],                                         2),
    ("wide block",   [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]],            8),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_maximal_rectangle_ones(solution, name, matrix, expected):
    assert solution(matrix) == expected
