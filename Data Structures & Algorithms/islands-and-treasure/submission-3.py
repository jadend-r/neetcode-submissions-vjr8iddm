class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        #seed q with treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()
                grid[row][col] = dist
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 2147483647
                    ):
                        q.append((r, c))
                        grid[r][c] = dist + 1
            dist += 1

