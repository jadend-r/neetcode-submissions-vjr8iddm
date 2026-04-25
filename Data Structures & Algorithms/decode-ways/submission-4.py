class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(dp)):
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            s2 = s[i-2:i]
            if int(s2) in range(10,27):
                dp[i] += dp[i-2]

        return dp[n]