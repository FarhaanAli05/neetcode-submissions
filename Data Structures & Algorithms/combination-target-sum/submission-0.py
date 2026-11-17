class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # logic: iterate through nums. check if x number of i in range(i, len(nums)) satsifies target
        # we subtract x number of i from target, if target == 0, then we add that combination to res (list of lists)
        # nums = [2,3,6,7], target = 7
        # res = [[2,2,3],[7]]
        # tc: O(2^n), sc: O(n)
        nums.sort()
        res = []
        def comb(cur, start, target):
            if target == 0:
                res.append(cur)
                return
            for i in range(start, len(nums)):
                if nums[i] > target:
                    break
                comb(cur + [nums[i]], i, target - nums[i])
            return
        comb([], 0, target)
        return res