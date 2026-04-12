class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addIsland(r, c):
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == 2147483647 and
                    (r, c) not in visited
                ):
                    q.append((r, c))
                    visited.add((r, c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                grid[r][c] = dist
                addIsland(r + 1, c)
                addIsland(r - 1, c)
                addIsland(r, c + 1)
                addIsland(r, c -1)
            dist += 1