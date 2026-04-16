# Next Greater Element

For each element, return the next strictly greater element to its right, or `-1` if none.

## Signature

```python
def solution(nums: list[int]) -> list[int]
```

## Drill focus

- **Foundational monotonic stack scaffold.** Every variant in this family builds on this.
- Stack of **indices** with values in decreasing order (top has smallest unresolved)
- On each new element: while stack top's value < current, pop and resolve
- Remaining stack entries at end get `-1`

## Reference template

```python
def solution(nums):
    out = [-1] * len(nums)
    stack = []  # indices, values strictly decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            out[stack.pop()] = x
        stack.append(i)
    return out
```

## Test cases

| # | nums | expected |
|---|---|---|
| 1 | `[2,1,3]` | `[3,3,-1]` |
| 2 | `[1,2,3,4]` | `[2,3,4,-1]` |
| 3 | `[4,3,2,1]` | `[-1,-1,-1,-1]` |
| 4 | `[2,7,3,5,4,6,8]` | `[7,8,5,6,6,8,-1]` |
| 5 | `[5]` | `[-1]` |
| 6 | `[]` | `[]` |
| 7 | `[1,1,1]` | `[-1,-1,-1]` |
| 8 | `[3,1,4,1,5,9,2,6]` | `[4,4,5,5,9,-1,6,-1]` |
