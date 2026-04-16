# Sum of Subarray Minimums (LC 907)

Return the sum of `min(subarray)` over all contiguous subarrays, modulo `10**9 + 7`.

## Signature

```python
def solution(nums: list[int]) -> int
```

## Drill focus

- **Contribution technique** — fundamentally different use of monotonic stack
- For each index `i`, count the number of subarrays where `nums[i]` is the min
- Find `left[i]` = distance to previous **strictly** smaller element
- Find `right[i]` = distance to next **smaller-or-equal** element
- (Asymmetric strict/non-strict handles duplicates without double-counting)
- Contribution: `nums[i] * left[i] * right[i]`

## Reference template

```python
def solution(nums):
    MOD = 10**9 + 7
    n = len(nums)
    left = [0] * n   # count including i, extending left while prev > nums[i]
    right = [0] * n  # count including i, extending right while next >= nums[i]
    stack = []
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > nums[i]:
            count += stack.pop()[1]
        left[i] = count
        stack.append((nums[i], count))
    stack = []
    for i in range(n - 1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= nums[i]:
            count += stack.pop()[1]
        right[i] = count
        stack.append((nums[i], count))
    total = 0
    for i in range(n):
        total = (total + nums[i] * left[i] * right[i]) % MOD
    return total
```

## Test cases

| # | nums | expected |
|---|---|---|
| 1 | `[3,1,2,4]` | 17 |
| 2 | `[11,81,94,43,3]` | 444 |
| 3 | `[1]` | 1 |
| 4 | `[1,2,3]` | 10 |
| 5 | `[3,2,1]` | 10 |
| 6 | `[5,5,5]` | 30 |
