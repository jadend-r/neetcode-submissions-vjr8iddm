class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def bfs(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and
                    col in range(cols) and
                    grid[row][col] == 2147483647 and
                    (row, col) not in visited
                ):
                    q.append((row, col))
                    visited.add((row, col))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        print(q)
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                grid[r][c] = dist

                bfs(r, c)
            dist += 1