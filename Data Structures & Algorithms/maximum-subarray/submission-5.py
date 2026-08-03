class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #O(N) utilize kadane's/greedy
        #keep running total sum as we scan l->r

        maxSum = -math.inf
        currSum = 0
        for n in nums:
            currSum += n
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum