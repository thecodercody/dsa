# Submatrix Sum Equals K (Exists)

Return True if any submatrix of the given matrix has sum equal to target, False otherwise.

## Signature

```python
def solution(matrix: list[list[int]], target: int) -> bool
```

## Drill focus

- Same column-pair collapse + hashmap scaffold as `count_submatrices_target`
- Short-circuit: return `True` on first match instead of counting
- Drills the existence/boolean answer axis (all other problems return max/min/count)

## Reference template

Read once, then solve without peeking.

```python
from collections import defaultdict

def solution(matrix, target):
    R, C = len(matrix), len(matrix[0])
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            seen = {0}
            curr = 0
            for s in row_sums:
                curr += s
                if curr - target in seen:
                    return True
                seen.add(curr)
    return False
```

## Test cases

| # | matrix | target | expected |
|---|---|---|---|
| 1 | `[[1,2],[3,4]]` | 3 | True |
| 2 | `[[1,2],[3,4]]` | 100 | False |
| 3 | `[[1,2],[3,4]]` | 10 | True |
| 4 | `[[0]]` | 0 | True |
| 5 | `[[5]]` | 0 | False |
| 6 | `[[1,-1],[1,-1]]` | 0 | True |
| 7 | `[[1,1],[1,1]]` | 2 | True |
| 8 | `[[1,1],[1,1]]` | 5 | False |
| 9 | `[[0,1,0],[1,1,1],[0,1,0]]` | 5 | True |
