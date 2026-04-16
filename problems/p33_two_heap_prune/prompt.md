# Two-Heap: `prune`

Part of the two-heap sliding window median algorithm.

When elements leave the sliding window they are **lazily deleted**: instead of finding and removing them from the middle of the heap (O(n)), we record them in a `delayed` dict and skip them when they eventually surface at a heap top.

`prune(heap)` cleans the top of a heap by discarding any element that is present in `delayed`.

## Your task

Implement `prune(heap)`:

1. While `heap` is non-empty:
   - Peek at the top element. For **minHeap** it is `heap[0]`; for **maxHeap** it is `-heap[0]` (undo the negation).
   - If that value is in `self.delayed`, decrement its count. If the count hits 0, delete the key. Pop the element from the heap.
   - Otherwise **break** — the top is a live element, stop.

## Signature

```python
def prune(self, heap) -> None
```

Called via `solution(heap_vals, delayed, is_max_heap)` → top element after pruning (`None` if empty).

## Test cases

| # | heap vals | delayed | max heap? | Expected top |
|---|---|---|---|---|
| 1 | `[1,2,3]` | `{}` | No | `1` |
| 2 | `[1,2,3]` | `{1:1}` | No | `2` |
| 3 | `[1,2,3]` | `{1:1, 2:1}` | No | `3` |
| 4 | `[1,2,3]` | `{1:1, 2:1, 3:1}` | No | `None` |
| 5 | `[3,2,1]` | `{}` | Yes | `3` |
| 6 | `[3,2,1]` | `{3:1}` | Yes | `2` |
| 7 | `[5]` | `{5:1}` | No | `None` |
| 8 | `[1,2]` | `{1:2}` | No | `2` |
