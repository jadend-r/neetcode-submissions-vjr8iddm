class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = list(counts.values())
        heapq.heapify_max(maxHeap)
        q = deque() 
        time = 0
        print(q, maxHeap)
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time