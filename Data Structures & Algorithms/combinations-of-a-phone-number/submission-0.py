class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        part = []

        hashmap = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        def backtrack(i):

            # base case:
            if len(part) == len(digits):
                res.append("".join(part))
                return

            if i > len(digits):
                return
            
            #main logic
            # i is digits[0] => 2
            for j in hashmap[int(digits[i])]:
                part.append(j)
                backtrack(i+1)
                part.pop()

        if digits:
            backtrack(0)
        return res


        