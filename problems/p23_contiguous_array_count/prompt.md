# Contiguous Array Count

Count the number of contiguous subarrays containing an equal number of 0s and 1s.

## Signature

```python
def solution(nums: list[int]) -> int
```

## Drill focus

- Transform: `0 → -1`, `1 → +1`; then "equal 0/1" = "sum == 0"
- Hashmap `count[prefix_sum] → occurrences`
- Seed `{0: 1}` for empty prefix
- `total += count[curr]` then `count[curr] += 1` (count variant, not length)

## Reference template

```python
from collections import defaultdict

def solution(nums):
    count = defaultdict(int)
    count[0] = 1
    curr = 0
    total = 0
    for x in nums:
        curr += 1 if x == 1 else -1
        total += count[curr]
        count[curr] += 1
    return total
```

## Test cases

| # | nums | expected |
|---|---|---|
| 1 | `[0,1]` | 1 |
| 2 | `[0,1,0]` | 2 |
| 3 | `[0,1,0,1]` | 4 |
| 4 | `[0,0,1,1]` | 2 |
| 5 | `[0,0,0]` | 0 |
| 6 | `[]` | 0 |
| 7 | `[1,0,1,0,1]` | 6 |
| 8 | `[1,1,0,0]` | 2 |
| 9 | `[0]` | 0 |
| 10 | `[1,0,0,1,0,1,1]` | 8 |
