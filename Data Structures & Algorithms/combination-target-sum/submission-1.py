class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [[] for _ in range(target + 1)]
        res[0] = [[]]
        for num in nums:
            for i in range(num, target + 1):
                for x in res[i - num]:
                    res[i] += [x + [num]]
        return res[target]