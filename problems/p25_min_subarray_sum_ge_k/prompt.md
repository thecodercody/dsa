# Min Subarray Sum ≥ k  (Track B2)

Given an integer array `nums` (may contain negatives) and an integer `k`, return the **minimum** sum of any non-empty contiguous subarray whose sum is `≥ k`.

Guaranteed: at least one subarray qualifies.

This is the **mirror** of B1. Same scaffold, flipped query and flipped comparison.

## Signature
```python
def solution(nums: list[int], k: int) -> int
```

## Reference template

```python
from bisect import bisect_right, insort

prefixes = [0]
curr = 0
best = float('inf')
for x in nums:
    curr += x
    # we want: subarray = curr - p  ≥  k  →  p ≤ curr - k
    # among all valid p, the LARGEST one gives the SMALLEST subarray
    idx = bisect_right(prefixes, curr - k) - 1
    if idx >= 0:
        best = min(best, curr - prefixes[idx])
    insort(prefixes, curr)
return best
```

## Drill focus
- Flip 1: `best = inf`, `min(...)`.
- Flip 2: query is "largest `p ≤ target`" → `bisect_right - 1` (guards empty with `idx >= 0`).
- Everything else is identical to B1. Do NOT flip the comparison inside the query — only the direction.

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1, 2, 3]` | 4 | 5 |
| 2 | `[1, 2, 3]` | 6 | 6 |
| 3 | `[10]` | 5 | 10 |
| 4 | `[-1, 2, -1, 3]` | 2 | 2 |
| 5 | `[-3, -2, -1]` | -3 | -3 |
| 6 | `[2, -1, 3, -2, 4]` | 5 | 5 |
| 7 | `[1, 2]` | 0 | 1 |
| 8 | `[5, -1, 5]` | 4 | 4 |
| 9 | `[1, 5, 1]` | 5 | 5 |
