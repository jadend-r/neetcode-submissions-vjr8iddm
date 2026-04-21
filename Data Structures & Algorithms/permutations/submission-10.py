class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = [False] * len(nums)
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]: continue
                curr.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                curr.pop()
        dfs()
        return res