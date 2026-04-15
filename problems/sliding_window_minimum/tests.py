import pytest

cases = [
    ("standard",          [1,3,-1,-3,5,3,6,7], 3, [-1,-3,-3,-3,3,3]),
    ("k=1",               [4,2,7,1],           1, [4,2,7,1]),
    ("k=len",             [5,2,8,1,9],         5, [1]),
    ("all equal",         [3,3,3,3],           2, [3,3,3]),
    ("sorted ascending",  [1,2,3,4,5],         3, [1,2,3]),
    ("sorted descending", [5,4,3,2,1],         3, [3,2,1]),
    ("single element",    [7],                 1, [7]),
    ("two elements",      [2,1],               2, [1]),
    ("negatives",         [-1,-2,-3,-4],       2, [-2,-3,-4]),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_sliding_window_minimum(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
