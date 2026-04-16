# Sliding Window Minimum

Given an integer array `nums` and an integer `k`, there is a sliding window of size `k` that moves from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return an array of the **minimum** value in each window.

## Signature
```python
def solution(nums: list[int], k: int) -> list[int]
```

## Example
```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Window position           Min
---------------           ---
[1  3 -1] -3  5  3  6  7   -1
 1 [3 -1 -3] 5  3  6  7   -3
 1  3 [-1 -3  5] 3  6  7   -3
 1  3  -1 [-3  5  3] 6  7   -3
 1  3  -1  -3 [5  3  6] 7    3
 1  3  -1  -3  5 [3  6  7]   3

→ [-1, -3, -3, -3, 3, 3]
```

## Test cases

| # | `nums` | `k` | Expected |
|---|---|---|---|
| 1 | `[1,3,-1,-3,5,3,6,7]` | `3` | `[-1,-3,-3,-3,3,3]` |
| 2 | `[4,2,7,1]` | `1` | `[4,2,7,1]` |
| 3 | `[5,2,8,1,9]` | `5` | `[1]` |
| 4 | `[3,3,3,3]` | `2` | `[3,3,3]` |
| 5 | `[1,2,3,4,5]` | `3` | `[1,2,3]` |
| 6 | `[5,4,3,2,1]` | `3` | `[3,2,1]` |
| 7 | `[7]` | `1` | `[7]` |
| 8 | `[2,1]` | `2` | `[1]` |
| 9 | `[-1,-2,-3,-4]` | `2` | `[-2,-3,-4]` |
