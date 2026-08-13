class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # create rank to help track depth of tree from each node
        rank = [1] * n

        # maintain parent list
        par = [i for i in range(n)]

        print(rank,par)

        # find parent 
        def find(node):

            res = node 

            while res != par[res]:
                par[res] = par[par[res]] # go upstream
                res = par[res]  # change to root/ parent 

            return res # return parent / root

        # union - join shallower tree to bigger tree
        def union(n1,n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2: 
                # same roots mean already connected
                return 0
            
            # check ranks to connect shallower tree to deeper tree:
            if rank[p1] > rank[p2]:
                # p1 = 0   p2 = 2
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                # p1 = 3;  p2 =0   [3,0]
                # rank[p2] > rank[p1]
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1


        # maintain result
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)

        # return remainiing result == no. of different trees

        return res
        