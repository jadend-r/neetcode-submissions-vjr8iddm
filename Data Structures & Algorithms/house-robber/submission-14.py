class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = dp[i - 2] + nums[i - 2]
        n = len(nums)
        dp = nums.copy()
        if len(dp) > 1:
            dp[1] = max(dp[1], dp[0])
        for i in range(n):
            if i >= 2:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    
        return dp[n - 1]