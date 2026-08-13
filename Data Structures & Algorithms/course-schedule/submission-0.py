class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visit = set()
        
        premap = {i:[] for i in range(numCourses)}
        #create hasmap with null for each i and append prereqs
        for crs,pre in prerequisites:
            premap[crs].append(pre)


        # dfs(i,visit)
        def dfs(i):
            if i in visit:
                return False

            if premap[i] == []:
                return True 

            visit.add(i)
            for pre in premap[i]:
                if not dfs(pre): return False
            
            visit.remove(i)
            premap[i] = []
            return True 

        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

        
         

            



        