# Two-Heap: `add`

Part of the two-heap sliding window median algorithm. The algorithm maintains two heaps:

- **maxHeap** — the lower half of seen numbers (stored negated so Python's min-heap acts as a max-heap).
- **minHeap** — the upper half of seen numbers (stored normally).

Virtual sizes `maxSize` and `minSize` track how many elements each side logically contains (accounting for lazy deletions via `delayed`).

**Invariant after every operation:** `maxSize == minSize` (even total) or `maxSize == minSize + 1` (odd total). This means the median is always at the top of `maxHeap` (or the average of both tops for even).

## Your task

Implement `add(num)`:

1. If `maxHeap` is empty **or** `num <= top of maxHeap` (`-maxHeap[0]`), push `num` to `maxHeap` (as `-num`) and increment `maxSize`.  
   Otherwise push `num` to `minHeap` and increment `minSize`.
2. Call `rebalance()` to restore the size invariant.

## Signature

```python
def add(self, num: int) -> None
```

Called via `solution(nums)` → `List[float]`: medians after each successive `add`.

## Test cases

| # | `nums` | Expected medians |
|---|---|---|
| 1 | `[1]` | `[1.0]` |
| 2 | `[1, 2]` | `[1.0, 1.5]` |
| 3 | `[2, 1]` | `[2.0, 1.5]` |
| 4 | `[1, 2, 3]` | `[1.0, 1.5, 2.0]` |
| 5 | `[3, 1, 2]` | `[3.0, 2.0, 2.0]` |
| 6 | `[-1, -2, -3]` | `[-1.0, -1.5, -2.0]` |
| 7 | `[5, 5, 5]` | `[5.0, 5.0, 5.0]` |
| 8 | `[1, 100, 2, 99, 3]` | `[1.0, 50.5, 2.0, 50.5, 3.0]` |
