import pytest

cases = [
    ("basic",         [1, -1, 5, -2, 3], 3, 4),
    ("no match",      [1, 2, 3],       100, 0),
    ("single fits",   [5],               5, 1),
    ("whole",         [1, 2, 3],         6, 3),
    ("prefix best",   [1, 2, 3],         3, 2),
    ("mixed",         [-2, -1, 2, 1],    1, 2),
    ("empty",         [],                0, 0),
    ("zero prefix",   [0, 0, 0],         0, 3),
    ("all neg",       [-1, -2, -3],     -3, 2),
    ("interior zero", [1, 0, -1, 0, 1],  0, 4),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_longest_subarray_sum_eq_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
