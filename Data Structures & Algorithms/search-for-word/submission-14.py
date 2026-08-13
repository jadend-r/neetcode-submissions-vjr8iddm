class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #brute force: try every cell as a starting point
            #dfs in every direction trying to find the complete word
            #O(3^(m*n) * n) time / O(m*n) space
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i >= len(word):
                return True
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in path or 
                board[r][c] != word[i]
            ):
                return False
            path.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                #if neighbor in bounds and not visited, try searching down that path
                if dfs(nr, nc, i + 1):
                    return True
            path.remove((r, c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False