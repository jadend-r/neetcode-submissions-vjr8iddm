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
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            match = i < len(s) and (p[j] == s[i] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                res = dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return dp[(i, j)]
        return dfs(0, 0)

        #Input: s = "nnn", p = "n*"
        #dp = {}