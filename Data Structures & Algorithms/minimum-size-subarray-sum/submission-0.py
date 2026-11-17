class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        l = 0
        cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_size = min(min_size, r-l+1)
                cur_sum -= nums[l]
                l += 1
        if min_size == float('inf'):
            return 0
        return min_size