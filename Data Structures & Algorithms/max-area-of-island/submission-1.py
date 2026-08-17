class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS , COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r,c,land):
            # when to return 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1 or (r,c) in visited:
                return
            
            land.add((r,c))
            visited.add((r,c))

            dfs(r+1,c,land)
            dfs(r-1,c,land)
            dfs(r,c-1,land)
            dfs(r,c+1,land)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island = set()
                    dfs(r,c,island)
                    maxArea = max(maxArea,len(island))
        
        return maxArea
