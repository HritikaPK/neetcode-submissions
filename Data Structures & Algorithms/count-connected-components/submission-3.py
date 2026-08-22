class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)] # [1,2,3,4,5]
        rank = [1] * n   # [1,1,1,1,1]

        def find(node):
            res = node
            while res != par[res]:
                res = par[res]
            return res

        
        def union(e1,e2):
            p1,p2 = find(e1),find(e2)

            if p1 == p2:
                return 0
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        
        res = n
        for e1,e2 in edges:
            res -= union(e1,e2)
        
        return res