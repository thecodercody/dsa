# Subarray Sum Closest to K

Find the minimum `|subarray_sum - k|` over all non-empty contiguous subarrays.

## Signature

```python
def solution(nums: list[int], k: int) -> int
```

## Drill focus

- Prefix sum + bisect_left + insort scaffold (same as max_subarray_sum_le_k)
- Key difference: inspect **both neighbors** of the insertion point (`idx` and `idx-1`)
- "Closest to" requires two-sided check; one-sided bisect is insufficient

## Reference template

Read once, then solve without peeking.

```python
from bisect import bisect_left, insort

def solution(nums, k):
    prefixes = [0]
    curr = 0
    best = float('inf')
    for x in nums:
        curr += x
        target = curr - k
        idx = bisect_left(prefixes, target)
        for j in (idx, idx - 1):
            if 0 <= j < len(prefixes):
                best = min(best, abs(curr - prefixes[j] - k))
        insort(prefixes, curr)
    return best
```

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1,2,3]` | 4 | 1 |
| 2 | `[1,2,3]` | 6 | 0 |
| 3 | `[1,2,3]` | 100 | 94 |
| 4 | `[1]` | 5 | 4 |
| 5 | `[-5,3,-1]` | 0 | 1 |
| 6 | `[10,-10,10]` | 5 | 5 |
| 7 | `[1,2,3,4,5]` | 7 | 0 |
| 8 | `[-1,-2,3,2,-1]` | 5 | 0 |
| 9 | `[1]` | 1 | 0 |
