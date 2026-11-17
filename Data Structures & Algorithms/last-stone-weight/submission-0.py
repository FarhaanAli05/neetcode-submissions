class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            large = -heapq.heappop(stones)
            small = -heapq.heappop(stones)
            if (large == small):
                continue
            else:
                diff = large - small
                heapq.heappush(stones, -diff)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]