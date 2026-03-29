class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] in found:
                left = max(left, found[s[right]] + 1)

            found[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest