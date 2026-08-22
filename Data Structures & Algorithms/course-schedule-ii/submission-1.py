class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mapping = defaultdict(list)
        for a,b in prerequisites:
            mapping[a].append(b)

        path = []
        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(node,path):
            
            if states[node] == visiting:
                return False
            elif states[node] == visited:
                return True
            
            states[node] = visiting

            for g in mapping[node]:
                if not dfs(g,path):
                    return False
            path.append(node)
            states[node] = visited
            return True
        

        for i in range(numCourses):
            if not dfs(i,path):
                return []
        return path
        