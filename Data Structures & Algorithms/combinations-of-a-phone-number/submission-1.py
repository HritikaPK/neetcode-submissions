class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(i,sub):
            # base case
            if len(sub) == len(digits):
                res.append(sub)
                return

            for d in hashmap[digits[i]]:
                dfs(i+1,sub+d)
        if digits:
            dfs(0,"")
        return res