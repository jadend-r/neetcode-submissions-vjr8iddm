class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # def dfs(r, c, visited, prevHeight):
        #     if (
        #         r not in range(ROWS) or
        #         c not in range(COLS) or
        #         (r, c) in visited or
        #         heights[r][c] < prevHeight
        #      ):
        #         return 
        #     visited.add((r, c))
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc, visited, heights[r][c])

        def bfs(r, c, visited):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        heights[r][c] >= heights[row][col]
                    ):
                        visited.add((r, c))
                        q.append((r, c))

        for c in range(COLS):
            # dfs(0, c, pac, heights[0][c])
            # dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

            bfs(0, c, pac)
            bfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            # dfs(r, 0, pac, heights[r][0])
            # dfs(r, COLS - 1, atl, heights[r][COLS - 1])

            bfs(r, 0, pac)
            bfs(r, COLS - 1, atl)

        return [[r, c] for r, c in pac.intersection(atl)]