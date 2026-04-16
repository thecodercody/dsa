import pytest

cases = [
    ("k=3 standard", [1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
    ("k=1 all",      [1, 2, 3, 4, 5],             1, [1.0, 2.0, 3.0, 4.0, 5.0]),
    ("k=n",          [1, 2, 3, 4, 5],             5, [3.0]),
    ("k=2",          [1, 2],                       2, [1.5]),
    ("single",       [1],                          1, [1.0]),
    ("k=3 mix",      [2, 1, 5, 4, 3],             3, [2.0, 4.0, 4.0]),
    ("duplicates",   [2, 2, 2, 2],                2, [2.0, 2.0, 2.0]),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_median(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
