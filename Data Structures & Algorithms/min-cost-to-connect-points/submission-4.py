class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        minHeap = [(0, 0)]
        visited = set()
        cost = 0
        while len(visited) < len(points):
            c, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            cost += c
            for adjacent, dist in adj[node]:
                if adjacent not in visited:
                    heapq.heappush(minHeap, (dist, adjacent))

        return cost