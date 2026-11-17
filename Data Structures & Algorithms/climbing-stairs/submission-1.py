class Solution:
    def climbStairs(self, n: int) -> int:
        # DP bottom-up: constant-space
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev, cur = 1, 2
        for _ in range(2, n):
            prev, cur = cur, prev+cur
        return cur
        # time: O(n)
        # space: O(1)