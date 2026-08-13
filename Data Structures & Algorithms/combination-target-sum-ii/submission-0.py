class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def backtrack(i, cur, total):

            # achieved target value
            if total == target:
                res.append(cur.copy())
                return 
            
            # when to end or return to skip
            if total > target or i == len(candidates):
                return 
            
            # include i 
            cur.append(candidates[i])
            backtrack(i+1,cur, candidates[i] + total)
            cur.pop()

            # dont include i 
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1,cur,total)
        backtrack(0,[],0)
        return res

