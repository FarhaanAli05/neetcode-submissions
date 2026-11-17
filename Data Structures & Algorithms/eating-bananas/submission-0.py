class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        l = 1
        r = largest
        while l <= r:
            counter = 0
            mid = (l + r) // 2
            for i in piles:
                counter += math.ceil((i * 1.0) / mid)
            if counter <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l