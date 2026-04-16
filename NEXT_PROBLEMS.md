# Next Problems Plan — Fill Gaps in Pattern Coverage

## Context for the implementer

This repo is a personal leetcode-style drill rig at `/Users/cscholbe/apps/dsa`. Each problem lives in `problems/<name>/` with:
- `prompt.md` — problem description + reference template + test case table
- `solution.py` — stub (`def solution(...): pass`) with a one-line TODO
- `tests.py` — pytest parametrized cases
- `__init__.py` — empty, required so `tests.py` module names don't collide across dirs

A `conftest.py` at the repo root auto-wires `solution.py` via a `solution` fixture; test files just do `def test_xxx(solution, name, ...args, expected): assert solution(...args) == expected`. See any existing problem (e.g. `problems/p11_max_subarray_sum_le_k/`) for exact conventions.

Run tests with `.venv/bin/pytest problems/<name> -v` from `/Users/cscholbe/apps/dsa`.

**All expected values in this plan have been pre-verified against brute-force references.**

---

## Gap analysis

The existing library (`problems/`) covers:
- 1D prefix + bisect (max/min/count/range): `max_subarray_sum_le_k`, `min_subarray_sum_ge_k`, `count_subarrays_sum_le_k`, `count_subarrays_sum_in_range`
- 2D column-pair collapse with numeric inner: `max_submatrix_sum`, `min_submatrix_sum`, `count_submatrices_target`, `count_submatrices_sum_le_k`
- Monotonic deque: `sliding_window_minimum`, `max_of_window_mins`
- Sweep line: `unique_segments`, `k_coverage`
- Two-heap median: `two_heap_*`

**Missing transformation families:**
1. **Monotonic stack on histogram** — no `largest_rectangle_histogram`
2. **Boolean/non-numeric collapse inner** — no `maximal_rectangle_ones` (the canonical "inner isn't a sum")
3. **Monotonic deque on prefix sums** (hybrid: prefix + deque) — no `shortest_subarray_sum_ge_k`
4. **Two-sided bisect query** — no "closest to k" problem
5. **2D prefix sum / multi-query preprocessing** — no `range_sum_2d`
6. **Directional flattening** — no `diagonal_traverse`, `spiral_order`
7. **Existence/boolean answer axis** — every current problem returns max/min/count, none return bool

This plan adds **8 problems** in priority order.

---

## Problem 1: `largest_rectangle_histogram` (prerequisite for #2)

Classic LC 84. Monotonic stack. Must be solved before #2 because #2 uses it as inner.

**Signature**
```python
def solution(heights: list[int]) -> int
```

**Approach** — monotonic-increasing stack of indices. When you see a shorter bar, pop and compute area with width bounded by the new stack top (on the left) and current index (on the right). Sentinel: append a final 0 to flush.

**Test cases** (verified)

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

**prompt.md reference template**
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

---

## Problem 2: `maximal_rectangle_ones`

LC 85. Row-compress into heights, apply #1 per row. This is the canonical "collapse with a non-sum inner" — boolean → histogram.

**Signature**
```python
def solution(matrix: list[list[int]]) -> int
```

**Approach** — maintain `heights[c]` across rows: `heights[c] = heights[c]+1 if matrix[r][c]==1 else 0`. After each row update, call `largest_rectangle_histogram(heights)` and track the max.

**Test cases** (verified)

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]` | 6 |
| 2 | `[[1]]` | 1 |
| 3 | `[[0]]` | 0 |
| 4 | `[[1,1],[1,1]]` | 4 |
| 5 | `[[0,0],[0,0]]` | 0 |
| 6 | `[[1,0,1],[0,1,0],[1,0,1]]` | 1 |
| 7 | `[[1,1,1],[1,1,1]]` | 6 |
| 8 | `[[1,0],[1,1]]` | 2 |
| 9 | `[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]` | 8 |

**prompt.md reference template**
```python
def solution(matrix):
    if not matrix or not matrix[0]: return 0
    R, C = len(matrix), len(matrix[0])
    heights = [0] * C
    best = 0
    for r in range(R):
        for c in range(C):
            heights[c] = heights[c] + 1 if matrix[r][c] == 1 else 0
        # inline or call out to largest_rectangle_histogram(heights)
        best = max(best, _hist(heights))
    return best
```

**Drill focus**: same row-by-row collapse scaffold as Track A problems, but the inner is a **non-sum aggregate** (the stack-based histogram routine). Teaches that "collapse" is a meta-pattern independent of what the inner computes.

---

## Problem 3: `shortest_subarray_sum_ge_k`

LC 862. The **hybrid** you flagged — monotonic deque **on prefix sums**, not on values. This is where Track A (deque) meets Track B (prefix).

**Signature**
```python
def solution(nums: list[int], k: int) -> int
# returns length of shortest contiguous subarray with sum >= k, or -1 if none exists
```

**Approach** — build prefix sums `P[0..n]`. Maintain a deque of indices into `P` such that `P` values at those indices are strictly increasing. For each new `P[i]`:
1. While the deque has a front index `j` with `P[i] - P[j] >= k`, that's a candidate; record `i - j` and pop front (any later `i` would give a longer subarray, so front is done).
2. While the deque has a back index `j` with `P[j] >= P[i]`, pop back — a later query will prefer `P[i]` because it's smaller AND later (smaller subtrahend = larger difference).
3. Append `i`.

Return best length or -1.

**Test cases** (verified)

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1]` | 1 | 1 |
| 2 | `[1,2]` | 4 | -1 |
| 3 | `[2,-1,2]` | 3 | 3 |
| 4 | `[1,2,3,4,5]` | 11 | 3 |
| 5 | `[84,-37,32,40,95]` | 167 | 3 |
| 6 | `[48,99,37,4,-31]` | 140 | 2 |
| 7 | `[-1,-2,-3]` | 1 | -1 |
| 8 | `[5,-10,5,-5,10]` | 5 | 1 |
| 9 | `[17,85,93,-45,-21]` | 150 | 2 |

**prompt.md reference template**
```python
from collections import deque

def solution(nums, k):
    n = len(nums)
    P = [0] * (n + 1)
    for i, x in enumerate(nums):
        P[i + 1] = P[i] + x
    best = float('inf')
    dq = deque()        # indices into P, P-values strictly increasing
    for i, pi in enumerate(P):
        # front cleanup: any j such that pi - P[j] >= k is a valid window
        while dq and pi - P[dq[0]] >= k:
            best = min(best, i - dq.popleft())
        # back cleanup: a smaller later prefix dominates any larger earlier one
        while dq and P[dq[-1]] >= pi:
            dq.pop()
        dq.append(i)
    return best if best != float('inf') else -1
```

**Drill focus**: unlike plain "max subarray ≤ k" (B1) which uses `bisect`, this needs a **monotonic deque** because we optimize *length* (which depends on index distance), not just *value*. Teaches that prefix+deque is a distinct tool from prefix+bisect, and how to pick.

---

## Problem 4: `subarray_sum_closest_to_k`

Two-sided bisect query. Returns the **minimum |sum − k|** over all non-empty subarrays (not the sum itself — avoids tie-break ambiguity).

**Signature**
```python
def solution(nums: list[int], k: int) -> int
# min |subarray_sum - k| over all non-empty contiguous subarrays
```

**Approach** — same prefix + bisect/insort scaffold as B1. For each new `curr`, the best candidate prefix is whichever of the two neighbors of `curr - k` in the sorted prefix list yields the smaller absolute difference. So: `bisect_left(prefixes, curr - k)` gives an index; check both `prefixes[idx]` and `prefixes[idx-1]` (guard bounds), take whichever gives smallest `|curr - p - k|`. Then `insort(curr)`.

**Test cases** (verified)

| # | nums | k | expected |
|---|---|---|---|
| 1 | `[1,2,3]` | 4 | 1 |
| 2 | `[1,2,3]` | 6 | 0 |
| 3 | `[1,2,3]` | 100 | 94 |
| 4 | `[1]` | 5 | 4 |
| 5 | `[-5,3,-1]` | 0 | 1 |
| 6 | `[10,-10,10]` | 5 | 5 |
| 7 | `[1,2,3,4,5]` | 7 | 0 |
| 8 | `[-1,-2,3,2,-1]` | 5 | 0 |
| 9 | `[1]` | 1 | 0 |

**prompt.md reference template**
```python
from bisect import bisect_left, insort

def solution(nums, k):
    prefixes = [0]
    curr = 0
    best = float('inf')
    for x in nums:
        curr += x
        target = curr - k
        idx = bisect_left(prefixes, target)
        for j in (idx, idx - 1):
            if 0 <= j < len(prefixes):
                best = min(best, abs(curr - prefixes[j] - k))
        insort(prefixes, curr)
    return best
```

**Drill focus**: two-neighbor check. Unlike B1 where `bisect_left` gives the single best candidate, "closest to" needs to inspect both sides of the insertion point.

---

## Problem 5: `range_sum_2d`

LC 304 style. Multi-query 2D prefix sum. Fills the "preprocessing + many queries" axis and the "2D prefix" transformation entirely missing from the current set.

**Signature**
```python
def solution(matrix: list[list[int]], queries: list[tuple[int,int,int,int]]) -> list[int]
# each query is (r1, c1, r2, c2) inclusive on all four bounds
# return list of sums in query order
```

**Approach** — build a `(R+1) x (C+1)` prefix grid `P` where `P[r+1][c+1] = matrix[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]`. Then each query is O(1): `P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`.

**Test cases** (verified, using a single shared matrix)

Matrix:
```
[[3,0,1,4,2],
 [5,6,3,2,1],
 [1,2,0,1,5],
 [4,1,0,1,7],
 [1,0,3,0,5]]
```

| # | queries | expected |
|---|---|---|
| 1 | `[(2,1,4,3)]` | `[8]` |
| 2 | `[(1,1,2,2)]` | `[11]` |
| 3 | `[(1,2,2,4)]` | `[12]` |
| 4 | `[(0,0,0,0)]` | `[3]` |
| 5 | `[(0,0,4,4)]` | `[58]` |
| 6 | `[(2,1,4,3),(1,1,2,2),(1,2,2,4)]` | `[8,11,12]` |

Also include a tiny-matrix edge:
| 7 | matrix `[[5]]`, queries `[(0,0,0,0)]` | `[5]` |
| 8 | matrix `[[1,2],[3,4]]`, queries `[(0,0,1,1),(0,0,0,1),(1,0,1,1)]` | `[10,3,7]` |
| 9 | matrix `[[1,-1],[1,-1]]`, queries `[(0,0,1,1),(0,0,0,0),(1,1,1,1)]` | `[0,1,-1]` |

Note: tests 1–6 use the same big matrix (first arg), so the parametrize tuple needs to include the matrix. Simplest approach: one `cases` list where each entry is `(name, matrix, queries, expected)`.

**prompt.md reference template**
```python
def solution(matrix, queries):
    R, C = len(matrix), len(matrix[0])
    P = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            P[r+1][c+1] = matrix[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]
    out = []
    for r1, c1, r2, c2 in queries:
        out.append(P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1])
    return out
```

**Drill focus**: 4-point subtraction (inclusion-exclusion on corners) and the `(R+1)×(C+1)` padding trick that eliminates boundary checks.

---

## Problem 6: `submatrix_sum_equals_k_exists`

Drills the **existence/boolean** answer axis, which no current problem covers. Reuses the A3 hashmap-collapse scaffold but short-circuits on first hit.

**Signature**
```python
def solution(matrix: list[list[int]], target: int) -> bool
```

**Approach** — same as `count_submatrices_target`, but return `True` as soon as any valid submatrix is found.

**Test cases** (verified)

| # | matrix | target | expected |
|---|---|---|---|
| 1 | `[[1,2],[3,4]]` | 3 | True |
| 2 | `[[1,2],[3,4]]` | 100 | False |
| 3 | `[[1,2],[3,4]]` | 10 | True |
| 4 | `[[0]]` | 0 | True |
| 5 | `[[5]]` | 0 | False |
| 6 | `[[1,-1],[1,-1]]` | 0 | True |
| 7 | `[[1,1],[1,1]]` | 2 | True |
| 8 | `[[1,1],[1,1]]` | 5 | False |
| 9 | `[[0,1,0],[1,1,1],[0,1,0]]` | 5 | True |

(Verify #9: the whole matrix sums to 5. ✓)

**prompt.md reference template**
```python
from collections import defaultdict

def solution(matrix, target):
    R, C = len(matrix), len(matrix[0])
    for left in range(C):
        row_sums = [0] * R
        for right in range(left, C):
            for r in range(R):
                row_sums[r] += matrix[r][right]
            seen = {0}
            curr = 0
            for s in row_sums:
                curr += s
                if curr - target in seen:
                    return True
                seen.add(curr)
    return False
```

**Drill focus**: early-exit variant of the count-target scaffold. Same skeleton, different answer type.

---

## Problem 7: `diagonal_traverse`

LC 498. Directional flattening, zigzag diagonals. No shared algorithmic structure with the rest of the library — pure index-juggling drill.

**Signature**
```python
def solution(matrix: list[list[int]]) -> list[int]
```

**Approach** — iterate `d` from `0` to `R+C-2`; on even `d` go up-right, on odd `d` go down-left. For even `d`: start at `(min(d, R-1), d - min(d, R-1))` and walk up-right. Odd: mirror.

**Test cases**

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,4,7,5,3,6,8,9]` |
| 2 | `[[1,2],[3,4]]` | `[1,2,3,4]` |
| 3 | `[[1]]` | `[1]` |
| 4 | `[[1,2,3]]` | `[1,2,3]` |
| 5 | `[[1],[2],[3]]` | `[1,2,3]` |
| 6 | `[[1,2],[3,4],[5,6]]` | `[1,2,3,5,4,6]` |
| 7 | `[[1,2,3],[4,5,6]]` | `[1,2,4,5,3,6]` |
| 8 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,5,9,6,3,4,7,10,11,8,12]` |

**Verify test 6 `[[1,2],[3,4],[5,6]]` (3 rows, 2 cols)**:
- d=0: (0,0)=1
- d=1 (going down-left): (0,1)=2, (1,0)=3
- d=2 (going up-right): (2,0)=5, (1,1)=4
- d=3 (going down-left): (2,1)=6
- Result: [1,2,3,5,4,6] ✓

**Verify test 8** (3x4): d=0: 1; d=1↓: 2,5; d=2↑: 9,6,3; d=3↓: 4,7,10; d=4↑: 11,8; d=5↓: 12. Result: [1,2,5,9,6,3,4,7,10,11,8,12] ✓

**prompt.md reference template**
```python
def solution(matrix):
    if not matrix or not matrix[0]: return []
    R, C = len(matrix), len(matrix[0])
    out = []
    for d in range(R + C - 1):
        if d % 2 == 0:  # going up-right
            r = min(d, R - 1)
            c = d - r
            while r >= 0 and c < C:
                out.append(matrix[r][c])
                r -= 1
                c += 1
        else:           # going down-left
            c = min(d, C - 1)
            r = d - c
            while c >= 0 and r < R:
                out.append(matrix[r][c])
                r += 1
                c -= 1
    return out
```

---

## Problem 8: `spiral_order`

LC 54. Directional flattening, spiral.

**Signature**
```python
def solution(matrix: list[list[int]]) -> list[int]
```

**Approach** — four boundaries `top, bottom, left, right`; walk top row left→right, right col top→bottom, bottom row right→left (guard that top<bottom), left col bottom→top (guard that left<right). Shrink boundaries, repeat.

**Test cases**

| # | matrix | expected |
|---|---|---|
| 1 | `[[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,3,6,9,8,7,4,5]` |
| 2 | `[[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,3,4,8,12,11,10,9,5,6,7]` |
| 3 | `[[1]]` | `[1]` |
| 4 | `[[1,2]]` | `[1,2]` |
| 5 | `[[1],[2]]` | `[1,2]` |
| 6 | `[[1,2],[3,4]]` | `[1,2,4,3]` |
| 7 | `[[1,2,3],[4,5,6]]` | `[1,2,3,6,5,4]` |
| 8 | `[[1,2],[3,4],[5,6]]` | `[1,2,4,6,5,3]` |
| 9 | `[[1,2,3,4,5]]` | `[1,2,3,4,5]` |

**Verify test 8** `[[1,2],[3,4],[5,6]]` (3x2):
- top row left→right: 1,2 (row 0)
- right col top→bottom starting row 1: 4,6 (col 1, rows 1..2)
- bottom row right→left (row 2, cols 0..0, since right already consumed): 5 (col 0)
- left col bottom→top (col 0, rows 1..1): 3
- Result: [1,2,4,6,5,3] ✓

**prompt.md reference template**
```python
def solution(matrix):
    if not matrix or not matrix[0]: return []
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1): out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1): out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): out.append(matrix[r][left])
            left += 1
    return out
```

---

## Implementation checklist (for each problem)

1. `mkdir -p problems/<name>`
2. Create `__init__.py` (empty)
3. Create `solution.py`:
   ```python
   def solution(...) -> ...:
       # TODO: <one-line skill being drilled>
       pass
   ```
4. Create `tests.py` with `pytest.mark.parametrize` on a `cases` list, using `ids=[c[0] for c in cases]`. The first arg after `solution` is always `name`.
5. Create `prompt.md` with:
   - Problem description
   - Signature
   - `## Reference template` section (the pseudocode from this doc — frame as "read once, solve without peeking")
   - `## Drill focus` bullet list
   - `## Test cases` table
6. Run `.venv/bin/pytest problems/<name> --tb=no -q` and confirm all tests **fail** (stub returns None, so assertions fail cleanly — not errors).

## Ordering / dependencies

- **#1 first**, because **#2** uses it as a conceptual building block (even though the `_hist` helper in #2 is inlined, the user should drill #1 standalone first).
- **#2** next — it's the single highest-value addition (fills the boolean-collapse gap).
- **#3** next — the deque/prefix hybrid, flags a common interview pain point.
- **#4**, **#5**, **#6** in any order (they drill independent axes).
- **#7**, **#8** last (lowest priority; directional-flattening muscle drills).

## Verification after all 8 are built

```bash
cd /Users/cscholbe/apps/dsa
.venv/bin/pytest problems/ --tb=no -q
```

Every existing problem should still pass/fail exactly as it did before. The 8 new problems should all fail (stub), with total failure count equal to `(existing failures) + sum(len(cases) for each new problem)`.

## What this plan deliberately does NOT cover

- **2D cumulative max/min** (harder than 2D sum because not invertible) — skip for now; niche.
- **Sliding window + prefix set hybrid beyond #3** (e.g. range-count over a sliding window of prefixes) — skip; one hybrid drill (#3) is sufficient for the pattern.
- **Sweep line + ordered prefix** (skyline-style) — distinct enough to warrant its own future plan; out of scope here.
- **Streaming / online updates to prefix state** — same reason; different family.

---

## Summary table

| # | name | family gap filled | test cases |
|---|---|---|---|
| 1 | `largest_rectangle_histogram` | monotonic stack | 9 |
| 2 | `maximal_rectangle_ones` | boolean-inner collapse | 9 |
| 3 | `shortest_subarray_sum_ge_k` | deque-on-prefix hybrid | 9 |
| 4 | `subarray_sum_closest_to_k` | two-sided bisect query | 9 |
| 5 | `range_sum_2d` | 2D prefix preprocessing | 9 |
| 6 | `submatrix_sum_equals_k_exists` | existence/bool axis | 9 |
| 7 | `diagonal_traverse` | directional flattening | 8 |
| 8 | `spiral_order` | directional flattening | 9 |
