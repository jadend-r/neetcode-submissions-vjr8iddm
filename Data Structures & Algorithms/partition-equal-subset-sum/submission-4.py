class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        #If I can find any subset of nums that sums to total / 2, I'm done

        #dp[i] = Is there some subset of the numbers I've seen so far that sums to exactly i

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num] #to make sum i, either we could already make it (dp[i]) or we could make
                                                        #dp[i - num] and have added num 

        return dp[target]