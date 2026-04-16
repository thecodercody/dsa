import pytest

cases = [
    ("basic",         [2, 1, 5, 6, 2, 3],    10),
    ("two bars",      [2, 4],                  4),
    ("flat",          [1, 1, 1, 1],            4),
    ("single",        [5],                     5),
    ("zero",          [0],                     0),
    ("valley",        [2, 1, 2],               3),
    ("mixed",         [6, 2, 5, 4, 5, 1, 6],  12),
    ("zero gaps",     [0, 1, 0, 1],            1),
    ("plateau dip",   [4, 2, 0, 3, 2, 5],      6),
]


@pytest.mark.parametrize("name,heights,expected", cases, ids=[c[0] for c in cases])
def test_largest_rectangle_histogram(solution, name, heights, expected):
    assert solution(heights) == expected
