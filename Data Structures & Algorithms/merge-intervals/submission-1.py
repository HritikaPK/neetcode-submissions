class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = output[-1]
            curr = intervals[i]

            # does prev end before curr starts?
            if prev[1] < curr[0]:
                output.append(curr)
            else:  
                output[-1] = [min(prev[0],curr[0]),max(prev[1],curr[1])]     
                  
        return output
                # OVERLAP ALERT!!!!


        
        
       
        