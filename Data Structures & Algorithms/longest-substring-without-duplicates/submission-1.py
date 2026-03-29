class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        windowChars = set()
        for right in range(len(s)):
            while s[right] in windowChars:
                windowChars.remove(s[l])
                l += 1
            windowChars.add(s[right])
            res = max(res, right - l + 1)

        return res