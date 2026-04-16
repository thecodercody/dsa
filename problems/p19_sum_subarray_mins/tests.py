import pytest

cases = [
    ("lc example",  [3, 1, 2, 4],         17),
    ("lc larger",   [11, 81, 94, 43, 3],  444),
    ("single",      [1],                  1),
    ("increasing",  [1, 2, 3],            10),
    ("decreasing",  [3, 2, 1],            10),
    ("all equal",   [5, 5, 5],            30),
]


@pytest.mark.parametrize("name,nums,expected", cases, ids=[c[0] for c in cases])
def test_sum_subarray_mins(solution, name, nums, expected):
    assert solution(nums) == expected
