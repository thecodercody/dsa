import heapq
from typing import List


class _TwoHeap:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.minSize, self.maxSize = 0, 0
        self.delayed = {}

    def remove(self, num: int) -> None:
        # TODO: mark num as delayed (increment its count in self.delayed).
        #       Determine which virtual size to decrement:
        #         - if num <= top of maxHeap (-self.maxHeap[0]), decrement maxSize;
        #           if num is physically at the maxHeap top (-num == self.maxHeap[0]),
        #           also call self._prune(self.maxHeap) immediately.
        #         - otherwise decrement minSize;
        #           if num is physically at the minHeap top (num == self.minHeap[0]),
        #           also call self._prune(self.minHeap) immediately.
        #       Then call self._rebalance().
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

    def _getMedian(self) -> float:
        if self.maxSize == self.minSize:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return float(-self.maxHeap[0])


def solution(nums_to_add: List[int], nums_to_remove: List[int]) -> float:
    """Add all nums_to_add, then remove all nums_to_remove; return the resulting median."""
    h = _TwoHeap()
    for n in nums_to_add:
        h._add(n)
    for n in nums_to_remove:
        h.remove(n)
    return h._getMedian()
