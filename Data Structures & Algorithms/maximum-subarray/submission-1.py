class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = nums[0]
        curSum = 0

        for n in nums:
            #reset and ignore prev values 
            if curSum < 0:
                curSum = 0
            curSum += n
            maxsum = max(curSum,maxsum)
        
        return maxsum
        