class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # 1 pile an hour
        # 10 piles = max speed is 10

        l = 1 
        r = max(piles)
        res = r

        
        while l<=r:
            hours = 0   
            k = (l+r)//2

            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1

        
        return res


            
         
        