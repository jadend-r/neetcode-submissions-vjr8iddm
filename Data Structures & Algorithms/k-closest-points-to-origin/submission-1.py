class Solution:
    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            heapq.heappush_max(maxHeap, [self.distance(point, [0, 0]), point])

        while len(maxHeap) > k:
            heapq.heappop_max(maxHeap)

        res = []
        while maxHeap:
            res.append(heapq.heappop_max(maxHeap)[1])
        return res

        
        