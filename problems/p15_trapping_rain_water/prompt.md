# Trapping Rain Water

Given bar heights, return total trapped water.

## Signature

```python
def solution(height: list[int]) -> int
```

## Drill focus

- **Two-sided bounding** variant of monotonic stack
- Stack of decreasing heights (indices)
- On `height[i] > height[stack[-1]]`: pop `mid`; if stack still non-empty, water above `mid` = `(min(height[i], height[new_top]) - height[mid]) * (i - new_top - 1)`

## Reference template

```python
def solution(height):
    water = 0
    stack = []  # indices, decreasing heights
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            mid = stack.pop()
            if not stack:
                break
            left = stack[-1]
            bounded = min(height[left], h) - height[mid]
            water += bounded * (i - left - 1)
        stack.append(i)
    return water
```

## Test cases

| # | height | expected |
|---|---|---|
| 1 | `[0,1,0,2,1,0,1,3,2,1,2,1]` | 6 |
| 2 | `[4,2,0,3,2,5]` | 9 |
| 3 | `[3,0,2,0,4]` | 7 |
| 4 | `[5]` | 0 |
| 5 | `[]` | 0 |
| 6 | `[1,2,3]` | 0 |
| 7 | `[3,2,1]` | 0 |
| 8 | `[2,0,2]` | 2 |
