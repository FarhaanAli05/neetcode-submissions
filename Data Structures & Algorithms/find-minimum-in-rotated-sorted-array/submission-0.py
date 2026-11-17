class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l += 1
            elif nums[l] > nums[m]:
                r -= 1
            elif nums[l] < nums[m] < nums[r]:
                return nums[l]
            else:
                return nums[m]