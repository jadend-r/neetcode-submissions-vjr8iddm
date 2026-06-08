class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask      # keep only 32 bits
            b = carry & mask        # carry also clamped
        return a if a <= max_int else ~(a ^ mask)