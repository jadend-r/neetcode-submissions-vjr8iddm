class Solution:
    def robline(self, houses):
        n = len(houses)
        dp = [0] * n
        if n == 1:
            return houses[0]
        dp[0] = houses[0]
        dp[1] = max(dp[0], houses[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])
            
        return dp[n - 1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        noFirstHouse = self.robline(nums[1:])
        noLastHouse = self.robline(nums[:n-1])
        return max(noFirstHouse, noLastHouse)