# Two-Heap: `getMedian`

Part of the two-heap sliding window median algorithm.

The two-heap structure keeps:
- **maxHeap** — lower half (stored negated). `maxSize` = virtual element count.
- **minHeap** — upper half. `minSize` = virtual element count.

The size invariant guarantees `maxSize == minSize` (even total) or `maxSize == minSize + 1` (odd total), so the median is always accessible in O(1).

## Your task

Implement `getMedian()`:

- If `maxSize == minSize` (even total elements), the median is the average of both tops: `(-maxHeap[0] + minHeap[0]) / 2`.
- Otherwise (`maxSize == minSize + 1`, odd total), the median is the max-heap top: `-maxHeap[0]` (as a float).

## Signature

```python
def getMedian(self) -> float
```

Called via `solution(max_vals, min_vals, max_size, min_size)` → `float`.  
`max_vals` are the actual values on the max side (stored negated internally).

## Test cases

| # | max side | min side | maxS | minS | Expected |
|---|---|---|---|---|---|
| 1 | `[1]` | `[]` | 1 | 0 | `1.0` |
| 2 | `[2]` | `[3]` | 1 | 1 | `2.5` |
| 3 | `[3,1]` | `[5,7]` | 2 | 2 | `4.0` |
| 4 | `[3,2,1]` | `[5,7]` | 3 | 2 | `3.0` |
| 5 | `[-1]` | `[]` | 1 | 0 | `-1.0` |
| 6 | `[-2,-3]` | `[-1]` | 2 | 1 | `-2.0` |
| 7 | `[10]` | `[20]` | 1 | 1 | `15.0` |
