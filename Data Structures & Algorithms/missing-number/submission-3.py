class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] == i:
            i += 1
        return i