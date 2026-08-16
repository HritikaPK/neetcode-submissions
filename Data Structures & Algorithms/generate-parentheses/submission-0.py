class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sub = [],[]

        def dfs(c,o):
            # rule: base
            if o==c==n:
                res.append(''.join(sub.copy()))
                return 

            # rule: if close == open : add open 
            if o < n:
                sub.append('(')
                dfs(c,o+1)
                sub.pop()

            # rule: if close < open: add open and close
            if c < o:
                sub.append(')')
                dfs(c+1,o)
                sub.pop()
            
        dfs(0,0)
        return res