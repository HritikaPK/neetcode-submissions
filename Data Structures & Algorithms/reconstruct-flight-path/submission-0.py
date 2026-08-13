class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dest in tickets}
        tickets.sort()

        for src,dst in tickets:
            adj[src].append(dst)

        
        res = ["JFK"]

        def dfs(src):
            # base case:
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src]) # JFK = ABC, DEF
            for i,v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)

                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i,v)
            return False
        
        dfs("JFK")
        return res
