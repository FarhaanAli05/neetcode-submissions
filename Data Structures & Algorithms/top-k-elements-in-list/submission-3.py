class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        n = len(nums)
        freqs = [0] * (n + 1)
        for val, fr in freq.items():
            if freqs[fr] == 0:
                freqs[fr] = [val]
            else:
                freqs[fr].append(val)
        res = []
        for i in range(n, 0, -1):
            if len(res) == k:
                break
            if freqs[i] != 0:
                res.extend(freqs[i])
        return res