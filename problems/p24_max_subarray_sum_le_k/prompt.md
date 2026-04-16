# Max Subarray Sum ≤ k  (Track B1)

Given an integer array `nums` (may contain negatives) and an integer `k`, return the **maximum** sum of any non-empty contiguous subarray whose sum is `≤ k`.

Guaranteed: at least one subarray qualifies.

## Signature
```python
def solution(nums: list[int], k: int) -> int
```

## Reference template (read once, then solve without peeking)

```python
from bisect import bisect_left, insort

prefixes = [0]          # sentinel: empty prefix
curr = 0
best = float('-inf')
for x in nums:
    curr += x
    # we want: subarray = curr - p  ≤  k  →  p ≥ curr - k
    # among all valid p, the smallest one gives the LARGEST subarray
    idx = bisect_left(prefixes, curr - k)
    if idx < len(prefixes):
        best = max(best, curr - prefixes[idx])
    insort(prefixes, curr)   # query BEFORE insert to avoid matching self
return best
```

## Drill focus
- `prefixes = [0]` sentinel — allows the answer to come from an empty prefix (whole-from-start subarray).
- Query **before** `insort` — otherwise you can match your own current prefix (a zero-length subarray).
- `bisect_left` for "smallest `p ≥ target`".
- `curr - prefixes[idx]` is the subarray sum; take `max`.

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[2, 2, -1]` | 3 | 3 |
| 2 | `[1, 2, 3]` | 6 | 6 |
| 3 | `[-2, 2, -1]` | 0 | 0 |
| 4 | `[5, 6, 7]` | 5 | 5 |
| 5 | `[2, -1, 2, 1, -3, 3]` | 4 | 4 |
| 6 | `[-3, -2, -1]` | -2 | -2 |
| 7 | `[3]` | 5 | 3 |
| 8 | `[1, 1, 1, 1]` | 4 | 4 |
| 9 | `[2, 1, -1, 2]` | 3 | 3 |
