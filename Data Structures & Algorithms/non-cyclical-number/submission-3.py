class Solution:
    def isHappy(self, n: int) -> bool:
        # use a set to store computed sum of squares
        # if a sum of squares is seen again, return false
        
        #O(n) memory for seen set
        seen = set()
        while n != 1:
            summ = 0
            while n:
                digit = n % 10 # %10 gives last digit
                summ += digit**2
                n //= 10        # chop off last digit
            if summ in seen:
                return False
            seen.add(summ)
            n = summ
        return True