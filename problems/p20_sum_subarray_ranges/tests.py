import pytest

cases = [
    ("lc example",  [1, 2, 3],          4),
    ("dup max",     [1, 3, 3],          4),
    ("mixed",       [4, -2, -3, 4, 1], 59),
    ("single",      [1],                0),
    ("all equal",   [5, 5, 5],          0),
    ("two",         [1, 2],             1),
]


@pytest.mark.parametrize("name,nums,expected", cases, ids=[c[0] for c in cases])
def test_sum_subarray_ranges(solution, name, nums, expected):
    assert solution(nums) == expected
