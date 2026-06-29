class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs, seed q with rotten fruit and spread to neighbor fresh
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh:
            qLen = len(q)
            for _ in range(qLen):
                #pop a rotten orange
                r, c = q.popleft()
                #for all neighbors, rot fresh fruit and add them to q
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr >= 0 and nr < ROWS and
                        nc >= 0 and nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1

        return time if not fresh else -1
                
