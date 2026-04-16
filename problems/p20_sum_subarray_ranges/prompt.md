# Sum of Subarray Ranges (LC 2104)

Return `sum(max(sub) - min(sub))` over all contiguous subarrays.

## Signature

```python
def solution(nums: list[int]) -> int
```

## Drill focus

- **Composed contribution technique** — builds directly on `p34_sum_subarray_mins`
- `answer = sum_of_maxes - sum_of_mins`
- Two passes of the contribution pattern: one for mins, one for maxes (flip the comparisons)
- Drills that the contribution scaffold is symmetric between min and max

## Reference template

```python
def solution(nums):
    def helper(op_lt, op_le):
        n = len(nums)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            c = 1
            while stack and op_lt(stack[-1][0], nums[i]):
                c += stack.pop()[1]
            left[i] = c
            stack.append((nums[i], c))
        stack = []
        for i in range(n - 1, -1, -1):
            c = 1
            while stack and op_le(stack[-1][0], nums[i]):
                c += stack.pop()[1]
            right[i] = c
            stack.append((nums[i], c))
        return sum(nums[i] * left[i] * right[i] for i in range(n))

    sum_mins = helper(lambda a, b: a > b,  lambda a, b: a >= b)
    sum_maxes = helper(lambda a, b: a < b, lambda a, b: a <= b)
    return sum_maxes - sum_mins
```

## Test cases

| # | nums | expected |
|---|---|---|
| 1 | `[1,2,3]` | 4 |
| 2 | `[1,3,3]` | 4 |
| 3 | `[4,-2,-3,4,1]` | 59 |
| 4 | `[1]` | 0 |
| 5 | `[5,5,5]` | 0 |
| 6 | `[1,2]` | 1 |
