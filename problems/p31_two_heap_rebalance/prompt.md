# Two-Heap: `rebalance`

Part of the two-heap sliding window median algorithm.

After every `add` or `remove`, the heap sizes may violate the invariant:

> `maxSize == minSize` **or** `maxSize == minSize + 1`

`rebalance` fixes a one-step violation by moving one element between heaps.

## Your task

Implement `rebalance()`:

- If `maxSize > minSize + 1`: pop the top of `maxHeap` (negate it back), push it to `minHeap`, adjust sizes, then call `_prune(maxHeap)`.
- Elif `maxSize < minSize`: pop the top of `minHeap`, push it to `maxHeap` (negate it), adjust sizes, then call `_prune(minHeap)`.
- Otherwise do nothing.

## Signature

```python
def rebalance(self) -> None
```

Called via `solution(max_vals, min_vals, max_size, min_size)` → `(maxSize, minSize)`.  
`max_vals` are the actual values on the max side; they are stored negated internally.  
`delayed = {}` for these tests (no lazy deletions).

## Test cases

| # | max side | min side | maxS | minS | Expected |
|---|---|---|---|---|---|
| 1 | `[1,2]` | `[3,4]` | 2 | 2 | `(2,2)` — balanced |
| 2 | `[1,2,3]` | `[4,5]` | 3 | 2 | `(3,2)` — balanced (3 == 2+1) |
| 3 | `[1,2,3,4]` | `[5,6]` | 4 | 2 | `(3,3)` — max too large |
| 4 | `[1]` | `[2,3,4]` | 1 | 3 | `(2,2)` — min too large |
| 5 | `[1,2]` | `[]` | 2 | 0 | `(1,1)` — max only, unbalanced |
| 6 | `[]` | `[1,2]` | 0 | 2 | `(1,1)` — min only, unbalanced |
