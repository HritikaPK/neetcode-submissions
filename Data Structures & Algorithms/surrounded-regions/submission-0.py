class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows , cols = len(board), len(board[0])

        def dfs(r,c):
            # base case
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # 1. DFS to change Os to T which are on the border and conencted to it 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]):
                    dfs(r,c)


        # 2. Change all Os to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Change all Ts to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        