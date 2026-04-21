class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(remaining):
            if not remaining:
                res.append(curr.copy())
                return
            for i in range(len(remaining)):
                curr.append(remaining[i])
                dfs(remaining[:i] + remaining[i + 1:])
                curr.pop()
        dfs(nums)
        return res