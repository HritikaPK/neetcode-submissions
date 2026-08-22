class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        mapping = defaultdict(list)

        for a,b in edges:
            mapping[a].append(b)
            mapping[b].append(a)

        visited = set()

        def dfs(curr,prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for j in mapping[curr]:
                if j == prev:
                    continue
                if not dfs(j,curr):
                    return False

            return True

        if dfs(0,-1) and n == len(visited):
            return True
        else:
            return False