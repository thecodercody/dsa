# Range Sum 2D

Given a matrix and a list of queries `(r1, c1, r2, c2)`, return the sum of elements in each rectangular subregion (inclusive on all four bounds).

## Signature

```python
def solution(matrix: list[list[int]], queries: list[tuple[int,int,int,int]]) -> list[int]
```

## Drill focus

- Build a `(R+1)×(C+1)` prefix grid to eliminate boundary checks
- Inclusion-exclusion on 4 corners: `P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`
- O(RC) preprocessing, O(1) per query

## Reference template

Read once, then solve without peeking.

```python
def solution(matrix, queries):
    R, C = len(matrix), len(matrix[0])
    P = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            P[r+1][c+1] = matrix[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]
    out = []
    for r1, c1, r2, c2 in queries:
        out.append(P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1])
    return out
```

## Test cases

Matrix for cases 1–6:
```
[[3,0,1,4,2],
 [5,6,3,2,1],
 [1,2,0,1,5],
 [4,1,0,1,7],
 [1,0,3,0,5]]
```

| # | queries | expected |
|---|---|---|
| 1 | `[(2,1,4,3)]` | `[8]` |
| 2 | `[(1,1,2,2)]` | `[11]` |
| 3 | `[(1,2,2,4)]` | `[12]` |
| 4 | `[(0,0,0,0)]` | `[3]` |
| 5 | `[(0,0,4,4)]` | `[58]` |
| 6 | `[(2,1,4,3),(1,1,2,2),(1,2,2,4)]` | `[8,11,12]` |
| 7 | matrix `[[5]]`, `[(0,0,0,0)]` | `[5]` |
| 8 | matrix `[[1,2],[3,4]]`, `[(0,0,1,1),(0,0,0,1),(1,0,1,1)]` | `[10,3,7]` |
| 9 | matrix `[[1,-1],[1,-1]]`, `[(0,0,1,1),(0,0,0,0),(1,1,1,1)]` | `[0,1,-1]` |
