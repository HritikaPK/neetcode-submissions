class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows , cols = len(heights), len(heights[0])

        pac, atl = set(), set()
        
        def dfs(r,c,visit,prevH):
            #base case
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or heights[r][c] < prevH):
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        #column wise
        for c in range(cols):
            # traverse pac cols
            dfs(0,c,pac,heights[0][c])

            # traverse atl cols 
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        # row-wise
        for r in range(rows):
            #traverse pac rows:
            dfs(r,0,pac,heights[r][0])

            #traverse atl rows:
            dfs(r,cols-1,atl,heights[r][cols-1])

        res = []
        # interate throough all and find common 
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
                

        
        