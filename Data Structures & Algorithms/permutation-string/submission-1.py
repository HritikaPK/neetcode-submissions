class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counts_s1 = [0] * 26
        counts_s2 = [0] * 26

        for i in range(len(s1)):
            counts_s1[ord(s1[i])-97] += 1
            counts_s2[ord(s2[i])-97] += 1
        
        if counts_s1 == counts_s2:
                return True
        
        for i in range(len(s1),len(s2)):
            counts_s2[ord(s2[i])-97] += 1
            counts_s2[ord(s2[i-len(s1)])-97] -= 1
            if counts_s1 == counts_s2:
                return True
            
        return False



        
