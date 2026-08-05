class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #brute force, for every number 2 choices, add or subtract
        #2^n * total
        #optimize to O(n * total) with cache
        dp = {}
        def dfs(i, remaining):
            if i == len(nums) and remaining == 0:
                return 1
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            if i == len(nums):
                return 0
            dp[(i, remaining)] = dfs(i + 1, remaining + nums[i]) + dfs(i + 1, remaining - nums[i])
            return dp[(i, remaining)]
        return dfs(0, target)

        #Input: nums = [2,2,2], target = 2
        # i = 0, dfs(0, 6)
        # i = 1, dfs(1, 4)
        # i = 2, dfs(1, 2)
        # i = 3, dfs(1, 0)