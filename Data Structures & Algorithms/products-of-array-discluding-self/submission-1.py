class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [nums[0]] + [1] * (len(nums) - 1)
        postfix = [1] * (len(nums) - 1) + [nums[-1]]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            postfix[len(nums) - 1 - i] = nums[len(nums) - 1 - i] * postfix[len(nums) - i]

        for i in range(len(output)):
            pfx = 1 if i == 0 else prefix[i - 1]
            postfx = 1 if i == len(postfix) - 1 else postfix[i + 1]
            output[i] = pfx * postfx
        
        return output
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output[i] = product

        # return output