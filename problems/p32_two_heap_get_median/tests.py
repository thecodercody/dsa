import pytest

cases = [
    ("single",       [1],      [],      1, 0, 1.0),
    ("even two",     [2],      [3],     1, 1, 2.5),
    ("even four",    [3, 1],   [5, 7],  2, 2, 4.0),
    ("odd three",    [3, 2, 1],[5, 7],  3, 2, 3.0),
    ("negative",     [-1],     [],      1, 0, -1.0),
    ("neg max side", [-2, -3], [-1],    2, 1, -2.0),
    ("large values", [10],     [20],    1, 1, 15.0),
]


@pytest.mark.parametrize("name,max_vals,min_vals,max_size,min_size,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_get_median(solution, name, max_vals, min_vals, max_size, min_size, expected):
    assert solution(max_vals, min_vals, max_size, min_size) == expected
