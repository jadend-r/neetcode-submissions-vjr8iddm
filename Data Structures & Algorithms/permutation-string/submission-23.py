class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        {a: 1, b: 1,  c: 2}
        { c: 2}
        abcc
        arbcccbacc
            l
             r
        aaa
        aaa
        '''
        if len(s1) > len(s2):
            return False
        from collections import defaultdict
        s1Count = [0] * 26
        s2Count = [0] * 26

        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            c = s2[r]
            idx = ord(c) - ord('a')
            s2Count[idx] += 1

            while s2Count[idx] > s1Count[idx]:
                left_c_idx = ord(s2[l]) - ord('a')
                s2Count[left_c_idx] -= 1
                l += 1

            if s1Count == s2Count:
                return True
        return False