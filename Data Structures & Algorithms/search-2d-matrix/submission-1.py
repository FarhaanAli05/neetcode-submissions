class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        if not l <= r:
            return False
        m = (l + r) // 2
        b, t = 0, COLS - 1
        while b <= t:
            mid = (b + t) // 2
            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] > target:
                t = mid - 1
            else:
                b = mid + 1
        return False