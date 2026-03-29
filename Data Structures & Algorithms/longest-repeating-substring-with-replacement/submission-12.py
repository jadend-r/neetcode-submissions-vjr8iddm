# ABBB

# {a: 1, b: 2}

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxf = 0
        left = 0
        res = 0
        for right in range(len(s)): 
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxf = max(maxf, counts[s[right]])
            if right - left + 1 - maxf <= k:
                res = max(res, right - left + 1)
            else:
                counts[s[left]] -= 1
                left += 1
                
        return res