# Set Matrix Zeros

If any cell is 0, set its entire row and column to 0. In-place with O(1) extra space.

## Signature

```python
def solution(matrix: list[list[int]]) -> list[list[int]]
```

## Drill focus

- **In-place marker pass** — uses row 0 / col 0 as flags to avoid extra storage
- Tricky cell: `matrix[0][0]` conflicts between row-flag and col-flag — handle with two separate booleans
- Two passes: first mark, then apply

## Reference template

```python
def solution(matrix):
    R, C = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(C))
    first_col_zero = any(matrix[r][0] == 0 for r in range(R))
    for r in range(1, R):
        for c in range(1, C):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    for r in range(1, R):
        for c in range(1, C):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row_zero:
        for c in range(C):
            matrix[0][c] = 0
    if first_col_zero:
        for r in range(R):
            matrix[r][0] = 0
    return matrix
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,1,1],[1,0,1],[1,1,1]]` | `[[1,0,1],[0,0,0],[1,0,1]]` |
| 2 | `[[0,1,2,0],[3,4,5,2],[1,3,1,5]]` | `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]` |
| 3 | `[[1]]` | `[[1]]` |
| 4 | `[[0]]` | `[[0]]` |
| 5 | `[[1,2,3]]` | `[[1,2,3]]` |
| 6 | `[[1],[0],[3]]` | `[[0],[0],[0]]` |
