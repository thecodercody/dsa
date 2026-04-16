# Max Submatrix Sum  (Track A1)

Given an integer matrix, return the **maximum** sum of any non-empty rectangular submatrix.

The matrix may contain negative values. This is the 2D generalization of "max subarray sum" (Kadane's).

## Signature
```python
def solution(matrix: list[list[int]]) -> int
```

## Reference template

```python
def solution(matrix):
    R, C = len(matrix), len(matrix[0])
    best = float('-inf')
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            # === 1D Kadane's on row_sums ===
            cur = row_sums[0]
            local_best = cur
            for i in range(1, R):
                cur = max(row_sums[i], cur + row_sums[i])
                local_best = max(local_best, cur)
            best = max(best, local_best)
    return best
```

## Drill focus
- Outer loop = **column-pair** `(left, right)`.
- `row_sums` is built incrementally: when `right` advances, add the new column's values into `row_sums`. Never reset it while `right` advances — only when `left` advances.
- Inner = ordinary 1D Kadane's on the current `row_sums`.
- Pick the smaller dimension for the outer pair if you care about efficiency (matrix could be tall or wide). Default: columns outer, rows inner.

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[5]]` | 5 |
| 2 | `[[-3]]` | -3 |
| 3 | `[[1,2],[3,4]]` | 10 |
| 4 | `[[1,-2],[3,4]]` | 7 |
| 5 | `[[-2,1,3,-1,4]]` | 7 |
| 6 | `[[-2],[1],[3],[-1],[4]]` | 7 |
| 7 | `[[-1,-2],[-3,-4]]` | -1 |
| 8 | `[[1,-1,1],[1,1,-1]]` | 2 |
| 9 | `[[1,2,3],[-5,-5,-5]]` | 6 |
