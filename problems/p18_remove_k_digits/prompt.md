# Remove K Digits

Remove exactly `k` digits from `num` (as a string) to produce the smallest possible resulting number.

## Signature

```python
def solution(num: str, k: int) -> str
```

## Drill focus

- **Lexicographic monotonic stack** — different objective from "next greater" family
- Greedy: for each digit, pop while `stack[-1] > digit` and `k > 0` (removes expensive prefixes)
- If `k` still > 0 at end, pop from the right
- Strip leading zeros; return `"0"` if empty

## Reference template

```python
def solution(num, k):
    stack = []
    for c in num:
        while stack and k and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    while k:
        stack.pop()
        k -= 1
    result = "".join(stack).lstrip("0")
    return result or "0"
```

## Test cases

| # | num | k | expected |
|---|---|---|---|
| 1 | `"1432219"` | 3 | `"1219"` |
| 2 | `"10200"` | 1 | `"200"` |
| 3 | `"10"` | 2 | `"0"` |
| 4 | `"1234"` | 2 | `"12"` |
| 5 | `"9876"` | 3 | `"6"` |
| 6 | `"112"` | 1 | `"11"` |
| 7 | `"10001"` | 4 | `"0"` |
| 8 | `"5337"` | 2 | `"33"` |
