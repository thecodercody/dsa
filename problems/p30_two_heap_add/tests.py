import pytest

cases = [
    ("single",    [1],                [1.0]),
    ("two asc",   [1, 2],             [1.0, 1.5]),
    ("two desc",  [2, 1],             [2.0, 1.5]),
    ("three asc", [1, 2, 3],          [1.0, 1.5, 2.0]),
    ("three mix", [3, 1, 2],          [3.0, 2.0, 2.0]),
    ("negatives", [-1, -2, -3],       [-1.0, -1.5, -2.0]),
    ("all same",  [5, 5, 5],          [5.0, 5.0, 5.0]),
    ("extremes",  [1, 100, 2, 99, 3], [1.0, 50.5, 2.0, 50.5, 3.0]),
]


@pytest.mark.parametrize("name,nums,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_add(solution, name, nums, expected):
    assert solution(nums) == expected
