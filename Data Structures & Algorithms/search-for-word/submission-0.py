class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through board, if coordinate equals first letter in word, begin dfs
        # dfs condition: if the adjacent letter is in bounds, if it's not in seen, and it matches the pointer at the current letter in word
        # return false if the above condition doesn't match, true if we found the word

        # tc: O(m * n * 4^x), x is len(word)
        # sc: O(x), x is len(word)

        # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        # seen = {}
        # res = True
        # return res
        seen = set()
        rows, cols = len(board), len(board[0])
        def dfs(row, col, i):
            if i == len(word): return True
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in seen or word[i] != board[row][col]:
                return False
            seen.add((row, col))
            res = dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1, col, i+1) or dfs(row, col-1, i+1)
            seen.remove((row, col))
            return res
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0): return True
        return False