class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        totalCost = 0
        adj = defaultdict(list)

        # builds our undirected graph
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minHeap = [(0, 0)]
        visited = set()
        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            totalCost += cost
            visited.add(point)
            for dist, adjacent in adj[point]:
                if adjacent not in visited:
                    heapq.heappush(minHeap, (dist, adjacent))
        return totalCost

        