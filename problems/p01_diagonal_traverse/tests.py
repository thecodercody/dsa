import pytest

cases = [
    ("3x3",    [[1,2,3],[4,5,6],[7,8,9]],              [1,2,4,7,5,3,6,8,9]),
    ("2x2",    [[1,2],[3,4]],                           [1,2,3,4]),
    ("1x1",    [[1]],                                   [1]),
    ("1x3",    [[1,2,3]],                               [1,2,3]),
    ("3x1",    [[1],[2],[3]],                           [1,2,3]),
    ("3x2",    [[1,2],[3,4],[5,6]],                     [1,2,3,5,4,6]),
    ("2x3",    [[1,2,3],[4,5,6]],                       [1,2,4,5,3,6]),
    ("3x4",    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],     [1,2,5,9,6,3,4,7,10,11,8,12]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_diagonal_traverse(solution, name, matrix, expected):
    assert solution(matrix) == expected
