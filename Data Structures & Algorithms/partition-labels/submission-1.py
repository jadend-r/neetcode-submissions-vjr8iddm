class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #track the last index of each unique character (hashmap)

        
        # when we reach the last index of a char, cut that as a substring
        #O(n) passthrough with ptr called end

        res = []
        start, end = 0, 0

        #O(n) passthrough to get the last index of each char
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i

        #iterate thru string, update end ptr, if end == i take that substring
        for i in range(len(s)):
            end = max(end, lastIdx[s[i]])
            if end == i:
                res.append(end - start + 1)
                start = i + 1

        return res
