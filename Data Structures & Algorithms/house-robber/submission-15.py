class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums.copy()
        if len(dp) > 1:
            dp[1] = max(dp[1], dp[0])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    
        return dp[n - 1]