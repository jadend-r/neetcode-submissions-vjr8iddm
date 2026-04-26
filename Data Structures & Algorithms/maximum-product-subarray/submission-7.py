class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        curr_min = curr_max = res = nums[0]

        for i in range(1, n):
            cands = (nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_max = max(cands)
            curr_min = min(cands)
            res = max(res, curr_max)

        return res