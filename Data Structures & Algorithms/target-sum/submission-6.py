class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]
            res = 0
            res += dfs(i + 1, total + nums[i])
            res += dfs(i + 1, total - nums[i])
            print("i is", i, "res is", res)
            memo[(i, total)] = res
            return memo[(i, total)]
        return dfs(0, 0)