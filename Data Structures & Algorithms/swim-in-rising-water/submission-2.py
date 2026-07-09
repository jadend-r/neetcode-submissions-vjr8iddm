class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #perform a dfs starting at the top left cell
            #take max elevation/time along path to bottom right

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        minH = [(grid[0][0], 0, 0)]
        visited = set()

        while minH:
            elv, r, c = heapq.heappop(minH)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return elv
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    (nr, nc) not in visited
                ):
                    heapq.heappush(minH, (max(grid[nr][nc], elv), nr, nc))
