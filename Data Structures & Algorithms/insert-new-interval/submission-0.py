class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):

            #what if new ends before interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # what if new starts after intervak
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # else its somewhere between 
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            
        res.append(newInterval)
        return res
        