class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for k, v in enumerate(nums):
            if k > 0 and v == nums[k - 1]:
                continue
            
            i, j = k + 1, len(nums) - 1
            while i < j:
                threeSum = v + nums[i] + nums[j]
                if threeSum < 0:
                    i += 1
                elif threeSum > 0:
                    j -= 1
                else:
                    output.append([v, nums[i], nums[j]])
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

        return output

               
                
        
            