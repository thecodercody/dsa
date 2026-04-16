import pytest

cases = [
    ("basic k=2",          [[1,3],[2,4]],            2, [[2,3]]),
    ("no overlap k=2",     [[1,2],[4,5]],            2, []),
    ("full overlap k=2",   [[1,5],[1,5]],            2, [[1,5]]),
    ("nested k=2",         [[1,10],[3,7]],           2, [[3,7]]),
    ("union k=1",          [[1,3],[5,7]],            1, [[1,3],[5,7]]),
    ("triple k=3",         [[1,3],[2,4],[3,5]],      3, [[3,3]]),
    ("three ivls k=2",     [[1,5],[2,6],[4,8]],      2, [[2,6]]),
    ("three ivls k=3",     [[1,5],[2,6],[4,8]],      3, [[4,5]]),
    ("edge overlap k=2",   [[1,3],[3,5]],            2, [[3,3]]),
    ("deeply nested k=3",  [[1,10],[2,8],[4,6]],     3, [[4,6]]),
    ("k exceeds count",    [[1,5],[2,4]],            3, []),
]


@pytest.mark.parametrize("name,intervals,k,expected", cases, ids=[c[0] for c in cases])
def test_k_coverage(solution, name, intervals, k, expected):
    assert solution(intervals, k) == expected
