class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            op[i] *= prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            op[i] *= postfix
            postfix *= nums[i]

        return op