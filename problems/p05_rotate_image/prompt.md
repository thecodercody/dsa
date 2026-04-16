# Rotate Image

Rotate a square matrix 90° clockwise. In-place preferred.

## Signature

```python
def solution(matrix: list[list[int]]) -> list[list[int]]
```

## Drill focus

- **In-place index juggling** — this is the *write* subpattern that p25/p26 (read-only traversals) don't cover
- Standard trick: **transpose + reverse each row**
- Alternative: 4-way swap within each concentric ring

## Reference template

```python
def solution(matrix):
    n = len(matrix)
    # transpose
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    # reverse each row
    for row in matrix:
        row.reverse()
    return matrix
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[[7,4,1],[8,5,2],[9,6,3]]` |
| 2 | `[[1]]` | `[[1]]` |
| 3 | `[[1,2],[3,4]]` | `[[3,1],[4,2]]` |
| 4 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]` | `[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]` |
