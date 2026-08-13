class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # maintain rank
        rank = [1] * (len(edges)+1)

        # maintain parents
        par = [i for i in range(len(edges)+1)]


        # find root node
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res


        # union- and connect to shallow trees to deeper ones
        # if the roots are the same for 2 nodes alrwady, means a connection already exists, so return false
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # go through each edge
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        