class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # key : (i,buy/not buying)
        dp = {}


        def dfs(i,buying):
            #base cases

            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            #main logic:
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy,cooldown)
            else:
                selling = dfs(i+2, not buying) + prices[i]
                dp[(i,buying)] = max(selling,cooldown)
            return dp[(i,buying)]
        return dfs(0,True)

            
        