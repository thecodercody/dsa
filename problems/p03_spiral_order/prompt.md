# Spiral Order

Return all elements of a matrix in clockwise spiral order.

## Signature

```python
def solution(matrix: list[list[int]]) -> list[int]
```

## Drill focus

- Four boundary pointers: `top`, `bottom`, `left`, `right`
- Walk: top row L→R, right col T→B, bottom row R→L (guard `top <= bottom`), left col B→T (guard `left <= right`)
- Shrink the relevant boundary after each side walk

## Reference template

Read once, then solve without peeking.

```python
def solution(matrix):
    if not matrix or not matrix[0]: return []
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1): out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1): out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): out.append(matrix[r][left])
            left += 1
    return out
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,3,6,9,8,7,4,5]` |
| 2 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,3,4,8,12,11,10,9,5,6,7]` |
| 3 | `[[1]]` | `[1]` |
| 4 | `[[1,2]]` | `[1,2]` |
| 5 | `[[1],[2]]` | `[1,2]` |
| 6 | `[[1,2],[3,4]]` | `[1,2,4,3]` |
| 7 | `[[1,2,3],[4,5,6]]` | `[1,2,3,6,5,4]` |
| 8 | `[[1,2],[3,4],[5,6]]` | `[1,2,4,6,5,3]` |
| 9 | `[[1,2,3,4,5]]` | `[1,2,3,4,5]` |
