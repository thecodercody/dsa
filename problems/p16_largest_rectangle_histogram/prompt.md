# Largest Rectangle in Histogram

Given an array of bar heights, find the area of the largest rectangle that can be formed using contiguous bars.

## Signature

```python
def solution(heights: list[int]) -> int
```

## Drill focus

- Monotonic-increasing stack of indices
- When a shorter bar is encountered, pop and compute area: width bounded by new stack top (left) and current index (right)
- Append sentinel `0` to flush all remaining bars at the end

## Reference template

Read once, then solve without peeking.

```python
def solution(heights):
    stack = []          # indices, strictly increasing heights
    best = 0
    heights = heights + [0]   # sentinel flush
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] >= h:
            j = stack.pop()
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, heights[j] * width)
        stack.append(i)
    return best
```

## Test cases

| # | heights | expected |
|---|---|---|
| 1 | `[2,1,5,6,2,3]` | 10 |
| 2 | `[2,4]` | 4 |
| 3 | `[1,1,1,1]` | 4 |
| 4 | `[5]` | 5 |
| 5 | `[0]` | 0 |
| 6 | `[2,1,2]` | 3 |
| 7 | `[6,2,5,4,5,1,6]` | 12 |
| 8 | `[0,1,0,1]` | 1 |
| 9 | `[4,2,0,3,2,5]` | 6 |
