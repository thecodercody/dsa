# Spiral Matrix II

Generate an `n × n` matrix filled with `1..n²` in clockwise spiral order.

## Signature

```python
def solution(n: int) -> list[list[int]]
```

## Drill focus

- **Write counterpart** of `p26_spiral_order` — same four-boundary walk, writes instead of reads
- Four pointers `top, bottom, left, right`; shrink after each side
- Counter `v` from 1 to n²

## Reference template

```python
def solution(n):
    m = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    v = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            m[top][c] = v; v += 1
        top += 1
        for r in range(top, bottom + 1):
            m[r][right] = v; v += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                m[bottom][c] = v; v += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                m[r][left] = v; v += 1
            left += 1
    return m
```

## Test cases

| # | n | expected |
|---|---|---|
| 1 | 1 | `[[1]]` |
| 2 | 2 | `[[1,2],[4,3]]` |
| 3 | 3 | `[[1,2,3],[8,9,4],[7,6,5]]` |
| 4 | 4 | `[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]` |
| 5 | 5 | `[[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]` |
