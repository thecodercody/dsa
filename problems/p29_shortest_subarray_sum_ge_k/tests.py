import pytest

cases = [
    ("single exact",  [1],              1,    1),
    ("impossible",    [1, 2],           4,   -1),
    ("negatives",     [2, -1, 2],       3,    3),
    ("end window",    [1, 2, 3, 4, 5],  11,   3),
    ("mixed large",   [84, -37, 32, 40, 95],  167, 3),
    ("front two",     [48, 99, 37, 4, -31],   140, 2),
    ("all neg",       [-1, -2, -3],     1,   -1),
    ("early hit",     [5, -10, 5, -5, 10],    5,  1),
    ("pair",          [17, 85, 93, -45, -21], 150, 2),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_shortest_subarray_sum_ge_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
