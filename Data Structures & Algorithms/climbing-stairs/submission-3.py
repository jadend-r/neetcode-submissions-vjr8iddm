class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 0
        for i in range(n):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1