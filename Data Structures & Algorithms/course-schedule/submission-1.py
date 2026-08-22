class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapping = defaultdict(list) 

        for a,b in prerequisites:
            mapping[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * (numCourses)
        
        def dfs(i):
            state = states[i]

            if state == VISITING:
                return False
            elif state == VISITED:
                return True
            
            states[i] = VISITING

            for q in mapping[i]:
                if not dfs(q):
                    return False
            states[i] = VISITED
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True 

        