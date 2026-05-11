class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for inter in intervals[1:]:
            if inter[0] <= res[-1][1]:
                res[-1][1] = max(inter[1], res[-1][1])
            else:
                res.append(inter)

        return res
