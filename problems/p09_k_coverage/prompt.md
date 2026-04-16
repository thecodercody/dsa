# K-Coverage

Generalisation of **Unique Segments** (`count == 1`) to `count >= k`.

Given a list of closed integer intervals `[a, b]` and a threshold `k`, return all maximal contiguous segments of the number line that are covered by **at least `k`** of the input intervals.

Output is a sorted list of `[start, end]` inclusive intervals. Adjacent regions that both meet the threshold should be merged into one.

## Signature
```python
def solution(intervals: list[list[int]], k: int) -> list[list[int]]
```

## Example
```
intervals = [[1,5], [2,6], [4,8]], k = 2

Coverage count by point:
  1    2    3    4    5    6    7    8
  1    2    2    3    3    2    1    1

Points with count >= 2: 2–6  →  [[2, 6]]
```

## Hint

Sweep line: for each `[a, b]`, record `+1` at `a` and `−1` at `b+1`. Sort the unique event positions, walk through accumulating the count. Every time the count crosses the `k` boundary, open or close a result segment.

## Connection to Unique Segments

| variant | condition | k |
|---|---|---|
| Unique Segments | covered by exactly 1 | — |
| K-Coverage (this problem) | covered by ≥ k | any |
| Union of Intervals | covered by ≥ 1 | k=1 |

## Test cases

| # | intervals | k | expected |
|---|---|---|---|
| 1 | `[[1,3],[2,4]]` | 2 | `[[2,3]]` |
| 2 | `[[1,2],[4,5]]` | 2 | `[]` |
| 3 | `[[1,5],[1,5]]` | 2 | `[[1,5]]` |
| 4 | `[[1,10],[3,7]]` | 2 | `[[3,7]]` |
| 5 | `[[1,3],[5,7]]` | 1 | `[[1,3],[5,7]]` |
| 6 | `[[1,3],[2,4],[3,5]]` | 3 | `[[3,3]]` |
| 7 | `[[1,5],[2,6],[4,8]]` | 2 | `[[2,6]]` |
| 8 | `[[1,5],[2,6],[4,8]]` | 3 | `[[4,5]]` |
| 9 | `[[1,3],[3,5]]` | 2 | `[[3,3]]` |
| 10 | `[[1,10],[2,8],[4,6]]` | 3 | `[[4,6]]` |
| 11 | `[[1,5],[2,4]]` | 3 | `[]` |
