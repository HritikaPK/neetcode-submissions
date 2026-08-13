class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minute = 0
        
        fresh = 0

        q = deque()
        visit = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            nonlocal fresh 

            #base case
            if (r < 0 or (r,c) in visit or c < 0 or r == rows or c == cols or grid[r][c] == 0):
                return
            
            grid[r][c] = 2
            rotten = 1
            visit.add((r,c))
            fresh -= 1
            q.append([r,c])


        # add rotten food to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        
        # look around rotten food:
        while q:
            for f in range(len(q)):
                r,c = q.popleft()

                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            if q:
                minute += 1
            

        return minute if fresh == 0 else -1


        

        