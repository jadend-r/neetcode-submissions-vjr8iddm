class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,t in times:
            adj[u].append((v, t))

        visited = set()
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            time = max(time, t)
            visited.add(node)
            for adjacent, w in adj[node]:
                if adjacent not in visited:
                    heapq.heappush(minHeap, (t + w, adjacent))

        return time if len(visited) == n else -1