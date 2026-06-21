"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start)
        minH = []

        for inter in intervals:
            if minH and minH[0] <= inter.start:
                heapq.heappop(minH)
            heapq.heappush(minH, inter.end)

        return len(minH)
