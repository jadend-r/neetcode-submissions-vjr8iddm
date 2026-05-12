class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        res = [intervals[0]]
        print(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= res[-1][1]:
                res.append(intervals[i])
        return len(intervals) - len(res)