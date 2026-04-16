import pytest

cases = [
    ("basic",            [1, 2, 3],              2,    5,   4),
    ("exact",            [1, 2, 3],              3,    3,   2),
    ("mixed",            [-1, 2, -1, 3],        -1,    2,   7),
    ("empty",            [1, 2, 3],             10,   20,   0),
    ("all",              [1, 1, 1],           -100,  100,   6),
    ("zero only",        [1, -1, 2, -2],         0,    0,   3),
    ("small mix",        [-2, 5, -1],            2,    5,   4),
    ("zero v2",          [1, 2, -3, 4],          0,    0,   1),
    ("neg range",        [-2, -1, 3],           -3,   -1,   3),
]


@pytest.mark.parametrize("name,nums,lo,hi,expected", cases, ids=[c[0] for c in cases])
def test_count_subarrays_sum_in_range(solution, name, nums, lo, hi, expected):
    assert solution(nums, lo, hi) == expected
