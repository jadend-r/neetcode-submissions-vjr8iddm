class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        counts = list(Counter(tasks).values())
        heapq.heapify_max(counts)
        currTime = 0
        while counts or q:
            currTime +=1 
            if counts:
                cnt = heapq.heappop_max(counts) - 1
                if cnt > 0:
                    q.append([cnt, currTime + n])
            if q and currTime == q[0][1]:
                task = q.popleft()
                heapq.heappush_max(counts, task[0]) 
        return currTime