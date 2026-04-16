# Transpose Matrix

Return the transpose of the matrix (may be non-square).

## Signature

```python
def solution(matrix: list[list[int]]) -> list[list[int]]
```

## Drill focus

- Simplest index-remap: `out[c][r] = matrix[r][c]`
- Must allocate new `C × R` grid (cannot reuse in-place for non-square)
- Baseline for `p39_rotate_image`

## Reference template

```python
def solution(matrix):
    R, C = len(matrix), len(matrix[0])
    out = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            out[c][r] = matrix[r][c]
    return out
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[[1,4,7],[2,5,8],[3,6,9]]` |
| 2 | `[[1,2,3]]` | `[[1],[2],[3]]` |
| 3 | `[[1],[2],[3]]` | `[[1,2,3]]` |
| 4 | `[[1,2],[3,4],[5,6]]` | `[[1,3,5],[2,4,6]]` |
| 5 | `[[1]]` | `[[1]]` |
