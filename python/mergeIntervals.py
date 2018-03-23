# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
            return intervals
        merged = []
        intervals_sorted = sorted(intervals, key=lambda intervals: intervals.start)
        start = intervals_sorted[0].start
        end = intervals_sorted[0].end
        for interval in intervals_sorted:
            if end>=interval.start:
                end = max(end, interval.end)
            else:
                merged.append(Interval(start, end))
                start = interval.start
                end = interval.end
        merged.append(Interval(start, end))
        return merged
        