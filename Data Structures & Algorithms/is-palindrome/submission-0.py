class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i<j:
            print("enter loop")
            #if non-alpha num
            #if i = j
            # if i!=j
            if s[i].isalnum() == False:
                i += 1
                continue
            elif s[j].isalnum() == False:
                j -= 1
                continue
            print("ch1",i,j)
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
            print("ch2",i,j)
        return True
