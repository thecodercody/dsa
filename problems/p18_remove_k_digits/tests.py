import pytest

cases = [
    ("lc example",    "1432219", 3, "1219"),
    ("zero jump",     "10200",   1, "200"),
    ("all removed",   "10",      2, "0"),
    ("keep start",    "1234",    2, "12"),
    ("strict dec",    "9876",    3, "6"),
    ("dup",           "112",     1, "11"),
    ("zeros after",   "10001",   4, "0"),
    ("tail keep",     "5337",    2, "33"),
]


@pytest.mark.parametrize("name,num,k,expected", cases, ids=[c[0] for c in cases])
def test_remove_k_digits(solution, name, num, k, expected):
    assert solution(num, k) == expected
