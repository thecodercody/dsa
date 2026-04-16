# Count Submatrices with Sum ≤ k  (Track A4 — fusion)

Given an integer matrix (may contain negatives) and an integer `k`, return the number of non-empty rectangular submatrices whose sum is `≤ k`.

**This is the synthesis problem.** The outer scaffold is from A1–A3. The inner is **Track B3** (`count_subarrays_sum_le_k`) — prefix sum with `bisect`/`insort`, counting variant.

It uses bisect-prefix as the inner instead of a hashmap because sums can be arbitrary integers (not bounded by `target`), so we need a sorted structure to range-query over.

## Signature
```python
def solution(matrix: list[list[int]], k: int) -> int
```

## Reference template

```python
from bisect import bisect_left, insort

def solution(matrix, k):
    R, C = len(matrix), len(matrix[0])
    count = 0
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            # === 1D B3: count subarrays with sum ≤ k via prefix + bisect ===
            prefixes = [0]
            curr = 0
            for s in row_sums:
                curr += s
                idx = bisect_left(prefixes, curr - k)
                count += len(prefixes) - idx
                insort(prefixes, curr)
    return count
```

## Drill focus
- Two chunks you already own: outer collapse (A1) + inner count-le-k (B3). If you've drilled both, this is just plugging them together.
- The `prefixes` list is **reset to `[0]`** for every `(left, right)` pair — each collapse is an independent 1D problem.
- This is LC 363's architecture with the **count** query instead of the **max** query. Once mechanical, LC 363 itself is just swapping B3's inner for B1's inner.

## Test cases

| # | matrix | k | expected |
|---|---|---|---|
| 1 | `[[5]]` | 5 | 1 |
| 2 | `[[5]]` | 4 | 0 |
| 3 | `[[1,2],[3,4]]` | 100 | 9 |
| 4 | `[[1,2],[3,4]]` | 3 | 4 |
| 5 | `[[-1,-2],[-3,-4]]` | 0 | 9 |
| 6 | `[[0,0],[0,0]]` | 0 | 9 |
| 7 | `[[1,-1],[1,-1]]` | 0 | 6 |
| 8 | `[[1,0,1],[0,-2,3]]` | 2 | 15 |
| 9 | `[[1,-2,3,-1,2]]` | 1 | 8 |
