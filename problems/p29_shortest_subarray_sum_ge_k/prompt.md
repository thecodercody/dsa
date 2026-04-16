# Shortest Subarray with Sum ≥ K

Find the length of the shortest contiguous subarray with sum ≥ k. Return -1 if none exists.

## Signature

```python
def solution(nums: list[int], k: int) -> int
```

## Drill focus

- Hybrid: prefix sums + monotonic deque **on prefix indices** (not values)
- Deque maintains strictly increasing P values; front = candidate to subtract, back = dominance prune
- Unlike prefix+bisect (max/min), here we optimize *length* (index distance), so bisect doesn't work

## Reference template

Read once, then solve without peeking.

```python
from collections import deque

def solution(nums, k):
    n = len(nums)
    P = [0] * (n + 1)
    for i, x in enumerate(nums):
        P[i + 1] = P[i] + x
    best = float('inf')
    dq = deque()        # indices into P, P-values strictly increasing
    for i, pi in enumerate(P):
        # front cleanup: any j such that pi - P[j] >= k is a valid window
        while dq and pi - P[dq[0]] >= k:
            best = min(best, i - dq.popleft())
        # back cleanup: a smaller later prefix dominates any larger earlier one
        while dq and P[dq[-1]] >= pi:
            dq.pop()
        dq.append(i)
    return best if best != float('inf') else -1
```

## Test cases

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1]` | 1 | 1 |
| 2 | `[1,2]` | 4 | -1 |
| 3 | `[2,-1,2]` | 3 | 3 |
| 4 | `[1,2,3,4,5]` | 11 | 3 |
| 5 | `[84,-37,32,40,95]` | 167 | 3 |
| 6 | `[48,99,37,4,-31]` | 140 | 2 |
| 7 | `[-1,-2,-3]` | 1 | -1 |
| 8 | `[5,-10,5,-5,10]` | 5 | 1 |
| 9 | `[17,85,93,-45,-21]` | 150 | 2 |
