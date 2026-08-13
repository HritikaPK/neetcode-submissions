class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i,cursum):
            if (i,cursum) in dp:
                return dp[(i,cursum)]

            if i == len(nums):
                if cursum == target: 
                    return 1
                else:
                    return 0 
            
            dp[(i,cursum)] = backtrack(i+1,cursum + nums[i]) + backtrack(i+1,cursum - nums[i])
            return dp[(i,cursum)]
        return backtrack(0,0)
        