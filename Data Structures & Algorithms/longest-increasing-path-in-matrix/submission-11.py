class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #brute force approach we could try every cell as a start to our path
        #dfs to all neighbors > curr cell and update the longest length as 
            #we go
            #O(m*n * 3^(m*n)) time o(m*n) space for recursion stack
        #optimize o(m*n) with dp dp[i][j] where dp[i][j] LIP starting from
            #cell i, j
        #top down memo
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    matrix[nr][nc] > matrix[i][j]
                ):
                    res = max(res, 1 + dfs(nr, nc))
            dp[(i, j)] = res
            return dp[(i, j)]
        lip = 0
        for r in range(ROWS):
            for c in range(COLS):
                lip = max(lip, dfs(r, c))
        return lip