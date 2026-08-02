class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev = prev = 0
        for n in nums:
            prev_prev, prev = prev, max(prev, prev_prev + n)
        return prev