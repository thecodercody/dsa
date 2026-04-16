# Daily Temperatures

For each day, return the number of days to wait until a strictly warmer temperature (0 if none).

## Signature

```python
def solution(temperatures: list[int]) -> list[int]
```

## Drill focus

- Same monotonic stack scaffold as `p31_next_greater_element`
- **Difference:** answer is `j - i` (distance), not `nums[j]` (value)
- Drills that the stack stores *indices* and the answer shape is flexible

## Reference template

```python
def solution(temperatures):
    out = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            out[j] = i - j
        stack.append(i)
    return out
```

## Test cases

| # | temperatures | expected |
|---|---|---|
| 1 | `[73,74,75,71,69,72,76,73]` | `[1,1,4,2,1,1,0,0]` |
| 2 | `[30,40,50,60]` | `[1,1,1,0]` |
| 3 | `[30,60,90]` | `[1,1,0]` |
| 4 | `[90,80,70]` | `[0,0,0]` |
| 5 | `[50]` | `[0]` |
| 6 | `[]` | `[]` |
