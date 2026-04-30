class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #dp[i] = is there some subset of nums that sums to i
        total = sum(nums)
        target = total // 2
        if total % 2 != 0:
            return False

        n = len(nums)
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for i in range(target, num -1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
        

        
                    