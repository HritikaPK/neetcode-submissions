class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1 # 1 way to sum to zero 

        for i in range(len(nums)): # 0 to 4 for [1,1,1,1,1]
            for cursum, count in dp[i].items():
                dp[i+1][cursum + nums[i]] += count
                dp[i+1][cursum - nums[i]] += count

        return dp[len(nums)][target]