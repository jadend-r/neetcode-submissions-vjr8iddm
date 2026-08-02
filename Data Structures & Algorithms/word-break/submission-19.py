class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        L = max(map(len, wordDict))
        for i in range(n-1, -1, -1):
            for j in range(i + 1, min(i + L + 1, len(s) + 1)):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True

        return dp[0]