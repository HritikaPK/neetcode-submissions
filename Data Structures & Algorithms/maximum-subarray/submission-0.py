class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # first set [0] as maxsum

        # if [-2 1 -3 4 -1 2 1 -5 4 ]

        maxsub = nums[0]
        currsum = 0

        for n in nums:
            if currsum < 0:
                currsum = 0
            
            currsum += n
            maxsub = max(maxsub, currsum)

        return maxsub
