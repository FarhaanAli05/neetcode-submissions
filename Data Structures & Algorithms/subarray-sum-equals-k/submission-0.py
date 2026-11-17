class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        freq = {0: 1}
        subarrays = 0
        for i in range(len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i])
        for i in range(1, len(prefix_sum)):
            if (prefix_sum[i] - k) in freq:
                subarrays += freq[prefix_sum[i] - k]
            freq[prefix_sum[i]] = freq.get(prefix_sum[i], 0) + 1
        return subarrays