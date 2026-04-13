class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        minutes, fresh = 0, 0

        def addFruit(r, c):
            nonlocal fresh
            if (
                r in range(rows) and
                c in range(cols) and
                grid[r][c] == 1
            ):
                grid[r][c] = 2
                fresh -= 1
                q.append((r, c))
                 

        # 1. Seed the bfs queue with rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            minutes += 1

        return minutes if fresh == 0 else -1
