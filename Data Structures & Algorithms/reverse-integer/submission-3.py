class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -(2**31)

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            res = (res * 10) + digit
        if res > MAX or res < MIN:
            return 0
        return res