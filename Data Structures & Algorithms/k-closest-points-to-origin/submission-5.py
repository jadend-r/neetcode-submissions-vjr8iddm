class Solution:
    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        # O(n)
        for point in points:
            d = self.distance(point, [0, 0])
            minHeap.append([d, point[0], point[1]])

        # O(n)
        heapq.heapify(minHeap)
        res = []

        # O?
        while k > 0:
            point = heapq.heappop(minHeap)
            res.append([point[1], point[2]])
            k -= 1
        return res

        
        