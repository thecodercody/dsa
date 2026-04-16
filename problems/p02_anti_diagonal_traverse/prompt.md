# Anti-Diagonal Traverse

Return all elements of a matrix grouped by anti-diagonal (sum `r+c`), each diagonal always traversed top-down (no zigzag).

## Signature

```python
def solution(matrix: list[list[int]]) -> list[int]
```

## Drill focus

- **Non-zigzag** cousin of `p25_diagonal_traverse` — same diagonal index `d = r + c`, but always walk top-to-bottom
- No direction flipping; simpler bounds arithmetic
- Drills that the diagonal decomposition is independent of traversal direction

## Reference template

```python
def solution(matrix):
    if not matrix or not matrix[0]:
        return []
    R, C = len(matrix), len(matrix[0])
    out = []
    for d in range(R + C - 1):
        r = max(0, d - C + 1)
        c = d - r
        while r < R and c >= 0:
            out.append(matrix[r][c])
            r += 1
            c -= 1
    return out
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,4,3,5,7,6,8,9]` |
| 2 | `[[1,2],[3,4]]` | `[1,2,3,4]` |
| 3 | `[[1]]` | `[1]` |
| 4 | `[[1,2,3]]` | `[1,2,3]` |
| 5 | `[[1],[2],[3]]` | `[1,2,3]` |
| 6 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,5,3,6,9,4,7,10,8,11,12]` |
