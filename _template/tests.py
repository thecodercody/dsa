def test_name(solution):
    tests = [
        # (input, expected),
    ]

    for i, (args, expected) in enumerate(tests):
        result = solution(args)
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
