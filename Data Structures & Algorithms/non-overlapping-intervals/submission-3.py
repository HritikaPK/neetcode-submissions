class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        res = 0 

        prevend = intervals[0][1]

        for i in intervals[1:]:

            if prevend <= i[0]:
                prevend = i[1]
                
            else:
                res += 1 #overlap
                if prevend >= i[1]:
                    prevend = i[1]

        return res
                    



        

       