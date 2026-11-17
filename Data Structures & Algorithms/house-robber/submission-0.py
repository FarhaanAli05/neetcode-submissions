class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP: bottom-up (constants)
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        prev = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, n):
            prev, cur = cur, max(prev + nums[i], cur)
        return cur
        # tc: o(n)
        # sc: o(1)