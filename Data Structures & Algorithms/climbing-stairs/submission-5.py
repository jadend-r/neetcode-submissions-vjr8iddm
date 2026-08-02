class Solution:
    def climbStairs(self, n: int) -> int:
        #brute force try every possible way to climb steps
        #2^n

        #optimize to o(n) with dp where dp[i] = num of ways to 
            #(climb to step i-1 + ways to climb to step i - 2) + 1
        
        dp = [0] * (n + 1)
        #dp[0] = 0, 0 ways to climb to step 0
        dp[0] = 1
        if len(dp) >= 2:
            dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2])
        return dp[n]