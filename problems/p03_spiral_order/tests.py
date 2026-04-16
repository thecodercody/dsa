import pytest

cases = [
    ("3x3",    [[1,2,3],[4,5,6],[7,8,9]],                          [1,2,3,6,9,8,7,4,5]),
    ("3x4",    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],                 [1,2,3,4,8,12,11,10,9,5,6,7]),
    ("1x1",    [[1]],                                               [1]),
    ("1x2",    [[1,2]],                                             [1,2]),
    ("2x1",    [[1],[2]],                                           [1,2]),
    ("2x2",    [[1,2],[3,4]],                                       [1,2,4,3]),
    ("2x3",    [[1,2,3],[4,5,6]],                                   [1,2,3,6,5,4]),
    ("3x2",    [[1,2],[3,4],[5,6]],                                 [1,2,4,6,5,3]),
    ("1x5",    [[1,2,3,4,5]],                                       [1,2,3,4,5]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_spiral_order(solution, name, matrix, expected):
    assert solution(matrix) == expected
