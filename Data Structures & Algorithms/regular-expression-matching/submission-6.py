class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #brute force: i, j ptr into s, p
            #chars are same or p[j] is "." -> i + 1, j + 1
            #p is *, dfs(i + 1, j) or dfs(i, j + 2)
            #2^n
        #optimize to O(m*n) with dp, memo (i. j) where i, j means
        #can s[i:] p[j:] be matched

        dp = {}
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            if j+1 < len(p) and p[j+1] == "*":
                res = dfs(i, j + 2)
                if i < len(s) and (p[j] == s[i] or p[j] == "."):
                    res = res or dfs(i + 1, j) 
            elif i < len(s) and (s[i] == p[j] or p[j] == "."):
                res = dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return dp[(i, j)]
        return dfs(0, 0)

        #Input: s = "nnn", p = "n*"
        #dp = {}