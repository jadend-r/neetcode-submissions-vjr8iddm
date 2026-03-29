class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxf = 0
        longest = 0
        counts = {}

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxf = max(maxf, counts[s[right]])

            if right - left + 1 - maxf <= k:
                longest = max(longest, right - left + 1)
            else:
                counts[s[left]] -= 1
                left += 1
        return longest

            