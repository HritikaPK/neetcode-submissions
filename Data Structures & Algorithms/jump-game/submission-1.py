class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal post
        goal = len(nums) - 1
        check = goal - 1
        
        # start from last element
        while check >= 0:

            # check last-1 element. Can it reach goal?
            if nums[check] + check >= goal:
                # yes - move goal post closer
                goal = check
                check -= 1

                #no - move to last-1 -1 element
            else:
                check -= 1

        if goal == 0:
            return True
        else:
            return False    
        # if goal post == 1st position return true
