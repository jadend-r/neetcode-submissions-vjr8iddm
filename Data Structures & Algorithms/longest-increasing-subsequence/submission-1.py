class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n)
        #dp[i] = length of LIS at indx i
        dp[0] = 1

        for length in range(1, n):
            for j in range(length):
                if nums[j] < nums[length]:
                    dp[length] = max(dp[length], dp[j] + 1)
        print(dp)
        return max(dp)