class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []

        for i in range(len(intervals)):

            curr = intervals[i]

            # what if new interval finishes before curr
            if newInterval[1] < curr[0]:
                output.append(newInterval)
                return output + intervals[i:]

            # what if new interval finishes after curr
            elif newInterval[0] > curr[1]:
                output.append(curr)
            
            else:
                newInterval = [min(newInterval[0],curr[0]),max(newInterval[1],curr[1])]
        output.append(newInterval)
        
        return output

