import pytest

cases = [
    ("lc example",  [100, 80, 60, 70, 60, 75, 85],  [1, 1, 1, 2, 1, 4, 6]),
    ("increasing",  [10, 20, 30, 40],               [1, 2, 3, 4]),
    ("decreasing",  [40, 30, 20, 10],               [1, 1, 1, 1]),
    ("single",      [10],                           [1]),
    ("empty",       [],                             []),
    ("zigzag",      [100, 90, 100, 90, 100],        [1, 1, 3, 1, 5]),
]


@pytest.mark.parametrize("name,prices,expected", cases, ids=[c[0] for c in cases])
def test_stock_span(solution, name, prices, expected):
    assert solution(prices) == expected
