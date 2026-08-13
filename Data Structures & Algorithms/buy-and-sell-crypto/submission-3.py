class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # declare L and R
        l = 0 # buy
        r = 1 # sell
        gain = 0

        while r <len(prices):

            #check if buy < sell
            # check profit and update it with max

            if prices[l] <= prices[r]:
                gain = max(gain, prices[r]-prices[l])
                r += 1
            else:
                l = r
                r += 1
            
        return gain