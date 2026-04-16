# Max Submatrix Sum No Larger Than K (LC 363)

Return the max sum of any submatrix with sum ≤ `k`.

## Signature

```python
def solution(matrix: list[list[int]], k: int) -> int
```

## Drill focus

- **Fusion of Track A (2D→1D collapse) + Track B (prefix+bisect)**
- Outer: iterate column pairs `(left, right)`, maintain incremental `row_sums`
- Inner: for each `row_sums`, find max `curr - p ≤ k` via `bisect_left(prefixes, curr - k)`
- Per-inner ans: `curr - prefixes[idx]` (the smallest `p ≥ curr-k`)
- Pick the smaller dim as outer loop for efficiency

## Reference template

```python
from bisect import bisect_left, insort

def solution(matrix, k):
    R, C = len(matrix), len(matrix[0])
    # Pick smaller dim as outer
    if R > C:
        return solution([list(col) for col in zip(*matrix)], k)
    best = float("-inf")
    for top in range(R):
        col_sums = [0] * C
        for bot in range(top, R):
            for c in range(C):
                col_sums[c] += matrix[bot][c]
            # inner: max subarray sum ≤ k in col_sums
            prefixes = [0]
            curr = 0
            for s in col_sums:
                curr += s
                idx = bisect_left(prefixes, curr - k)
                if idx < len(prefixes):
                    best = max(best, curr - prefixes[idx])
                insort(prefixes, curr)
    return best
```

## Test cases

| # | matrix | k | expected |
|---|---|---|---|
| 1 | `[[1,0,1],[0,-2,3]]` | 2 | 2 |
| 2 | `[[2,2,-1]]` | 3 | 3 |
| 3 | `[[2,2,-1]]` | 0 | -1 |
| 4 | `[[1,1],[1,1]]` | 3 | 2 |
| 5 | `[[1,1],[1,1]]` | 100 | 4 |
| 6 | `[[-1,-2],[-3,-4]]` | -3 | -3 |
| 7 | `[[1,2,3],[4,5,6],[7,8,9]]` | 100 | 45 |
| 8 | `[[1,2,3],[4,5,6],[7,8,9]]` | 10 | 9 |
| 9 | `[[5]]` | 10 | 5 |
