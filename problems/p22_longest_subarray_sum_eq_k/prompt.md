# Longest Subarray Sum Equals K

Return the length of the longest contiguous subarray whose sum equals `k`.

## Signature

```python
def solution(nums: list[int], k: int) -> int
```

## Drill focus

- Hashmap of **first-occurrence** prefix sum (length answer, not count/value)
- Seed `{0: -1}` so a full-prefix match gives length `i - (-1) = i + 1`
- Check `curr - k in first` and take `i - first[curr-k]`
- Only insert `curr` if not already present (first occurrence → longest span)

## Reference template

```python
def solution(nums, k):
    first = {0: -1}
    curr = 0
    best = 0
    for i, x in enumerate(nums):
        curr += x
        if curr - k in first:
            best = max(best, i - first[curr - k])
        if curr not in first:
            first[curr] = i
    return best
```

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1,-1,5,-2,3]` | 3 | 4 |
| 2 | `[1,2,3]` | 100 | 0 |
| 3 | `[5]` | 5 | 1 |
| 4 | `[1,2,3]` | 6 | 3 |
| 5 | `[1,2,3]` | 3 | 2 |
| 6 | `[-2,-1,2,1]` | 1 | 2 |
| 7 | `[]` | 0 | 0 |
| 8 | `[0,0,0]` | 0 | 3 |
| 9 | `[-1,-2,-3]` | -3 | 2 |
| 10 | `[1,0,-1,0,1]` | 0 | 4 |
