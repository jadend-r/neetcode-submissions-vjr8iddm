class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = [False] * len(nums)
        def dfs():
            if all(used):
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