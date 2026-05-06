class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                rn, cn = r + dr, c + dc
                if (
                    rn in range(ROWS) and
                    cn in range(COLS) and
                    heights[rn][cn] >= heights[r][c] and
                    (rn, cn) not in visited
                ):
                    dfs(rn, cn, visited)

        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        return list(pac.intersection(atl))
