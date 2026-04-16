from collections import deque
class Solution:
    def sliding_window_minimum(self, nums, k):
        # im going to use a sliding window with a monotonic increasing deque to store the minimum
        q = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while q and q[0] < l:
                q.popleft()
            
            while q and nums[q[-1]] > nums[r]:
                q.pop()
            
            q.append(r)

            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1

        return res
