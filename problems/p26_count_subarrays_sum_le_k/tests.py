import pytest

cases = [
    ("all fit big k",    [1, 2, 3],             6,   6),
    ("tight",            [1, 2, 3],             3,   4),
    ("zero with negs",   [-1, 2, -3],           0,   4),
    ("all neg",          [-3, -2, -1],          0,   6),
    ("none",             [5, 6, 7],             4,   0),
    ("single",           [3],                   3,   1),
    ("mixed",            [1, -2, 3, -4, 5],     0,   6),
    ("all equal",        [2, 2, 2],             100, 6),
    ("sentinel zero",    [1, -1],               0,   2),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_count_subarrays_sum_le_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
