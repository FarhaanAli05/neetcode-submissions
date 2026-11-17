class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                inRow = (board[i][j], "row", i)
                inColumn = (board[i][j], "column", j)
                inSubBox = (board[i][j], "sub-box", i//3, j//3)
                if inRow in seen or inColumn in seen or inSubBox in seen:
                    return False
                seen.add(inRow)
                seen.add(inColumn)
                seen.add(inSubBox)
        return True