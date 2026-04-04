class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.summ = 0
        res = []
        combination = []
        def dfs(i):
            if self.summ == target:
                res.append(combination.copy())
                return
            elif self.summ > target or i >= len(nums):
                return
            self.summ += nums[i]
            combination.append(nums[i])
            dfs(i)

            self.summ -= nums[i]
            combination.pop()
            dfs(i + 1)
        dfs(0)
        return res