class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()
        res = []
        n = len(nums)
        for i in range(k):
            while len(dq) > 0 and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        res.append(dq[0])
        for i in range(k, n):
            if dq[0] == nums[i-k]:
                dq.popleft()
            while len(dq) > 0 and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
            res.append(dq[0])
        return res