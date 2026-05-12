class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1]) # sort by end ensures any interval we keep has smallest end time, leaving more room for future
        prevEnd = -math.inf
        res = 0
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
        return res