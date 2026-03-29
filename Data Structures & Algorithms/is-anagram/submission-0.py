class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        hm2 = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            hm[charS] = 0 if charS not in hm else hm[charS] + 1
            hm2[charT] = 0 if charT not in hm2 else hm2[charT] + 1
        for char in s:
            if char not in hm or char not in hm2:
                return False
            if hm[char] != hm2[char]:
                return False

        return True