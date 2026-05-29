class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #modified dijkstra's
        #minHeap (maxHeight, r, c)
        ROWS, COLS = len(grid), len(grid[0])
        minH = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while minH:
            maxHeight, r, c = heapq.heappop(minH)
            if (r, c) in visited:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return maxHeight
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    (nr, nc) not in visited 
                ):
                    maxH = max(maxHeight, grid[nr][nc])
                    heapq.heappush(minH, (maxH, nr, nc))

