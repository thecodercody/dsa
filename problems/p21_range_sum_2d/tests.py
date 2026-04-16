import pytest

BIG = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]

cases = [
    ("q1",         BIG,                    [(2, 1, 4, 3)],                   [8]),
    ("q2",         BIG,                    [(1, 1, 2, 2)],                   [11]),
    ("q3",         BIG,                    [(1, 2, 2, 4)],                   [12]),
    ("single cell",BIG,                    [(0, 0, 0, 0)],                   [3]),
    ("whole",      BIG,                    [(0, 0, 4, 4)],                   [58]),
    ("multi query",BIG,                    [(2, 1, 4, 3), (1, 1, 2, 2), (1, 2, 2, 4)], [8, 11, 12]),
    ("1x1",        [[5]],                  [(0, 0, 0, 0)],                   [5]),
    ("2x2 multi",  [[1, 2], [3, 4]],       [(0, 0, 1, 1), (0, 0, 0, 1), (1, 0, 1, 1)], [10, 3, 7]),
    ("neg values", [[1, -1], [1, -1]],     [(0, 0, 1, 1), (0, 0, 0, 0), (1, 1, 1, 1)], [0, 1, -1]),
]


@pytest.mark.parametrize("name,matrix,queries,expected", cases, ids=[c[0] for c in cases])
def test_range_sum_2d(solution, name, matrix, queries, expected):
    assert solution(matrix, queries) == expected
