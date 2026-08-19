class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        minutes = -1
        fresh = 0

        # add to queue the rotten fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh +=1

        if fresh == 0:
            return 0
        #bfs
        def bfs(r,c):
            # when to simply return 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return

            visited.add((r,c))
            q.append([r,c])
            grid[r][c] = 2
            nonlocal fresh
            fresh -= 1
        

        # if no rotten fruits -> return -1
        if not q:
            return -1
        
        
        # go through each fruit per min 
        # case 1: all fruits do rot
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
                
            minutes += 1

        # case 2: all fruits DONT rot (some left) -> grid has 1 somewhere
        if fresh > 0:
            return -1
        else:
            return minutes 


        
        