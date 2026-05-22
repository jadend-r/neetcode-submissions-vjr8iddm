class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        target = sum(nums) / 2
        def dfs(i, total):
            if total == target:
                return True

            if i == len(nums):
                return False

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return memo[(i, total)]
        return dfs(0, 0)


        #bottom up
        #dp[i] = 
        #dp = [0] * target

