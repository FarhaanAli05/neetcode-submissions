"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        hmap = {}
        ends = {}
        if len(intervals) == 0:
            return True
        for i in intervals:
            for j in range(i.start, i.end):
                if not hmap.get(j):
                    hmap[j] = "true"
                else:
                    return False
        return True