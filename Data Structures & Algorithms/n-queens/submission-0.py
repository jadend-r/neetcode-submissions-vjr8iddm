class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #brute force backtracking solution
        #attempt to place 1 queen per row
        #we need to ensure that queens are not:
            #placed in the same col
            #place in same neg/pos diagonal

        #utilize 3 sets, col, negDiag, posDiag
        col = set()
        negDiag = set()
        posDiag = set()
        res = []
        grid = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            #try every column to place a queen
            for c in range(n):
                if c in col: # already added a queen to col, skip
                    continue
                if r - c in negDiag: # r - c is constant across a negative diag
                    continue
                if r + c in posDiag: # r + c is constant across a positive diag
                    continue

                col.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)
                grid[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                grid[r][c] = "."
        backtrack(0)
        return res
                
