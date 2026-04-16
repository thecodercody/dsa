# Stock Span

For each price, return the number of consecutive days (ending today) with price ≤ today's price.

## Signature

```python
def solution(prices: list[int]) -> list[int]
```

## Drill focus

- **Previous greater element** variant — mirror of `p31_next_greater_element`
- Stack of indices with strictly decreasing prices
- Pop while top's price ≤ current; span = `i - stack[-1]` (or `i + 1` if empty)

## Reference template

```python
def solution(prices):
    out = []
    stack = []  # indices, prices strictly decreasing
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] <= p:
            stack.pop()
        out.append(i - stack[-1] if stack else i + 1)
        stack.append(i)
    return out
```

## Test cases

| # | prices | expected |
|---|---|---|
| 1 | `[100,80,60,70,60,75,85]` | `[1,1,1,2,1,4,6]` |
| 2 | `[10,20,30,40]` | `[1,2,3,4]` |
| 3 | `[40,30,20,10]` | `[1,1,1,1]` |
| 4 | `[10]` | `[1]` |
| 5 | `[]` | `[]` |
| 6 | `[100,90,100,90,100]` | `[1,1,3,1,5]` |
