class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # coins = [1,2,5]
        # amount = 5
        # (5) (1,1,1,1,1) (2,2,1) (2,1,2) (2,1,1,1)

        # requirements:
        #- do not repeat combinations
        # optimal time and space complex

        dp = [[0] * (len(coins)+1) for _ in range(amount+1)]

        dp[0] = [1] * (len(coins)+1)

        # outer loop - amount
        for a in range(1,amount+1):
            for i in range(len(coins)-1,-1,-1):
                dp[a][i] = dp[a][i+1]

                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]

        return dp[amount][0]

        # innerloop - coins [] 

        





        
        