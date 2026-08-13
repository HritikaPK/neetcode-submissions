class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map1, map2 = {}, {}

        if len(s) == len(t):
            for i in range(len(s)):
                map1[s[i]] = map1.get(s[i],0) + 1
                map2[t[i]] = map2.get(t[i],0) + 1
        else:
            return False

        print(map1,map2)
        if map1 == map2:
            return True
        return False
