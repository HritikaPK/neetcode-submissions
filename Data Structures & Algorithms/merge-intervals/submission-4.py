class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorted
        intervals.sort()

        #merge all overlapping intervals
        output = [intervals[0]]
        
        # compare interval i with j
        for start,end in intervals[1:]:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1]=max(lastend,end)
            else:
                output.append([start,end])
        return output


