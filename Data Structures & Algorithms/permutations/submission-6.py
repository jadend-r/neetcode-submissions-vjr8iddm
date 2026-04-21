class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()
        def dfs():
            if len(used) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if i in used: continue
                curr.append(nums[i])
                used.add(i)
                dfs()
                used.remove(i)
                curr.pop()
        dfs()
        return res