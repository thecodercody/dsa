# Count Subarrays with Sum ≤ k  (Track B3)

Given an integer array `nums` (may contain negatives) and an integer `k`, return the **number** of non-empty contiguous subarrays whose sum is `≤ k`.

## Signature
```python
def solution(nums: list[int], k: int) -> int
```

## Reference template

```python
from bisect import bisect_left, insort

prefixes = [0]
curr = 0
count = 0
for x in nums:
    curr += x
    # we want: subarray = curr - p  ≤  k  →  p ≥ curr - k
    # COUNT all valid p, not just best one
    idx = bisect_left(prefixes, curr - k)
    count += len(prefixes) - idx
    insort(prefixes, curr)
return count
```

## Drill focus
- Same query shape as B1, but instead of tracking the best value you count how many prefixes are ≥ target.
- `len(prefixes) - idx` because everything from `idx` onward qualifies (they are all ≥ target thanks to `bisect_left`).
- Still query **before** `insort`.

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1, 2, 3]` | 6 | 6 |
| 2 | `[1, 2, 3]` | 3 | 4 |
| 3 | `[-1, 2, -3]` | 0 | 4 |
| 4 | `[-3, -2, -1]` | 0 | 6 |
| 5 | `[5, 6, 7]` | 4 | 0 |
| 6 | `[3]` | 3 | 1 |
| 7 | `[1, -2, 3, -4, 5]` | 0 | 6 |
| 8 | `[2, 2, 2]` | 100 | 6 |
| 9 | `[1, -1]` | 0 | 2 |
