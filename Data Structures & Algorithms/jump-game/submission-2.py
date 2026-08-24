class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):

            # can n reach goal?
            if nums[i] + i >= goal:
                # if yes change goal to new goal (n)
                goal = i
                #conitue
            
        return True if goal == 0 else False
        
