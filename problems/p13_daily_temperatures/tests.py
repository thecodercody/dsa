import pytest

cases = [
    ("lc example",  [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ("increasing",  [30, 40, 50, 60],                 [1, 1, 1, 0]),
    ("sparse",      [30, 60, 90],                     [1, 1, 0]),
    ("decreasing",  [90, 80, 70],                     [0, 0, 0]),
    ("single",      [50],                             [0]),
    ("empty",       [],                               []),
]


@pytest.mark.parametrize("name,temperatures,expected", cases, ids=[c[0] for c in cases])
def test_daily_temperatures(solution, name, temperatures, expected):
    assert solution(temperatures) == expected
