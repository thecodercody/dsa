# Min Submatrix Sum  (Track A2)

Given an integer matrix, return the **minimum** sum of any non-empty rectangular submatrix.

Mirror of A1.

## Signature
```python
def solution(matrix: list[list[int]]) -> int
```

## Reference template

```python
def solution(matrix):
    R, C = len(matrix), len(matrix[0])
    best = float('inf')
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            # === 1D min-Kadane's on row_sums ===
            cur = row_sums[0]
            local_best = cur
            for i in range(1, R):
                cur = min(row_sums[i], cur + row_sums[i])
                local_best = min(local_best, cur)
            best = min(best, local_best)
    return best
```

## Drill focus
- Same outer scaffold as A1 — no change.
- Only the inner flips: `max` → `min`, `-inf` → `inf`. Muscle memory for "don't also flip the outer collapse."

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[5]]` | 5 |
| 2 | `[[-3]]` | -3 |
| 3 | `[[1,2],[3,4]]` | 1 |
| 4 | `[[1,-2],[3,4]]` | -2 |
| 5 | `[[-1,-2],[-3,-4]]` | -10 |
| 6 | `[[2,-3,-4,1,5]]` | -7 |
| 7 | `[[2],[-3],[-4],[1],[5]]` | -7 |
| 8 | `[[1,-5],[2,-5],[3,-5]]` | -15 |
| 9 | `[[-1,-2,3],[4,-5,-6]]` | -11 |
