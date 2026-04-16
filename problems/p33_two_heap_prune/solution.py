import heapq
from typing import List, Optional


class _TwoHeap:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.minSize, self.maxSize = 0, 0
        self.delayed = {}

    def prune(self, heap) -> None:
        # TODO: while heap is non-empty, peek at the top element.
        #       For minHeap the top is heap[0]; for maxHeap it is -heap[0].
        #       If that element is in self.delayed, decrement its count
        #       (delete the key if count reaches 0) and pop it from the heap.
        #       Otherwise break.
        pass

    def _rebalance(self):
        if self.maxSize > self.minSize + 1:
            val = -heapq.heappop(self.maxHeap)
            self.maxSize -= 1
            heapq.heappush(self.minHeap, val)
            self.minSize += 1
            self.prune(self.maxHeap)
        elif self.maxSize < self.minSize:
            val = heapq.heappop(self.minHeap)
            self.minSize -= 1
            heapq.heappush(self.maxHeap, -val)
            self.maxSize += 1
            self.prune(self.minHeap)

    def _add(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            self.maxSize += 1
        else:
            heapq.heappush(self.minHeap, num)
            self.minSize += 1
        self._rebalance()

    def _remove(self, num: int) -> None:
        self.delayed[num] = self.delayed.get(num, 0) + 1
        if self.maxHeap and num <= -self.maxHeap[0]:
            self.maxSize -= 1
            if -num == self.maxHeap[0]:
                self.prune(self.maxHeap)
        else:
            self.minSize -= 1
            if self.minHeap and num == self.minHeap[0]:
                self.prune(self.minHeap)
        self._rebalance()

    def _getMedian(self) -> float:
        if self.maxSize == self.minSize:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return float(-self.maxHeap[0])


def solution(heap_vals: List[int], delayed: dict, is_max_heap: bool) -> Optional[int]:
    """
    Construct a heap from heap_vals, apply the given delayed dict, call prune,
    then return the top element (None if heap is empty after pruning).
    is_max_heap=True  → values stored negated (max-heap via negation).
    is_max_heap=False → values stored directly (min-heap).
    """
    h = _TwoHeap()
    h.delayed = dict(delayed)  # copy so the test dict is not mutated

    if is_max_heap:
        h.maxHeap = [-v for v in heap_vals]
        heapq.heapify(h.maxHeap)
        h.prune(h.maxHeap)
        return -h.maxHeap[0] if h.maxHeap else None
    else:
        h.minHeap = list(heap_vals)
        heapq.heapify(h.minHeap)
        h.prune(h.minHeap)
        return h.minHeap[0] if h.minHeap else None
