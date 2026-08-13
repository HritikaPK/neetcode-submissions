class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag =set() # r+c
        negDiag = set() #r-c

        res = [] # all sols

        board = [["."] * n for i in range(n)]
        # . . . .
        # . . . .
        # . . . .
        # . . . .   

        def backtrack(r):

            # base case with n-queens soln 
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n): 
                # every single pos in current row 
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res





