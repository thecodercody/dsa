# Max of Window Minimums

Given an array `arr` and a window length `k`, for every contiguous subarray of length `k`, find the minimum. Return the **maximum** of those minimums.

## Example
```
arr = [1, 2, 3, 4, 5], k = 2
windows: [1,2], [2,3], [3,4], [4,5]
mins:    [ 1,   2,    3,    4 ]
answer:  4
```

## Signature
```python
def solution(arr: list[int], k: int) -> int
```

## Constraints
- `1 ≤ n ≤ 10^6`
- `1 ≤ arr[i] ≤ 10^9`
- `1 ≤ k ≤ n`

An O(n·k) brute force (min of every window) times out at `n = 10^6`. Use a monotonic-increasing deque to emit each window's min in amortized O(1) — same pattern as `sliding_window_minimum`, just take the max of the emitted mins.

## Reference template

```python
from collections import deque

def solution(arr, k):
    q = deque()       # indices, values arr[q[i]] strictly? non-strictly increasing
    best = float('-inf')
    for r, v in enumerate(arr):
        # evict indices that fell out of the window
        while q and q[0] <= r - k:
            q.popleft()
        # maintain monotonicity (min at front)
        while q and arr[q[-1]] > v:
            q.pop()
        q.append(r)
        if r >= k - 1:
            best = max(best, arr[q[0]])
    return best
```

## Drill focus
- Exact same deque pattern as `sliding_window_minimum`.
- Only difference: instead of appending each window min to a list, fold them into a running `max`.

## Test cases

| # | arr | k | expected |
|---|---|---|---|
| 1 | `[1,2,3,4,5]` | 2 | 4 |
| 2 | `[3,1,4,1,5]` | 5 | 1 |
| 3 | `[3,1,4,1,5]` | 1 | 5 |
| 4 | `[5,4,3,2,1]` | 3 | 3 |
| 5 | `[1,2,3,4,5]` | 3 | 3 |
| 6 | `[7,7,7,7]` | 2 | 7 |
| 7 | `[5,1,1,1,5]` | 2 | 1 |
| 8 | `[10,3,5,4,7,2,8]` | 3 | 4 |
| 9 | `[42]` | 1 | 42 |
