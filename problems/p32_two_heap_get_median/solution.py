import heapq
from typing import List


class _TwoHeap:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.minSize, self.maxSize = 0, 0
        self.delayed = {}

    def getMedian(self) -> float:
        # TODO: if maxSize == minSize (even total), return the average of the two heap tops.
        #       Otherwise (maxSize == minSize + 1, odd total), return the maxHeap top.
        # Remember: maxHeap stores negated values, so the actual max is -self.maxHeap[0].
        # Return value must be a float.
        pass

    def _rebalance(self):
        if self.maxSize > self.minSize + 1:
            val = -heapq.heappop(self.maxHeap)
            self.maxSize -= 1
            heapq.heappush(self.minHeap, val)
            self.minSize += 1
            self._prune(self.maxHeap)
        elif self.maxSize < self.minSize:
            val = heapq.heappop(self.minHeap)
            self.minSize -= 1
            heapq.heappush(self.maxHeap, -val)
            self.maxSize += 1
            self._prune(self.minHeap)

    def _prune(self, heap):
        while heap:
            num = heap[0] if heap is self.minHeap else -heap[0]
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heapq.heappop(heap)
            else:
                break

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
                self._prune(self.maxHeap)
        else:
            self.minSize -= 1
            if self.minHeap and num == self.minHeap[0]:
                self._prune(self.minHeap)
        self._rebalance()


def solution(max_vals: List[int], min_vals: List[int], max_size: int, min_size: int) -> float:
    """
    Set up heap state from the given values and virtual sizes, call getMedian(),
    return the result.
    max_vals are the actual values on the max side (stored negated internally).
    delayed={} for these tests.
    """
    h = _TwoHeap()
    h.maxHeap = [-v for v in max_vals]
    heapq.heapify(h.maxHeap)
    h.minHeap = list(min_vals)
    heapq.heapify(h.minHeap)
    h.maxSize = max_size
    h.minSize = min_size
    return h.getMedian()
