class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]

            num_ways = 0
            num_ways += dfs(i - 1) if i - 1 >= 0 and s[i-1] != '0' else 0
            num_ways += dfs(i - 2) if i - 2 >= 0 and int(s[i-2:i]) in range(10, 27) else 0
            memo[i] = num_ways
            return num_ways
        return dfs(len(s))