import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        tc: o(n log n)
        sc: o(1)
        """
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]