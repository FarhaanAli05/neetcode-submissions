class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            dict[i] = 1 + dict.get(i, 0)
        for i in dict:
            if dict[i] > 1:
                return True
        return False