class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        def backtrack(i,cursum):
            nonlocal count
            if i == len(nums):
                if cursum == target: 
                    return 1
                else:
                    return 0 
    
            return backtrack(i+1,cursum + nums[i]) + backtrack(i+1,cursum - nums[i])

        return backtrack(0,0)
        