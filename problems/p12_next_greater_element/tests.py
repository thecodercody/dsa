import pytest

cases = [
    ("basic",       [2, 1, 3],                [3, 3, -1]),
    ("increasing",  [1, 2, 3, 4],             [2, 3, 4, -1]),
    ("decreasing",  [4, 3, 2, 1],             [-1, -1, -1, -1]),
    ("valleys",     [2, 7, 3, 5, 4, 6, 8],    [7, 8, 5, 6, 6, 8, -1]),
    ("single",      [5],                      [-1]),
    ("empty",       [],                       []),
    ("all equal",   [1, 1, 1],                [-1, -1, -1]),
    ("mixed",       [3, 1, 4, 1, 5, 9, 2, 6], [4, 4, 5, 5, 9, -1, 6, -1]),
]


@pytest.mark.parametrize("name,nums,expected", cases, ids=[c[0] for c in cases])
def test_next_greater_element(solution, name, nums, expected):
    assert solution(nums) == expected
