class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case

        total = sum([i for i in nums])
        
        if total % 2 != 0:
            return False

        target = total/2
        # main logic
        # DP using hashmap

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for j in dp:
                nextDP.add(j+nums[i])
                nextDP.add(j)
            dp = nextDP
        
        return target in dp



