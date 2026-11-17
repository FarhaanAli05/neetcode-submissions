class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            for j in range(len(matrix[i])//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i])-1-j]
                matrix[i][len(matrix[i])-1-j] = temp