# Two-Heap: Sliding Window Median (main loop)

Given an integer array `nums` and window size `k`, return the median of each window as it slides from left to right.

All five helper functions are already implemented for you: `add`, `rebalance`, `prune`, `remove`, `getMedian`. Your job is to wire them together into the sliding window loop.

## Algorithm outline

1. **Seed** the first window: call `add(nums[i])` for `i in range(k)`. Record `getMedian()`.
2. **Slide**: for each subsequent index `i` from `k` to `len(nums)-1`:
   - `add(nums[i])` — bring in the new right element.
   - `remove(nums[i - k])` — evict the element that just left the window.
   - Append `getMedian()`.
3. Return the collected medians.

## Signature

```python
def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]
```

Called via `solution(nums, k)` → `List[float]`.

## Example

```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Window            Sorted       Median
[1  3 -1]        [-1, 1, 3]   1.0
[3 -1 -3]        [-3,-1, 3]  -1.0
[-1 -3  5]       [-3,-1, 5]  -1.0
[-3  5  3]       [-3, 3, 5]   3.0
[5  3  6]        [ 3, 5, 6]   5.0
[3  6  7]        [ 3, 6, 7]   6.0

→ [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

## Test cases

| # | `nums` | `k` | Expected |
|---|---|---|---|
| 1 | `[1,3,-1,-3,5,3,6,7]` | 3 | `[1.0,-1.0,-1.0,3.0,5.0,6.0]` |
| 2 | `[1,2,3,4,5]` | 1 | `[1.0,2.0,3.0,4.0,5.0]` |
| 3 | `[1,2,3,4,5]` | 5 | `[3.0]` |
| 4 | `[1,2]` | 2 | `[1.5]` |
| 5 | `[1]` | 1 | `[1.0]` |
| 6 | `[2,1,5,4,3]` | 3 | `[2.0,4.0,4.0]` |
| 7 | `[2,2,2,2]` | 2 | `[2.0,2.0,2.0]` |
