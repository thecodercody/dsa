# Maximal Rectangle of Ones

Given a binary matrix, find the area of the largest rectangle containing only 1s.

## Signature

```python
def solution(matrix: list[list[int]]) -> int
```

## Drill focus

- Row-by-row collapse: `heights[c] = heights[c]+1 if matrix[r][c]==1 else 0`
- After each row update, apply the histogram rectangle algorithm on `heights`
- Teaches that "collapse" is a meta-pattern independent of what the inner computes (here: stack, not sum)

## Reference template

Read once, then solve without peeking.

```python
def solution(matrix):
    if not matrix or not matrix[0]: return 0
    R, C = len(matrix), len(matrix[0])
    heights = [0] * C
    best = 0
    for r in range(R):
        for c in range(C):
            heights[c] = heights[c] + 1 if matrix[r][c] == 1 else 0
        # inline or call out to largest_rectangle_histogram(heights)
        best = max(best, _hist(heights))
    return best
```

## Test cases

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]` | 6 |
| 2 | `[[1]]` | 1 |
| 3 | `[[0]]` | 0 |
| 4 | `[[1,1],[1,1]]` | 4 |
| 5 | `[[0,0],[0,0]]` | 0 |
| 6 | `[[1,0,1],[0,1,0],[1,0,1]]` | 1 |
| 7 | `[[1,1,1],[1,1,1]]` | 6 |
| 8 | `[[1,0],[1,1]]` | 2 |
| 9 | `[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]` | 8 |
