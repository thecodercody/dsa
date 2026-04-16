import pytest

cases = [
    ("3x3",    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ("2x2",    [[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ("4x4",    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
               [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]),
]


@pytest.mark.parametrize("name,matrix,expected", cases, ids=[c[0] for c in cases])
def test_rotate_image(solution, name, matrix, expected):
    m = [row[:] for row in matrix]
    result = solution(m)
    # Accept either in-place (mutates m, returns None or m) or pure (returns new)
    actual = result if result is not None else m
    assert actual == expected
