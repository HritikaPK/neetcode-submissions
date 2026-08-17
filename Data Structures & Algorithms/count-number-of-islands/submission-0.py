class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS =  len(grid), len(grid[0])
        path = set()
        islands = 0


        def dfs(r,c):           
            
            #base case: to return 
            if r < 0 or c < 0 or r >=ROWS or c >= COLS or (r,c) in path or grid[r][c]!="1":
                return 
            
            path.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

    
                
        
        # go through each [][]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in path:
                    dfs(r,c)
                    islands += 1

        #check if path and increment islands
        return islands
