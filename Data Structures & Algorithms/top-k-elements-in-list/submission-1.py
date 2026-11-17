class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in count.items():
            buckets[v].append(key)
        ret = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                if len(ret) == k:
                    return ret
                ret.append(j)
        return ret