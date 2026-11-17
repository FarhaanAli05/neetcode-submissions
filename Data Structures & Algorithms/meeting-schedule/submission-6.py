"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda i : i.start)
        for i in range(1, len(intervals)):
            one = intervals[i-1].end
            two = intervals[i].start
            if two < one:
                return False
        return True