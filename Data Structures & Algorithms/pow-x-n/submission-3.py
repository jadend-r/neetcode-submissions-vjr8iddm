class Solution:
    def helper(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = self.helper(x, n // 2) # log(n) recursive calls
        res = res * res
        return x * res if n % 2 else res

    def myPow(self, x: float, n: int) -> float:
        #O(log(n)) time
        #O(log(n)) space for recursive call stack
        res = self.helper(x, abs(n))
        return res if n >= 0 else 1 / res