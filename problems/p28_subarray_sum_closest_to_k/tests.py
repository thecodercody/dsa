import pytest

cases = [
    ("off by one",    [1, 2, 3],          4,    1),
    ("exact hit",     [1, 2, 3],          6,    0),
    ("far above",     [1, 2, 3],          100,  94),
    ("single gap",    [1],                5,    4),
    ("neg array",     [-5, 3, -1],        0,    1),
    ("zero cancel",   [10, -10, 10],      5,    5),
    ("exact mid",     [1, 2, 3, 4, 5],   7,    0),
    ("mixed exact",   [-1, -2, 3, 2, -1], 5,   0),
    ("single exact",  [1],                1,    0),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_subarray_sum_closest_to_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
