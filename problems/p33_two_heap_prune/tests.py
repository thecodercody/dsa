import pytest

cases = [
    ("min no delay",    [1, 2, 3], {},              False, 1),
    ("min skip one",    [1, 2, 3], {1: 1},          False, 2),
    ("min skip two",    [1, 2, 3], {1: 1, 2: 1},    False, 3),
    ("min all delayed", [1, 2, 3], {1: 1, 2: 1, 3: 1}, False, None),
    ("max no delay",    [3, 2, 1], {},              True,  3),
    ("max skip top",    [3, 2, 1], {3: 1},          True,  2),
    ("single delayed",  [5],       {5: 1},          False, None),
    ("multi count",     [1, 2],    {1: 2},          False, 2),
]


@pytest.mark.parametrize("name,heap_vals,delayed,is_max_heap,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_prune(solution, name, heap_vals, delayed, is_max_heap, expected):
    assert solution(heap_vals, delayed, is_max_heap) == expected
