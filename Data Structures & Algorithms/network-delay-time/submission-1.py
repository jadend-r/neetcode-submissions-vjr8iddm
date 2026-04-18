class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        visited = set()
        minHeap = [(0, k)]

        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for w2, n2 in adj[n1]:
                #if n2 not in visited:
                heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visited) == n else -1

