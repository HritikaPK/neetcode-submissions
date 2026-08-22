class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # covert all Os to T
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)

        #find all Os in boarder and cal DFS
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if r in [0,ROWS-1] or c in [0,COLS-1]:
                        dfs(r,c)

        # convert remaining Os to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # convert Ts to Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        