class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        Sarr = list(s)
        Sarr.sort()
        
        Tarr = list(t)
        Tarr.sort()

        if Sarr == Tarr:
            return True
        else:
            return False