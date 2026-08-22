class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        #same parents = cycle

        def find(node):
            res = node
            while res != par[res]:
                #res = par[par[res]]
                res = par[res]
            return res


        def union(n1,n2):
            #find parent
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                #cycle
                return [n1,n2]
            elif rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

    
        for e1,e2 in edges:
            cycle = union(e1,e2)
            if cycle:
                return cycle


        