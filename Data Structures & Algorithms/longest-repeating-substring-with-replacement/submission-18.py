class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        res = 0
        counts = {}
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxf = max(maxf, counts[s[right]])

            if right - l + 1 - maxf <= k:
                res = max(res, right - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1

        return res
