class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        #dp[i][j] when s[i..j] is palindrome
        # dp = [[False] * n for i in range(n)]

        # for i in range(n):
        #     dp[i][i] = True
        #     count += 1

        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1
        #         if s[i] == s[j] and (dp[i+1][j-1] or length == 2):
        #             dp[i][j] = True
        #             count += 1


        # return count

        for i in range(n):
            #odd pals
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # even pals
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
