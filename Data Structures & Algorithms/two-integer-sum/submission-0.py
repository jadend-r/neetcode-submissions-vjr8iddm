# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(numbers)):
            n = numbers[i]
            if target - n in prevMap:
                return [prevMap[target - n], i]
            prevMap[n] = i
