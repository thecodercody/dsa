import pytest

cases = [
    ("basic",            [2, 2, -1],            3,  3),
    ("exact whole",      [1, 2, 3],             6,  6),
    ("neg k=0",          [-2, 2, -1],           0,  0),
    ("pos tight",        [5, 6, 7],             5,  5),
    ("mixed tight",      [2, -1, 2, 1, -3, 3],  4,  4),
    ("negative k",       [-3, -2, -1],         -2, -2),
    ("single fits",      [3],                   5,  3),
    ("whole fits",       [1, 1, 1, 1],          4,  4),
    ("two equal best",   [2, 1, -1, 2],         3,  3),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_max_subarray_sum_le_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
