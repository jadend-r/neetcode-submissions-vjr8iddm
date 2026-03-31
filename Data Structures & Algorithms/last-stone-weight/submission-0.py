class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = stones
        heapq.heapify_max(self.maxHeap)

        while len(self.maxHeap) > 1:
            stone1 = heapq.heappop_max(self.maxHeap)
            stone2 = heapq.heappop_max(self.maxHeap)
            if stone1 - stone2 > 0:
                heapq.heappush_max(self.maxHeap, stone1 - stone2)

        return self.maxHeap[0] if self.maxHeap else 0