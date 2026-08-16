class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        palin = []

        #check palin logic
        def checkpalin(substring):
            l = 0
            r = len(substring) - 1
            while l <= r:
                if substring[l]==substring[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        # backtrack logic
        def dfs(i):
            if i == len(s):
                res.append(palin.copy())
                return 

            for j in range(i,len(s)):
                if checkpalin(s[i:j+1]):
                    palin.append(s[i:j+1])
                    dfs(j+1)
                    palin.pop()
            
        dfs(0)
        return res

            