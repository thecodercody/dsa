import pytest

cases = [
    ("simple pair",  [0, 1],                   1),
    ("three",        [0, 1, 0],                2),
    ("alt four",     [0, 1, 0, 1],             4),
    ("grouped",      [0, 0, 1, 1],             2),
    ("all zero",     [0, 0, 0],                0),
    ("empty",        [],                       0),
    ("alt five",     [1, 0, 1, 0, 1],          6),
    ("grouped2",     [1, 1, 0, 0],             2),
    ("single",       [0],                      0),
    ("mixed seven",  [1, 0, 0, 1, 0, 1, 1],    8),
]


@pytest.mark.parametrize("name,nums,expected", cases, ids=[c[0] for c in cases])
def test_contiguous_array_count(solution, name, nums, expected):
    assert solution(nums) == expected
