import pytest

cases = [
    ("balanced equal",  [1, 2],       [3, 4],    2, 2, (2, 2)),
    ("balanced max+1",  [1, 2, 3],    [4, 5],    3, 2, (3, 2)),
    ("max too large",   [1, 2, 3, 4], [5, 6],    4, 2, (3, 3)),
    ("min too large",   [1],          [2, 3, 4], 1, 3, (2, 2)),
    ("max only unbal",  [1, 2],       [],        2, 0, (1, 1)),
    ("min only unbal",  [],           [1, 2],    0, 2, (1, 1)),
]


@pytest.mark.parametrize("name,max_vals,min_vals,max_size,min_size,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_rebalance(solution, name, max_vals, min_vals, max_size, min_size, expected):
    assert solution(max_vals, min_vals, max_size, min_size) == expected
