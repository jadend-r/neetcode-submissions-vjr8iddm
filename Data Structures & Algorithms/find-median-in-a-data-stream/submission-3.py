class MedianFinder:
    #utilize two heaps, small (maxHeap) large (minHeap)
    #we want to maintain heaps of roughly equal size (must not differ by > 1)
    #all values in small < all values in large
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)

        #make sure that small < large
        if self.small and self.large and self.small[0] > self.large[0]:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

        #make sure that heaps are roughly equal length
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2
        