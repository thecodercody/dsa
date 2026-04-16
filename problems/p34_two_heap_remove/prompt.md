# Two-Heap: `remove`

Part of the two-heap sliding window median algorithm.

When the window slides, the outgoing element must be removed. Physically removing from the middle of a heap is O(n), so instead we **lazily delete**: mark the element in `delayed` and decrement the *virtual* size of whichever heap logically owns it.

`prune` will clean up the physical heap top next time it's checked.

## Your task

Implement `remove(num)`:

1. Add `num` to `self.delayed` (increment its count).
2. Decide which virtual size to decrement:
   - If `maxHeap` is non-empty and `num <= -maxHeap[0]` (num belongs to the lower half), decrement `maxSize`.  
     If `num` is currently at the physical top of `maxHeap` (`-num == maxHeap[0]`), also call `self._prune(self.maxHeap)` right away.
   - Otherwise decrement `minSize`.  
     If `num` is at the physical top of `minHeap` (`num == minHeap[0]`), also call `self._prune(self.minHeap)` right away.
3. Call `self._rebalance()`.

## Signature

```python
def remove(self, num: int) -> None
```

Called via `solution(nums_to_add, nums_to_remove)` → `float` (median after all removes).

## Test cases

| # | add | remove | Expected median | remaining |
|---|---|---|---|---|
| 1 | `[1,2,3]` | `[1]` | `2.5` | `{2,3}` |
| 2 | `[1,2,3]` | `[3]` | `1.5` | `{1,2}` |
| 3 | `[1,3,4]` | `[3]` | `2.5` | `{1,4}` |
| 4 | `[1,2,3,4,5]` | `[1,2]` | `4.0` | `{3,4,5}` |
| 5 | `[1,3,5,5,5]` | `[5]` | `4.0` | `{1,3,5,5}` |
| 6 | `[2,4,6,8,10]` | `[4,6]` | `8.0` | `{2,8,10}` |
| 7 | `[1,2]` | `[1]` | `2.0` | `{2}` |
| 8 | `[1,2]` | `[2]` | `1.0` | `{1}` |
