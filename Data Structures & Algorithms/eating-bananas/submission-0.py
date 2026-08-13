class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        l = 1

        kmin = r 

        while(l<=r):
            k = (l+r)//2
            
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            
            if hours <= h:
                kmin = min(kmin,k)
                r = k - 1
            else: 
                l = k + 1
        return kmin
