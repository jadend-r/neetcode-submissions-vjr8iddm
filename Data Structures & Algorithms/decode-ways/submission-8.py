class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(i): #O(n) time/space
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]

            num_ways = 0
            num_ways += dfs(i + 1) if s[i] != '0' else 0
            num_ways += dfs(i + 2) if i + 2 <= len(s) and int(s[i:i+2]) in range(10, 27) else 0
            memo[i] = num_ways
            return num_ways
        return dfs(0)