import pytest

cases = [
    ("example",        [1, 2, 3, 4, 5],           2, 4),
    ("k=n",            [3, 1, 4, 1, 5],           5, 1),
    ("k=1",            [3, 1, 4, 1, 5],           1, 5),
    ("decreasing",     [5, 4, 3, 2, 1],           3, 3),
    ("increasing",     [1, 2, 3, 4, 5],           3, 3),
    ("all same",       [7, 7, 7, 7],              2, 7),
    ("valley",         [5, 1, 1, 1, 5],           2, 1),
    ("mixed",          [10, 3, 5, 4, 7, 2, 8],    3, 4),
    ("single",         [42],                      1, 42),
]


@pytest.mark.parametrize("name,arr,k,expected", cases, ids=[c[0] for c in cases])
def test_max_of_window_mins(solution, name, arr, k, expected):
    assert solution(arr, k) == expected
