class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #brute force: try every cell as a starting point
            #dfs in every direction trying to find the complete word
            #O(3^(m*n) * n) time / O(m*n) space
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, curr, visited):
            visited.add((r, c))
            curr.append(board[r][c])
            if "".join(curr) == word:
                return True
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                #if neighbor in bounds and not visited, try searching down that path
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    (nr, nc) not in visited
                ):
                    if dfs(nr, nc, curr, visited):
                        return True
            curr.pop()
            visited.remove((r, c))
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, [], set()):
                    return True
        return False