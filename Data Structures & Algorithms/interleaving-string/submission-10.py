class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # len(s1) + len(s2) = len(s3)
        # if len(s1) + len(s2) != len(s3):
        #     return False
        
        #memo[(i, j)]: can s1[i:] be interlieved with s2[j:] to form s3[i+j]
        #O(m * n) time & space
        # memo = {}
        # def dfs(i, j):
        #     if i + j == len(s3):
        #         return True

        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     res = False
        #     if i < len(s1) and s1[i] == s3[i + j]:
        #         res = res or dfs(i + 1, j)
        #     if j < len(s2) and s2[j] == s3[i + j]:
        #         res = res or dfs(i, j + 1)
        #     memo[(i, j)] = res
        #     return memo[(i, j)]
        # return dfs(0, 0)

        #bottom up
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for k in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i + j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]

        #aaaa
        #bbbb
        #aabbbbaa