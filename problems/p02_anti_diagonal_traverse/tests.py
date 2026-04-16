import pytest

cases = [
    ("3x3",    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 3, 5, 7, 6, 8, 9]),
    ("2x2",    [[1, 2], [3, 4]],                    [1, 2, 3, 4]),
    ("single", [[1]],                               [1]),
    ("1xN",    [[1, 2, 3]],                         [1, 2, 3]),
    ("Nx1",    [[1], [2], [3]],                     [1, 2, 3]),
    ("3x4",    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
               [1, 2, 5, 3, 6, 9, 4, 7, 10, 8, 11, 12]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_anti_diagonal_traverse(solution, name, matrix, expected):
    assert solution(matrix) == expected
