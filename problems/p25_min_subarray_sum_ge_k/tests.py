import pytest

cases = [
    ("basic",            [1, 2, 3],             4,  5),
    ("exact whole",      [1, 2, 3],             6,  6),
    ("single large",     [10],                  5, 10),
    ("neg with pos k",   [-1, 2, -1, 3],        2,  2),
    ("all neg",          [-3, -2, -1],         -3, -3),
    ("mixed",            [2, -1, 3, -2, 4],     5,  5),
    ("small k",          [1, 2],                0,  1),
    ("tight",            [5, -1, 5],            4,  4),
    ("large k single",   [1, 5, 1],             5,  5),
]


@pytest.mark.parametrize("name,nums,k,expected", cases, ids=[c[0] for c in cases])
def test_min_subarray_sum_ge_k(solution, name, nums, k, expected):
    assert solution(nums, k) == expected
