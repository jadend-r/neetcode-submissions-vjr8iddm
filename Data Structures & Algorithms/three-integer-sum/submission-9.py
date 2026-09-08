class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force n^3
        #optimize to n^2 with 2 sum

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                ts = nums[i] + nums[j] + nums[k]
                if ts == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                elif ts > 0:
                    k -= 1
                else:
                    j += 1

        return res