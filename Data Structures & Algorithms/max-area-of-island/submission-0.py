class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        
        m , n = len(grid), len(grid[0])

        def dfs(r,c):
            nonlocal res
            nonlocal count
            # base case: return
            if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] != 1:
                return 
            else:
                count += 1
                res = max(res,count)
                grid[r][c] = 0
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i,j)
        return res
        
                

        