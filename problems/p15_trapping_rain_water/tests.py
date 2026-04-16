import pytest

cases = [
    ("lc example",  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ("valley",      [4, 2, 0, 3, 2, 5],                    9),
    ("deep basins", [3, 0, 2, 0, 4],                       7),
    ("single",      [5],                                   0),
    ("empty",       [],                                    0),
    ("monotone up", [1, 2, 3],                             0),
    ("monotone dn", [3, 2, 1],                             0),
    ("u shape",     [2, 0, 2],                             2),
]


@pytest.mark.parametrize("name,height,expected", cases, ids=[c[0] for c in cases])
def test_trapping_rain_water(solution, name, height, expected):
    assert solution(height) == expected
