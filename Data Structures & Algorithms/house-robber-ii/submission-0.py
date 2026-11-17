class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        prev1, cur1 = nums[0], max(nums[0], nums[1])
        prev2, cur2 = nums[1], max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            prev1, cur1 = cur1, max(prev1 + nums[i], cur1)
        for i in range(2, len(nums) - 1):
            prev2, cur2 = cur2, max(prev2 + nums[i+1], cur2)
        return max(cur1, cur2)