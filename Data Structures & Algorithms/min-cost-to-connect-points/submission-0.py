class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points = [(1,1), (2,3), .......]
        n = len(points)

        # create adj 
        adj = {i:[] for i in range(n)}
        # adj = {  0:[],
        #          1:[].....}

        # adj = [node1:[cost,node2],[node2:[cost,node1]]
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        print(adj)
        # maintain visit
        visit = set()
        # use heap 
        minH = [[0,0]]
        # maintain result
        res = 0
        
        # go through heap unti we reach all points 
        while len(visit) < n:
            cost, i = heapq.heappop(minH)   # cost = min. cost 
            if i in visit:
                continue
            visit.add(i)
            res += cost 

            for neiC,nei in adj[i]:
                if nei in visit:
                    continue
                
                heapq.heappush(minH,[neiC,nei])
        print(visit)
        return res
        # return result 

        