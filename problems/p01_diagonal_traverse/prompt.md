# Diagonal Traverse

Return all elements of a matrix in diagonal zigzag order (even diagonals go up-right, odd go down-left).

## Signature

```python
def solution(matrix: list[list[int]]) -> list[int]
```

## Drill focus

- Iterate `d` from `0` to `R+C-2`; direction alternates each diagonal
- Even `d`: start at `(min(d, R-1), d - min(d, R-1))`, walk up-right (`r-=1, c+=1`)
- Odd `d`: start at `(d - min(d, C-1), min(d, C-1))`, walk down-left (`r+=1, c-=1`)
- Pure index-juggling; no shared structure with prefix/deque problems

## Reference template

Read once, then solve without peeking.

```python
def solution(matrix):
    if not matrix or not matrix[0]: return []
    R, C = len(matrix), len(matrix[0])
    out = []
    for d in range(R + C - 1):
        if d % 2 == 0:  # going up-right
            r = min(d, R - 1)
            c = d - r
            while r >= 0 and c < C:
                out.append(matrix[r][c])
                r -= 1
                c += 1
        else:           # going down-left
            c = min(d, C - 1)
            r = d - c
            while c >= 0 and r < R:
                out.append(matrix[r][c])
                r += 1
                c -= 1
    return out
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,4,7,5,3,6,8,9]` |
| 2 | `[[1,2],[3,4]]` | `[1,2,3,4]` |
| 3 | `[[1]]` | `[1]` |
| 4 | `[[1,2,3]]` | `[1,2,3]` |
| 5 | `[[1],[2],[3]]` | `[1,2,3]` |
| 6 | `[[1,2],[3,4],[5,6]]` | `[1,2,3,5,4,6]` |
| 7 | `[[1,2,3],[4,5,6]]` | `[1,2,4,5,3,6]` |
| 8 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,5,9,6,3,4,7,10,11,8,12]` |
