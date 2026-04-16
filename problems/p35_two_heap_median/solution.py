import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap, maxHeap = [], []
        minSize, maxSize = 0, 0
        delayed = {}

        def add(num):
            nonlocal maxSize, minSize
            if not maxHeap or num <= -maxHeap[0]:
                heapq.heappush(maxHeap, -num)
                maxSize += 1
            else:
                heapq.heappush(minHeap, num)
                minSize += 1
            rebalance()

        def rebalance():
            nonlocal maxSize, minSize
            if maxSize > minSize + 1:
                val = -heapq.heappop(maxHeap)
                maxSize -= 1
                heapq.heappush(minHeap, val)
                minSize += 1
                prune(maxHeap)
            elif maxSize < minSize:
                val = heapq.heappop(minHeap)
                minSize -= 1
                heapq.heappush(maxHeap, -val)
                maxSize += 1
                prune(minHeap)

        def prune(heap):
            while heap:
                num = heap[0] if heap is minHeap else -heap[0]
                if num in delayed:
                    delayed[num] -= 1
                    if delayed[num] == 0:
                        del delayed[num]
                    heapq.heappop(heap)
                else:
                    break

        def remove(num):
            nonlocal maxSize, minSize
            delayed[num] = delayed.get(num, 0) + 1
            if maxHeap and num <= -maxHeap[0]:
                maxSize -= 1
                if -num == maxHeap[0]:
                    prune(maxHeap)
            else:
                minSize -= 1
                if num == minHeap[0]:
                    prune(minHeap)
            rebalance()

        def getMedian():
            if maxSize == minSize:
                return (-maxHeap[0] + minHeap[0]) / 2
            return float(-maxHeap[0])

        # TODO: implement the sliding window loop using add, remove, getMedian.
        # Hint: seed the first k elements, record the first median,
        #       then for each new element slide the window one step right.
        pass
