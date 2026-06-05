class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        # O(m*n) space
        res = [0] * (m  + n) #Most digits a product can be is sum of lengths

        #O(m*n) time 
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                p1, p2 = i + j, i + j + 1
                # Add product into the ONE's place p2
                val = res[p2] + int(num1[i]) * int(num2[j])
                res[p2] = val % 10      # keep the one's digit
                res[p1] += val // 10    # carry the carry LEFT

        # Skip past leading zeros
        beg, end = 0, len(res)
        while beg < end and res[beg] == 0:
            beg += 1

        return "".join(map(str, res[beg:]))