class Solution:
    def isValid(self, s: str) -> bool:
        
        #stack
        stk = []

        # hashmap
        opentoclose = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in opentoclose:
                if stk and stk[-1] == opentoclose[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        
        return True if not stk else False
            

            

# { [ ( 

