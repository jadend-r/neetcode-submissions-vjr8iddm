class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n            # dp[i] = max amount of money robbale up to this house 0 .. i
        if n == 1:
            return nums[0]
        dp[0] = nums[0]         # dp[0] = nums[0] first house can only rob itself
        dp[1] = max(nums[0], nums[1]) # dp[1] = max(nums[0], nums[1]), house 1 can rob itself or only rob house 0, chose richer
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    
        return dp[n - 1]