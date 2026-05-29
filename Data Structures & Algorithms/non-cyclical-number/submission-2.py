class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to store computed sum of squares
        # if a sum of squares is seen again, return false
        
        #O(n) memory for seen set
        seen = set()
        while n != 1:
            s = str(n)
            summ = 0
            while n:
                digit = n % 10
                summ += digit**2
                n //= 10
            if summ in seen:
                return False
            seen.add(summ)
            n = summ
        return True