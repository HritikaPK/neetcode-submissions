class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curmax, curmin = 1,1
        res = max(nums)

        for i in nums:

            if i == 0:
                curmax,curmin = 1,1
                continue
            
            temp = curmax
            curmax = max(i*curmax, i*curmin, i)
            curmin = min (i*temp, i*curmin, i)
            res = max(res,curmax)
        
        return res

        