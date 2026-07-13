class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #brute force would be try every character as a start, scan for chars from t
            #n^2 * t time, o(1) space
            #o(n) optimize w/ 2d dp
            #dp[i][j] number of distinct subsequnces s[i:] and t[j:]
                #base cases s exhausted -> num distinct subeqnces 0
                # t exhausted -> num distinct subsequnces is 1 empty subsequence of s
                #recurrce if s[i] == t[j] = dp[i + 1][ j+ 1]
                # else, dp[i + 1][j] 
        m, n = len(s), len(t)
        dp=[[0] * (n + 1) for _ in range(m + 1)]
        # when t is empty, distinct subseq btwen s[i] .. t is 1, empty subseq
        for r in range(m + 1):
            dp[r][n] = 1

        #fill in dp starting from bottom right corner
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
