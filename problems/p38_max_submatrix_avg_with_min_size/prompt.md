# Max Submatrix Average With Min Size

Return the maximum average of any submatrix whose dimensions are at least `min_rows × min_cols`.

## Signature

```python
def solution(matrix: list[list[int]], min_rows: int, min_cols: int) -> float
```

## Drill focus

- 2D prefix sum preprocessing (same as `p22_range_sum_2d`)
- Enumerate all (r1, r2, c1, c2) with `r2-r1+1 >= min_rows` and `c2-c1+1 >= min_cols`
- Query sum in O(1), divide by area, track max

## Reference template

```python
def solution(matrix, min_rows, min_cols):
    R, C = len(matrix), len(matrix[0])
    P = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            P[r+1][c+1] = matrix[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]
    best = float("-inf")
    for r1 in range(R):
        for r2 in range(r1 + min_rows - 1, R):
            for c1 in range(C):
                for c2 in range(c1 + min_cols - 1, C):
                    s = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
                    area = (r2 - r1 + 1) * (c2 - c1 + 1)
                    best = max(best, s / area)
    return best
```

## Test cases

| # | matrix | min_rows | min_cols | expected |
|---|---|---|---|---|
| 1 | `[[1,2],[3,4]]` | 1 | 1 | 4.0 |
| 2 | `[[1,2],[3,4]]` | 2 | 2 | 2.5 |
| 3 | `[[1,2],[3,4]]` | 2 | 1 | 3.0 |
| 4 | `[[-1,-2],[-3,-4]]` | 1 | 1 | -1.0 |
| 5 | `[[5]]` | 1 | 1 | 5.0 |
| 6 | `[[1,2,3],[4,5,6],[7,8,9]]` | 2 | 2 | 7.0 |
| 7 | `[[1,2,3],[4,5,6],[7,8,9]]` | 1 | 1 | 9.0 |
| 8 | `[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5]]` | 2 | 2 | 3.5 |
