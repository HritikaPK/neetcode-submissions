class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        
        def bfs(r,c,p):
            # REturn: incase nothing works out
            if r < 0 or c < 0 or r >=ROWS or c >= COLS or (r,c) in visited or grid[r][c] == -1:
                return
            
            grid[r][c] = p + 1
            q.append([r,c])
            visited.add((r,c))

        # add all gates to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        while q:
            r,c = q.popleft()
            n = grid[r][c]

            bfs(r+1,c,n)
            bfs(r-1,c,n)
            bfs(r,c+1,n)
            bfs(r,c-1,n)




        

        