class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #brute force approach try every position as a start
            #dfs in all directions where new val > prev
            #O(m*n)^2

        ROWS, COLS = len(matrix), len(matrix[0])

        #add memo to dfs 
        memo = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        longest = 0
        def dfs(r, c, prev):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                matrix[r][c] <= prev
            ):
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            #get the LSI from all 4 neighbors and add 1
            lsi = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                lsi = max(lsi, dfs(nr, nc, matrix[r][c]))
            memo[(r, c)] = 1 + lsi
            return memo[(r, c)]
        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r, c, -1))
        return longest
            