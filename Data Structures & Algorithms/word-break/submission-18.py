class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        memo = defaultdict(bool)
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and dfs(j):
                    memo[i] = True
            return memo[i]
        return dfs(0)