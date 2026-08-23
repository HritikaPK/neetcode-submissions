class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):

            # not overlapping cases:
            if newInterval[1] < intervals[i][0]:
                #ends before i starts
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                #starts sometime after i ends
                res.append(intervals[i])
            else:
                #overlap
                newInterval = [min(intervals[i][0],newInterval[0]),max(newInterval[1],intervals[i][1])]
        
        #incase it happens after all intervals
        res.append(newInterval)
        return res
                

        

                