class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = set()
        q = deque()

        def addFruit(r, c):
            if (
                r in range(rows) and
                c in range(cols) and
                grid[r][c] == 1 and
                (r, c) not in rotten
            ):
                rotten.add((r, c))
                q.append((r, c))

        # 1. Seed the bfs queue with rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                    q.append((r, c))

        minutes = -1
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                grid[r][c] = 2

                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            minutes += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return max(minutes, 0)
