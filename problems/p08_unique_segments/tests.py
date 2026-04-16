import pytest

cases = [
    ("basic overlap",      [[1,3], [2,4]],                  [[1,1], [4,4]]),
    ("no overlap",         [[1,2], [4,5]],                  [[1,2], [4,5]]),
    ("full overlap",       [[1,5], [1,5]],                  []),
    ("nested",             [[1,10], [3,7]],                 [[1,2], [8,10]]),
    ("multiple overlaps",  [[1,3], [2,4], [3,5]],           [[1,1], [5,5]]),
    ("mixed",              [[1,3], [2,4], [6,11], [8,9]],   [[1,1], [4,4], [6,7], [10,11]]),
    ("single",             [[5,10]],                        [[5,10]]),
    ("touching",           [[1,2], [3,4]],                  [[1,2], [3,4]]),
    ("edge overlap",       [[1,3], [3,5]],                  [[1,2], [4,5]]),
]


@pytest.mark.parametrize("name,intervals,expected", cases, ids=[c[0] for c in cases])
def test_unique_segments(solution, name, intervals, expected):
    assert solution(intervals) == expected
