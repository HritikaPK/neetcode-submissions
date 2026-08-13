"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        count = 0
        # create start and end arrays
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        #sort both of them
        res = 0

        s = 0
        e = 0
        #traverse both until start array is completly traversed
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            elif start[s] >= end[e]:
                count -= 1
                e += 1
            res = max(res,count)
        return res
            


        # edge case where start = finish



        