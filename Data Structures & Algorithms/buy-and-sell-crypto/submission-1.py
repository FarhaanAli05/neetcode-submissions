class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        max_p = 0
        for r in range(1, n):
            if prices[r] - prices[l] < 1:
                l = r
            max_p = max(max_p, prices[r] - prices[l])
        return max_p