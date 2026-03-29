class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(len(nums)):
            mask = [nums[i]] * len(nums)
            mask[i] = 1
            output = [a * b for a, b in zip(output, mask)]
        
        return output
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output[i] = product

        # return output