class Solution:
    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            d = self.distance(point, [0, 0])
            heapq.heappush_max(maxHeap, [d, point])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        return [point[1] for point in maxHeap]

        
        