import pytest

cases = [
    ("remove min",       [1, 2, 3],       [1],       2.5),   # {2,3}
    ("remove max",       [1, 2, 3],       [3],       1.5),   # {1,2}
    ("remove mid",       [1, 3, 4],       [3],       2.5),   # {1,4}
    ("remove two",       [1, 2, 3, 4, 5], [1, 2],    4.0),   # {3,4,5}
    ("duplicates",       [1, 3, 5, 5, 5], [5],       4.0),   # {1,3,5,5}
    ("remove both ends", [2, 4, 6, 8, 10],[4, 6],    8.0),   # {2,8,10}
    ("leave one lo",     [1, 2],          [1],       2.0),   # {2}
    ("leave one hi",     [1, 2],          [2],       1.0),   # {1}
]


@pytest.mark.parametrize("name,nums_to_add,nums_to_remove,expected", cases, ids=[c[0] for c in cases])
def test_two_heap_remove(solution, name, nums_to_add, nums_to_remove, expected):
    assert solution(nums_to_add, nums_to_remove) == expected
