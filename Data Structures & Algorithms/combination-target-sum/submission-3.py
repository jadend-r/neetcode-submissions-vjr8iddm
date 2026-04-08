class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb, summ):
            if summ == target:
                res.append(comb.copy())
                return
            if summ > target or i == len(nums):
                return

            summ += nums[i]
            comb.append(nums[i])
            backtrack(i, comb, summ)

            summ -= nums[i]
            comb.remove(nums[i])
            backtrack(i + 1, comb, summ)

        backtrack(0, [], 0)
        return res