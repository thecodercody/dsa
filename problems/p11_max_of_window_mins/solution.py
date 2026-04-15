from collections import deque
def solution(arr: list[int], k: int) -> int:
    q = deque()
    max_val = float('-inf')
    l = 0
    for i in range(len(arr)):
        while q and q[0] < l:
            q.popleft()

        while q and arr[q[-1]] > arr[i]:
            q.pop()
        
        q.append(i)
        if i - l + 1 == k:
            max_val = max(max_val, arr[q[0]])
            l += 1
        
            
    return max_val