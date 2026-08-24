class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        

        HmapS , HmapT = {}, {}

        for i in range(len(s)):

            HmapS[s[i]] = 1 + HmapS.get(s[i], 0)
            HmapT[t[i]] = 1 + HmapT.get(t[i], 0)
        
        return HmapS == HmapT