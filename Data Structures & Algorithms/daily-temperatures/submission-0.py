class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for t, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                tmp, i = stack.pop()
                res[i] = t - i
            stack.append((n, t))
        return res