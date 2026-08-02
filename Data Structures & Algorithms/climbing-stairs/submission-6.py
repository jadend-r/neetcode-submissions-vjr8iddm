class Solution:
    def climbStairs(self, n: int) -> int:
        #brute force try every possible way to climb steps
        #2^n

        #optimize to o(n) with dp where dp[i] = num of ways to 
            #(climb to step i-1 + ways to climb to step i - 2)
        
        #dp[0] = 1, 1 ways to climb to step 0
        prev_prev = prev = 1
        for i in range(2, n + 1):
            prev_prev, prev =  prev, (prev + prev_prev)
        return prev