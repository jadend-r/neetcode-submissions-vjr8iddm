class Solution:
    def countSubstrings(self, s: str) -> int:
        #brute force approach to generate every possible substring
            #check if that substring is a palindrome
            #O(N^3) 

        palindromes = 0 

        #Overall O(n^2) time
        #O(1) space
        for i in range(len(s)): #O(n)
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]: #O(n)
                palindromes += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1
        return palindromes
        #Input: s = "aaa" palindromes = 6