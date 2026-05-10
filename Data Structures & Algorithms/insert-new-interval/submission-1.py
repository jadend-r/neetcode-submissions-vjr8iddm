class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # new interval comes before -- append it and add everyting after
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            # new interval comes after -- append interval[i]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # intervals overlap, merge them
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        res.append(newInterval)
        return res