class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        
        

        if sorted(s) == sorted(t):
            return True
        else:
            return False

        # # s = t
        # #hashmap

        # # base case: length dont match
        # if len(s)!=len(t):
        #     return False

        # sh, th = {}, {}
        
        # # creating hashmaps and filling em
        # for i in range(len(s)):
        #     sh[s[i]] = 1 + sh.get(s[i],0)
        #     th[t[i]] = 1 + th.get(t[i],0)
        
        # # parsing through each char and comapring counts. if char not exist, 0
        # for c in sh:
        #     if sh[c] != th.get(c,0):
        #         return False
        
        # return True

            


        
        
