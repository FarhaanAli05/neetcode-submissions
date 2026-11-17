class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = n * m
        l = 0
        r = t - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False