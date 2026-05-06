class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if heights[r][c] < prevHeight:
                return 

            if (r, c) in visited:
                return

            prevHeight = heights[r][c]
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                rn, cn = r + dr, c + dc
                if (
                    rn in range(ROWS) and
                    cn in range(COLS) and
                    (rn, cn) not in visited
                ):
                    dfs(rn, cn, visited, prevHeight)

        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)

        return list(pac.intersection(atl))
