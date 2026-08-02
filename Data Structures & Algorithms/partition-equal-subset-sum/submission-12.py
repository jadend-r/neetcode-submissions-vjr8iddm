class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #brute force is use backtracking to find every possible
            #way to divide nums into 2 subsets
                #check how many have equal sums
                #O(2^n)
        #to divide into equal sum, total must be evenly divisible by 2
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]

        return dp[target]