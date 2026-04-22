class Solution:
    def robline(self, houses):
        n = len(houses)
        prev1, prev2 = 0, 0
        for house in houses:
            prev2, prev1 = prev1, max(prev2 + house, prev1)
        return prev1
            
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        noFirstHouse = self.robline(nums[1:])
        noLastHouse = self.robline(nums[:n-1])
        return max(noFirstHouse, noLastHouse)