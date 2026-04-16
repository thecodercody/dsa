# Count Subarrays with Sum in [lo, hi]  (Track B4)

Given an integer array `nums` and integers `lo ≤ hi`, return the number of non-empty contiguous subarrays whose sum `s` satisfies `lo ≤ s ≤ hi`.

## Signature
```python
def solution(nums: list[int], lo: int, hi: int) -> int
```

## Reference template

```python
from bisect import bisect_left, bisect_right, insort

prefixes = [0]
curr = 0
count = 0
for x in nums:
    curr += x
    # subarray = curr - p  must be in [lo, hi]
    # so p must be in [curr - hi, curr - lo]
    left  = bisect_left(prefixes,  curr - hi)
    right = bisect_right(prefixes, curr - lo)
    count += right - left
    insort(prefixes, curr)
return count
```

## Drill focus
- **Two** bisect calls. `bisect_left` for the inclusive lower bound, `bisect_right` for the inclusive upper bound.
- Watch the flip: `subarray ≥ lo` becomes `p ≤ curr - lo`; `subarray ≤ hi` becomes `p ≥ curr - hi`. The subtraction reverses the inequality.
- `right - left` counts everything in `[curr - hi, curr - lo]`.

## Test cases

| # | nums | lo | hi | expected |
|---|---|---|---|---|
| 1 | `[1, 2, 3]` | 2 | 5 | 4 |
| 2 | `[1, 2, 3]` | 3 | 3 | 2 |
| 3 | `[-1, 2, -1, 3]` | -1 | 2 | 7 |
| 4 | `[1, 2, 3]` | 10 | 20 | 0 |
| 5 | `[1, 1, 1]` | -100 | 100 | 6 |
| 6 | `[1, -1, 2, -2]` | 0 | 0 | 3 |
| 7 | `[-2, 5, -1]` | 2 | 5 | 4 |
| 8 | `[1, 2, -3, 4]` | 0 | 0 | 1 |
| 9 | `[-2, -1, 3]` | -3 | -1 | 3 |
