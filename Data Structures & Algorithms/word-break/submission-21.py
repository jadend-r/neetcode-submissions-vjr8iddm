class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        memo = defaultdict(bool)
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            L = max(map(len, wordDict))
            for j in range(i + 1, min(len(s) + 1, i + 1 + L)):
                if s[i:j] in wordDict and dfs(j):
                    memo[i] = True
                    return memo[i]
            return memo[i]
        return dfs(0)