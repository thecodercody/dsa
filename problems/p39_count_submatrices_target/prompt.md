# Count Submatrices with Sum = Target  (Track A3)

Given an integer matrix and an integer `target`, return the number of non-empty rectangular submatrices whose sum equals `target`.

This is LC 1074. Same outer scaffold as A1/A2, different inner: hashmap prefix sum (the LC 560 "Subarray Sum Equals K" trick).

## Signature
```python
def solution(matrix: list[list[int]], target: int) -> int
```

## Reference template

```python
from collections import defaultdict

def solution(matrix, target):
    R, C = len(matrix), len(matrix[0])
    count = 0
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            # === 1D: count subarrays of row_sums with sum == target ===
            seen = defaultdict(int)
            seen[0] = 1
            curr = 0
            for s in row_sums:
                curr += s
                count += seen[curr - target]
                seen[curr] += 1
    return count
```

## Drill focus
- Outer scaffold unchanged (same for all Track A problems).
- Inner is **LC 560**: for each prefix `curr`, add `seen[curr - target]` to count, then record `curr` in `seen`.
- `seen[0] = 1` sentinel — same role as `prefixes = [0]` in Track B.
- Order matters: add count **before** incrementing `seen[curr]` (otherwise a subarray of length 0 is counted when `target == 0`).

## Test cases

| # | matrix | target | expected |
|---|---|---|---|
| 1 | `[[0]]` | 0 | 1 |
| 2 | `[[5]]` | 5 | 1 |
| 3 | `[[5]]` | 0 | 0 |
| 4 | `[[1,2],[3,4]]` | 3 | 2 |
| 5 | `[[1,-1],[1,-1]]` | 0 | 3 |
| 6 | `[[0,0],[0,0]]` | 0 | 9 |
| 7 | `[[1,0],[0,1]]` | 1 | 6 |
| 8 | `[[0,1,0],[1,1,1],[0,1,0]]` | 0 | 4 |
| 9 | `[[1,-2,1],[-1,1,-1]]` | -1 | 9 |
