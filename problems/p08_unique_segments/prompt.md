# Unique Segments

Given a list of integer intervals `[a, b]` (inclusive on both ends), return the portions of the number line that are covered by **exactly one** input interval.

Output is a list of inclusive integer intervals, sorted left-to-right. If two adjacent output regions come from different source intervals, keep them separate.

## Signature
```python
def solution(intervals: list[list[int]]) -> list[list[int]]
```

## Test cases

| # | Input | Expected | Note |
|---|---|---|---|
| 1 | `[[1,3],[2,4]]` | `[[1,1],[4,4]]` | basic overlap |
| 2 | `[[1,2],[4,5]]` | `[[1,2],[4,5]]` | no overlap |
| 3 | `[[1,5],[1,5]]` | `[]` | full overlap |
| 4 | `[[1,10],[3,7]]` | `[[1,2],[8,10]]` | nested |
| 5 | `[[1,3],[2,4],[3,5]]` | `[[1,1],[5,5]]` | multiple overlaps |
| 6 | `[[1,3],[2,4],[6,11],[8,9]]` | `[[1,1],[4,4],[6,7],[10,11]]` | mixed |
| 7 | `[[5,10]]` | `[[5,10]]` | single |
| 8 | `[[1,2],[3,4]]` | `[[1,2],[3,4]]` | touching (disjoint) |
| 9 | `[[1,3],[3,5]]` | `[[1,2],[4,5]]` | edge overlap at 3 |
