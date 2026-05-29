class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to store computed sum of squares
        # if a sum of squares is seen again, return false
        #O(n) sweepthru to sum squares
        #O(n) memory for seen set
        seen = set()
        while n != 1:
            s = str(n)
            summ = 0
            for i in range(len(s)):
                digit = int(s[i])
                summ += digit**2
            if summ in seen:
                return False
            seen.add(summ)
            n = summ
        return True