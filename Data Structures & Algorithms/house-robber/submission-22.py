class Solution:
    def rob(self, nums: List[int]) -> int:
        # prev1 = dp[i-1]
        # prev2 = dp[i-2]
        # dp[n] = max(dp[i - 2] + nums[n], dp[i - 1])
        prev1, prev2 = 0, 0
        for n in nums:
            prev2, prev1 = prev1, max(prev2 + n, prev1)
    
        return prev1