"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()
        res = 0
        count = 0
        j = 0
        i = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            elif start[i] >= end[j]:
                j += 1
                count -= 1
            res = max(count,res)
        return res



        
        