class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        prevEnd = -math.inf
        res = 0
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
        return res