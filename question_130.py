class Solution(object):
    def solve(self, board):
        if not board:
            return 
        rows, columns = len(board), len(board[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != "O":
                return 

            board[r][c] = "S"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in [0, columns - 1]:
                dfs(r, c)

        for c in range(columns):
            for r in [0, rows - 1]:
                dfs(r, c)

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"


