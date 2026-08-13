class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def dfs(i,j):

            if j == len(t):
                return 1 # end of string

            if i == len(s):
                return 0 # end of s before end of t = before matched
            
            if (i,j) in cache:
                return cache[(i,j)]

            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
            
            return res
        return dfs(0,0)

            




        