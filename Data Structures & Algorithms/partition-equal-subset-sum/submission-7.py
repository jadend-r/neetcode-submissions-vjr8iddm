class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i] = is there some subset of nums that sums to i
        total = sum(nums)
        target = total // 2
        if total % 2 != 0:
            return False

        # n = len(nums)
        # dp = [False] * (target+1)
        # dp[0] = True

        # for num in nums:
        #     for i in range(target, num -1, -1):
        #         dp[i] = dp[i] or dp[i - num]

        # return dp[target]
        
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return True

            if i >= len(nums) or remaining < 0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            memo[(i, remaining)] = dfs(i + 1, remaining - nums[i]) or dfs(i+1, remaining)
            return memo[(i, remaining)]
        return dfs(0, target)

        
                    