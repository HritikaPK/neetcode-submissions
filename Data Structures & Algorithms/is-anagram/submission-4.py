class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s = t
        #hashmap
        if len(s)!=len(t):
            return False

        sh, th = {}, {}

        for i in range(len(s)):
            sh[s[i]] = 1 + sh.get(s[i],0)
            th[t[i]] = 1 + th.get(t[i],0)
        
        for c in sh:
            if sh[c] != th.get(c,0):
                return False
        
        return True

            


        
        
