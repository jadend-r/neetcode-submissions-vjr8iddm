# ABBB

# {a: 1, b: 2}

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        mostFreqChar = s[0]
        maxf = 0
        left = 0
        res = 0
        for right in range(len(s)):
            
            counts[s[right]] = 1 + counts.get(s[right], 0)
            print("count", s[right], counts[s[right]])
            maxf = max(maxf, counts[s[right]])
            if counts[s[right]] >= counts[mostFreqChar]:
                mostFreqChar = s[right]
            if right - left + 1 - maxf <= k:
                res = max(res, right - left + 1)
            else:
                while right - left + 1 - maxf > k:
                    print("shifting right from", s[left])
                    counts[s[left]] -= 1
                    left += 1
                res = max(res, right - left + 1)
                
        print(counts, mostFreqChar)
        return res