class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       # cost(n) = min(cost(n-1), cost(n-2))
        dp = [0] * (len(cost) + 1)
        dp[-1] = 0
        dp[-2] = cost[-1]
        for i in range(len(cost) - 2, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

        return dp[0] if dp[0] <= dp[1] else dp[1]
