class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visit = set()
        ROWS, COLS =  len(grid) , len(grid[0])
        q = deque()

        def bfs(r,c):
            
            #base case
            if ( r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append([r,c])



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        # BFS 
        while q:

            for room in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist += 1







        