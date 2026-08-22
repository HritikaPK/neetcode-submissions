class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        res =[]

        #DFS
        def dfs(r,c,visited,preH):
            #base case return
            if (r,c) in visited or r < 0 or c<0 or r >= ROWS or c >= COLS or preH > heights[r][c]:
                return
            
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])

        #rows
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl, heights[ROWS-1][c])

        #cols
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl, heights[r][COLS-1])
        
        # intersection between pac and atl
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
                    
         

        