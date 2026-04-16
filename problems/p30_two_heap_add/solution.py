import heapq
from typing import List


class _TwoHeap:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.minSize, self.maxSize = 0, 0
        self.delayed = {}

    def add(self, num: int) -> None:
        # TODO: if maxHeap is empty OR num <= top of maxHeap, push num to maxHeap
        #       (remember: maxHeap stores negated values, so push -num).
        #       Otherwise push num to minHeap.
        #       Increment the relevant size counter.
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

    def _getMedian(self) -> float:
        if self.maxSize == self.minSize:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        return float(-self.maxHeap[0])


def solution(nums: List[int]) -> List[float]:
    """Add nums one by one; return list of medians (as floats) after each add."""
    h = _TwoHeap()
    result = []
    for n in nums:
        h.add(n)
        result.append(h._getMedian())
    return result
